import os

import requests

api_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/"


def get_all_currencies():
    res = requests.get(api_url + "currencies.json")
    return res.json()


def get_currency_rate(currency, main_currency):
    res = requests.get(api_url + "currencies/" + currency + ".json")
    return res.json()[currency][main_currency]


def main():
    main_currency = "uah"
    currency_codes = get_all_currencies()
    currency_list = []
    while True:
        os.system("cls")
        print("Меню\n\n1. Додати валюту\n2. Вивести курси\n3. Завершити\n\n")
        match input("Оберіть функцію: "):
            case "1":
                os.system("cls")
                currency_list.append(input("Введіть код валюти: "))
            case "2":
                os.system("cls")
                print(currency_codes[main_currency] + " (" + main_currency.upper() + ")\n")
                for currency in currency_list:
                    print(currency_codes[currency] + " (" + currency.upper() + "): " + str(get_currency_rate(currency, main_currency)) + " " + main_currency.upper())
                input("Натисніть Enter, щоб продовжити...")

            case "3":
                break


main()
