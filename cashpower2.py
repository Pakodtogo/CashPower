from datetime import datetime
T1 = 96
T2 = 108
T3 = 114
T4 = 60
T5 = 96
Ttva = 18/100
Seuil = 0

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
                if (M - TQR) / (T1 + 3) + Ec <= 50:
                    Ea = (M - TQR) / (T1 + 3)
                    TVA = 0
                    Tsdaae = Ea
                    Tde = 2 * Ea
                    CEa = Ea * T1
                elif 50 < (M - (2 * Ec) - TQR - ((T2 - T1) * (Ec - 50))) / (T2 + 5) + Ec <= 150:
                    Ea = (M - (2 * Ec) - TQR - ((T2 - T1) * (Ec - 50))) / (T2 + 5)
                    TVA = 0
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    CEa = (Ea * T2) + ((Ec - 50) * (T2 - T1))
                elif 150 < (M - TQR - Ttva * ((PF + Rd) + (T2 + 5) * (Ec - 150)) - (Ec - 50) * (T2 - T1) - 2 * Ec) / ((T2 + 5) + Ttva * (T2 + 5)) + Ec <= 200:
                    Ea = (M - TQR - Ttva * ((PF + Rd) + (T2 + 5) * (Ec - 150)) - (Ec - 50) * (T2 - T1) - 2 * Ec) / ((T2 + 5) + Ttva * (T2 + 5))
                    TVA = Ttva * (PF + Rd + (Ec - 150) * (T2 + 5) + Ea * (T2 + 5))
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    CEa = (Ea * T2) + ((Ec - 50) * (T2 - T1))
                else:
                    Ea = (M - (2 * Ec) - TQR - Ttva * (PF + Rd + (50 * T2) + (Ec - 200) * T3 + (Ec - 150) * 5) - (Ec - 200) * T3 - (150 * T2) - (50 - Ec) * T1) / ((T3 + 5) + Ttva * (T3 + 5))
                    Tsdaae = (3 * Ea) + (2 * Ec)
                    Tde = 2 * Ea
                    TVA = Ttva * (Ea * (T3 + 5) + (PF + Rd + (50 * T2) + (Ec - 200) * T3 + (Ec - 150) * 5))
                    CEa = Ea * T3 + (Ec - 200) * T3 + 150 * T2 + (50 - Ec) * T1

            elif 50 < Ec <= 150:
                if (M - TQR) / (T2 + 5) + Ec <= 150:
                    Ea = (M - TQR) / (T2 + 5)
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = 0
                    CEa = Ea * T2
                elif 150 < (M - TQR - Ttva * (PF + Rd + (Ec - 150) * (T2 + 5))) / ((T2 + 5) + Ttva * (T2 + 5)) + Ec <= 200:
                    Ea = (M - TQR - Ttva * (PF + Rd + (Ec - 150) * (T2 + 5))) / ((T2 + 5) + Ttva * (T2 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = Ttva * (PF + Rd + (Ec - 150) * (T2 + 5) + Ea * (T2 + 5))
                    CEa = Ea * T2
                else:
                    Ea = (M - TQR - (Ec - 200) * (T3 - T2) - Ttva * (PF + Rd + (50 * T2) + (Ec - 200) * T3 + (Ec - 150) * 5)) / ((T3 + 5) + Ttva * (T3 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = Ttva * (PF + Rd + (50 * T2) + (Ec - 200) * T3 + (Ec - 150) * 5 + Ea * (T3 + 5))
                    CEa = (Ea * T3) + (Ec - 200) * (T3 - T2)

            elif 150 < Ec <= 200:
                if (M - TQR) / ((T2 + 5) + Ttva * (T2 + 5)) + Ec <= 200:
                    Ea = (M - TQR) / ((T2 + 5) + Ttva * (T2 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = Ttva * (Ea * (T2 + 5))
                    CEa = Ea * T2
                else:
                    Ea = (M - TQR - (Ttva * (Ec - 200) * (T3 - T2)) - (Ec - 200) * (T3 - T2)) / ((T3 + 5) + Ttva * (T3 + 5))
                    Tde = 2 * Ea
                    Tsdaae = 3 * Ea
                    TVA = Ttva * (Ea * (T3 + 5) + (Ec - 200) * (T3 - T2))
                    CEa = Ea * T3 + (Ec - 200) * (T3 - T2)

            else:
                Ea = (M - TQR) / ((T3 + 5) + Ttva * (T3 + 5))
                Tde = 2 * Ea
                Tsdaae = 3 * Ea
                TVA = Ttva * (Ea * (T3 + 5))
                CEa = Ea * T3
            
            return Ea, TVA, Tsdaae, Tde, CEa
        
def calculer_valeurs(M, TQR, PF, Rd, dd):
    if (M - PF - Rd - TQR) / (T1 + 3) <= 50:
        E = (M - PF - Rd - TQR) / (T1 + 3)
        CE = T1 * E
        Tde = 2 * E
        Tsdaae = E
        TVA = 0
    elif 50 < (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5) <= 150:
        E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5)
        CE = (T1 * 50) + (E - 50) * T2
        Tde = 2 * E
        Tsdaae = 3 * E
        TVA = 0
    elif 150 < (M + (Ttva * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (Ttva * ((PF + Rd) / dd))) / ((T2 + 5) + Ttva * (5 + T2)) <= 200:
        E = (M + (Ttva * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (Ttva * ((PF + Rd) / dd))) / ((T2 + 5) + Ttva * (5 + T2))
        CE = (T1 * 50) + (E - 50) * T2
        Tde = 2 * E
        Tsdaae = 3 * E
        TVA = Ttva * ((PF + Rd) / dd + (E - 150) * T2 + (E - 150) * 5)
    else:
        E = (M + (Ttva * (200 * T3 + 750)) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - Ttva * ((PF + Rd) / dd + (50 * T2))) / ((T3 + 5) + Ttva * (5 + T3))
        CE = (T1 * 50) + (150 * T2) + (E - 200) * T3
        Tde = 2 * E
        Tsdaae = 3 * E
        TVA = Ttva * ((PF + Rd) / dd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5)
    
    return CE, E, Tde, Tsdaae, TVA


def main():
    M = int(input("\n Entrez un Montant : "))
    TQR = calcul_TQR(M)
    CT = int(input("\n Entrez le code tarif du compteur : "))
    if CT != 17032 and CT != 17042 and CT != 17052 and CT != 17062 and CT != 17072 and CT != 17030 and CT != 17040 and CT != 17050 and CT != 17060 and CT != 17070:
        print("\nLa valeur que vous avez saisie ne correspond\na aucun code tarif de compteur triphase!\n")
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
                CE, E, Tde, Tsdaae, TVA = calculer_valeurs(M, TQR, PF, Rd, dd)
            
            elif CT == 17042:
                PF = 15918 * dd
                Rd = 1226 * dd
                CE, E, Tde, Tsdaae, TVA = calculer_valeurs(M, TQR, PF, Rd, dd)
         
            elif CT == 17052:
                PF = 21224 * dd
                Rd = 1373 * dd
                CE, E, Tde, Tsdaae, TVA = calculer_valeurs(M, TQR, PF, Rd, dd) 
         
            elif CT == 17062:
                PF = 26531 * dd
                Rd = 1373 * dd
                CE, E, Tde, Tsdaae, TVA = calculer_valeurs(M, TQR, PF, Rd, dd)
                
            elif CT == 17072:
                PF = 31837 * dd
                Rd = 1373  * dd
                CE, E, Tde, Tsdaae, TVA = calculer_valeurs(M, TQR, PF, Rd, dd)
            
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
            print("\nVous ne pouvez pas acheter des unites!\nVous avez un credit de" ,  Taxes , "FCFA \navant d'avoir droit à des unites\n")
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
