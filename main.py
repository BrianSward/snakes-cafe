logo = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
*********************************** 
"""

user_input = {

}


def order():
    """function to get order for foods"""
    ask_again = True
    print(logo)
    while ask_again:
        user_order = input("> ")
        if user_order != "quit":
            if user_order in user_input:
                user_input[user_order] += 1
                print(f"** {user_input[user_order]} orders of {user_order} have been added to your meal. **")
            else:
                user_input[user_order] = 1
                print(f"** {user_input[user_order]} order of {user_order} have been added to your meal. **")
        else:
            ask_again = False


if __name__ == "__main__":
    order()
