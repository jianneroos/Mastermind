import random
geheimecode = ""

#Aantal variabelen vaststellen
aantal_kleuren = 4
aantal_beurten = 10
kleuren = ["r", "b", "g", "c", "p", "m"]

#Computer kiest geheime code
def kiesgeheimecode(kleuren):
  geheimecode = ""
  for i in range (0,4):
    plek = random.randint(0,5)
    geheimecode += kleuren[plek]
  
  return geheimecode

#Feedback
def geeffeedback(gok, geheimecode):
  if gok == geheimecode:
    return "De kleurcode is gekraakt!"

#Kopie geheime code (list) voor juiste feedback
kopiegok = []
for i in range(len(geheimecode)):
    kopiegok.append(geheimecode [i])

feedback = []

#Regel tekst
print("Welkom bij mastermind!")
print("Leuk dat je ons spel wilt spelen. In dit spel wordt er een geheime kleurencode uitgekozen door de computer. De code bestaat uit %s letters." % (aantal_kleuren))
print("Een kleur kan vaker in de code voorkomen.")
print("De kleuren waaruit de computer kan kiezen zijn:")
print("Rood = R    Blauw = B    Groen = G    Citroengeel = C    Paars = P    Magenta = M")
print()
print("Jij als speler moet de code proberen te kraken door 4 letters in te vullen. Hiervoor heb je 10 beurten. Na elke beurt wordt er aangegeven voor hoeverre jouw geraden code overeenkomt met de geheime code.")
print()
print("Het aantal letters Z geeft aan hoeveel geraden kleuren goed zijn en op de goede plek staan.")
print("Het aantal letters W geeft aan hoeveel geraden kleuren goed zijn maar NIET op de goede plek staan.")
print()
print("Je kan alleen de letters invullen van de kleuren waaruit je kan kiezen. Bij het invullen van meer, minder of andere letters, tekens of cijfers gaat er een beurt af.")
print()
print("Voorbeeld: ZWW, dit betekent dat er drie kleuren goed zijn geraden en er daarvan één op de goede plek zit en twee op de verkeerde plek.")

#Loop van het spel
while True:
  beurt = 1
  geheimeCode = kiesgeheimecode(kleuren)
  print("Je hebt " + str(aantal_beurten) + " beurten")
  while beurt <= aantal_beurten:
    gokopnieuw = False
    print("Beurt " + str(beurt))
    gok = input().lower()
    for i in gok:
      if i.isdigit():
        gokopnieuw = True
      elif i not in kleuren:
        gokopnieuw = True

    print(geeffeedback(gok, geheimecode))
    beurt += 1

    if gok == geheimecode:
      break

#Eerste deel feedback: zitten geraden kleuren op de goede plek?
#Naar x veranderen, dus geen duplicaties voor tweede deel feedback
for i in range(aantal_kleuren):
    if gok[i] == kopiegok[i]:
      feedback.append("Z")
      kopiegok[i] = "X"

#Tweede deel feedback: zitten de geraden kleuren in de code?
#Naar x veranderen, dus geen duplicaties
for gokletter in range(aantal_kleuren):
    for codeletter in range(len(kopiegok)):
      if gok[gokletter] == kopiegok[codeletter]:
        feedback.append("W")
        kopiegok[codeletter] = "X"