import matplotlib.pyplot as plt
import xlrd


workbook = xlrd.open_workbook('/home/etudiant/SAE_105_BILLON_DIALLO_MBOUP/docs/conductivite_amont_20211012.xls')

onglet1 = workbook.sheet_by_index(0)

temps = [onglet1.cell_value(row,3)for row in range (1,onglet1.nrows)]  
conductivite = [onglet1.cell_value(row,4) for row in range (1,onglet1.nrows)]  




plt.plot(temps, conductivite, label='Conductivité (µs/cm)', color='blue')

plt.xlabel('Temps (secondes)')
plt.ylabel('Conductivité (µs/cm)')
plt.title('Évolution de la conductivité par rapport au temps')


plt.legend()

plt.show()

