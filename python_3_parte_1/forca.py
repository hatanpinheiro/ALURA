def jogar():
    print("********************************")
    print("*********Jogo da Forca**********")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #Enquanto True E True
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            
            index = index + 1
        
        print("jogando ...")

    print("fim do jogo!")

if(__name__ == "__main__"):
    jogar()