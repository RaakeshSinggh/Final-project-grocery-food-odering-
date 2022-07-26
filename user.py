import admin as ad


# User Module
#menu_card = {"Email": {"Full_Name": "Rakesh", "Phoneno": 7017329358, "Address": 235, "Password": Rakesh@810324}}
class User:
    login_info = {}

    def __init__(self, email, name, phoneno, address, password):
        print("Register on the Application")
        self.email = email
        self.name = name
        self.phoneno = phoneno
        self.address = address
        self.password = password
        User.login_info[self.email] = {
            "Email": self.email,
            "Full_Name": self.name,
            "Phoneno": self.phoneno,
            "Address": self.address,
            "Password": self.password,
        }
        self.order_history = {}

#{1:{"foodId":1,"Name":"Vegan Burger","Quantity":20,"Price":320,"Discount":5,"Stock":20},

    def place_new_order(self):
        print("What do you want to order here in at the Restaurent ")
        ad.show_menu_item()
        User_choice = int(
            input("If you want to order then select 1.YES  2.NO"))
        if User_choice == 1:
            n = int(input("How many Item do You Want to Order "))
            x = 0
            y = 0
            for i in range(n):
                itemid = int(input("Enter the Item id here: "))
                quan = int(input("Enter the quantity of the item: "))
                #here x for bill and y for discount
                x += ad.menu_list[itemid]["Price"] * quan
                y += ad.menu_list[itemid]["Discount"]
                ad.menu_list[itemid][
                    "Stock"] = ad.menu_list[itemid]["Stock"] - quan
                # Add Item in User List
                self.order_history[itemid] = {
                    "Name": ad.menu_list[itemid]["Name"],
                    "Price": ad.menu_list[itemid]["Price"],
                    "Quantity": quan
                }
            again_ask = input("Confirmed ?? Yes Otherwise NO ")
            if again_ask == "Yes":
                print(f"Total Discount Allowed is {y} ")
                print(f"After Deduced Discount It costs is {x-y} INR in total")
                print("You're order is successfully placed...")

            elif again_ask == "No":
                print("Your Order has Cancelled Now...")
                self.order_history.clear()

            else:
                print("Invalid Input...")

        elif User_choice == 2:
            print("You Selected 2 option So we Cancelled This....")

        else:
            print(" Invalid no.... ")

    def order_history_see(self):
        print(self.order_history)

    def update_profile(self):
        print("****Update Profile Here****")
        email = input("Enter Your Mail-id: ")
        if email in User.login_info.keys():
            print("Email Matched !!!!")
            del User.login_info[email]

            # update
            new_email = input("Enter new  Email: ")
            new_name = input("Enter new  Name: ")
            new_phoneno = int(input("Enter new  Phone No: "))
            new_Address = input("Enter new  Address: ")
            new_password = input("Enter new  Password: ")

            User.login_info[new_email] = {
                "Email": new_email,
                "Full_Name": new_name,
                "Phone_no": new_phoneno,
                "Address": new_Address,
                "Password": new_password,
            }
            print("*****Profile Updated Successfully *****")

        else:
            print("Email not Registered... Please Try Again****  ")

    @classmethod
    def login(cls, email, password):
        if email in cls.login_info.keys():
            if cls.login_info.get(email)["Password"] == password:
                print(
                    f"logged in  *******  Successfully  ********** {cls.login_info.get(email)['Full_Name']}"
                )
                return True
            else:
                print("SORRY!!! These are the Wrong Credentials")
                return False
        else:
            print(
                f"{email} Not Registered ... First Register then Come Again !!!!! "
            )
            return False


