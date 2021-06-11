aantal_kleuren = 4

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
