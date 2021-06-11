import random
import os

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
  else:
    return "".join(feedback)

#Vraag de speler of ze opnieuw willen spelen
def speelopnieuw():
  while True:
    opnieuw = input("Wil je nog een ronde spelen? (ja of nee)\n").lower()  
    if opnieuw == "nee":
      return False
    elif opnieuw != "ja":
      print("Zeg ja of nee alstublieft")
    else:
      return True

#Regel tekst
print("Welkom bij Mastermind!")
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
  #Kopie geheime code (list) voor juiste feedback
  kopiegok = []
  feedback = []

  beurt = 1
  geheimecode = kiesgeheimecode(kleuren)

  for i in range(len(geheimecode)):
      kopiegok.append(geheimecode [i])

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

    if gokopnieuw == True:
      print("Geen geldige tekens ingevoerd, probeer het opnieuw.")
      continue
    if len(gok) != aantal_kleuren:
      beurt += 1
      print("De code die is ingevuld was te lang of te kort, er gaat een beurt vanaf. Probeer het nog eens.")
      continue

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

    print(geeffeedback(gok, geheimecode))
    beurt += 1

    if gok == geheimecode:
#In de functie geef feedback zit de felicitatie
      break
 
  if beurt > aantal_beurten:
    print("Je hebt verloren")
    print("de geheime code was: %s" % (geheimecode))
  
  if speelopnieuw() == False:
    break
  else:
    os.system('cls' if os.name == 'nt' else 'clear')