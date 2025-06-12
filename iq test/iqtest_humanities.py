from main import best_sub
import json

def iqtest_humanities():
  global best_sub

  questions = [
    {
      "question": "Which of the following is NOT a function of a constitution?",
      "options": ["A. It gives a guarantee of the rights of the citizen", "B. It marks out different spheres of power for different branches of government", "C. It ensures that good people come to power", "D. It gives expression to some shared values"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Which of these is NOT a Fundamental Right listed in the Indian Constitution?",
      "options": ["A. Right to Equality", "B. Right to Property", "C. Right to Freedom", "D. Right against Exploitation"],
      "answer": "B",
      "subject": "Political Science"
    },
    {
      "question": "What is the system of elections followed in India for Lok Sabha elections?",
      "options": ["A. Proportional Representation", "B. First Past the Post", "C. Preferential Voting", "D. Cumulative Voting"],
      "answer": "B",
      "subject": "Political Science"
    },
    {
      "question": "Who is the real head of the executive in a parliamentary system like India?",
      "options": ["A. The President", "B. The Chief Justice", "C. The Prime Minister", "D. The Speaker of Lok Sabha"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Which of the following is NOT a function of the legislature?",
      "options": ["A. Making laws", "B. Implementing laws", "C. Controlling the executive", "D. Representing the people"],
      "answer": "B",
      "subject": "Political Science"
    },
    {
      "question": "Which of the following is essential for the independence of the judiciary?",
      "options": ["A. Judges must be appointed by politicians", "B. Judges must be financially dependent on the government", "C. Judges must hold office at the pleasure of the President", "D. Judges must have security of tenure and fixed salaries"],
      "answer": "D",
      "subject": "Political Science"
    },
    {
      "question": "What is the key feature of Indian federalism?",
      "options": ["A. Equal powers to all states", "B. Complete independence of states from the centre", "C. Strong centre with some autonomy for states", "D. A confederation of sovereign states"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Which constitutional amendment provided for the establishment of Panchayati Raj institutions?",
      "options": ["A. 52nd Amendment", "B. 61st Amendment", "C. 73rd Amendment", "D. 86th Amendment"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "What is meant by describing the Indian Constitution as a living document?",
      "options": ["A. It can be rewritten entirely after elections", "B. It adapts through amendments and judicial interpretation", "C. It is the same as any other historical text", "D. It never changes under any circumstances"],
      "answer": "B",
      "subject": "Political Science"
    },
    {
      "question": "According to the philosophy of the Indian Constitution, who is the source of all authority?",
      "options": ["A. The Prime Minister", "B. The President", "C. The Parliament", "D. The People of India"],
      "answer": "D",
      "subject": "Political Science"
    },
    {
      "question": "What is the significance of the Preamble to the Indian Constitution?",
      "options": ["A. It is legally enforceable in the court of law", "B. It defines the duties of citizens", "C. It outlines the objectives and philosophy of the Constitution", "D. It provides for emergency provisions"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Which body is responsible for resolving disputes between states or between a state and the centre?",
      "options": ["A. Lok Sabha", "B. Election Commission", "C. Supreme Court", "D. Rajya Sabha"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "The term 'Secular' in the Indian Constitution means:",
      "options": ["A. India has a national religion", "B. The state gives preference to majority religion", "C. The state does not favour or discriminate against any religion", "D. All religious festivals are national holidays"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "What is the main function of the Election Commission of India?",
      "options": ["A. To enact laws", "B. To elect the President", "C. To conduct free and fair elections", "D. To appoint the Prime Minister"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Who has the power to amend the Constitution of India?",
      "options": ["A. President alone", "B. Judiciary", "C. Parliament", "D. Prime Minister with Cabinet"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "What is meant by Universal Adult Franchise?",
      "options": ["A. Only educated people can vote", "B. All adults have the right to vote regardless of caste, gender or wealth", "C. Voting is only for men above 21", "D. Only property owners can vote"],
      "answer": "B",
      "subject": "Political Science"
    },
    {
      "question": "Which of the following statements about the Directive Principles of State Policy is true?",
      "options": ["A. They are legally enforceable", "B. They are suggestions to the judiciary", "C. They are guidelines for the government to frame policies", "D. They are punishable if violated"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "What is the main purpose of separation of powers in a democracy?",
      "options": ["A. To centralize decision-making", "B. To avoid delays in government", "C. To prevent the concentration of power in one authority", "D. To allow dictatorship in emergencies"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "Which part of the Indian Constitution contains the Fundamental Duties?",
      "options": ["A. Part III", "B. Part IV", "C. Part IVA", "D. Part V"],
      "answer": "C",
      "subject": "Political Science"
    },
    {
      "question": "The idea of Fundamental Rights in the Indian Constitution was inspired by:",
      "options": ["A. French Revolution", "B. Russian Constitution", "C. American Constitution", "D. British Constitution"],
      "answer": "C",
      "subject": "Political Science"
    },
      {
        "question": "By the time of Constantine I in the fourth century CE, which of the following was true about the Roman aristocracy?",
        "options": ["A. It was entirely military and came from noble Roman families.", "B. It had merged into a wealthy but more diverse class, including African and eastern families.", "C. It consisted only of senators who were descendants of Italian patricians.", "D. It was made up mostly of slaves who had gained wealth and power."],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "Which ancient civilization is credited with developing early systems of time reckoning, mathematics, and record-keeping involving square roots and compound interest?",
        "options": ["A. Indus Valley", "B. Mesopotamian", "C. Egyptian", "D. Greek"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "In early Mesopotamian cities, what role did temples mainly play?",
        "options": ["A. They served only as homes for rulers.", "B. They were solely used for religious festivals.", "C. They acted as religious centers and also managed economic and administrative activities.", "D. They were places for entertainment and sports."],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "What was a key factor in Genghis Khan military success?",
        "options": ["A. Relying only on large, heavily armored infantry units", "B. Avoiding harsh weather and difficult terrains", "C. Adapting steppe combat techniques into fast, innovative strategies using mobile cavalry and siege weapons", "D. Conquering mainly by naval warfare across rivers and seas"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "Why did knights become important in Europe from the ninth century onward?",
        "options": ["A. They were scholars responsible for teaching noble children.", "B. They replaced kings as rulers of large territories.", "C. They provided professional military service as peasant soldiers and cavalry proved insufficient.", "D. They acted as merchants and tax collectors in rural areas."],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "What was one major difference between free peasants and serfs in medieval society?",
        "options": ["A. Free peasants owned land while serfs rented land from the church.", "B. Serfs were paid regular wages, but peasants worked only for food.", "C. Free peasants could leave the estate and owned some land; serfs were bound to the lord land and needed permission to leave.", "D. Serfs were allowed to serve in the army while free peasants were not."],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "What was a key feature of the new educational programme influenced by humanism during the early Renaissance?",
        "options": ["A. It focused mainly on religious teachings and church doctrines.", "B. It discouraged the study of ancient authors.", "C. It emphasised grammar, rhetoric, poetry, and history, rooted in classical Roman culture.", "D. It trained students only in law and trade skills for commercial use."],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "Why did Christian humanists like Erasmus and Thomas More criticize the Church during the Renaissance?",
        "options": ["A. Because the Church encouraged translating the Bible into local languages", "B. Because they believed the Church had become corrupt and greedy", "C. Because the Church promoted classical education", "D. Because they opposed all forms of religious practice"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "What was one common purpose of building large cathedrals in medieval towns?",
        "options": ["A) To provide a marketplace for merchants", "B) To serve as a place for religious gatherings and pilgrimages", "C) To act as defensive forts against invasions", "D) To be used as royal palaces for kings and queens"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "What was a major reason native peoples in the USA and Canada resisted government efforts to end special provisions for them in the 1950s and 1960s?",
        "options": ["A) They wanted to maintain their cultural traditions and lands", "B) They wished to fully adopt European culture instead", "C) They were seeking to leave their reservations voluntarily", "D) They preferred to give up their citizenship rights"],
        "answer": "A",
        "subject": "History"
      },
      {
        "question": "Who was the ruler responsible for the spread of Buddhism outside India through missionary work?",
        "options": ["A. Harshavardhana", "B. Ashoka", "C. Chandragupta II", "D. Samudragupta"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "The term 'polis' in ancient Greece referred to:",
        "options": ["A. A form of tax", "B. A type of weapon", "C. A city-state", "D. A council of elders"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "In the context of Roman society, 'patricians' were:",
        "options": ["A. Slaves granted freedom", "B. Elected representatives of common people", "C. Members of noble and wealthy Roman families", "D. Foreign settlers"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "Which philosopher method of questioning is referred to as the Socratic method?",
        "options": ["A. Plato", "B. Pythagoras", "C. Aristotle", "D. Socrates"],
        "answer": "D",
        "subject": "History"
      },
      {
        "question": "Which of the following dynasties ruled China during the time of Confucius?",
        "options": ["A. Han", "B. Tang", "C. Zhou", "D. Qin"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "What was the main aim of the Silk Road in ancient times?",
        "options": ["A. Military invasions", "B. Religious pilgrimages", "C. Trade and cultural exchange between East and West", "D. Migration of farmers"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "The period known as the Pax Romana refers to:",
        "options": ["A. A Roman civil war", "B. Peace and prosperity in the Roman Empire", "C. The fall of the Western Roman Empire", "D. The rise of Christianity"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "What event is considered the immediate trigger for the French Revolution?",
        "options": ["A. The coronation of Napoleon", "B. The storming of the Bastille", "C. Execution of Louis XVI", "D. The Tennis Court Oath"],
        "answer": "B",
        "subject": "History"
      },
      {
        "question": "What was the role of monasteries in medieval Europe?",
        "options": ["A. Centers of entertainment", "B. Training places for knights", "C. Centers for learning, preserving books, and religious life", "D. Military headquarters"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "Which of the following best describes feudalism in medieval Europe?",
        "options": ["A. A democratic system of government", "B. A system where kings ruled through elected representatives", "C. A social and economic system based on land ownership and service", "D. A form of slavery under church rule"],
        "answer": "C",
        "subject": "History"
      },
      {
        "question": "At consumer equilibrium, the budget line is tangent to the indifference curve because:",
        "options": ["a) The prices of the two goods are equal", "b) The MRS is equal to the ratio of marginal utilities", "c) The MRS equals the price ratio", "d) The consumer is spending less than their income"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "Which of the following would not cause a shift in the production possibility curve (PPC)?",
        "options": ["a) A technological innovation", "b) An increase in labour force", "c) Reallocation of existing resources", "d) Discovery of new resources"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "If marginal product of a factor is negative, total product is:",
        "options": ["a) Rising", "b) Constant", "c) Falling", "d) Zero"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "A fall in the price of a Giffen good leads to:",
        "options": ["a) Increase in quantity demanded", "b) Decrease in quantity demanded", "c) No change in quantity demanded", "d) Increase in marginal utility"],
        "answer": "b",
        "subject": "Economics"
      },
      {
        "question": "If cross elasticity of demand between goods X and Y is negative, then the goods are:",
        "options": ["a) Complements", "b) Substitutes", "c) Unrelated", "d) Normal goods"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "At what stage of the law of variable proportions is the marginal product increasing?",
        "options": ["a) Stage I", "b) Stage II", "c) Stage III", "d) Marginal product never increases"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "If a firm marginal cost is rising and is above average cost, then:",
        "options": ["a) Average cost is rising", "b) Average cost is falling", "c) Average cost is constant", "d) Total cost is constant"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "If elasticity of supply is greater than 1, it means:",
        "options": ["a) Supply is perfectly elastic", "b) Supply is relatively elastic", "c) Supply is perfectly inelastic", "d) Supply is unitary elastic"],
        "answer": "b",
        "subject": "Economics"
      },
      {
        "question": "Which of the following is the best example of a public good in microeconomics?",
        "options": ["a) Mobile data", "b) Public park with entry fee", "c) National defence", "d) Cinema ticket"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "If the marginal utility per rupee of good X is greater than that of good Y, a rational consumer will:",
        "options": ["a) Buy more of Y", "b) Reduce consumption of X", "c) Buy more of X and less of Y", "d) Keep consumption unchanged"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "A consumer consumes only two goods. If the price of one good falls, the budget line will:",
        "options": ["a) Shift to the left", "b) Shift to the right", "c) Pivot outwards from the intercept of the other good", "d) Pivot inwards from the origin"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "In which of the following cases is the price elasticity of demand equal to unity?",
        "options": ["a) Total expenditure remains constant when price changes", "b) Demand remains constant when price changes", "c) Demand changes more than proportionately to price", "d) Total expenditure increases when price decreases"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "If marginal utility of good X is higher than marginal utility of good Y, the consumer can increase total utility by:",
        "options": ["a) Increasing consumption of Y only", "b) Decreasing consumption of X only", "c) Substituting Y with X", "d) Substituting X with Y"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "If the marginal rate of substitution is diminishing, the indifference curve will be:",
        "options": ["a) Concave to the origin", "b) Convex to the origin", "c) A straight line", "d) A right-angle curve"],
        "answer": "b",
        "subject": "Economics"
      },
      {
        "question": "At the point of consumer equilibrium, assuming two goods X and Y, the following condition must hold:",
        "options": ["a) MUx/Px = MUy/Py", "b) MUx × Px = MUy × Py", "c) MUx = MUy", "d) MUx – MUy = Px – Py"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "Which of the following statements is incorrect about the law of diminishing marginal utility?",
        "options": ["a) It assumes units are homogeneous", "b) It holds only if consumption is continuous", "c) It implies total utility increases at an increasing rate", "d) It assumes the consumer is rational"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "Which of the following is a case of perfectly competitive firm equilibrium in the short run?",
        "options": ["a) MC = MR and MC cuts MR from below", "b) MR = AR and MC is constant", "c) AR = MR = AC", "d) MR = MC and AC = AR"],
        "answer": "a",
        "subject": "Economics"
      },
      {
        "question": "The shape of marginal cost curve is U-shaped due to:",
        "options": ["a) Law of diminishing marginal utility", "b) Increasing returns to scale", "c) Law of variable proportions", "d) Economies of scale"],
        "answer": "c",
        "subject": "Economics"
      },
      {
        "question": "Which of the following combinations of elasticity is NOT possible in real life?",
        "options": ["a) Price elasticity = 1", "b) Cross elasticity = 0", "c) Income elasticity < 0", "d) Price elasticity > 10"],
        "answer": "d",
        "subject": "Economics"
      },
      {
        "question": "If a production function shows constant returns to scale, then:",
        "options": ["a) Marginal product of each factor is constant", "b) Total product increases less than proportionately", "c) Output increases in the same proportion as inputs", "d) Marginal cost is falling"],
        "answer": "c",
        "subject": "Economics"
      }
  ]
  score = {"History": 0, "Political Science": 0, "Economics": 0}
  count = 1
  for q in questions:
      print("\nQ" + str(count) + ". " + q["question"])
      for opt in q['options']:
          print(" " + opt)
      ans = input("Your answer (a/b/c/d): ").strip().lower()
      if ans == q['answer']:
          score[q['subject']] += 1
      count += 1


  best_sub += (max(score, key=score.get))
  
  with open('data.json', 'r') as file:
      data = json.load(file)

    
  data["score"] = f'{score}'
  data['best_subject'] = f'{best_sub}'

  with open('data.json', 'w') as data_file:
      json.dump(data, data_file, indent=4)

