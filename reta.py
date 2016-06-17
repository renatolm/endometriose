import mamdani
import vassilis
import numpy as np
import matplotlib.pyplot as plt

#Coletando os resultados para a variacao do sintoma dismenorreia
dismenorreia = np.arange(0,11,1)
dismenorreiaResMam = []
dismenorreiaResVas = []

for intensidade in dismenorreia:
	dismenorreiaResMam.append(mamdani.mamdani_defuzz(intensidade, 5, 5, 5))
	dismenorreiaResVas.append(vassilis.vassilis_defuzz(intensidade, 5, 5, 5))

#Coletando os resultados para a variacao do sintoma dispareunia
dispareunia = np.arange(0,11,1)
dispareuniaResMam = []
dispareuniaResVas = []

for intensidade in dispareunia:
	dispareuniaResMam.append(mamdani.mamdani_defuzz(5, intensidade, 5, 5))
	dispareuniaResVas.append(vassilis.vassilis_defuzz(5, intensidade, 5, 5))

#Coletando os resultados para a variacao do sintoma dor nas costas/pernas
dorcp = np.arange(0,11,1)
dorcpResMam = []
dorcpResVas = []

for intensidade in dorcp:
	dorcpResMam.append(mamdani.mamdani_defuzz(5, 5, intensidade, 5))
	dorcpResVas.append(vassilis.vassilis_defuzz(5, 5, intensidade, 5))

#Coletando os resultados para a variacao do sintoma cansaco
cansaco = np.arange(0,11,1)
cansacoResMam = []
cansacoResVas = []

for intensidade in cansaco:	
	cansacoResMam.append(mamdani.mamdani_defuzz(5, 5, 5, intensidade))
	cansacoResVas.append(vassilis.vassilis_defuzz(5, 5, 5, intensidade))


fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8,9))
#fig, ((ax0, ax4), (ax1, ax5), (ax2, ax6), (ax3, ax7)) = plt.subplots(nrows=4, ncols=2, figsize=(8,9), sharey=True)

ax0.plot(dismenorreia, dismenorreiaResMam, 'b', linewidth=1.5)	
ax0.set_title("Dismenorreia")
ax0.set_ylim([0,100])
	
ax1.plot(dispareunia, dispareuniaResMam, 'b', linewidth=1.5)	
ax1.set_title("Dispareunia")

ax2.plot(dorcp, dorcpResMam, 'b', linewidth=1.5)	
ax2.set_title("Dor nas Costas/Pernas")

ax3.plot(cansaco, cansacoResMam, 'b', linewidth=1.5)	
ax3.set_title("Cansaco")

#ax4.plot(dismenorreia, dismenorreiaResVas, 'b', linewidth=1.5)	
#ax4.set_title("Dismenorreia")
	
#ax5.plot(dispareunia, dispareuniaResVas, 'b', linewidth=1.5)	
#ax5.set_title("Dispareunia")

#ax6.plot(dorcp, dorcpResVas, 'b', linewidth=1.5)	
#ax6.set_title("Dor nas Costas/Pernas")

#ax7.plot(cansaco, cansacoResVas, 'b', linewidth=1.5)	
#ax7.set_title("Cansaco")

plt.tight_layout()
plt.show()