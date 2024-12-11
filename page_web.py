graphe= "/home/etudiant/SAE_105_BILLON_DIALLO_MBOUP/debit_riviere/debit_riviere.py"

html = f"""<h1>Graphe debit riviere</h1>
        <p><img src="{graphe}" alt="" /></p>"""
        
fichier = open("html/index.html", mode ='w', encoding="utf-8")
fichier.write(html)
fichier.close()
    