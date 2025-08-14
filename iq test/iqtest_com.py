from main import best_sub
import json

def iqtest_com():
  global best_sub
  questions = [
      {"question": "The balance of cash book (debit side) is ₹10,000. A cheque of ₹2,000 deposited but not yet credited by the bank. What is the balance as per the passbook?", "options": ["a ₹12,000", "b ₹8,000", "c ₹10,000", "d ₹2,000"], "answer": "b", "subject": "Accountancy"},
      {"question": "Which of the following errors will affect the trial balance?", "options": ["a Purchases book undercast by ₹1,000", "b Sale of goods to Ramesh recorded as to Suresh", "c Cash paid to Ram ₹2,000 posted as ₹200 to his account", "d Wages paid debited to Machinery account"], "answer": "c", "subject": "Accountancy"},
      {"question": "Which of the following is a real account?", "options": ["a Capital account", "b Furniture account", "c Rent account", "d Commission received account"], "answer": "b", "subject": "Accountancy"},
      {"question": "If wages paid for installation of machinery is debited to wages account, it is an error of:", "options": ["a Principle", "b Omission", "c Commission", "d Compensating"], "answer": "a", "subject": "Accountancy"},
      {"question": "Which of the following is NOT a characteristic of a bill of exchange?", "options": ["a Unconditional order", "b It must be in writing", "c Signed by the drawer and the drawee", "d Certain amount and date"], "answer": "c", "subject": "Accountancy"},
      {"question": "The total of the debit side of the trial balance is ₹1,00,000, and that of the credit side is ₹97,000. The difference is placed in the suspense account. Later, an error is found: sales of ₹3,000 was not posted to the sales account. What will be the new balance in the suspense account?", "options": ["a ₹0", "b ₹1,000", "c ₹3,000", "d ₹4,000"], "answer": "b", "subject": "Accountancy"},
      {"question": "If closing stock is included in the trial balance, it will be shown:", "options": ["a On the credit side of trading account only", "b On the asset side of balance sheet only", "c Both in trading account and balance sheet", "d In profit and loss account"], "answer": "b", "subject": "Accountancy"},
      {"question": "Provision for doubtful debts appears in the:", "options": ["a Trading account", "b Profit and loss account only", "c Balance sheet only", "d Both profit and loss account and balance sheet"], "answer": "d", "subject": "Accountancy"},
      {"question": "Goods costing ₹2,000 distributed as free samples should be:", "options": ["a Credited to purchases and debited to drawings", "b Credited to sales and debited to advertisement", "c Debited to drawings and credited to purchases", "d Debited to advertisement and credited to purchases"], "answer": "d", "subject": "Accountancy"},
      {"question": "What is the effect of providing depreciation on fixed assets?", "options": ["a Increases profit", "b Decreases profit", "c Has no effect on profit", "d Increases asset value"], "answer": "b", "subject": "Accountancy"},
      {"question": "Which of the following is not a feature of a trial balance?", "options": ["a) It is a statement", "b) It has debit and credit columns", "c) It is an account", "d) It helps in preparing final accounts"], "answer": "c", "subject": "Accountancy"},
        {"question": "If wages are paid for installation of machinery, they should be:", "options": ["a) Debited to Wages A/c", "b) Debited to Profit & Loss A/c", "c) Debited to Machinery A/c", "d) Ignored"], "answer": "c", "subject": "Accountancy"},
        {"question": "A cheque deposited but not credited by the bank will be:", "options": ["a) Added to cash book balance", "b) Deducted from cash book balance", "c) Added to pass book balance", "d) Deducted from pass book balance"], "answer": "d", "subject": "Accountancy"},
        {"question": "Which of the following errors is not revealed by trial balance?", "options": ["a) Error of omission", "b) Error of principle", "c) Error of commission", "d) Compensating error"], "answer": "a", "subject": "Accountancy"},
        {"question": "Capital expenditure is shown in the:", "options": ["a) Trading account", "b) Profit and loss account", "c) Balance sheet", "d) Cash book only"], "answer": "c", "subject": "Accountancy"},
        {"question": "A liability that may or may not arise in future is called:", "options": ["a) Fixed liability", "b) Current liability", "c) Contingent liability", "d) Outstanding liability"], "answer": "c", "subject": "Accountancy"},
        {"question": "Which concept assumes that business will continue for a long time?", "options": ["a) Money Measurement Concept", "b) Going Concern Concept", "c) Matching Concept", "d) Dual Aspect Concept"], "answer": "b", "subject": "Accountancy"},
        {"question": "Rent paid in advance is:", "options": ["a) A liability", "b) An income", "c) A current asset", "d) An expense"], "answer": "c", "subject": "Accountancy"},
        {"question": "Goods costing ₹1,000 were taken by the proprietor for personal use. The journal entry will be:", "options": ["a) Drawings A/c Dr. ₹1,000; To Sales A/c ₹1,000", "b) Drawings A/c Dr. ₹1,000; To Purchases A/c ₹1,000", "c) Purchases A/c Dr. ₹1,000; To Drawings A/c ₹1,000", "d) Sales A/c Dr. ₹1,000; To Drawings A/c ₹1,000"], "answer": "b", "subject": "Accountancy"},
        {"question": "Goods worth ₹5,000 were returned by a customer, but were wrongly recorded as purchases returns. The effect of this error will be:", "options": ["a) Gross profit will increase", "b) Gross profit will decrease", "c) No effect on gross profit", "d) Net profit will increase"], "answer": "b", "subject": "Accountancy"},
        {"question": "A partnership firm continues to exist even after the death of a partner if there is:", "options": ["a) Unlimited liability", "b) Mutual agency", "c) Provision in the partnership deed", "d) Goodwill in the market"], "answer": "c", "subject": "Business Studies"},
        {"question": "Which of the following documents is filed to register a company with the Registrar of Companies?", "options": ["a) Articles of Association only", "b) Memorandum of Association only", "c) Prospectus only", "d) All of the above"], "answer": "d", "subject": "Business Studies"},
        {"question": "A public company must issue a prospectus when:", "options": ["a) It wants to take loans", "b) It wants to invite the public to subscribe to shares", "c) It wants to register as a private company", "d) It wants to appoint directors"], "answer": "b", "subject": "Business Studies"},
        {"question": "Which of the following is a limitation of retained earnings?", "options": ["a) No dilution of control", "b) Increases creditworthiness", "c) May lead to inefficient use of funds", "d) Avoids issue costs"], "answer": "c", "subject": "Business Studies"},
        {"question": "Which type of business is easiest to wind up?", "options": ["a) Cooperative society", "b) Partnership", "c) Sole proprietorship", "d) Company"], "answer": "c", "subject": "Business Studies"},
        {"question": "Which of the following statements about joint stock companies is FALSE?", "options": ["a) It has separate legal existence", "b) Shareholders have limited liability", "c) All companies are listed on stock exchanges", "d) Ownership and management are separate"], "answer": "c", "subject": "Business Studies"},
        {"question": "Who issues a Certificate of Commencement of Business?", "options": ["a) SEBI", "b) Registrar of Companies", "c) Ministry of Finance", "d) Board of Directors"], "answer": "b", "subject": "Business Studies"},
        {"question": "Which of the following is not a function of wholesalers?", "options": ["a) Risk bearing", "b) Grading of products", "c) Advertising to consumers", "d) Financing retailers"], "answer": "c", "subject": "Business Studies"},
        {"question": "Equity shareholders are called real owners because:", "options": ["a) They get fixed dividends", "b) They receive interest", "c) They bear the ultimate risk", "d) They work as company directors"], "answer": "c", "subject": "Business Studies"},
        {"question": "Which business organisation works on the principle of one man, one vote?", "options": ["a) Partnership", "b) Sole proprietorship", "c) Company", "d) Cooperative society"], "answer": "d", "subject": "Business Studies"},
        {"question": "Which feature of e-business makes it highly scalable?", "options": ["a) Cost-effectiveness", "b) Personalised experience", "c) Global reach", "d) Low need for physical space"], "answer": "c", "subject": "Business Studies"},
        {"question": "The main feature distinguishing a Joint Hindu Family business from other forms is:", "options": ["a) Profit motive", "b) Membership through agreement", "c) Management by the eldest member", "d) Limited liability of all members"], "answer": "c", "subject": "Business Studies"},
        {"question": "A private company must have a minimum of:", "options": ["a) 1 member", "b) 2 members", "c) 7 members", "d) 3 directors"], "answer": "b", "subject": "Business Studies"},
        {"question": "In which type of business risk is insurance most useful?", "options": ["a) Speculative risk", "b) Pure risk", "c) Financial risk", "d) Social risk"], "answer": "b", "subject": "Business Studies"},
        {"question": "Which principle of insurance limits the insured to recover only the actual amount of loss?", "options": ["a) Contribution", "b) Subrogation", "c) Utmost good faith", "d) Indemnity"], "answer": "d", "subject": "Business Studies"},
        {"question": "Which of the following statements is incorrect regarding a multinational company (MNC)?", "options": ["a) It has assets and operations in more than one country", "b) Its headquarters are always in a developing country", "c) It operates through branches or subsidiaries", "d) It brings foreign investment and technology"], "answer": "b", "subject": "Business Studies"},
        {"question": "Which one of the following is not a feature of departmental undertakings?", "options": ["a) Funded by annual government budget", "b) Managed by government officials", "c) Greater operational autonomy", "d) Directly under a ministry"], "answer": "c", "subject": "Business Studies"},
        {"question": "Which clause in the Memorandum of Association defines the scope of operations of the company?", "options": ["a) Name clause", "b) Liability clause", "c) Capital clause", "d) Object clause"], "answer": "d", "subject": "Business Studies"},
        {"question": "Which of the following services is considered auxiliary to trade?", "options": ["a) Warehousing", "b) Manufacturing", "c) Mining", "d) Assembly"], "answer": "a", "subject": "Business Studies"},
        {"question": "A major limitation of e-business is:", "options": ["a) Easy formation", "b) Paperless transactions", "c) Low operational cost", "d) Risk of data theft and hacking"], "answer": "d", "subject": "Business Studies"},
        {"question": "At consumer equilibrium, the budget line is tangent to the indifference curve because:", "options": ["a) The prices of the two goods are equal", "b) The MRS is equal to the ratio of marginal utilities", "c) The MRS equals the price ratio", "d) The consumer is spending less than their income"], "answer": "c", "subject": "Economics"},
        {"question": "Which of the following would not cause a shift in the production possibility curve (PPC)?", "options": ["a) A technological innovation", "b) An increase in labour force", "c) Reallocation of existing resources", "d) Discovery of new resources"], "answer": "c", "subject": "Economics"},
        {"question": "If marginal product of a factor is negative, total product is:", "options": ["a) Rising", "b) Constant", "c) Falling", "d) Zero"], "answer": "c", "subject": "Economics"},
        {"question": "A fall in the price of a Giffen good leads to:", "options": ["a) Increase in quantity demanded", "b) Decrease in quantity demanded", "c) No change in quantity demanded", "d) Increase in marginal utility"], "answer": "b", "subject": "Economics"},
        {"question": "If cross elasticity of demand between goods X and Y is negative, then the goods are:", "options": ["a) Complements", "b) Substitutes", "c) Unrelated", "d) Normal goods"], "answer": "a", "subject": "Economics"},
        {"question": "At what stage of the law of variable proportions is the marginal product increasing?", "options": ["a) Stage I", "b) Stage II", "c) Stage III", "d) Marginal product never increases"], "answer": "a", "subject": "Economics"},
        {"question": "If a firm marginal cost is rising and is above average cost,then:", "options": ["a) Average cost is rising", "b) Average cost is falling", "c) Average cost is constant", "d) Total cost is constant"], "answer": "a", "subject": "Economics"},
        {"question": "If elasticity of supply is greater than 1, it means:", "options": ["a) Supply is perfectly elastic", "b) Supply is relatively elastic", "c) Supply is perfectly inelastic", "d) Supply is unitary elastic"], "answer": "b", "subject": "Economics"},
        {"question": "Which of the following is the best example of a public good in microeconomics?", "options": ["a) Mobile data", "b) Public park with entry fee", "c) National defence", "d) Cinema ticket"], "answer": "c", "subject": "Economics"},
        {"question": "If the marginal utility per rupee of good X is greater than that of good Y, a rational consumer will:", "options": ["a) Buy more of Y", "b) Reduce consumption of X", "c) Buy more of X and less of Y", "d) Keep consumption unchanged"], "answer": "c", "subject": "Economics"},
        {"question": "A consumer consumes only two goods. If the price of one good falls, the budget line will:", "options": ["a) Shift to the left", "b) Shift to the right", "c) Pivot outwards from the intercept of the other good", "d) Pivot inwards from the origin"], "answer": "c", "subject": "Economics"},
        {"question": "In which of the following cases is the price elasticity of demand equal to unity?", "options": ["a) Total expenditure remains constant when price changes", "b) Demand remains constant when price changes", "c) Demand changes more than proportionately to price", "d) Total expenditure increases when price decreases"], "answer": "a", "subject": "Economics"},
        {"question": "If marginal utility of good X is higher than marginal utility of good Y, the consumer can increase total utility by:", "options": ["a) Increasing consumption of Y only", "b) Decreasing consumption of X only", "c) Substituting Y with X", "d) Substituting X with Y"], "answer": "c", "subject": "Economics"},
        {"question": "If the marginal rate of substitution is diminishing, the indifference curve will be:", "options": ["a) Concave to the origin", "b) Convex to the origin", "c) A straight line", "d) A right-angle curve"], "answer": "b", "subject": "Economics"},
        {"question": "At the point of consumer equilibrium, assuming two goods X and Y, the following condition must hold:", "options": ["a) MUx/Px = MUy/Py", "b) MUx × Px = MUy × Py", "c) MUx = MUy", "d) MUx – MUy = Px – Py"], "answer": "a", "subject": "Economics"},
        {"question": "Which of the following statements is incorrect about the law of diminishing marginal utility?", "options": ["a) It assumes units are homogeneous", "b) It holds only if consumption is continuous", "c) It implies total utility increases at an increasing rate", "d) It assumes the consumer is rational"], "answer": "c", "subject": "Economics"},
        {"question": "Which of the following is a case of perfectly competitive firm equilibrium in the short run?", "options": ["a) MC = MR and MC cuts MR from below", "b) MR = AR and MC is constant", "c) AR = MR = AC", "d) MR = MC and AC = AR"], "answer": "a", "subject": "Economics"},
        {"question": "The shape of marginal cost curve is U-shaped due to:", "options": ["a) Law of diminishing marginal utility", "b) Increasing returns to scale", "c) Law of variable proportions", "d) Economies of scale"], "answer": "c", "subject": "Economics"},
        {"question": "Which of the following combinations of elasticity is NOT possible in real life?", "options": ["a) Price elasticity = 1", "b) Cross elasticity = 0", "c) Income elasticity < 0", "d) Price elasticity > 10"], "answer": "d", "subject": "Economics"},
        {"question": "If a production function shows constant returns to scale, then:", "options": ["a) Marginal product of each factor is constant", "b) Total product increases less than proportionately", "c) Output increases in the same proportion as inputs", "d) Marginal cost is falling"], "answer": "c", "subject": "Economics"}

    ]
  score = {"Accountancy": 0, "Business Studies": 0, "Economics": 0}
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


