import pandas as pd

if __name__ == "__main__":
    data = pd.read_excel("/home/etudiant/SAE_105_BILLON_DIALLO_MBOUP/data/conductivite_amont_20211012.xls", usecols="D,E,F,G,H,I,J")

print (data) 
