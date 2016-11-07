import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as pl
import mamdani_kleber

#Antecedentes
dor = np.arange(0,11,1)		#nivel de dor pelvica (0 a 10)

#Consequente
risco = np.arange(0,100,1)		#nivel de risco de endometriose (0 a 10)

#Funcoes de pertinencia de Dor Pelvica
#dor_leve = fuzz.trimf(dor, [0,0,5])	#dor pelvica fraca
#dor_moderada = fuzz.trimf(dor, [0,5,10])	#dor pelvica media
#dor_intensa = fuzz.trimf(dor, [5,10,10])	#dor pelvica forte
#entrada = 

#Funcoes de pertinencia do Risco de Endometriose
#risco_improvavel = fuzz.trimf(risco, [0,0,33])		#risco de endometriose baixo
#risco_poucoprovavel = fuzz.trimf(risco, [0,33,66])		#risco de endometriose medio
#risco_provavel = fuzz.trimf(risco, [33,66,100])		#risco de endometriose alto
#risco_muitoprovavel = fuzz.trimf(risco, [66,100,100])		#risco de endometriose alto

dismenorreia = []
dispareunia = []
dorcp = []
cansaco = []

k=10

for i in range(0,11):
	dismenorreia.append(mamdani_kleber.mamdani_defuzz(i,k,k,k))
	dispareunia.append(mamdani_kleber.mamdani_defuzz(k,i,k,k))	
	dorcp.append(mamdani_kleber.mamdani_defuzz(k,k,i,k))
	cansaco.append(mamdani_kleber.mamdani_defuzz(k,k,k,i))

#Montar graficos das funcoes de pertinencia
fig, (ax0, ax1, ax2, ax3) = pl.subplots(nrows=4)


#Exibir graficos das funcoes de pertinencia
#plt.xlabel('risco (%)')
ax0.plot(dor, dismenorreia)
ax0.set_ylim([0,100])
ax0.set_title("Dysmenorrhea")

ax1.plot(dor, dispareunia)
ax1.set_ylim([0,100])
ax1.set_title("Dyspareunia")

ax2.plot(dor, dorcp)
ax2.set_ylim([0,100])
ax2.set_title("Back and/or leg pains")

ax3.plot(dor, cansaco)
ax3.set_ylim([0,100])
ax3.set_title("Fatigue")

pl.tight_layout()
pl.show()
