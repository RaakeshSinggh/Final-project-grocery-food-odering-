import admin as admin
from user import User

user = User(str, str, str, str, str)
# start code
temp_variable = 1
temp = True
Temp_var = True
while Temp_var:

    inp = int(
        input(
            "Where You Want to Login?? 1. Admin  2. User  3. User Registration 4. Exit:   "
        ))
    if temp_variable == 0:
        temp = True
# check inp
    if inp == 1:
        print("Login AS  Admin Panel..")
        username = input("Enter a Username: ")
        password = input("Enter a Password: ")
        if admin.admin_info[username] == password:
            print(
                "you Logged in ********** Successfully  ********************")
            while Temp_var:
                admin_input = int(
                    input(
                        "Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW MENU CARD 4.REMOVE ITEM 5.EXIT  "
                    ))
                if admin_input == 1:
                    admin.add_food_item()
                elif admin_input == 2:
                    admin.edit_food_item()
                elif admin_input == 3:
                    admin.show_menu_item()
                elif admin_input == 4:
                    admin.removing_food_item()
                elif admin_input == 5:
                    print(f"You're Exit to the admin panel   {username}")
                    Temp_var = False
                else:
                    print("Wrong input Please Read Carefully Instruction  !!!")

        else:
            print("Invalid Credentials !!!!! ")

    elif inp == 2:
        print("Login As User Panel..")
        email_enter = input("Enter a Email: ")
        password = input("Enter a Password: ")

        if User.login(email_enter, password):

            while temp:
                choice_user = int(
                    input(
                        f"{email_enter},Enter the option 1. Place new order 2. Order history 3. Update Profile 4. Exit  "
                    ))
                if choice_user == 1:
                    user.place_new_order()

                elif choice_user == 2:
                    user.order_history_see()

                elif choice_user == 3:
                    user.update_profile()
                    temp = False
                    temp_variable = 0

                elif choice_user == 4:
                    print("You're Successfully looged out")
                    temp = False
                    temp_variable = 0

						
                else:
                    print("Wrong Number Please follow this Instruction  ")

    elif inp == 3:

        new_email = input("Enter new  Email: ")
        if new_email in User.login_info.keys():
            print("Email Already Registered.......")
        else:
            print("Enter Your Detail Here...")
            new_name = input("Enter new  Name: ")
            new_phone_no = int(input("Enter new  Phone No: "))
            new_Address = input("Enter new  Address: ")
            new_password = input("Enter new  Password: ")
            user = User(new_email, new_name, new_phone_no, new_Address,
                        new_password)

            print("Your have Registered Successfully.......")
            print("Now you can Login... ")

    elif inp == 4:
        Temp_var = False
        exit()

    else:
        print("Follow option's ")
