# Je créer ma variable x qui vas demander a l'utilisateur si il est pret a faire son calcul de son IMC
x=input("Yoo are you ready for calculate your IMC ? ")
# Je mes la condition si l'utilisateur répond "Yes" (le == définit si la reponse et strictment Yes)
if x=='Yes':
    #  Je créer ma nouvelle variable weight qui vas demander a l'utilisateur un nombre entier ou a virgule grace a la fonction float
    weight=float(input("Okay give me your weight in KILOGRAM : "))
    # Je recréer une nouvelle variables size qui vas demander a l'utilisateur un nombre entier ou a virgule grace a la fonction float
    size=float(input("And give me your size in METER : "))
    # J'affiche un texte avec print
    print("Thank let's calculate your IMC")
    # Je créer une nouvelle variable imc qui vas faire la formule de imc en faisant weight diviser par size au carré (**2)
    imc=weight/size**2
    # Je fais une condition qui dis que si l'imc et inférieur a 18.5 alors
    if imc<18.5:
        # J'affiche la variale grace a f et {imc}
        print(f"Bruh you have {imc} IMC you are so skinny")
    # Je refais une condition qui dis que si l'imc et egal ou supérieur a 18.5 et l'imc et egal ou inférieur a 24.9 alors
    if imc>=18.5 and imc<=24.9:
        print(f"You are okay you have {imc} IMC")
    # Je refais une condition qui dis que si l'imc et egal ou supérieur a 25.0 et l'imc et egal ou inférieur a 29.9 alors
    if imc>=25.0 and imc<=29.9:
        print(f"Bruh you have {imc} IMC STOP MCDO PLSSS !")
    # Je refais une condition qui dis que si l'imc et egal ou supérieur a 30 alors
    if imc>=30:
        print(f"YOO YOU HAVE {imc} IMC ARE YOU CRAZY ???")