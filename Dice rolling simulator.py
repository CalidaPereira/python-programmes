import random

 #Random no. generation between 1 and 6
def rand():
    for i in range(1):
        print(random.randint(1,7))


rand()
while 1:

    answer = input("Do you wish to generate another random no.? Answer Yes or No")
    if answer=="Yes" or answer=="yes":
        rand()
    else:
        print("Ok bye")
        break;





