for i in range(1, 11):
    # 1
    print()
    for j in range(1, 11):
        # 1 * 1
        # 1 * 2
        # ...
        print(str(i * j) + " ", end='')

phone_list = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']

print()
print()


print(len(phone_list))

for index, value in enumerate(phone_list):
    if (index + 1) % 3 == 0:
        print(index + 1)
        print(value)
