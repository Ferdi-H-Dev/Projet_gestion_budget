print("**************************************************")
print("                               GESTION DU BUDGET")
print("**************************************************")


# CREATION DE LA CLASS GESTIONBUDGET
class GestionBudget():
    # DEFINITION DES ATTRIBUTS CONSTRUCTEUR DE LA CLASS
    def __init__(self, sommeSalaireetRevenu, sommeEnergies, sommeTransports, sommeImpotetTaxes, sommeAssurances,
                 sommeCotisationBancaire, sommeMobileetFixe, sommeLoisirs):
        self.sommeSalaireetRevenu = sommeSalaireetRevenu
        self.sommeEnergies = sommeEnergies
        self.sommeTransports = sommeTransports
        self.sommeImpotetTaxes = sommeImpotetTaxes
        self.sommeAssurances = sommeAssurances
        self.sommeCotisationBancaire = sommeCotisationBancaire
        self.sommeMobileetFixe = sommeMobileetFixe
        self.sommeLoisirs = sommeLoisirs

    # CREATION ET DEFINITION D'UNE FONCTION DEPENSE DANS LA CLASS
    def Depense(self):
        self.sommeSalaireetRevenu = sSalaireetRevenu - (
                    self.sommeEnergies + self.sommeTransports + self.sommeImpotetTaxes + self.sommeAssurances + self.sommeCotisationBancaire + self.sommeMobileetFixe + self.sommeLoisirs)
        print("Votre budget a été crée.")
        # print("Vous venez de créer un budget :", "\n", self.sommeSalaireetRevenu, "€ de revenu net.")

    # CREATION ET DEFINITION D'UNE FONCTION MONTANTDEPENSE DANS LA CLASS
    def MontantDepense(self):
        self.sommeMontantDepense = float(input("Entrez un montant: "))
        print("Le montant de votre dépense est de : ", "\n", self.sommeMontantDepense, "€")
        self.sommeSalaireetRevenu -= self.sommeMontantDepense
        # print("Il vous reste :", "\n", self.sommeSalaireetRevenu, "€ de budget.")

    # CREATION ET DEFINITION D'UNE FONCTION AFFICHERSOLDE DANS LA CLASS
    def AfficherSolde(self):
        self.sommeSoldeBudget = self.sommeSalaireetRevenu
        print("Il vous reste un budget de: ", "\n", self.sommeSalaireetRevenu, "€")

# CREATION D'UNE BOUCLE TANTQUE EN LUI AFFILANT TRUE POUR QUELLE SOIT INFINI
while True:

    # CREATION DES VARIABLES POUR INCREMENTER LES CONSTRUCTEURS DE LA CLASS GESTIONBUDGET
    sSalaireetRevenu = float(input("Entrez la somme du salaire net et autres revenue: "))
    sEnergies = float(input("Entrez la somme des energies: "))
    sTransports = float(input("Entrez la somme des transports: "))
    sImpotetTaxes = float(input("Entrez la somme impôt et taxes: "))
    sAssurances = float(input("Entrez la somme des assurances: "))
    sCotisationBancaire = float(input("Entrez la somme de la cotisation bancaire: "))
    sMobileetFixe = float(input("Entrez la somme abonnement mobile et fixe: "))
    sLoisirs = float(input("Entrez la somme des loisirs: "))

    # LA VARIABLE BUDGET1 PREND LA VALEUR DE LA CLASS GEASTIONBUDGET
    budget1 = GestionBudget(sSalaireetRevenu, sEnergies, sTransports, sImpotetTaxes, sAssurances, sCotisationBancaire, sMobileetFixe, sLoisirs)

    # APPEL DE LA FONCTION DEPENSE PAR LE BIAIS DE LA VARIABLE BUDGET1 POUR POUVOIR EXERCER LES ACTIONS DECU
    budget1.Depense()

    # CREATION DE LA VARIABLE QUITTER QUI  DETERMINE LA CONDITION DE LA BOUCLE TANTQUE
    quitter = 0

    # CREATION DE LA BOUCLE TANTQUE QUITTER
    while quitter == 0:

        # CREATION DU MENU
        print(" 1=> ENTREZ UNE DEPENSE", "\n", "2=> POUR AFFICHER LE SOLDE", "\n", "3=> QUITTER")
        print("---------------------------------------------------------------------------------------")

        # CREATION DE LA VARIABLE ACTION  POUR ENTRER LE CHOIX DE L'UTILISATEUR
        action = int(input("Entrez votre choix: "))

        # APPEL DE LA FONCTION MONTANTDEPENSE SI ACTION A UNE VALEUR DE 1
        if action == 1:
            budget1.MontantDepense()

        # APPEL DE LA FONCTION AFFICHERSOLDE SI ACTION A UNE VALEUR DE 2
        elif action == 2:
            budget1.AfficherSolde()

        # PERMET DE SORTIR DE LA BOUCLE TANTQUE QUITTER SI ACTION A UNE VALEUR DE 3
        elif action == 3:
            print("Vous quitter le programme!")
            quitter = 1

    # PERMET DE CASSER LA BOUCLE TANTQUE TRUE POUR FERMER LE PROGRAMME
    break