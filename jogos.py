import forca
import adivinhacao



print("*********************************")
print("********Escolha seu Jogo!********")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Digite o jogo: "))

if(jogo == 1):
    print("Forca")
    forca.jogar_forca()
elif (jogo == 2):
    print("Adivinhação")
    adivinhacao.jogar_advinhacao()
else:
    print("nenhum jogo")

print("**************************")
