def calcul_TQR(M):
    if M < 100:
        TQR = 0
    elif 100 <= M <= 1000:
        TQR = 20
    elif 1000 < M <= 5000:
        TQR = 30
    elif 5000 < M <= 10000:
        TQR = 50
    elif 10000 < M <= 50000:
        TQR = 100
    else:
        n = M // 50000
        TQR = 50 * (n + 2)
    return TQR

def main():
    M = int(input("Entrez un Montant : "))
    TQR = calcul_TQR(M)
    CT = int(input("Entrez le code tarif du compteur : "))

    if CT == 17032:
        PF = 10613
        Rd = 1226

        if M <= 16889:
            E = (M - PF - Rd - TQR) / (96 + 3)
            CE = 96 * E
            Tde = 2 * E
            Tsdaae = E
            TVA = 0
        elif 16889 < M <= 27089:
            E = (M + (50 * 108) - PF - Rd - TQR - (50 * 96)) / (108 + 5)
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0
        elif 27089 < M <= 37987.02:
            E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd))) / ((108 + 5) + 0.18 * (5 + 108))
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 150) * 108 + (E - 150) * 5)
        else:
            E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * (PF + Rd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
            CE = (96 * 50) + (150 * 108) + (E -200) * 114
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
    elif CT == 17042:
        PF = 15918
        Rd = 1226

        if M <= 22194:
            E = (M - PF - Rd - TQR) / (96 + 3)
            CE = 96 * E
            Tde = 2 * E
            Tsdaae = E
            TVA = 0
        elif 22194 < M <= 32394:
            E = (M + (50 * 108) - PF - Rd - TQR - (50 * 96)) / (108 + 5)
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0
        elif 32394 < M <= 44246.92:
            E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd))) / ((108 + 5) + 0.18 * (5 + 108))
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 150) * 108 + (E - 150) * 5)
        else:
            E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * (PF + Rd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
            CE = (96 * 50) + (150 * 108) + (E -200) * 114
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
    elif CT == 17052:
        PF = 21224
        Rd = 1373

        if M <= 27647:
            E = (M - PF - Rd - TQR) / (96 + 3)
            CE = 96 * E
            Tde = 2 * E
            Tsdaae = E
            TVA = 0
        elif 27647 < M <= 37847:
            E = (M + (50 * 108) - PF - Rd - TQR - (50 * 96)) / (108 + 5)
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0
        elif 37847 < M <= 50731.46:
            E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd))) / ((108 + 5) + 0.18 * (5 + 108))
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 150) * 108 + (E - 150) * 5)
        else:
            E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * (PF + Rd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
            CE = (96 * 50) + (150 * 108) + (E -200) * 114
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
    elif CT == 17062:
        PF = 26531
        Rd = 1373

        if M <= 32954:
            E = (M - PF - Rd - TQR) / (96 + 3)
            CE = 96 * E
            Tde = 2 * E
            Tsdaae = E
            TVA = 0
        elif 32954 < M <= 43154:
            E = (M + (50 * 108) - PF - Rd - TQR - (50 * 96)) / (108 + 5)
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0
        elif 43154 < M <= 56993.72:
            E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd))) / ((108 + 5) + 0.18 * (5 + 108))
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 150) * 108 + (E - 150) * 5)
        else:
            E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * (PF + Rd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
            CE = (96 * 50) + (150 * 108) + (E -200) * 114
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
    elif CT == 17072:
        PF = 31837
        Rd = 1373

        if M <= 38260:
            E = (M - PF - Rd - TQR) / (96 + 3)
            CE = 96 * E
            Tde = 2 * E
            Tsdaae = E
            TVA = 0
        elif 38260 < M <= 48460:
            E = (M + (50 * 108) - PF - Rd - TQR - (50 * 96)) / (108 + 5)
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0
        elif 48460 < M <= 63254.8:
            E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd))) / ((108 + 5) + 0.18 * (5 + 108))
            CE = (96 * 50) + (E - 50) * 108
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 150) * 108 + (E - 150) * 5)
        else:
            E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * (PF + Rd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
            CE = (96 * 50) + (150 * 108) + (E -200) * 114
            Tde = 2 * E
            Tsdaae = 3 * E
            TVA = 0.18 * (PF + Rd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
    else:
        print("La valeur que vous avez entrée ne correspond à aucun code tarif de compteur triphasé!")
        return 1

    print("Redevance : ", Rd, "\n")
    print("Prime Fixe : ", PF, "\n")
    print("Tsdaae : ", Tsdaae, "\n")
    print("Tde : ", Tde, "\n")
    print("TVA : ", TVA, "\n")
    print("TQR : ", TQR, "\n")
    print("Cout Energie : ", CE, "\n")
    print("Energie payée : ", E, "\n")

if __name__ == "__main__":
    main()
