import logging
import openpyxl as xl
import datetime as dt

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)


# get the shortened month/year from the file name
def config_name(file_name):
    MONTHS = {'january': 'Jan', 'february': 'Feb',
              'march': 'Mar', 'april': 'Apr',
              'may': 'May', 'june': 'Jun',
              'july': 'Jul', 'august': 'Aug',
              'september': 'Sep', 'october': 'Oct',
              'november': 'Nov', 'december': 'Dec'}
    month, year = file_name.split('_')[-2:]
    try:
        month = MONTHS[month.lower()]
    except KeyError:
        logging.warning(f'Malformed filename: {file_name}')
    return f'{month}-{year[2:4]}'


def collect_data(file_name):
    def format_date(date):
        if not (type(date) is dt.date or type(date) is dt.datetime):
            logging.warning(f'Date Error: {date}')
        MONTHS = [0, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return f'{MONTHS[date.month]}-{str(date.year)[2:]}'

    def collect_voc_data(sheet, name):
        def map_func(t):
            lb, num = t
            if lb == 'Promoters':
                cat = 'good' if num > 200 else 'bad'
            elif lb == 'Passives':
                cat = 'good' if num > 100 else 'bad'
            else:
                cat = 'good' if num < 100 else 'bad'
            return lb, num, cat
        form = [
            ('Promoters', 4),
            ('Passives', 6),
            ('Detractors', 8)
        ]
        columns = 'BCDEFGHIJKLMNOPQRSTUVWX'
        data = []
        for c in columns:
            if format_date(sheet[c + '1'].value) == name:
                for label, cell in form:
                    data.append([label, sheet[c + str(cell)].value])
        data = list(map(map_func, data))
        for label, total, c in data:
            logging.info(f'{label}: {total}, {c}')

    def collect_sum_data(sheet, name):
        form = [
            ('Calls Offered', 'B#'),
            ('Abandon after 30s', 'C#'),
            ('FCR', 'D#'),
            ('DSAT', 'E#'),
            ('CSAT', 'F#')
        ]
        data = []
        # find the right row
        for n in range(2, 14):
            if format_date(sheet[f'A{n}'].value) == name:
                # gather data
                for label, cell in form:
                    data.append([label, sheet[cell.replace('#', str(n))].value])
        # convert percentages
        data = list(map(lambda x: [x[0], f'{x[1] * 100}%'] if x[1] < 1 else x, data))
        for label, value in data:
            logging.info(f'{label}: {value}')

    wb = xl.load_workbook(file_name, data_only=True)
    summary_sheet = wb['Summary Rolling MoM']
    voc_sheet = wb['VOC Rolling MoM']
    c_name = config_name(file_name)
    logging.info('------------------')
    logging.info(f'{c_name} Data:')
    collect_sum_data(summary_sheet, c_name)
    collect_voc_data(voc_sheet, c_name)


collect_data('expedia_report_monthly_march_2018.xlsx')


# fix the data in the march spreadsheet to match the correct format
def fix_data():
    filename = 'expedia_report_monthly_march_2018.xlsx'
    wb = xl.open(filename)
    sheet = wb['VOC Rolling MoM']
    sheet['B1'] = dt.date(2018, 3, 1)
    sheet['C1'] = dt.date(2018, 2, 1)
    sheet['D1'] = dt.date(2018, 1, 1)
    wb.save(filename)


# fix_data()
