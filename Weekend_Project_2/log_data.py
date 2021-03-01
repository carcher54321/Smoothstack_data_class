import logging
import pandas as pd
import phonenumbers as pn
import csv
import os
import re
import matplotlib.pyplot as plt
import private
import smtplib
import ssl

# if lbl == l[0], lbl = l[1]
LABEL_REPLACEMENTS = {
    'Agent Writing Contract Start Date (Carrier appointment start date)':
        'Agent Writing Contract Start Date',
    'Agent Writing Contract Status (actually active and cancelled\'s should come in two different files':
        'Agent Writing Contract Status'
}
LST_FILE = 'NYL.lst'
PHONE_NUMBER_HEADERS = ['Agency Phone Number', 'Agent Phone Number']
STATE_HEADERS = ['Agency State', 'Agent State']
STATE_CSV_HEADERS = ['Agent License State (active)']
EMAIL_HEADERS = ['Agent Email Address']
EMAIL_REGEX_PATTERN = """^\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$"""
STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL',
          'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE',
          'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC',
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']
FILE_FORMAT_REGEX = 'NYL_FieldAgent_[0-9]{8}.csv'
EMAIL_RECIPIENTS = ['colin.archer@smoothstack.com']


# get the actual path to a data filename
def data_path(relative):
    return os.path.join('data', relative)


# get the actual path to a figure filename
def figure_path(relative):
    return os.path.join('figures', relative)


# get actual path to a log
def logs_path(relative):
    return os.path.join('logs', relative)


# get a list of all the file names for this project
# includes regex check to only catch files with correct format
def get_data_filenames():
    file_names = [f for f in os.listdir(data_path('')) if os.path.isfile(data_path(f))]
    filtered = [f for f in file_names if re.search(FILE_FORMAT_REGEX, f) is not None]
    # get all file names which don't match the correct format
    not_formatted = list(set(file_names) - set(filtered))
    for f in not_formatted:
        # if any of those files is a csv, log that it is not formatted correctly
        if f[-4:] == '.csv':
            logging.info(f'CSV file not in correct filename format: {f}')
    return filtered


# grabs the first full integer from a string
def str_get_int(s):
    start = None
    end = None
    index = 0
    # loops through each character, trying to cast it as int
    for ch in s:
        try:
            int(ch)
        # if it can't be, check whether we have a start value. If so, this is the ending index
        except ValueError:
            if start:
                end = index
                break
        # if the casting succeeds, record the current index as the start index
        # unless it already exists
        else:
            if not start:
                start = index
        # with each loop, increase the index by one to keep up with the character loop
        finally:
            index += 1
    # catch case where number comes at end of string
    if not end:
        end = index
    # finally, return the whole index cast as an int
    try:
        return int(s[start:end])
    except ValueError:
        logging.exception(f'Something went wrong with getting an int: {s}')


# simple function to get the length of the csv file
# the only files that get to this point have already passed the regex check
# so there won't be any non-csv files
def get_file_length(file_name):
    with open(data_path(file_name), 'r') as csvFile:
        reader = csv.reader(csvFile)
        row_count = sum(1 for _row in reader)
    return row_count


# check whether the file has already been processed
def check_already_processed(file_name):
    # get the file names from the NYL.lst file
    with open(data_path(LST_FILE)) as file:
        rows = file.readlines()
    # check each file name to see if the passed value has already been processed
    for fn in rows:
        if fn == file_name:
            return True
    return False


# regex search for email patterns
def validate_email(email):
    return re.search(EMAIL_REGEX_PATTERN, email) is not None


# do all the preprocessing checks
def validate_preprocessing(file_names):
    already_done = check_already_processed(file_names[0])
    logging.info(f'{file_names[0]} is most recent file')
    # log that the file has already been processed
    if already_done:
        logging.exception(f'{file_names[0]} has already been processed')
        return False
    else:
        # log that the difference in length between latest and previous file is too much
        diff = get_file_length(file_names[0]) - get_file_length(file_names[1])
        if not (-500 <= diff <= 500):
            logging.exception(f'{file_names[0]} has more than 500 lines of variance from {file_names[1]}')
            return False
    # if all checks for invalidating circumstances fail, return that preprocessing was a success
    return True


# replace labels within the data frame, or do nothing if not necessary
def replace_labels(df):
    df.rename(columns=LABEL_REPLACEMENTS)


# check every phone number within the data frame
def check_phone_numbers(df):
    for col in df[PHONE_NUMBER_HEADERS].columns:
        # accumulator for the number of entries which are blank by column
        # more useful than hundreds of lines of "empty phone number"
        num_empty_numbers = 0
        for num in df[col]:
            # pn.parse must be in try block to catch NaN values
            try:
                phone_num = pn.parse(num, 'US')
            except pn.NumberParseException:
                num_empty_numbers += 1
                continue
            # after parsing, must validate number
            if not pn.is_valid_number(phone_num):
                logging.info(f'Invalid phone number: {num}')
        # log the number of empty phone numbers
        if num_empty_numbers > 0:
            logging.info(f'There are {num_empty_numbers} empty numbers in {col}')


