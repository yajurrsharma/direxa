from main import best_sub
import json

def iqtest_sci_math():
  global best_sub
  questions = [
      {"question":"A car moves in a circular path with constant speed. Which of the following is true?","options":["a) Velocity is constant","b) Acceleration is zero","c) Net force is zero","d) Acceleration is directed towards the centre"],"answer":"d","subject":"Physics"},
      {"question":"Which of the following quantities has different dimensions than the others?","options":["a) Work","b) Energy","c) Torque","d) Power"],"answer":"d","subject":"Physics"},
      {"question":"A projectile is thrown at an angle of 45° with the horizontal. The range is maximum when:","options":["a) Angle = 60°","b) Angle = 45°","c) Angle = 30°","d) Angle = 90°"],"answer":"b","subject":"Physics"},
      {"question":"If a body is moving with uniform velocity, its acceleration is:","options":["a) Zero","b) Constant","c) Increasing","d) Decreasing"],"answer":"a","subject":"Physics"},
      {"question":"The unit of impulse is:","options":["a) kg·m²/s²","b) N·s","c) N/m","d) J/s"],"answer":"b","subject":"Physics"},
      {"question":"The angle between velocity and acceleration in uniform circular motion is:","options":["a) 0°","b) 90°","c) 180°","d) 60°"],"answer":"b","subject":"Physics"},
      {"question":"A ball is dropped from a height of 20 m. The time taken to reach the ground is (take g = 10 m/s²):","options":["a) 2 s","b) √2 s","c) 4 s","d) √5 s"],"answer":"a","subject":"Physics"},
      {"question":"The work done by a centripetal force is:","options":["a) Positive","b) Negative","c) Zero","d) Maximum"],"answer":"c","subject":"Physics"},
      {"question":"A body moves with velocity v and momentum p. Its kinetic energy is:","options":["a) p²/2m","b) 2p²/m","c) ½ mv²","d) m²/p"],"answer":"a","subject":"Physics"},
      {"question":"Which law states that stress is directly proportional to strain within the elastic limit?","options":["a) Newton law","b) Hooke law","c) Boyle law","d) Pascal law"],"answer":"b","subject":"Physics"},
      {"question":"A satellite is revolving in a circular orbit around the Earth. What provides the necessary centripetal force?","options":["a) Satellite engine","b) Earth atmosphere","c) Gravitational force","d) Inertia"],"answer":"c","subject":"Physics"},
      {"question":"Bernoulli theorem is based on the conservation of:","options":["a) Mass","b) Energy","c) Momentum","d) Angular momentum"],"answer":"b","subject":"Physics"},
      {"question":"The dimensional formula for pressure is:","options":["a) [MLT⁻²]","b) [ML⁻¹T⁻²]","c) [M⁰L⁰T⁰]","d) [ML²T⁻²]"],"answer":"b","subject":"Physics"},
      {"question":"If the temperature of a black body increases, the wavelength corresponding to maximum emission:","options":["a) Increases","b) Decreases","c) Remains constant","d) Becomes infinite"],"answer":"b","subject":"Physics"},
      {"question":"Which of the following is not a scalar quantity?","options":["a) Work","b) Pressure","c) Momentum","d) Energy"],"answer":"c","subject":"Physics"},
      {"question":"When two bodies collide elastically in one dimension, which of the following is conserved?","options":["a) Kinetic energy only","b) Momentum only","c) Both kinetic energy and momentum","d) Neither"],"answer":"c","subject":"Physics"},
      {"question":"Which of the following statements about viscosity is true?","options":["a) It increases with temperature in liquids","b) It decreases with temperature in liquids","c) It remains constant","d) It is not dependent on temperature"],"answer":"b","subject":"Physics"},
      {"question":"What is the value of acceleration due to gravity at the centre of the Earth?","options":["a) g","b) Zero","c) Infinity","d) g/2"],"answer":"b","subject":"Physics"},
      {"question":"The area under force vs. displacement graph represents:","options":["a) Power","b) Momentum","c) Energy","d) Work"],"answer":"d","subject":"Physics"},
      {"question":"Which of the following graphs represents motion with uniform acceleration?","options":["a) Straight line in displacement vs. time graph","b) Parabola in velocity vs. time graph","c) Straight line in velocity vs. time graph","d) Curve in displacement vs. time graph"],"answer":"c","subject":"Physics"},
      {"question":"The number of significant figures in 0.005600 is:","options":["a) 2","b) 4","c) 3","d) 5"],"answer":"b","subject":"Chemistry"},
      {"question":"The correct order of increasing atomic radius is:","options":["a) Na < Mg < Al","b) Al < Mg < Na","c) Mg < Al < Na","d) Na < Al < Mg"],"answer":"b","subject":"Chemistry"},
      {"question":"Which of the following is an empirical formula?","options":["a) C₆H₁₂O₆","b) H₂O","c) CH₂O","d) C₂H₆"],"answer":"c","subject":"Chemistry"},
      {"question":"The number of orbitals in the 3rd shell is:","options":["a) 4","b) 9","c) 16","d) 1"],"answer":"b","subject":"Chemistry"},
      {"question":"Which quantum number determines the shape of an orbital?","options":["a) Principal quantum number (n)","b) Azimuthal quantum number (l)","c) Magnetic quantum number (m)","d) Spin quantum number (s)"],"answer":"b","subject":"Chemistry"},
      {"question":"Which of the following has the highest ionisation enthalpy?","options":["a) Li","b) Na","c) K","d) Be"],"answer":"d","subject":"Chemistry"},
      {"question":"The maximum number of electrons in a subshell is given by:","options":["a) 2l + 1","b) n²","c) 4l + 2","d) 2n²"],"answer":"c","subject":"Chemistry"},
      {"question":"Which of the following is not a postulate of Dalton atomic theory?","options":["a) Atoms are indivisible","b) Atoms of the same element are identical","c) Atoms cannot be created or destroyed","d) Atoms can be divided in nuclear reactions"],"answer":"d","subject":"Chemistry"},
      {"question":"Which of the following species is isoelectronic with Ne?","options":["a) Na⁺","b) O²⁻","c) F","d) Mg²⁺"],"answer":"d","subject":"Chemistry"},
      {"question":"Hydrogen bonding is strongest in:","options":["a) HCl","b) H₂O","c) HF","d) NH₃"],"answer":"c","subject":"Chemistry"},
      {"question":"The oxidation number of Cr in Cr₂O₇²⁻ is:","options":["a) +6","b) +3","c) +2","d) +7"],"answer":"a","subject":"Chemistry"},
      {"question":"Which of the following molecules has a linear shape?","options":["a) H₂O","b) CO₂","c) NH₃","d) SO₂"],"answer":"b","subject":"Chemistry"},
      {"question":"Which law relates pressure and volume at constant temperature?","options":["a) Charles Law","b) Avogadro Law","c) Boyle Law","d) Gay-Lussac Law"],"answer":"c","subject":"Chemistry"},
      {"question":"Which of the following gases will diffuse fastest at room temperature?","options":["a) O₂","b) CO₂","c) NH₃","d) Cl₂"],"answer":"c","subject":"Chemistry"},
      {"question":"The pH of a 10⁻³ M HCl solution is:","options":["a) 3","b) 11","c) 7","d) 1"],"answer":"a","subject":"Chemistry"},
      {"question":"Which of the following is not a strong electrolyte?","options":["a) NaCl","b) HCl","c) CH₃COOH","d) KOH"],"answer":"c","subject":"Chemistry"},
      {"question":"The reaction A + B ⇌ C + D is in equilibrium. What happens if B is increased?","options":["a) Reaction shifts left","b) Reaction shifts right","c) No effect","d) Reaction stops"],"answer":"b","subject":"Chemistry"},
      {"question":"In endothermic reactions, the value of ΔH is:","options":["a) Positive","b) Negative","c) Zero","d) Cannot be predicted"],"answer":"a","subject":"Chemistry"},
      {"question":"The number of unpaired electrons in O₂ molecule is:","options":["a) 0","b) 1","c) 2","d) 4"],"answer":"c","subject":"Chemistry"},
      {"question":"Which of the following is the correct IUPAC name?","options":["a) 2-methylpropane","b) 1-methylpropane","c) Isobutane","d) Trimethane"],"answer":"a","subject":"Chemistry"},
      {"question":"If A = {1, 2, 3}, B = {3, 4, 5}, then A ∩ B = ?","options":["a) {1, 2}","b) {3}","c) {1, 2, 3, 4, 5}","d) ∅"],"answer":"b","subject":"Mathematics"},
      {"question":"The number of subsets of the set {1, 2, 3, 4, 5} is:","options":["a) 10","b) 25","c) 32","d) 16"],"answer":"c","subject":"Mathematics"},
      {"question":"If f(x) = x² and g(x) = √x, then (f ∘ g)(x) is:","options":["a) x","b) x²","c) √x","d) |x|"],"answer":"a","subject":"Mathematics"},
      {"question":"The value of sin²30° + cos²30° is:","options":["a) 0","b) 1","c) ½","d) 2"],"answer":"b","subject":"Mathematics"},
      {"question":"If tan A = √3, then A = ?","options":["a) 30°","b) 45°","c) 60°","d) 90°"],"answer":"c","subject":"Mathematics"},
      {"question":"The general solution of sin x = 0 is:","options":["a) nπ","b) 2nπ","c) (2n+1)π","d) π/2 + nπ"],"answer":"a","subject":"Mathematics"},
      {"question":"The square of i⁵ is:","options":["a) -1","b) 1","c) i","d) -i"],"answer":"a","subject":"Mathematics"},
      {"question":"The roots of the quadratic equation x² - 4x + 5 = 0 are:","options":["a) real and distinct","b) real and equal","c) complex conjugates","d) none"],"answer":"c","subject":"Mathematics"},
      {"question":"If α and β are roots of x² + x + 1 = 0, then α³ + β³ = ?","options":["a) 0","b) 1","c) -1","d) 2"],"answer":"a","subject":"Mathematics"},
      {"question":"If the 3rd term of an AP is 8 and 7th term is 20, then the common difference is:","options":["a) 3","b) 4","c) 5","d) 6"],"answer":"b","subject":"Mathematics"},
      {"question":"Sum of first n natural numbers is:","options":["a) n(n+1)/2","b) n²","c) n(n-1)/2","d) 2n"],"answer":"a","subject":"Mathematics"},
      {"question":"If the first term of a GP is 3 and common ratio is 2, 4th term is:","options":["a) 12","b) 24","c) 48","d) 96"],"answer":"c","subject":"Mathematics"},
      {"question":"The slope of the line passing through points (1, 2) and (3, 6) is:","options":["a) 1","b) 2","c) 3","d) 4"],"answer":"b","subject":"Mathematics"},
      {"question":"Equation of a line parallel to x-axis and passing through (2, 3) is:","options":["a) x = 2","b) y = 3","c) y = x","d) x = y"],"answer":"b","subject":"Mathematics"},
      {"question":"Distance between points A(1, 2) and B(4, 6) is:","options":["a) 3","b) 4","c) 5","d) √13"],"answer":"c","subject":"Mathematics"},
      {"question":"limₓ→0 (sin x)/x = ?","options":["a) 0","b) 1","c) ∞","d) undefined"],"answer":"b","subject":"Mathematics"},
      {"question":"The derivative of x² is:","options":["a) 2x","b) x","c) x²","d) 1"],"answer":"a","subject":"Mathematics"},
      {"question":"The mean of 5, 10, 15, 20 is:","options":["a) 12.5","b) 10","c) 15","d) 20"],"answer":"a","subject":"Mathematics"},
      {"question":"If P(A) = 0.7, P(B) = 0.5, and A, B are independent, then P(A ∩ B) = ?","options":["a) 1.2","b) 0.2","c) 0.35","d) 0.7"],"answer":"c","subject":"Mathematics"},
      {"question":"A die is rolled once. Probability of getting an even number is:","options":["a) 1/2","b) 1/3","c) 1/6","d) 2/3"],"answer":"a","subject":"Mathematics"}
  ]
  score = {"Physics": 0, "Chemistry": 0, "Mathematics": 0}
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
    best_sub = "No subject"
  else:  
    best_sub = best

  with open('data.json', 'r') as file:
      data = json.load(file)
    
  data["score"] = score
  data['best_subject'] = best_sub

  with open('data.json', 'w') as data_file:
      json.dump(data, data_file)

  


  
