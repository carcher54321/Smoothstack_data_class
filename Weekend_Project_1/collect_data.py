import logging
import openpyxl as xl
import datetime as dt

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
file_to_open = 'expedia_report_monthly_january_2018.xlsx'


# get the shortened month/year from the file name
def get_date(file_name):
    MONTHS = {'january': 1, 'february': 2,
              'march': 3, 'april': 4,
              'may': 5, 'june': 6,
              'july': 7, 'august': 8,
              'september': 9, 'october': 10,
              'november': 11, 'december': 12}
    month, year = file_name.split('_')[-2:]
    try:
        month = MONTHS[month.lower()]
    except KeyError:
        logging.warning(f'Malformed filename: {file_name}')
    return month, int(year[:4])


def collect_data(file_name):
    def collect_voc_data(sheet, month, year):
        def map_func(t):
            lb, num = t
            ret = [lb, num]
            if lb == 'Promoters':
                ret.append('good' if num > 200 else 'bad')
            elif lb == 'Passives':
                ret.append('good' if num > 100 else 'bad')
            elif lb == 'Detractors':
                ret.append('good' if num < 100 else 'bad')
            elif lb in ['Overall NPS', 'Sat With Agent', 'DSat with Agent']:
                ret[1] = f'{num * 100}%'
            return ret
        # (label, cell row)
        form = [
            ('Promoters', 4),
            ('Passives', 6),
            ('Detractors', 8),
            ('Overall NPS', 13),
            ('Sat With Agent', 16),
            ('DSat with Agent', 19)
        ]
        columns = 'BCDEFGHIJKLMNOPQRSTUVWX'
        data = []
        for c in columns:
            dte = sheet[c + '1'].value
            if dte.month == month and dte.year == year:
                for label, cell in form:
                    data.append([label, sheet[c + str(cell)].value])
                break
        data = list(map(map_func, data))
        for r in data:
            logging.info(f'{r[0]}: ' + ', '.join([str(x) for x in r[1:]]))

    def collect_sum_data(sheet, month, year):
        # (label, column)
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
            dte = sheet[f'A{n}'].value
            if dte.month == month and dte.year == year:
                # gather data
                for label, cell in form:
                    data.append([label, sheet[cell.replace('#', str(n))].value])
                break
        # convert percentages
        data = list(map(lambda x: [x[0], f'{x[1] * 100}%'] if x[1] < 1 else x, data))
        for label, value in data:
            logging.info(f'{label}: {value}')

    wb = xl.load_workbook(file_name, data_only=True)
    summary_sheet = wb['Summary Rolling MoM']
    voc_sheet = wb['VOC Rolling MoM']
    mo, yr = get_date(file_name)
    logging.info('------------------')
    logging.info(f'{mo}/{yr} Data:')
    collect_sum_data(summary_sheet, mo, yr)
    collect_voc_data(voc_sheet, mo, yr)


collect_data(file_to_open)


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
