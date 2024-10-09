from datetime import datetime

import requests
import xml.etree.ElementTree as ET

date = datetime.now().strftime('%d/%m/%Y')
url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={date}'


# official Central Bank currency exchange rate on current date
async def calculate_cb(source: str, to_convert: float,
                       destination: str = None):
    # obtaining and processing xml
    response = requests.get(url)
    print(response.status_code)
    proc = ET.fromstring(response.text)
    # because all data from central bank linked to rub
    if source in ('rub', 'RUB'):
        val = 1
    else:
        # getting currency rate by currency name(except rub)
        val = float(
            proc.find(f"./Valute[CharCode='{source.upper()}']/Value").text.
            replace(',', '.'))
    # getting second currency rate by currency name(except rub)
    if destination and destination not in ('rub', 'RUB'):
        val_2 = float(
            proc.find(f"./Valute[CharCode='{destination.upper()}']/Value").text.
            replace(',', '.'))
        answer = (to_convert * val) / val_2
    # because all data from central bank linked to rub, directly multiply values
    else:
        answer = to_convert * val
    # formatting according to technical specification(2 signs after point)
    return "{:.2f}".format(answer)

res = requests.get(url)
print(res.status_code)