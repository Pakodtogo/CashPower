import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;
import java.util.Scanner;

public class CashPower {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        Random random = new Random();
        int T1 = 96;
        int T2 = 108;
        int T3 = 114;
        int T4 = 60;
        int T5 = 96;
        double Ttva = 18.0 / 100;
        int Seuil = 0;
        int TQR;
        int PF, Rd;
        double M, CE, E, Tde, Tsdaae, TVA;
        
        String[] groups_of_digits = new String[5];
        for (int i = 0; i < 5; i++) {
            groups_of_digits[i] = String.format("%04d", random.nextInt(10000));
        }
        String combinaison = String.join(" ", groups_of_digits);
        
        Date date_dernier_achat = new Date();
        
        System.out.print("\nEnter a Montant: ");
        M = scanner.nextInt();
        
        TQR = calculTQR(M);
        
        System.out.print("\nEnter the code tarif du compteur: ");
        int CT = scanner.nextInt();
        
        if (CT != 17032 && CT != 17042 && CT != 17052 && CT != 17062 && CT != 17072 && CT != 17030 && CT != 17040 && CT != 17050 && CT != 17060 && CT != 17070) {
            System.out.println("\nThe value you entered does not correspond to any triphase meter tariff code!\nYou are neither a customer nor an agent of SONABEL");
        } else {
            if (CT == 17030 || CT == 17040 || CT == 17050 || CT == 17060 || CT == 17070) {
                System.out.println("\nYou are an agent of SONABEL\n");
                System.out.print("\nEnter your category (1 to 9): ");
                int Cat = scanner.nextInt();
                
                if (Cat < 1 || Cat > 9) {
                    System.out.println("\nError! Please enter a value between 1 and 9\n");
                } else if (Cat <= 5) {
                    Seuil = 600;
                } else {
                    Seuil = 650;
                }
            } else {
                System.out.println("\nYou are a customer!");
            }
            
            System.out.print("\nEnter the date of last purchase (JJ-MM-AAAA): ");
            String date_dernier_achat_str = scanner.next();
            try {
                SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
                date_dernier_achat = dateFormat.parse(date_dernier_achat_str);
            } catch (ParseException e) {
                e.printStackTrace();
            }
            
            if (estPremierAchatDuMois(date_dernier_achat)) {
                Date date_actuelle = new Date();
                int y = date_actuelle.getYear() - date_dernier_achat.getYear();
                int m = date_actuelle.getMonth() - date_dernier_achat.getMonth();
                int dd = (12 * y) + m;
                
                PF = 0;
                Rd = 0;
                CE = 0;
                E = 0;
                TVA = 0;
                Tsdaae = 0;
                Tde = 0;
                
                if (CT == 17032) {
                    PF = 10613 * dd;
                    Rd = 1226 * dd;
                    double[] result = clientPAM(M, TQR, PF, Rd, dd);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                } else if (CT == 17042) {
                    PF = 15918 * dd;
                    Rd = 1226 * dd;
                    double[] result = clientPAM(M, TQR, PF, Rd, dd);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                } else if (CT == 17052) {
                    PF = 21224 * dd;
                    Rd = 1373 * dd;
                    double[] result = clientPAM(M, TQR, PF, Rd, dd);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                } else if (CT == 17062) {
                    PF = 26531 * dd;
                    Rd = 1373 * dd;
                    double[] result = clientPAM(M, TQR, PF, Rd, dd);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                } else if (CT == 17072) {
                    PF = 31837 * dd;
                    Rd = 1373 * dd;
                    double[] result = clientPAM(M, TQR, PF, Rd, dd);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                } else if (CT == 17030) {
                  PF = 10613;
                  Rd = 1226;
                    double[] result = agentPAM(M, TQR, PF, Rd, Seuil);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17040) {
                    PF = 15918;
                    Rd = 1226;
                    double[] result = agentPAM(M, TQR, PF, Rd, Seuil);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17050) {
                    PF = 21224;
                    Rd = 1373;
                    double[] result = agentPAM(M, TQR, PF, Rd, Seuil);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17060) {
                    PF = 26531;
                    Rd = 1373;
                    double[] result = agentPAM(M, TQR, PF, Rd, Seuil);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17070) {
                    PF = 31837;
                    Rd = 1226;
                    double[] result = agentPAM(M, TQR, PF, Rd, Seuil);
                    CE = result[0];
                    E = result[1];
                    Tde = result[2];
                    Tsdaae = result[3];
                    TVA = result[4];
                    PF = 0;
                    Rd = 0;
                }
                
                double Taxes = PF + Rd + calculTQR(PF + Rd);
                

            } else {
              System.out.print("\nEnter the cumulative energy paid previously in the month: ");
              double Ec = scanner.nextDouble();

              if (CT == 17032) {
                    PF = 10613;
                    Rd = 1226;
                    double[] result = clientNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
            } else if (CT == 17042) {
                    PF = 15918;
                    Rd = 1226;
                    double[] result = clientNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17052) {
                    PF = 21224;
                    Rd = 1373;
                    double[] result = clientNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17062) {
                    PF = 26531;
                    Rd = 1373;
                    double[] result = clientNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17072) {
                    PF = 31837;
                    Rd = 1373;
                    double[] result = clientNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17030) {
                    PF = 10613;
                    Rd = 1226;
                    double[] result = agentNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
            } else if (CT == 17040) {
                    PF = 15918;
                    Rd = 1226;
                    double[] result = agentNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17050) {
                    PF = 21224;
                    Rd = 1373;
                    double[] result = agentNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17060) {
                    PF = 26531;
                    Rd = 1373;
                    double[] result = agentNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } else if (CT == 17070) {
                    PF = 31837;
                    Rd = 1373;
                    double[] result = agentNonPAM(M, Ec, PF, Rd, TQR);
                    E = (int) result[0];
                    TVA = result[1];
                    Tsdaae = result[2];
                    Tde = result[3];
                    CE = result[4];
                    PF = 0;
                    Rd = 0;
                } 

            if (M - Taxes < 0) {
              System.out.println("\nYou cannot purchase units!\nYou have a credit of " + Taxes + " FCFA\nbefore being eligible for units\n");
          } else {
            System.out.println("\nRedevance : " + Rd);
            System.out.println("Prime Fixe : " + PF);
            System.out.println("Tsdaae : " + Tsdaae);
            System.out.println("Tde : " + Tde);
            System.out.println("TVA : " + TVA);
            System.out.println("TQR : " + TQR);
            System.out.println("Cout Energie : " + CE);
            System.out.println("Energie payée : " + E);
          }
        }
    }

    public static int calculTQR(int Montant) {
        if (Montant <= 5000) {
            return 100;
        } else if (Montant <= 10000) {
            return 200;
        } else {
            return 300;
        }
    }

    public static boolean estPremierAchatDuMois(Date date) {
        Date date_actuelle = new Date();
        SimpleDateFormat monthFormat = new SimpleDateFormat("MM");
        String currentMonth = monthFormat.format(date_actuelle);
        String purchaseMonth = monthFormat.format(date);

        return currentMonth.equals(purchaseMonth);
    }

    public static double[] clientPAM(int Montant, int TQR, int PF, int Rd, int dd) {
        double Td = (30 - dd) * TQR;
        double CE = 0.01 * Montant;
        double E = Montant - (Td + PF + Rd + CE);
        double TVA = Ttva * (E + TQR);
        double Tsdaae = 0.01 * (E + TQR);
        
        double[] result = { CE, E, Td, Tsdaae, TVA };
        return result;
    }
}
