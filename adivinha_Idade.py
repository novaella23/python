print("**************************")
print("Adivinha a minha idade !")
print("***************************")

minha_idade = 44

chute_str = input("Quantos anos você acha que eu tenho? Digite: ")
print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == minha_idade
maior   = chute  > minha_idade
menor   = chute  < minha_idade

if(acertou):
    print("Wow! Você acertou minha idade!")
else:
    if(maior):
        print("AHh errou! Você chutou uma idade maior que a minha!")
    elif(menor):
        print("AHh errou! Você chutou uma idade menor que a minha! Fiquei até feliz!")

print("A brincadeira acabou. Agora vamos voltar aos estudos de Python!")

