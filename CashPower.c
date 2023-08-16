#include<stdio.h>

const int T1 = 96;
const int T2 = 108;
const int T3 = 114;

int calculTQR(int M)
{
    int TQR;

    if (M < 100)
    {
        TQR = 0;
    }
    else if (M >= 100 && M <= 1000)
    {
        TQR = 20;
    }
    else if (M > 1000 && M <= 5000)
    {
        TQR = 30;
    }
    else if (M > 5000 && M <= 10000)
    {
        TQR = 50;
    }
    else if (M > 10000 && M <= 50000)
    {
        TQR = 100;
    }
    else
    {
        int n = M / 50000;
        TQR = 50 * (n + 2);
    }

    return TQR;
}

int main()
{
    int M, TQR, CT, PF, Rd;
    float E, CE, Tde, Tsdaae, TVA;

    printf("Entrez un Montant : ");
    scanf("%d", &M);

    TQR = calculTQR(M);
    printf("Entrez le code tarif du compteur : ");
    scanf("%d", &CT);

    if (CT == 17032)
    {
        PF = 10613;
        Rd = 1226;

        if (M >= 11939 && M <= 16889)
        {
            E = (M - PF - Rd - TQR) / (T1 + 3);
            CE = T1 * E;
            Tde = 2 * E;
            Tsdaae = E;
            TVA = 0;
        }
        else if (M > 16889 && M <= 27089)
        {
            E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5);
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0;
        }
        else if (M > 27089 && M <= 37987.02)
        {
            E = (M + (0.18 * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (0.18 * (PF + Rd))) / ((T2 + 5) + 0.18 * (5 + T2));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 150) * T2 + (E - 150) * 5);
        }
        else
        {
            E = (M + (0.18 * (200 * T2) + 750) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - (0.18 * (PF + Rd))) / ((T3 + 5) + 0.18 * (5 + T3));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5);
        }
    }
    else if (CT == 17042)
    {
        PF = 15918;
        Rd = 1226;

        if (M >= 17244 && M <= 22194)
        {
            E = (M - PF - Rd - TQR) / (T1 + 3);
            CE = T1 * E;
            Tde = 2 * E;
            Tsdaae = E;
            TVA = 0;
        }
        else if (M > 22194 && M <= 32394)
        {
            E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5);
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0;
        }
        else if (M > 32394 && M <= 44246.92)
        {
            E = (M + (0.18 * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (0.18 * (PF + Rd))) / ((T2 + 5) + 0.18 * (5 + T2));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 150) * T2 + (E - 150) * 5);
        }
        else
        {
            E = (M + (0.18 * (200 * T2) + 750) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - (0.18 * (PF + Rd))) / ((T3 + 5) + 0.18 * (5 + T3));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5);
        }
    }
    else if (CT == 17052)
    {
        PF = 21224;
        Rd = 1373;

        if (M >= 22697 && M <= 27647)
        {
            E = (M - PF - Rd - TQR) / (T1 + 3);
            CE = T1 * E;
            Tde = 2 * E;
            Tsdaae = E;
            TVA = 0;
        }
        else if (M > 27647 && M <= 37847)
        {
            E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5);
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0;
        }
        else if (M > 37847 && M <= 50731.46)
        {
            E = (M + (0.18 * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (0.18 * (PF + Rd))) / ((T2 + 5) + 0.18 * (5 + T2));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 150) * T2 + (E - 150) * 5);
        }
        else
        {
            E = (M + (0.18 * (200 * T2) + 750) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - (0.18 * (PF + Rd))) / ((T3 + 5) + 0.18 * (5 + T3));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5);
        }
    }
    else if (CT == 17062)
    {
        PF = 26531;
        Rd = 1373;

        if (M >= 28004 && M <= 32954)
        {
            E = (M - PF - Rd - TQR) / (T1 + 3);
            CE = T1 * E;
            Tde = 2 * E;
            Tsdaae = E;
            TVA = 0;
        }
        else if (M > 32954 && M <= 43154)
        {
            E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5);
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0;
        }
        else if (M > 43154 && M <= 56993.72)
        {
            E = (M + (0.18 * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (0.18 * (PF + Rd))) / ((T2 + 5) + 0.18 * (5 + T2));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 150) * T2 + (E - 150) * 5);
        }
        else
        {
            E = (M + (0.18 * (200 * T2) + 750) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - (0.18 * (PF + Rd))) / ((T3 + 5) + 0.18 * (5 + T3));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5);
        }
    }
    else if (CT == 17072)
    {
        PF = 31837;
        Rd = 1373;

        if (M >= 33310 && M <= 38260)
        {
            E = (M - PF - Rd - TQR) / (T1 + 3);
            CE = T1 * E;
            Tde = 2 * E;
            Tsdaae = E;
            TVA = 0;
        }
        else if (M > 38260 && M <= 48460)
        {
            E = (M + (50 * T2) - PF - Rd - TQR - (50 * T1)) / (T2 + 5);
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0;
        }
        else if (M > 48460 && M <= 63254.8)
        {
            E = (M + (0.18 * (5 + T2) * 150) + (50 * T2) - PF - Rd - TQR - (50 * T1) - (0.18 * (PF + Rd))) / ((T2 + 5) + 0.18 * (5 + T2));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 150) * T2 + (E - 150) * 5);
        }
        else
        {
            E = (M + (0.18 * (200 * T2) + 750) + (200 * T3) - PF - Rd - TQR - (150 * T2) - (50 * T1) - (0.18 * (PF + Rd))) / ((T3 + 5) + 0.18 * (5 + T3));
            CE = (T1 * 50) + (E - 50) * T2;
            Tde = 2 * E;
            Tsdaae = 3 * E;
            TVA = 0.18 * (PF + Rd + (E - 200) * T3 + (50 * T2) + (E - 150) * 5);
        }
    }
    else
    {
        printf("La valeur que vous avez entrée ne correspond à aucun code tarif de compteur triphasé!\n");
        return 1;
    }

    printf("Redevance : %d\n", Rd);
    printf("Prime Fixe : %d\n", PF);
    printf("Tsdaae : %.2f\n", Tsdaae);
    printf("Tde : %.2f\n", Tde);
    printf("TVA : %.2f\n", TVA);
    printf("TQR : %d\n", TQR);
    printf("Cout Energie : %.2f\n", CE);
    printf("Energie payée : %.2f\n", E);

    getchar(); 

    return 0;
}
