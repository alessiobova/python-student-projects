##gioco della morra cinese. 

import random

print("CIAO, OGGI GIOCHIAMO AL GIOCO DELLA MORRA CINESE!")

computer=random.randint(0,2)
if computer==0:
    computer="s"
elif computer==1:
    computer="f"
else:
    computer="c"
    
utente=input('Inserisci c per carta, s per sasso ed f per forbice: ')

if utente!="s" and utente!="f" and utente!="c":
    print("la lettera non corrisponde a nulla")
elif utente=='s' and computer=='s' or utente=='c' and computer=='c' or utente=='f' and computer=='f':   
    print("Parita'!")
elif utente=="s" and computer=="f" or utente=="f" and computer=="c" or utente=="c" and computer=="s":
    print("UTENTE HA VINTO!")
else:
    print("HA VINTO IL COMPUTER!")
