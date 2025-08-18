import json
import turtle

def eqtest():

    subject_careers = {"Mathematics": ["Ethical Hacker", "Pilot", "Data Analyst","Astronaut","Defense", "Engineer", "Astronaut", "Architect","Teacher"],
        "Biology": ["Doctor", "Psychologist","Teacher"],
        "Accountancy": ["Chartered Accountant","Teacher"],
        "Political Science": ["Lawyer", "Politician","Teacher"],
        "History": ["Archaeologist","Teacher"],
        "Business Studies": ["Entrepreneur","Teacher"],
        "Physics": ["Defense", "Engineer", "Astronaut", "Architect","Astronaut","Teacher"],
        "Chemistry": ["Defense", "Engineer", "Astronaut", "Architect","Teacher"],
        "No subject": ["Sports", "Fashion Designer", "Influencer", "Artist","UI/UX Designer", "Video Editor", "Career Counselor","Prompt Engineering", "Photographer","Teacher"]}


    career_questions = {"Ethical Hacker": ["Would you consider yourself a tech savvy person?","Do you enjoy solving puzzles?","Would you prefer a desk job?"],
        "Doctor": ["Would you consider yourself as an empathetic person?", "Are you up for long hours of work?", "Would you prefer an active field job?"],
        "Psychologist": ["Are you interested in human psychology?", "Are you approachable and lead to people opening up to you?", "Are you an extrovert?"],
        "Entrepreneur": ["Would you consider yourself a good leader?", "Are you up for taking risks in your career?", "Are you an extrovert?"],
        "Teacher": ["Would you consider yourself as an empathetic person?", "Are you adaptable in nature?", "Are you an extrovert?", "Do you have good mentorship skills?", "Are you a good communicator?"],
        "Lawyer": ["Are you a good communicator?", "Are you a good observer by nature?", "Would you consider yourself a good debater?", "Would you prefer an active field job?"],
        "Sports": ["Do you enjoy sports?", "Are you proud of your sports accomplishments?", "Are you up for long hours of physical training?", "Would you consider yourself fit?"],
        "Chartered Accountant": ["Would you prefer a desk job?", "Do you enjoy working with numbers and finances?"],
        "Pilot": ["Do you have a good memory?", "Are you up for long hours of work?", "Are you into a travel job?"],
        "Data Analyst": ["Would you consider yourself a tech savvy person?", "Would you prefer a desk job?", "Are you interested in data handling?"],
        "Fashion Designer": ["Would you consider yourself to have a good fashion sense?", "Would you consider yourself photogenic?", "Are you confident in nature?"],
        "Influencer": ["Are you a good communicator?", "Are you an extrovert?", "Are you comfortable in front of the camera?", "Would you consider yourself relatable to other people?"],
        "Artist": ["Would you consider yourself creative?", "Do you have a good eye for detail?", "Do you think you can make a career out of art? (Music/Dance/Art/Theatre)"],
        "Astronaut": ["Are you adaptable in nature?", "Are you good in a team?", "Do you have an interest in space?", "Can you swim well?"],
        "Politician": ["Would you consider yourself a good leader?", "Are you a good communicator?", "Are you an extrovert?"],
        "Archaeologist": ["Would you prefer an active field job?", "Are you up for long hours of work?", "Do you like exploring historical sites?"],
        "UI/UX Designer": ["Would you consider yourself a tech savvy person?", "Would you consider yourself creative?", "Do you have a good eye for detail?", "Would you prefer a desk job?", "Are you up for long hours of work?"],
        "Video Editor": ["Would you consider yourself creative?", "Would you prefer a desk job?", "Do you enjoy video editing?"],
        "Career Counselor": ["Would you consider yourself as an empathetic person?", "Are you an extrovert?", "Do you have a good knowledge of careers around you?"],
        "Defense": ["Would you consider yourself patriotic?", "Would you consider yourself a good leader?", "Are you a good observer by nature?", "Would you consider yourself fit?", "Are you up for long hours of physical training?"],
        "Engineer": ["Would you consider yourself a tech savvy person?", "Are you up for long hours of work?", "Would you prefer a desk job?", "Do you enjoy solving puzzles?", "Do you have a good memory?"],
        "Prompt Engineering": ["Would you consider yourself a tech savvy person?", "Would you consider yourself creative?", "Would you prefer a desk job?", "Are you interested in AI?"],
        "Architect": ["Would you consider yourself creative?", "Do you have a good eye for detail?", "Do you enjoy designing spaces?"],
        "Photographer": ["Do you have a good eye for detail?", "Are you interested in photography?", "Would you consider yourself creative?"]}

    response_values = {"Strongly Agree": 2,"Agree": 1,"Neutral": 0,"Disagree": -1,"Strongly Disagree": -2}

    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    subject = data['best_subject']

    if subject == "None":
        subject = "No subject"
    careers.extend(subject_careers.get(subject, []))
    all_questions = set()
    for career in careers:
        all_questions.update(career_questions.get(career, []))

    question_scores = {}
    for question in all_questions:
        print("\n" + question)
        print("Options: ")
        for option in response_values:
            print("- " + option)
        while True:
            response = input("Your answer: ").strip()
            if response in response_values:
                question_scores[question] = response_values[response]
                break
            else:
                print("Invalid input. Please enter a valid option exactly as shown.")

    career_scores = {}
    for career in careers:
        score = 0
        for q in career_questions.get(career, []):
            score += question_scores.get(q, 0)
        career_scores[career] = score

    top_score = max(career_scores.values())

    print("\nTop Recommended Career:")
    for career, score in career_scores.items():
        if score == top_score:
            print("- " + career)

            finalcareer = career

    
    attributes = {"Ethical Hacker": ["Tech Savvy", "Problem Solver", "Desk Job"],
    "Doctor": ["Empathetic", "Hardworking", "Active Field"],
    "Psychologist": ["Interested In Psychology", "Approachable", "Extrovert"],
    "Entrepreneur": ["Leader", "Risk Taker", "Extrovert"],
    "Teacher": ["Empathetic", "Mentor", "Communicator"],
    "Lawyer": ["Communicator", "Observant", "Active Field"],
    "Sports": ["Sports Enthusiast", "Physically Fit", "Hardworking"],
    "Chartered Accountant": ["Desk Job", "Numbers & Finance", "Detail-Oriented"],
    "Pilot": ["Good Memory", "Hardworking", "Likes Travel"],
    "Data Analyst": ["Tech Savvy", "Desk Job", "Data Handling"],
    "Fashion Designer": ["Fashion Sense", "Confident", "Photogenic"],
    "Influencer": ["Communicator", "Extrovert", "Camera Friendly"],
    "Artist": ["Creative", "Eye For Detail", "Passion For Art"],
    "Astronaut": ["Adaptable", "Team Player", "Interested In Space"],
    "Politician": ["Leader", "Communicator", "Extrovert"],
    "Archaeologist": ["Active Field", "Hardworking", "Interested In History"],
    "UI/UX Designer": ["Tech Savvy", "Creative", "Eye For Detail"],
    "Video Editor": ["Creative", "Desk Job", "Video Editing"],
    "Career Counselor": ["Empathetic", "Extrovert", "Career Knowledge"],
    "Defense": ["Patriotic", "Fit", "Leader"],
    "Engineer": ["Tech Savvy", "Problem Solver", "Desk Job"],
    "Prompt Engineering": ["Tech Savvy", "Creative", "AI Interest"],
    "Architect": ["Creative", "Eye For Detail", "Design-Oriented"],
    "Photographer": ["Eye For Detail", "Photography Interest", "Creative"]}

    screen = turtle.Screen()
    screen.bgcolor("white")
    turt = turtle.Turtle()
    turt.speed(0)
    turt.pensize(2)

    def ikigai(x, y, color, text, label_offset_x=0, label_offset_y=0):
        turt.penup()
        turt.goto(x, y - 60) 
        turt.pendown()
        turt.pencolor(color)
        turt.circle(100)
        turt.penup()
        turt.goto(x + label_offset_x, y + label_offset_y)
        turt.pencolor("black")
        turt.write(text, align="center", font=("Arial", 12, "bold"))

    r = 60
    factor = 1.1
    ikigai(0, r * factor, "red", subject, 0, 80)
    ikigai(r * factor, 0, "green", attributes[finalcareer][0], 60, 30) 
    ikigai(0, -r * factor, "blue", attributes[finalcareer][1], 0, -20) 
    ikigai(-r * factor, 0, "orange", attributes[finalcareer][2], -60, 30) 
    turt.penup()
    turt.goto(0, 10)
    turt.pencolor("black")
    turt.write(finalcareer, align="center", font=("Arial", 12, "bold"))
    turt.hideturtle()
    screen.mainloop()

    ans = input("Type yes to get your personal exam timetable! ")
    if ans == "yes":
        timetable = {"Engineer": { "Exam": "JEE Main 2026", "Registration": "Nov–Dec 2025", "Exam Sessions": "Jan 2026 (Session 1), Apr 2026 (Session 2)", "Next Steps": "JEE Advanced (May–Jun), JoSAA counselling (May–Jul), Start B.Tech (Aug 2026)" },
    "Doctor": { "Exam": "NEET UG 2026", "Registration": "7 Feb – 7 Mar 2026", "Correction": "9–11 Mar 2026", "Exam1": "3 May 2026", "Result": "3rd–4th week of Jun 2026", "Counselling": "July 2026" },
    "Chartered Accountant": { "Exam (Foundation)": "May 2026 session", "Registration Deadline": "1 Jan 2026" },
    "Pilot": { "Entry Path": "DGCA-approved CPL training", "Minimum Age/Eligibility": "≥17 years + Class 12", "Training": "Ground + 200 flight hours (12–18 months)", "License Exams": "DGCA CPL during/after training; ATPL 1500 hours → written after CPL" },
    "Data Analyst": { "Path": "UG admission in BSc/BA (Stats/CS/Data Science)/B.Tech CS", "Apply": "Summer 2026 after board results", "No National Entrance Exam": "Direct or Uni-level entrance" },
    "Psychologist": { "Path": "UG in Psychology (BSc/BA)", "Apply": "Summer 2026; no central exam except DU-ET or university", "Further": "M.A./M.Sc Psychology after graduation" },
    "Entrepreneur": { "Path": "Varied UG/PG programs (BBA/MBA/Engineering)", "Apply": "Summer 2026; no standardized exam except DU-ET, etc." },
    "Teacher": { "Exam": "NTSE + CTET (after graduation)", "Apply UG": "B.Ed. or BA.Ed. admissions Summer 2026", "Counselling": "University/State-level after results" },
    "Lawyer": { "Exam": "CLAT/LSAT–India 2026", "Registration": "Jan–May 2026 (approx.)", "Exam Date": "May 2026", "Admission": "LLB via 5-yr integrated programs" },
    "Sports": { "Path": "Sports quotas in universities/colleges", "Apply": "Summer 2026 with sports credentials" },
    "Fashion Designer": { "Exam": "NIFT UG–2026 / NID DAT–2026", "Registration": "Dec 2025 – Jan 2026", "Exam1": "Feb 2026", "Admission": "April–May 2026" },
    "Influencer": { "Path": "Any UG (Mass Comm, Marketing) + skill building", "Apply": "Summer 2026; no central exam" },
    "Artist": { "Exam": "NID DAT / UCEED / NIFT (for Arts)", "Registration": "Dec 2025 – Jan 2026", "Exam1": "Feb 2026" },
    "Astronaut": { "Path": "UG in Engineering/Science + apply for ISRO/NASA later" },
    "Politician": { "Path": "UG in Political Science, Law, or Social Sciences", "Apply": "Summer 2026; no central exam" },
    "Archaeologist": { "Path": "UG in Archaeology/History", "Apply": "Summer 2026; no central exam" },
    "UI/UX Designer": { "Exam1": "NID DAT or relevant Design UG", "Registration": "Dec 2025 – Jan 2026", "Exam": "Feb 2026" },
    "Video Editor": { "Path": "UG in Film, Media Studies, or vocational diploma", "Apply": "Summer 2026; focus on portfolio" },
    "Career Counselor": { "Path": "UG in Psychology/Education + certification", "Apply": "Summer 2026; no central exam" },
    "Defense": { "Exam": "NDA 2 (Sept 2026) or CDS 1 (Feb 2027)", "Registration NDA 2": "June–July 2026", "Apply": "Pre-commission training after undergrad" },
    "Prompt Engineering": { "Path": "UG in CS, Engineering, AI/Data Science", "Apply": "Summer 2026; no central exam" },
    "Architect": { "Exam": "NATA 2026 / JEE Paper 2", "Registration": "Dec 2025 – Feb 2026", "Exam1": "Apr 2026" },
    "Photographer": { "Path": "UG in Film/Photography or vocational course", "Apply": "Summer 2026; emphasize portfolio" }}

        for q,x in timetable.items():
            if finalcareer==q:
                for p,y in x.items():
                    print(p,y)
print("Thank you for trusting Direxa! Wishing you success in what you do!")

