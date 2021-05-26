from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))

def currency_rates(cod_val):
    val = response.split("Valute ID=")
    date = response.split("ValCurs Date=")[-1].split("name=")[0]
    for i in val:
        if cod_val.upper() in i:
            list_ = [float(i.replace("/", "").split("<Value>")[-2].replace(",", ".")), date[1:-2]]
            return list_




# a = input("Введите код валюты --->  ")
print(currency_rates("USD"))
print(currency_rates("aud"))
print(currency_rates("aboba"))
