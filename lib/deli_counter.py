katz_deli = []


def line(katz_deli):
    if len(katz_deli) > 0:
        current_line = [
            f"{index}. {person}" for index, person in enumerate(katz_deli, start=1)
        ]
        print(f"The line is currently: {' '.join(current_line)}")
    else:
        print("The line is currently empty.")


def take_a_number(katz_deli, name):
    number_in_line = len(katz_deli) + 1
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {number_in_line} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        person_served = katz_deli[0]
        print(f"Currently serving {person_served}.")
        del katz_deli[0]


take_a_number(katz_deli, name="Mai")
take_a_number(katz_deli, name="Lis")
take_a_number(katz_deli, name="Katherine")


print(line(katz_deli))

print(now_serving(katz_deli))

print(katz_deli)
