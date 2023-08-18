foods = []
more = True

print("Add your foods. Enter 'q' to quit.")
while more:
    answer = input("Enter the name of a food: ")
    if answer == 'q':
        more = False
    else:
        foods.append(answer)

print(foods)

print(range(len(foods)))


def print_list(nice_list):
    for i in range(len(nice_list)):
        print(str(i + 1) + ". " + nice_list[i])


# the enumerated list produces tuples with index, value
def print_list_enumed(ugly_list):
    for i, value in enumerate(ugly_list):
        print(str(i) + ". " + str(value))


# A tuple doesn't need to be index, value. It is actually
# a lot like a Java class. Each attribute in the tuple
# is like a class attribute. Behaviours (if any) are set by  the tuple.

print_list(foods)
print("enumed list: ")
print_list_enumed(foods)

first, last = ("james", "Moffat")
print(first.title() + " " + last.title())


def get_date():
    return (8, 16, 2023)


month, day, year = get_date()
print(get_date())
print(month)

letters = ['a', 'b', 'c']
print("List: ")
print(list)
print("Enumerated List: ")
print(list(enumerate(letters)))

i = 0
print("[", end='')
for letter in letters:
    e, l = i, letter
    # print(str(e) + ", " + str(l))
    print(f"({e}, '{l}')", end='')
    if i == len(letters) - 1:
        print("]", end='')
    else:
        print(", ", end='')
    i = i + 1

print("")
print("")
print("")

print("prime numbers")
for i in range(1, 100):
    factors = []
    for j in range(1, i + 1):
        if i % j == 0:
            factors.append(j)
    print(f"The factors of {str(i)} are {str(factors)}")
    # if len(factors) == 2:
    # print(f"The factors of {str(i)} are {str(factors)}")


def add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "invalid entry"


while True:
    print("add two numbers, press q to quit: ")
    first = input("number 1: ")
    second = input("number 2: ")
    numbers = first, second
    if "q" in numbers:
        break
    print(add(first, second))

for i in range(10):
    for j in range(i):
        print(i + j)