import json
from iqtest_com import *
from iqtest_humanities import *
from iqtest_sci_bio import *
from iqtest_sci_math import *
from iqtest_10th import *


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


print("All done! You're all set up and ready to work. We'll first be taking your IQ Test. \n")

if stream == 'science':
    math_bio = input("PCM or PCB?\n").lower()
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

subject_careers = {
    "Mathematics": ["Ethical Hacker", "Pilot", "Data Analyst"],
    "Biology": ["Doctor", "Psychologist"],
    "Accountancy": ["Chartered Accountant"],
    "Political Science": ["Lawyer", "Politician"],
    "History": ["Archaeologist"],
    "Commerce": ["Entrepreneur"],
    "PCM": ["Defense", "Engineer"],
    "Science": ["Astronaut"],
    "Any (score > 98%)": ["Teacher"],
    "No subject": [
        "Sports", "Fashion Designer", "Influencer", "Artist",
        "UI/UX Designer", "Video Editor", "Career Counselor",
        "Prompt Engineering", "Photographer"
    ]
}

with open('data.json', 'r') as file:
    data = json.load(file)

try:
    print(subject_careers[data['best_subject']])

except KeyError as e:
    print("We're still working on getting more careers related to your best subject!")