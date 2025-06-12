import json
from iqtest_com import *
from iqtest_humanities import *
from iqtest_sci_bio import *
from iqtest_sci_math import *
from iqtest_10th import *
from eqtest import eqtest
import time
import sys

best_sub = ''

print("""


 ______  _________ _______  _______           _______ 
(  __  \ \__   __/(  ____ )(  ____ \|\     /|(  ___  )
| (  \  )   ) (   | (    )|| (    \/( \   / )| (   ) |
| |   ) |   | |   | (____)|| (__     \ (_) / | (___) |
| |   | |   | |   |     __)|  __)     ) _ (  |  ___  |
| |   ) |   | |   | (\ (   | (       / ( ) \ | (   ) |
| (__/  )___) (___| ) \ \__| (____/\( /   \ )| )   ( |
(______/ \_______/|/   \__/(_______/|/     \||/     \|
                                                      


""")


name = input("Hey There! Welcome to Direxa! Please enter your name\n")
age = int(input(f"Hello {name}! Please enter your age.\n"))
grade = int(input("Please enter your class\n"))

if grade > 10:
    stream = input("Finally, please enter your stream. (science/humanities/commerce) \n").lower()

else:
    stream = None



data = {
    "name" : f"{name}",
    "age": f'{age}',
    "grade": f'{grade}',
    "stream": f'{stream}',
}

with open('data.json', 'w') as data_file:
    json.dump(data, data_file, indent=4)

time.sleep(1)

print("All done! You're all set up and ready to work. We'll first be taking your IQ Test. \n")

total = 25
for i in range(total + 1):
    percent = int((i / total) * 100)
    bar = ('#' * i).ljust(total)
    sys.stdout.write(f"\r[{bar}] {percent}%")
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(1)

if stream == 'science':
    math_bio = input("\n\nPCM or PCB?\n").lower()
    if math_bio == 'pcm':
        iqtest_sci_math()
    elif math_bio == 'pcb':
        iqtest_sci_bio()

elif stream == 'humanities':
    iqtest_humanities()

elif stream == 'commerce':
    iqtest_com()

elif grade <= 10 and grade > 8:
    iqtest_10th()

print("All done! Now, we'll be taking a quick EQ test based on your best scored subject.")

time.sleep(2)

total = 25 
for i in range(total + 1):
    percent = int((i / total) * 100)
    bar = ('#' * i).ljust(total)
    sys.stdout.write(f"\r[{bar}] {percent}%")
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(2)

eqtest()