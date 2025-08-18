from main import best_sub
import json


def iqtest_10th():
    global best_sub
    questions = [
        {"question": "The French Revolution began in the year:","options": ["A. 1789", "B. 1799", "C. 1776", "D. 1804"],"answer": "A","subject": "History"},
        {"question": "Who led the Non-Cooperation Movement?", "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Bhagat Singh"],"answer": "C","subject": "History"},
        {"question": "What was the main objective of the Simon Commission?","options": ["A. Reform education", "B. Introduce federal system", "C. Review constitutional system", "D. Provide independence"],"answer": "C","subject": "History"},
        {"question": "What was the impact of the Great Depression on India?","options": ["A. Increase in employment", "B. Industrial growth", "C. Fall in agricultural prices", "D. Rise in exports"],"answer": "C","subject": "History"},
        {"question": "The 'Rowlatt Act' was passed in the year:","options": ["A. 1917", "B. 1919", "C. 1921", "D. 1923"],"answer": "B","subject": "History"},
        {"question": "The Tropic of Cancer passes through how many Indian states?","options": ["A. 5", "B. 6", "C. 7", "D. 8"],"answer": "D","subject": "Geography"},
        {"question": "Which is the longest river in India?","options": ["A. Ganga", "B. Yamuna", "C. Brahmaputra", "D. Godavari"],"answer": "A","subject": "Geography"},
        {"question": "The Thar Desert is located in which state?","options": ["A. Gujarat", "B. Rajasthan", "C. Haryana", "D. Punjab"],"answer": "B","subject": "Geography"},
       {"question": "Which of the following is a tributary of River Ganga?", "options": ["A. Mahanadi", "B. Godavari", "C. Kosi", "D. Krishna"], "answer": "C", "subject": "Geography"},
       {"question": "Which soil is ideal for cotton cultivation?", "options": ["A. Black soil", "B. Red soil", "C. Laterite soil", "D. Alluvial soil"], "answer": "A", "subject": "Geography"},
        {"question": "What does GDP stand for?", "options": ["A. Gross Domestic Price", "B. Great Domestic Product", "C. Gross Domestic Product", "D. General Domestic Product"], "answer": "C", "subject": "Economics"},
        {"question": "Which sector contributes the most to India GDP?", "options": ["A. Primary", "B. Secondary", "C. Tertiary", "D. Quaternary"], "answer": "C", "subject": "Economics"},
        {"question": "MGNREGA provides:", "options": ["A. Food security", "B. Education", "C. Employment", "D. Housing"], "answer": "C", "subject": "Economics"},
        {"question": "Which is not a characteristic of the organized sector?", "options": ["A. Fixed working hours", "B. Job security", "C. No paid leave", "D. Pension benefits"], "answer": "C", "subject": "Economics"},
        {"question": "Who are considered the working poor?", "options": ["A. Rich businessmen", "B. Politicians", "C. People with low income", "D. Retired persons"], "answer": "C", "subject": "Economics"},
        {"question": "Who is the head of the Indian government?", "options": ["A. President", "B. Chief Justice", "C. Prime Minister", "D. Governor"], "answer": "C", "subject": "Political Science"},
        {"question": "What does the Preamble to the Constitution declare India as?", "options": ["A. Federal Republic", "B. Monarchy", "C. Sovereign, Socialist, Secular, Democratic Republic", "D. Religious State"], "answer": "C", "subject": "Political Science"},
        {"question": "The right to vote is a:", "options": ["A. Fundamental Right", "B. Legal Right", "C. Human Right", "D. Moral Right"], "answer": "B", "subject": "Political Science"},
        {"question": "Who appoints the Chief Justice of India?", "options": ["A. Parliament", "B. President", "C. Prime Minister", "D. Law Minister"], "answer": "B", "subject": "Political Science"},
        {"question": "What ensures separation of powers in a democracy?", "options": ["A. Judiciary", "B. Executive", "C. Legislature", "D. Constitution"], "answer": "D", "subject": "Political Science"},
        {"question": "What is the chemical formula of water?", "options": ["A. H2O2", "B. H2O", "C. HO", "D. OH2"], "answer": "B", "subject": "Chemistry"},
        {"question": "Which of the following is a compound?", "options": ["A. Air", "B. Soil", "C. Water", "D. Milk"], "answer": "C", "subject": "Chemistry"},
        {"question": "Which gas is used in the preparation of soda water?", "options": ["A. Oxygen", "B. Carbon dioxide", "C. Hydrogen", "D. Nitrogen"], "answer": "B", "subject": "Chemistry"},
        {"question": "Rusting of iron is a:", "options": ["A. Physical change", "B. Chemical change", "C. Reversible change", "D. Temporary change"], "answer": "B", "subject": "Chemistry"},
        {"question": "The valency of carbon is:", "options": ["A. 2", "B. 3", "C. 4", "D. 1"], "answer": "C", "subject": "Chemistry"},
        {"question": "Atomic number of oxygen is:", "options": ["A. 6", "B. 8", "C. 10", "D. 12"], "answer": "B", "subject": "Chemistry"},
        {"question": "Which of these is not a noble gas?", "options": ["A. Helium", "B. Neon", "C. Chlorine", "D. Argon"], "answer": "C", "subject": "Chemistry"},
        {"question": "SI unit of force is:", "options": ["a) Newton", "b) Joule", "c) Watt", "d) Pascal"], "answer": "a", "subject": "Physics"},
        {"question": "What is the acceleration due to gravity on Earth?", "options": ["a) 8.9 m/s²", "b) 9.8 m/s²", "c) 10.8 m/s²", "d) 6.8 m/s²"], "answer": "b", "subject": "Physics"},
        {"question": "Which law explains motion of a rocket?", "options": ["a) Newton's First Law", "b) Newton's Second Law", "c) Newton's Third Law", "d) Law of Gravitation"], "answer": "c", "subject": "Physics"},
        {"question": "The speed of light in vacuum is:", "options": ["a) 3 × 10⁶ m/s", "b) 3 × 10⁸ m/s", "c) 3 × 10⁴ m/s", "d) 3 × 10⁷ m/s"], "answer": "b", "subject": "Physics"},
        {"question": "What is the work done when displacement is zero?", "options": ["a) Positive", "b) Negative", "c) Zero", "d) Cannot be determined"], "answer": "c", "subject": "Physics"},
        {"question": "Unit of power is:", "options": ["a) Watt", "b) Joule", "c) Newton", "d) Ohm"], "answer": "a", "subject": "Physics"},
        {"question": "Energy possessed by a body due to motion is called:", "options": ["a) Potential energy", "b) Kinetic energy", "c) Thermal energy", "d) Chemical energy"], "answer": "b", "subject": "Physics"},
        {"question": "Which of these is a unicellular organism?", "options": ["a) Amoeba", "b) Earthworm", "c) Mango tree", "d) Fish"], "answer": "a", "subject": "Biology"},
        {"question": "Basic unit of life is:", "options": ["a) Atom", "b) Cell", "c) Tissue", "d) Organ"], "answer": "b", "subject": "Biology"},
        {"question": "Which part of the plant is involved in photosynthesis?", "options": ["a) Root", "b) Leaf", "c) Stem", "d) Flower"], "answer": "b", "subject": "Biology"},
        {"question": "Which of these is a communicable disease?", "options": ["a) Cancer", "b) Diabetes", "c) Tuberculosis", "d) Hypertension"], "answer": "c", "subject": "Biology"},
        {"question": "Which organ helps in blood purification in humans?", "options": ["a) Heart", "b) Kidney", "c) Lung", "d) Liver"], "answer": "b", "subject": "Biology"},
        {"question": "Which component in blood fights infection?", "options": ["a) RBC", "b) WBC", "c) Platelets", "d) Plasma"], "answer": "b", "subject": "Biology"},
        {"question": "What is the value of √144?", "options": ["a) 10", "b) 11", "c) 12", "d) 13"], "answer": "c", "subject": "Math"},
        {"question": "The value of (a + b)² is:", "options": ["a) a² + b²", "b) a² + 2ab + b²", "c) a² - 2ab + b²", "d) a² - b²"], "answer": "b", "subject": "Math"},
        {"question": "The distance between the points (3, 4) and (0, 0) is:", "options": ["a) 3", "b) 4", "c) 5", "d) 6"], "answer": "c", "subject": "Math"},
        {"question": "The HCF of 12 and 18 is:", "options": ["a) 6", "b) 3", "c) 12", "d) 9"], "answer": "a", "subject": "Math"},
        {"question": "What is the next term in the AP: 5, 9, 13, 17...?", "options": ["a) 21", "b) 22", "c) 23", "d) 25"], "answer": "a", "subject": "Math"},
        {"question": "The number of zeros of the polynomial f(x) = (x – 2)(x + 3) is:", "options": ["a) 0", "b) 1", "c) 2", "d) 3"], "answer": "c", "subject": "Math"},
        {"question": "In the triangle ABC, if angle A = 90°, then sin B =", "options": ["a) AB/AC", "b) AC/BC", "c) BC/AC", "d) AB/BC"], "answer": "c", "subject": "Math"},
        {"question": "A line parallel to one side of a triangle divides the other two sides:", "options": ["a) Equally", "b) In the ratio 1:2", "c) Proportionally", "d) At 90°"], "answer": "c", "subject": "Math"},
        {"question": "The formula for the area of a circle is:", "options": ["a) 2πr", "b) πr²", "c) πd", "d) πr"], "answer": "b", "subject": "Math"},
        {"question": "If the radius of a circle is doubled, its area becomes:", "options": ["a) 2 times", "b) 3 times", "c) 4 times", "d) Half"], "answer": "c", "subject": "Math"},
        {"question": "The surface area of a cube with edge 5 cm is:", "options": ["a) 100 cm²", "b) 150 cm²", "c) 200 cm²", "d) 150 cm³"], "answer": "b", "subject": "Math"},
        {"question": "In a frequency polygon, data is represented using:", "options": ["a) Bars", "b) Circles", "c) Line segments", "d) Boxes"], "answer": "c", "subject": "Math"},
        {"question": "The graph of a linear equation in two variables is a:", "options": ["a) Point", "b) Curve", "c) Line", "d) Circle"], "answer": "c", "subject": "Math"},
        {"question": "If 3x = 12, then x =", "options": ["a) 2", "b) 3", "c) 4", "d) 6"], "answer": "c", "subject": "Math"},
        {"question": "The sum of the first 10 natural numbers is:", "options": ["a) 50", "b) 55", "c) 60", "d) 45"], "answer": "b", "subject": "Math"},
        {"question": "A rational number between 1/2 and 3/4 is:", "options": ["a) 1/3", "b) 2/3", "c) 5/6", "d) 1/4"], "answer": "b", "subject": "Math"},
        {"question": "A number is divisible by 3 if:", "options": ["a) It ends in 0", "b) It ends in 5", "c) The sum of digits is divisible by 3", "d) It is even"], "answer": "c", "subject": "Math"},
        {"question": "In △ABC, if AB = AC and angle B = 40°, then angle C =", "options": ["a) 50°", "b) 60°", "c) 40°", "d) 100°"], "answer": "c", "subject": "Math"},
        {"question": "A cylinder has a height of 10 cm and radius of 7 cm. Its volume is:", "options": ["a) 1540 cm³", "b) 440 cm³", "c) 220 cm³", "d) 980 cm³"], "answer": "a", "subject": "Math"},
        {"question": "Median of 5, 10, 15, 20, 25 is:", "options": ["a) 10", "b) 15", "c) 20", "d) 25"], "answer": "b", "subject": "Math"}
 ]

    score = {"History": 0, "Political Science": 0, "Geography": 0, "Economics": 0, "Chemistry": 0, "Biology": 0, "Math": 0, "Physics": 0}
    count = 1
    for q in questions:
        print("\nQ" + str(count) + ". " + q["question"])
        for opt in q['options']:
            print(" " + opt)
        ans = input("Your answer (a/b/c/d): ").strip().lower()
        if ans == q['answer']:
            score[q['subject']] += 1
        count += 1
    
    best = max(score, key=score.get)   
    max_score = score[best]            
    if max_score < 7:
        best_sub = ["No subject"]  
    else:
        best_sub = [best] 

    with open('data.json', 'r') as file:
      data = json.load(file)

    
    data["score"] = f'{score}'
    data['best_subject'] = f'{best_sub}'

    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)


