from app.UI.menus import menu
import app.BL.customer_car_controller as cc
from app.UI.ui_functions import f_input, print_amount_matches, divider, print_list_of_tablerows, print_tablerow


def get_all_customer_cars():
    customer_cars = cc.get_all_customer_cars()
    print_list_of_tablerows(customer_cars)
    print_amount_matches(customer_cars)


def search_customer_cars_menu():
    def inner(column):
        return lambda: get_customer_cars_by_columnvalue(column)

    menu({str(i+1): {"info": c, "func": inner(c)} for i, c in enumerate(cc.get_columns())})


def get_customer_cars_by_columnvalue(column_name):
    print(f"enter searchvalue for {column_name}")
    name = f_input()
    customer_cars = cc.get_customer_cars_by_columnvalue(column_name, name)
    print_list_of_tablerows(customer_cars)
    print_amount_matches(customer_cars)


def update_customer_car():
    print("enter a license number: ")
    c_id = f_input()
    customer_car = cc.get_customer_car_by_id(c_id)

    def inner(column, customer_car):
        return lambda: update_customer_car_column(column, customer_car)

    menu({str(i + 1): {"info": c, "func": inner(c, customer_car)} for i, c in enumerate(cc.get_columns())})


def update_customer_car_column(column, customer_car):
    print("Enter new value: ")
    value = f_input()
    cc.update_customer_car_column(customer_car, column, value)
    print_tablerow(customer_car)


def combine_customer_car(customer_id, license_number):
    cc.add_customer_car({
        "CustomerId": customer_id,
        "LicenseNumber": license_number
    })


def add_customer_car():
    insert_dict = {}
    for column in cc.get_columns():
        if column != "id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    customer_car = cc.add_customer_car(insert_dict)


def drop_customer_car_by_license_number():
    print("Enter a license number to delete customer_car")
    c_id = f_input()
    cc.drop_customer_car_by_license_number(c_id)


def customer_car_menu():
    menu({
        "1": {
            "info": "get all customer_cars",
            "func": get_all_customer_cars
        },
        "2": {
            "info": "search customer_cars",
            "func": search_customer_cars_menu
        },
        "3": {
            "info": "update a customer_car by id and column",
            "func": update_customer_car
        },
        "4": {
            "info": "add a customer_car",
            "func": add_customer_car
        },
        "5": {
            "info": "drop customer_car by license number",
            "func": drop_customer_car_by_license_number
        }
    })


if __name__ == '__main__':
    customer_car_menu()
