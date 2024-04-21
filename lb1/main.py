import os

receipt_list = []


def add_receipt():
    receipt = {"name": input("Введіть ім'я: "), "amount": 0, "dish_list": []}

    while True:
        print("Додавання рахунку\n\n1. Додати страву\n2. Завершити\n\n")
        match input("Оберіть дію: "):
            case "1":
                print("Додати страву\n")
                dish_name = input("Введіть назву: ")
                price = input("Введіть ціну: ")
                quantity = input("Введіть кількість: ")
                receipt["amount"] += float(price) * int(quantity)
                receipt["dish_list"].append({
                    "dish_name": dish_name,
                    "price": price,
                    "quantity": quantity
                })
            case "2":
                break
    receipt_list.append(receipt)


def sum_all():
    total_amount = 0
    for receipt in receipt_list:
        total_amount += receipt["amount"]
    return total_amount





def show_all():
    for receipt in receipt_list:
        print("----------------------------------------")
        print("Name: " + receipt["name"])
        for dish in receipt["dish_list"]:
            print(dish["dish_name"] + "\t" + str(dish["price"]) + "\t x" + str(dish["quantity"]))
        print("\n\t Amount: " + str(receipt["amount"]))
        print("----------------------------------------\n")


def main():
    while True:
        os.system("cls")
        print("Меню\n\n1. Додати рахунок\n2. Загальна сума всіх рахунків\n3. Список рахунків\n4. Завершити\n\n")
        match input("Оберіть функцію: "):
            case "1":
                os.system("cls")
                add_receipt()
            case "2":
                os.system("cls")
                print("Загальна сума всіх рахунків\n")
                print(str(sum_all()) + "\n")
                input("Натисніть Enter, щоб продовжити...")
            case "3":
                os.system("cls")
                print("Список рахунків\n")
                show_all()
                input("Натисніть Enter, щоб продовжити...")
            case "4":
                break


main()
