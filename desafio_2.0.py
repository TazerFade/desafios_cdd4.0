while True:
    palavra = "PyThOn"  # Palavra secreta
    letras_descobertas = []
    for letra in palavra:
        letras_descobertas.append("_")

    letras_erradas = []
    vidas = 6

    bonecos = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    
         |    
         |    
         |
        --------
        """
    ]

    while True:
        print("\n\033[94mPalavra:\033[0m ", end="")
        for letra in letras_descobertas:
            print(letra, end=" ")
        print("\n")

        print("\033[91mLetras erradas:\033[0m", end=" ")
        for letra in letras_erradas:
            print(letra, end=" ")
        print("\n")

        print("\033[94mVidas restantes:\033[0m", vidas)

        tentativa = input("Digite uma letra ou chute a palavra: ")

        # Verificação de caractere válido
        valido = True
        for c in tentativa:
            if not (("a" <= c <= "z") or ("A" <= c <= "Z")):
                valido = False
        if valido == False or len(tentativa) == 0:
            print("\033[91mCaractere inválido, por favor digite novamente.\033[0m")
            continue

        # CHUTE DE PALAVRA
        if len(tentativa) > 1:
            if tentativa == palavra:
                for i in range(len(palavra)):
                    letras_descobertas[i] = palavra[i]
                print("\n\033[92mParabéns! Você acertou a palavra inteira!\033[0m")
                break
            else:
                print("\033[91mChute incorreto! Você perdeu DUAS vidas.\033[0m")
                vidas -= 2
                if vidas < 0:
                    vidas = 0
                print(bonecos[6 - vidas])
        else:
            # TENTATIVA DE UMA LETRA
            letra_tentativa = tentativa

            letra_repetida = False
            for letra in letras_descobertas:
                if letra == letra_tentativa:
                    letra_repetida = True
            for letra in letras_erradas:
                if letra == letra_tentativa:
                    letra_repetida = True

            if letra_repetida:
                print("Você já tentou essa letra.")
                continue

            acertou = False
            for i in range(len(palavra)):
                letra_palavra = palavra[i]
                if letra_palavra == letra_tentativa or (
                    "a" <= letra_palavra <= "z" and chr(ord(letra_palavra) - 32) == letra_tentativa) or (
                    "A" <= letra_palavra <= "Z" and chr(ord(letra_palavra) + 32) == letra_tentativa):
                    letras_descobertas[i] = palavra[i]
                    acertou = True

            if not acertou:
                letras_erradas.append(letra_tentativa)
                vidas -= 1
                print("\033[91mLetra errada!\033[0m")
                print("\033[91mDesenhando a forca...\033[0m")
                print(bonecos[6 - vidas])

        if "_" not in letras_descobertas:
            print("\n\033[92mParabéns! Você venceu! A palavra era:\033[0m", palavra)
            break

        if vidas <= 0:
            print("\n\033[91mVocê perdeu! A palavra era:\033[0m", palavra)
            print(bonecos[0])
            break

    print("\nDeseja jogar novamente? (s/n): ")
    resposta = input()
    if resposta != "s" and resposta != "S":
        print("Obrigado por jogar!")
        break