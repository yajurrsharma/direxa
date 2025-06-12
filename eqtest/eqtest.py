import json


def eqtest():
# Subject to Careers Mapping
    subject_careers = {
        "Mathematics": ["Ethical Hacker", "Pilot", "Data Analyst"],
        "Biology": ["Doctor", "Psychologist"],
        "Accountancy": ["Chartered Accountant"],
        "Political Science": ["Lawyer", "Politician"],
        "History": ["Archaeologist"],
        "Commerce": ["Entrepreneur"],
        "PCM": ["Defense", "Engineer", "Astronaut", "Architect"],
        "Science": ["Astronaut"],
        "Any (score > 98%)": ["Teacher"],
        "No subject": [
            "Sports", "Fashion Designer", "Influencer", "Artist",
            "UI/UX Designer", "Video Editor", "Career Counselor",
            "Prompt Engineering", "Photographer"
        ]
    }

    # Career to EQ Questions Mapping
    career_questions = {
        "Ethical Hacker": [
            "Would you consider yourself a tech savvy person?",
            "Do you enjoy solving puzzles?",
            "Would you prefer a desk job?"
        ],
        "Doctor": [
            "Would you consider yourself as an empathetic person?",
            "Are you up for long hours of work?",
            "Would you prefer an active field job?"
        ],
        "Psychologist": [
            "Are you interested in human psychology?",
            "Are you approachable and lead to people opening up to you?",
            "Are you an extrovert?"
        ],
        "Entrepreneur": [
            "Would you consider yourself a good leader?",
            "Are you up for taking risks in your career?",
            "Are you an extrovert?"
        ],
        "Teacher": [
            "Would you consider yourself as an empathetic person?",
            "Are you adaptable in nature?",
            "Are you an extrovert?",
            "Do you have good mentorship skills?",
            "Are you a good communicator?"
        ],
        "Lawyer": [
            "Are you a good communicator?",
            "Are you a good observer by nature?",
            "Would you consider yourself a good debater?",
            "Would you prefer an active field job?"
        ],
        "Sports": [
            "Do you enjoy sports?",
            "Are you proud of your sports accomplishments?",
            "Are you up for long hours of physical training?",
            "Would you consider yourself fit?"
        ],
        "Chartered Accountant": [
            "Would you prefer a desk job?",
            "Do you enjoy working with numbers and finances?"
        ],
        "Pilot": [
            "Do you have a good memory?",
            "Are you up for long hours of work?",
            "Are you into a travel job?"
        ],
        "Data Analyst": [
            "Would you consider yourself a tech savvy person?",
            "Would you prefer a desk job?",
            "Are you interested in data handling?"
        ],
        "Fashion Designer": [
            "Would you consider yourself to have a good fashion sense?",
            "Would you consider yourself photogenic?",
            "Are you confident in nature?"
        ],
        "Influencer": [
            "Are you a good communicator?",
            "Are you an extrovert?",
            "Are you comfortable in front of the camera?",
            "Would you consider yourself relatable to other people?"
        ],
        "Artist": [
            "Would you consider yourself creative?",
            "Do you have a good eye for detail?",
            "Do you think you can make a career out of art? (Music/Dance/Art/Theatre)"
        ],
        "Astronaut": [
            "Are you adaptable in nature?",
            "Are you good in a team?",
            "Do you have an interest in space?",
            "Can you swim well?"
        ],
        "Politician": [
            "Would you consider yourself a good leader?",
            "Are you a good communicator?",
            "Are you an extrovert?"
        ],
        "Archaeologist": [
            "Would you prefer an active field job?",
            "Are you up for long hours of work?",
            "Do you like exploring historical sites?"
        ],
        "UI/UX Designer": [
            "Would you consider yourself a tech savvy person?",
            "Would you consider yourself creative?",
            "Do you have a good eye for detail?",
            "Would you prefer a desk job?",
            "Are you up for long hours of work?"
        ],
        "Video Editor": [
            "Would you consider yourself creative?",
            "Would you prefer a desk job?",
            "Do you enjoy video editing?"
        ],
        "Career Counselor": [
            "Would you consider yourself as an empathetic person?",
            "Are you an extrovert?",
            "Do you have a good knowledge of careers around you?"
        ],
        "Defense": [
            "Would you consider yourself patriotic?",
            "Would you consider yourself a good leader?",
            "Are you a good observer by nature?",
            "Would you consider yourself fit?",
            "Are you up for long hours of physical training?"
        ],
        "Engineer": [
            "Would you consider yourself a tech savvy person?",
            "Are you up for long hours of work?",
            "Would you prefer a desk job?",
            "Do you enjoy solving puzzles?",
            "Do you have a good memory?"
        ],
        "Prompt Engineering": [
            "Would you consider yourself a tech savvy person?",
            "Would you consider yourself creative?",
            "Would you prefer a desk job?",
            "Are you interested in AI?"
        ],
        "Architect": [
            "Would you consider yourself creative?",
            "Do you have a good eye for detail?",
            "Do you enjoy designing spaces?"
        ],
        "Photographer": [
            "Do you have a good eye for detail?",
            "Are you interested in photography?",
            "Would you consider yourself creative?"
        ]
    }

    # Likert scale response mapping
    response_values = {
        "Strongly Agree": 2,
        "Agree": 1,
        "Neutral": 0,
        "Disagree": -1,
        "Strongly Disagree": -2
    }

    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    subject = data['best_subject']

    careers = subject_careers.get(subject, [])
    all_questions = set()
    for career in careers:
        all_questions.update(career_questions.get(career, []))

    # Ask each question and store response score
    question_scores = {}
    for question in all_questions:
        print(f"\n{question}")
        print("Options: ")
        for option in response_values:
            print(f"- {option}")
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

    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

    print("\nTop Recommended Career(s):")
    top_score = sorted_careers[0][1]
    for career, score in sorted_careers:
        if score == top_score:
            print(f"- {career} (Score: {score})")
        else:
            break

