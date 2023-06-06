from model import students
from utils import to_list, generator_password, push_to, get_email

young_group, adult_group = students
group_amount = len(students)

def registration (name:str, age:int, skills:str, password:str, email:str) -> dict:

    skills_collection = to_list(skills)

    return {
        "name" : name,
        "age" : age,
        "skills" : skills_collection,
        "password" : password,
        "E-mail" : email
    }


def main ():

    is_registred = False
    is_running = True

    context_menu = {
        "a" : "Registration",
        "b" : "Platform",
        "q" : "Exit"
    }

    while is_running:

        print("Greeting")

        for key , value in context_menu.items():

            if key == "b" and is_registred == False:
                continue

            if key == "a" and is_registred == True:
                continue

            print(key + ") " + value)

        picked_element = input("[Enter your answer :]\n")

        match(picked_element):
            case "a" :
                student_name = input("Enter your name")

                if len(student_name) < 5:
                    print("\nEnter name by 5 symbols and more\n")
                    continue

                try:
                    student_age = int(input("Enter your age"))
                except:
                    print("\nEnter a numbers\n")
                    continue

                if student_age < 5:
                    print("\nYou are small\n")
                    break

                student_skill = input("Enter your skills by coma")

                if len(student_skill) < 1:
                    print("Enter skills")
                    continue

                # get_email(student_name)

                new_student = registration(student_name, student_age, student_skill, generator_password(23), get_email(student_name))

                picked_group = int(input(f"Enter a numder of group you change from {group_amount} :\n"))

                try:
                    push_to(students[picked_group - 1], new_student)
                    is_registred = True
                    print(students)

                except:
                    print("Something wrong")

            case "b" :
                if is_registred:
                    print("First of all you have to have an account here!")

            case "q":
                is_running = False

            case _:
                print("\nIncorrect data\n"
                      "Please, try again\n")

if __name__ == "__main__":
    main()