from random import choice
def add_text_on_your_car():
    def your_random_car():
        car=('Honda','Lexus','BMW','Lada','Mercedes','Mazda')
        random=choice(car)
        return random
    def yor_random_text():
        text=('is non fast!',
              'is non beautiful!',
              'is very beautiful!',
              'is real fast car!',
              'this car non bad',
              'this car great!',
              'yes! I want this car!')
        random=choice(text)
        return random
    return print(your_random_car()+','+' '+yor_random_text())
while True:
    add_text_on_your_car()
    print("Do you agree?")
    choice_user=input()
    if choice_user.lower()=='yes':
        print("Okey, goodbye!! :)))))))))")
        break
    if choice_user.lower()=='no':
        print("Read again: ")
    else:
        print('Yes or no')
