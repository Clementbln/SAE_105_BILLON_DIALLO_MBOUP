#Importation des modules nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import xlrd


def lire_donnees_excel(fichier, colonnes):
    """Lecture des données depuis un fichier Excel avec pandas."""
    data = pd.read_excel(fichier, usecols=colonnes)
    print(data)
    return data

def tracer_graphique(fichier_excel, colonne_temps, colonne_conductivite, output_graphique):
    """Tracer et sauvegarder un graphique basé sur les données du fichier Excel."""
    workbook = xlrd.open_workbook(fichier_excel)
    onglet1 = workbook.sheet_by_index(0)

    temps = [onglet1.cell_value(row, colonne_temps) for row in range(1, onglet1.nrows)]
    conductivite = [onglet1.cell_value(row, colonne_conductivite) for row in range(1, onglet1.nrows)]

    plt.plot(temps, conductivite, label='Conductivité (µs/cm)', color='blue')
    plt.xlabel('Temps (secondes)')
    plt.ylabel('Conductivité (µs/cm)')
    plt.title('Évolution de la conductivité par rapport au temps')
    plt.legend()
    plt.savefig(output_graphique)
    plt.show()

def creer_page_html(graphe, chemin_html):
    """Créer une page HTML affichant le graphique."""
    html = f"""<h1>Graphe débit rivière</h1>
    <p><img src="{graphe}" alt="" /></p>"""

    with open(chemin_html, mode='w', encoding="utf-8") as fichier:
        fichier.write(html)





def tracer_graphique(fichier_excel, colonne_temps, colonne_conductivite, output_graphique): 
    masse= 500
    concentration_initiale= 0.2
    concentration_moyenne= 0.3
    temps= 3600
    debit= (masse/(concentation_moyenne-concentration_initiale))*temps
    print(f"le débit de la rivière est de {débit} l/s")
if __name__ == "__main__":
#Chemins des fichiers
    fichier_excel = "/home/etudiant/SAE_105_BILLON_DIALLO_MBOUP/data/conductivite_amont_20211012.xls"
    output_graphique = "/home/etudiant/SAE_105_BILLON_DIALLO_MBOUP/data/graphique_concentration.png"
    chemin_html = "html/index.html"

    #Lecture et affichage des données
    colonnes = "D,E,F,G,H,I,J"
    lire_donnees_excel(fichier_excel, colonnes)

    #Tracer et sauvegarder le graphique
    colonne_temps = 3
    colonne_conductivite = 4
    tracer_graphique(fichier_excel, colonne_temps, colonne_conductivite, output_graphique)

    #Créer une page HTML pour afficher le graphique
    creer_page_html(output_graphique, chemin_html)
