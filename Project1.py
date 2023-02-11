while True:
    number_one=input("Введіть ваше число: ")
    number_two=input("Введіть ваше друге число: ")
    if number_one == 'end' or number_two == 'end':
        break
    print((pow(int(number_one),int(number_two))))
