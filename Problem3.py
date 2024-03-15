class User:
    def __init__(self, user, name, age, email, phone_number):
        self.user = user
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def change_user(self, new):
        self.user = new

    def change_name(self, new):
        self.name = new

    def change_age(self, new : int):
        if new >= 18:
            self.age = new
        else:
            print("Siz voyaga yetmagansiz")

    def change_email(self, new : str):
        if new.endswith("@gmail.com"):
            self.email = new
        else:
            print("Your new email must end with @gmail.com")

    def change_phone_number(self, new : str):
        if new.startswith("+998"):
            self.phone_number = new
        else:
            print("Your new phone number must begin with +998")

    def info(self):
        print(f"User name {self.user}\nName {self.name}\nAge {self.age}\nEmail {self.email}\nPhone number {self.phone_number}\n")


user_name = input("Enter your user name: ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter email: ")
phone_number = input("Enter your phone number: ")
print()

if age >= 18 and email.endswith("@gmail.com") and phone_number.startswith("+998"):
    U = User(user_name, name, age, email, phone_number)
    U.info()
else:
    print("Kiritgan ma'lumotlaringizda hatolik bor")

print("----------------------------------")

print("You want to change your user datas")
answer = input("Choose Yes or No: ")

if answer.lower == "yes":
    U.change_user(input("Enter new user name: "))
    U.change_name(input("Enter new name: "))
    U.change_age(int(input("Enter new age: ")))
    U.change_email(input("Enter new email: "))
    U.change_phone_number("Enter new phone number: ")
    U.info()    