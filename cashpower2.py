from datetime import datetime

def est_premier_achat_du_mois(date_dernier_achat):
    date_actuelle = datetime.now()
    return date_dernier_achat.month != date_actuelle.month or date_dernier_achat.year != date_actuelle.year

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

def calculate_invoice(M, Ec, PF, Rd, TQR):
            if Ec <= 50:
                if (M - TQR) / (96 + 3) + Ec <= 50:
                    Ea = (M - TQR) / (96 + 3)
                    TVA = 0
                    Tsdaae = Ea
                    Tde = 2 * Ea
                    CEa = Ea * 96
                elif 50 < (M - (2 * Ec) - TQR - ((108 - 96) * (Ec - 50))) / (108 + 5) + Ec <= 150:
                    Ea = (M - (2 * Ec) - TQR - ((108 - 96) * (Ec - 50))) / (108 + 5)
                    TVA = 0
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    CEa = (Ea * 108) + ((Ec - 50) * (108 - 96))
                elif 150 < (M - TQR - (0.18 * ((PF + Rd) + (108 + 5) * (Ec - 150)) - (Ec - 50) * (108 - 96) - 2 * Ec)) / ((108 + 5) + 0.18 * (108 + 5)) + Ec <= 200:
                    Ea = (M - TQR - (0.18 * ((PF + Rd) + (108 + 5) * (Ec - 150)) - (Ec - 50) * (108 - 96) - 2 * Ec)) / ((108 + 5) + 0.18 * (108 + 5))
                    TVA = 0.18 * (PF + Rd) + (Ec - 150) * (108 + 5) * Ea * (108 + 5)
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    CEa = (Ea * 108) + ((Ec - 50) * (108 - 96))
                else:
                    Ea = (M - (2 * Ec) - TQR - 0.18 * (PF + Rd + (50 * 108) + (Ec - 200) * 114 + (Ec - 150) * 5) - (Ec - 200) * 114 - (150 * 108) - (50 - Ec) * 96) / ((114 + 5) + 0.18 * (114 + 5))
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    TVA = 0.18 * (Ea * (114 + 5) + (PF + Rd + (50 * 108) + (Ec - 200) * 114 + (Ec - 150) * 5))
                    CEa = Ea * 114 + (Ec - 200) * 114 + 150 * 108 + (50 - Ec) * 96

            elif 50 < Ec <= 150:
                if (M - TQR) / (108 + 5) + Ec <= 150:
                    Ea = (M - TQR) / (108 + 5)
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0
                    CEa = Ea * 108
                elif 150 < (M - TQR - 0.18 * (PF + Rd + (Ec - 150) * (108 + 5))) / ((108 + 5) + 0.18 * (108 + 5)) + Ec <= 200:
                    Ea = (M - TQR - 0.18 * (PF + Rd + (Ec - 150) * (108 + 5))) / ((108 + 5) + 0.18 * (108 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0.18 * (PF + Rd + (Ec - 150) * (108 + 5) + Ea * (108 + 5))
                    CEa = Ea * 108
                else:
                    Ea = (M - TQR - (Ec - 200) * (114 - 108) - 0.18 * (PF + Rd + (50 * 108) + (Ec - 200) * 114 + (Ec - 150) * 5)) / ((114 + 5) + 0.18 * (114 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0.18 * (PF + Rd + (50 * 108) + (Ec - 200) * 114 + (Ec - 150) * 5 + Ea * (114 + 5))
                    CEa = (Ea * 114) + (Ec - 200) * (114 - 108)

            elif Ec <= 200:
                if (M - TQR) / ((108 + 5) + 0.18 * (108 + 5)) + Ec <= 200:
                    Ea = (M - TQR) / ((108 + 5) + 0.18 * (108 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0.18 * (Ea * (108 + 5))
                    CEa = Ea * 108
                else:
                    Ea = (M - TQR - (0.18 * (Ec - 200) * (114 - 108)) - (Ec - 200) * (114 - 108)) / ((114 + 5) + 0.18 * (114 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0.18 * (Ea * (114 + 5) + (Ec - 200) * (114 - 108))
                    CEa = Ea * 114 + (Ec - 200) * (114 - 108)

            else:
                Ea = (M - TQR) / ((114 + 5) + 0.18 * (114 + 5))
                Tde = 2 * Ea
                Tsdaae = 3 * Ea
                TVA = 0.18 * (Ea * (114 + 5))
                CEa = Ea * 114
            
            return Ea, TVA, Tsdaae, Tde, CEa
        


def main():
    M = int(input("\n Entrez un Montant : "))
    TQR = calcul_TQR(M)
    CT = int(input("\n Entrez le code tarif du compteur : "))
    if CT != 17032 and CT != 17042 and CT != 17052 and CT != 17062 and CT != 17072:
        print("\n La valeur que vous avez saisie ne correspond\na aucun code tarif de compteur triphase!\n")
    else:
        date_dernier_achat_str = input("\n Entrez la date du dernier achat (YYYY-MM-DD) : ")
        date_dernier_achat = datetime.strptime(date_dernier_achat_str, "%Y-%m-%d")

        if est_premier_achat_du_mois(date_dernier_achat):
            date_actuelle = datetime.now()
            y = date_actuelle.year - date_dernier_achat.year
            m = date_actuelle.month - date_dernier_achat.month
            dd = (12 * y) + m
            if CT == 17032:
                PF = 10613 * dd
                Rd = 1226 * dd
            

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
                PF = 15918 * dd
                Rd = 1226 * dd

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
                PF = 21224 * dd
                Rd = 1373 * dd

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
                    E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * (PF + Rd) / dd)) / ((108 + 5) + 0.18 * (5 + 108))
                    CE = (96 * 50) + (E - 50) * 108
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 150) * 108 + (E - 150) * 5)
                else:
                    E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * ((PF + Rd) / dd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
                    CE = (96 * 50) + (150 * 108) + (E -200) * 114
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
         
            elif CT == 17062:
                PF = 26531 * dd
                Rd = 1373 * dd

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
                    E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * ((PF + Rd) / dd))) / ((108 + 5) + 0.18 * (5 + 108))
                    CE = (96 * 50) + (E - 50) * 108
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 150) * 108 + (E - 150) * 5)
                else:
                    E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * ((PF + Rd) / dd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
                    CE = (96 * 50) + (150 * 108) + (E -200) * 114
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
         
            elif CT == 17072:
                PF = 31837 * dd
                Rd = 1373  * dd

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
                    E = (M + (0.18 * (5 + 108) * 150) + (50 * 108) - PF - Rd - TQR - (50 * 96) - (0.18 * ((PF + Rd) / dd))) / ((108 + 5) + 0.18 * (5 + 108))
                    CE = (96 * 50) + (E - 50) * 108
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 150) * 108 + (E - 150) * 5)
                else:
                    E = (M + (0.18 * (200 * 114 + 750)) + (200 * 114) - PF - Rd - TQR - (150 * 108) - (50 * 96) - 0.18 * ((PF + Rd) / dd + (50 * 108))) / ((114 + 5) + 0.18 * (5 + 114))
                    CE = (96 * 50) + (150 * 108) + (E -200) * 114
                    Tde = 2 * E
                    Tsdaae = 3 * E
                    TVA = 0.18 * ((PF + Rd) / dd + (E - 200) * 114 + (50 * 108) + (E - 150) * 5)
          
            #else:
                #print("\n La valeur que vous avez saisie ne correspond\na aucun code tarif de compteur triphase!\n")
                #return 1
            Taxes = PF + Rd + TQR + TVA + Tsdaae + Tde 

        else:

            Ec = float(input("\nEntrez Le cumul d'énergie payee anterieurement dans le mois: "))
        
        
            if CT == 17032:
                PF = 10613
                Rd = 1226
                E, TVA, Tsdaae, Tde, CE = calculate_invoice(M, Ec, PF, Rd, TQR)

        
            elif CT == 17042:
                PF = 15918
                Rd = 1373
                E, TVA, Tsdaae, Tde, CE = calculate_invoice(M, Ec, PF, Rd, TQR)
        
        
            elif CT == 17052:
                PF = 21224
                Rd = 1373
                E, TVA, Tsdaae, Tde, CE = calculate_invoice(M, Ec, PF, Rd, TQR)
        

        
            elif CT == 17062:
                PF = 26531
                Rd = 1373
                E, TVA, Tsdaae, Tde, CE = calculate_invoice(M, Ec, PF, Rd, TQR)
        

        
            elif CT == 17072:
                PF = 31837
                Rd = 1373
                E, TVA, Tsdaae, Tde, CE = calculate_invoice(M, Ec, PF, Rd, TQR)
        
        
            #else:
                #print("\n Le code tarif que vous avez saisie ne correspond\na aucun code tarif de compteur triphase!\n")
                #return 1
            Taxes = TQR + TVA + Tsdaae + Tde


        if M - Taxes < 0:
            print("\n Vous ne pouvez pas acheter des unites!\n Vous avez un credit de" ,  Taxes , "FCFA \navant d'avoir droit à des unites\n")
        else:
            print("\nRedevance : ", Rd, "\n")
            print("Prime Fixe : ", PF, "\n")
            print("Tsdaae : ", Tsdaae, "\n")
            print("Tde : ", Tde, "\n")
            print("TVA : ", TVA, "\n")
            print("TQR : ", TQR, "\n")
            print("Cout Energie : ", CE, "\n")
            print("Energie payée : ", E, "\n")

if __name__ == "__main__":
    main()
