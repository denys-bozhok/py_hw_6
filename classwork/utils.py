from random import randint
#
# from model import symbols
# from random import randint
#
# def to_list(string:str) :
#     new_list = string.split(",")
#
#     return new_list
#
#
# def generate_password(amount_of:int) -> str:
#     password = ""
#
#     for i in range(amount_of):
#         latter_index = randint(0 , len(symbols) - 1)
#         password += symbols[latter_index - 1]
#
#     return password
#
#
# def push_to(arr:list , element:any) -> None:
#     arr.append(element)
#
# # to_list("HTML,C#,Hello world")

from model2 import symbols

def push_to(arr:list, element:any):
    arr.append(element)
def to_list(string:str) -> str:
    new_arr = string.split(",")
    return new_arr

def generator_password (amount_of:int) -> str:
    password = ""

    for i in range(amount_of):
        latter_index = randint(0, len(symbols) - 1)
        password += (symbols[latter_index - 1])

    return password

def check_email(email:str) -> bool:
    return "." in email and "@" in email

def get_email(name):
    student_email = input("Enter your E-mail")

    if not check_email(student_email):
        print("Incorrect email. We generated its for u")
        return generator_email(student_email, name)
    else:
        return student_email

def generator_email (email:str, name):
    new_email = ""

    new_email += email + name + "@" + "gmail.com"
    print(f"Your email is : {new_email}")
    return new_email


to_list("Html, CSS, Python")