# check every field with states within the data frame for validity
def check_valid_state(df):
    # check the columns with only one state
    for col in df[STATE_HEADERS].columns:
        for st in df[col]:
            if st not in STATES:
                logging.info(f'Invalid State: {st}')
    # check the columns which are comma separated states
    for col in df[STATE_CSV_HEADERS].columns:
        for st_l in df[col]:
            # if the value is not a string, we can't split it
            if not type(st_l) is str:
                logging.info(f'Incorrect type for State: {st_l}')
                continue
            # check individual states within the comma separated string
            for st in st_l.split(','):
                if st not in STATES and st != '':
                    logging.info(f'Invalid State: {st}')


# check all the email fields within the data frame
def check_emails(df):
    for col in df[EMAIL_HEADERS].columns:
        for email in df[col]:
            if not validate_email(email):
                logging.info(f'Invalid email: {email}')


# function to apply to Agent License State
def get_num_licensed_states(csv_states):
    if type(csv_states) is not str:
        return 0
    num_states = 0
    for s in csv_states.split(','):
        if s in STATES:
            num_states += 1
    return num_states


# create a plot figure and save it
def create_figure(data, kind, size, x_l, y_l, file_path):
    fig = data.plot(kind=kind, figsize=size)
    fig.set_xlabel(x_l)
    fig.set_ylabel(y_l)
    plt.savefig(figure_path(file_path))
    plt.clf()


# do the actual data processing
def process_file(file_name):
    # list of figure file paths for attachment to email
    figure_ps = []
    # read the data into a data frame
    df = pd.read_csv(data_path(file_name))
    replace_labels(df)
    check_phone_numbers(df)
    check_valid_state(df)
    check_emails(df)
    # log the data frame
    logging.info(f'Full data frame:\n{df}')
    # get the number of states which each agent is licensed in
    df['Num Licensed States'] = df['Agent License State (active)'].apply(get_num_licensed_states)
    # concatenate the agent's full name
    df['Agent Full Name'] = df['Agent First Name'].apply(lambda x: x.replace(' ', '') + ' ') + df[
        'Agent Last Name'].apply(lambda x: x.replace(' ', ''))
    group = df.groupby("Agency State")
    logging.info(f'Grouped by Agency State:\n{group.describe()}')
    logging.info(f'Agent Name, Contract Start Date, Date Agent A20:\n{df[["Agent Full Name", "Agent Writing Contract Start Date", "Date when an agent became A2O"]]}')
    # figure for the number of agents per state
    f_p = f'{file_name[:-4]}_Agent_Count.png'
    create_figure(group.count()['Agent Id'], 'bar', (12, 5), 'State', 'Agents in State', f_p)
    figure_ps.append(f_p)
    # figure for the average number of states each agent in a state is licensed in
    f_p = f'{file_name[:-4]}_Avg_Licensed_States.png'
    create_figure(group.mean()['Num Licensed States'], 'bar', (12, 5), 'State', 'Avg Number of States Licensed In', f_p)
    figure_ps.append(f_p)
    return figure_ps


# log that the file has been processed
def log_processed(file_name):
    logged = [file_name]
    with open(data_path(LST_FILE)) as file:
        for line in file.readlines():
            logged.append(line)
    with open(data_path(LST_FILE), 'w') as file:
        file.writelines(logged)


# send an email
def send_email(subject, body, attachments):
    from email.mime.base import MIMEBase
    from email import encoders
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # SMTP port
    port = 465
    # class for holding all data for the email
    message = MIMEMultipart()
    # add headers
    message['From'] = private.GMAIL_ADDRESS
    message['Subject'] = subject
    # attach body
    message.attach(MIMEText(body, 'plain'))
    # read and attach all files
    for file_name in attachments:
        # read in bytes mode to handle all file types
        with open(file_name, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            # add the file data to the MIME part
            part.set_payload(attachment.read())
        # apparently, encoding in ASCII is necessary for it to be in email
        encoders.encode_base64(part)
        # necessary headers to recognize as file attachment
        part.add_header("Content-Disposition", f'attachment; filename= {file_name}')
        # attach the file
        message.attach(part)
    # convert the message with attachments in order to send
    text = message.as_string()
    context = ssl.create_default_context()
    # connect to the gmail SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        # login to gmail account
        server.login(private.GMAIL_ADDRESS, private.GMAIL_PASSWORD)
        # send email to each recipient
        for recipient in EMAIL_RECIPIENTS:
            server.sendmail(private.GMAIL_ADDRESS, recipient, text)


# reset the logging basic config
def reset_logging():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)


def main():
    # this log tracks malformed files, overwritten for specific date's files
    logging.basicConfig(filename=logs_path('baselog.log'), level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p::')
    # get all the file names which are correctly formatted
    file_names = get_data_filenames()
    # sort them from most recent to earliest
    file_names.sort(key=str_get_int, reverse=True)
    # path to the specific log for this date
    log_path = logs_path(file_names[0][:-3] + 'log')
    reset_logging()
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p::', filemode='w')
    success = validate_preprocessing(file_names)
    if success:
        figure_paths = process_file(file_names[0])
        send_email(f'{file_names[0]} Files', f'Attached is the log file and graphs for the file {file_names[0]}',
                   [log_path] + [figure_path(f) for f in figure_paths])
        log_processed(file_names[0])


if __name__ == '__main__':
    try:
        main()
    except:
        logging.exception('Unknown fatal error')
