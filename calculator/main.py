import re

print("Welcome to MagiCalc!")
print("type x to exit")

previous = 0
run = True


def perform_math():
    global previous
    global run
    equation = ""
    if previous == 0:
        equation = input("Please input equation: ")
    else:
        equation = input(str(previous))

    if equation == 'x':
        print('Goodbye human!')
        run = False
    else:
        equation = re.sub('[A-Za-z:,()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
