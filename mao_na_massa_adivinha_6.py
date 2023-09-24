print(30*"*")
print("Adivinhe a idade do pet Juca")
print(30*"*")

idade_juca = 4

num_tentativa = 3
rodada = 1

while(rodada <= num_tentativa):
    print("Tentativa {} de {}".format(rodada, num_tentativa))
    idade_str = input("Quantos anos você acha que Juca tem?  ")
    print("Você acha que Juca tem {}".format(idade_str)," ano(s)!")
    idade = int(idade_str)

    acertou = idade == idade_juca
    maior   = idade >  idade_juca
    menor   = idade <  idade_juca

    if(acertou):
        print("Você acertou a idade de Juca! Auauauuuu !")
    else:
        if(maior):
            print("Errou! Juca é mais novinho!")
        elif(menor):
            print("Errou! Juca é mais velhinho!")

    rodada = rodada + 1

print("A brincadeira acabou! Vamos para a próxima lição de Python!")