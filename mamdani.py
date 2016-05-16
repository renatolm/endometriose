import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#Antecedentes
dorPelvica = np.arange(0,11,1)		#nivel de dor pelvica (0 a 10)
dificuldadeEngravidar = np.arange(0,11,1)		#nivel de dificuldade para engravidar (deveria ser um sim/nao?)
dorNasCostasPernas = np.arange(0,11,1)		#nivel de dor nas costas/pernas (0 a 10)

#Consequente
risco = np.arange(0,11,1)		#nivel de risco de endometriose (0 a 10)

#Funcoes de pertinencia de Dor Pelvica
dorP_fraca = fuzz.trimf(dorPelvica, [0,0,5])	#dor pelvica fraca
dorP_media = fuzz.trimf(dorPelvica, [0,5,10])	#dor pelvica media
dorP_forte = fuzz.trimf(dorPelvica, [5,10,10])	#dor pelvica forte

#Funcoes de pertinencia de Dificuldade Para Engravidar
dific_baixa = fuzz.trimf(dificuldadeEngravidar, [0,0,5])	#dificuldade baixa
dific_media = fuzz.trimf(dificuldadeEngravidar, [0,5,10])	#dificuldade media
dific_alta = fuzz.trimf(dificuldadeEngravidar, [5,10,10])	#dificuldade alta

#Funcoes de pertinencia de Dor Nas Costas e Pernas
dorCP_fraca = fuzz.trimf(dorNasCostasPernas, [0,0,5])		#dor nas costas e/ou pernas fraca
dorCP_media = fuzz.trimf(dorNasCostasPernas, [0,5,10])		#dor nas costas e/ou pernas media
dorCP_forte = fuzz.trimf(dorNasCostasPernas, [5,10,10])		#dor nas costas e/ou pernas forte

#Funcoes de pertinencia do Risco de Endometriose
risco_baixo = fuzz.trimf(risco, [0,0,5])		#risco de endometriose baixo
risco_medio = fuzz.trimf(risco, [0,5,10])		#risco de endometriose medio
risco_alto = fuzz.trimf(risco, [5,10,10])		#risco de endometriose alto

#Montar graficos das funcoes de pertinencia
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8,9))

ax0.plot(dorPelvica, dorP_fraca, 'b', linewidth=1.5, label='Fraca')
ax0.plot(dorPelvica, dorP_media, 'g', linewidth=1.5, label='Media')
ax0.plot(dorPelvica, dorP_forte, 'r', linewidth=1.5, label='Forte')
ax0.set_title("Dor Pelvica")
ax0.legend()

ax1.plot(dificuldadeEngravidar, dific_baixa, 'b', linewidth=1.5, label='Baixa')
ax1.plot(dificuldadeEngravidar, dific_media, 'g', linewidth=1.5, label='Media')
ax1.plot(dificuldadeEngravidar, dific_alta, 'r', linewidth=1.5, label='Alta')
ax1.set_title("Dificuldade Para Engravidar")
ax1.legend()

ax2.plot(dorNasCostasPernas, dorCP_fraca, 'b', linewidth=1.5, label='Fraca')
ax2.plot(dorNasCostasPernas, dorCP_media, 'g', linewidth=1.5, label='Media')
ax2.plot(dorNasCostasPernas, dorCP_forte, 'r', linewidth=1.5, label='Forte')
ax2.set_title("Dor Nas Costas e Pernas")
ax2.legend()

ax3.plot(risco, risco_baixo, 'b', linewidth=1.5, label='Baixo')
ax3.plot(risco, risco_medio, 'g', linewidth=1.5, label='Medio')
ax3.plot(risco, risco_alto, 'r', linewidth=1.5, label='Alto')
ax3.set_title("Risco de Endometriose")
ax3.legend()

#Exibir graficos das funcoes de pertinencia
plt.tight_layout()
plt.show()


## Simulando uma entrada com:
#Nivel de dor pelvica 9
dorP_nivel_fraca = fuzz.interp_membership(dorPelvica, dorP_fraca, 9)	#faz a interseção da entrada (9) com a funcao de pertinencia da dor pelvica fraca
dorP_nivel_media = fuzz.interp_membership(dorPelvica, dorP_media, 9)	#faz a interseção da entrada (9) com a funcao de pertinencia da dor pelvica media
dorP_nivel_forte = fuzz.interp_membership(dorPelvica, dorP_forte, 9)	#faz a interseção da entrada (9) com a funcao de pertinencia da dor pelvica forte

#Nivel de dificuldade para engravidar 7
dificuldade_nivel_baixa = fuzz.interp_membership(dificuldadeEngravidar, dific_baixa, 7)	#faz a interseção da entrada (7) com a funcao de pertinencia da dificuldade baixa
dificuldade_nivel_media = fuzz.interp_membership(dificuldadeEngravidar, dific_media, 7)	#faz a interseção da entrada (7) com a funcao de pertinencia da dificuldade media
dificuldade_nivel_alta = fuzz.interp_membership(dificuldadeEngravidar, dific_alta, 7)	#faz a interseção da entrada (7) com a funcao de pertinencia da dificuldade alta

#Nivel de dor nas costas/pernas 8
dorCP_nivel_fraca = fuzz.interp_membership(dorNasCostasPernas, dorCP_fraca, 8)	#faz a interseção da entrada (8) com a funcao de pertinencia da dor nas costas/pernas fraca
dorCP_nivel_media = fuzz.interp_membership(dorNasCostasPernas, dorCP_media, 8)	#faz a interseção da entrada (8) com a funcao de pertinencia da dor nas costas/pernas media
dorCP_nivel_forte = fuzz.interp_membership(dorNasCostasPernas, dorCP_forte, 8)	#faz a interseção da entrada (8) com a funcao de pertinencia da dor nas costas/pernas forte


## Base de regras
#Regra 1: dor pelvica fraca; dificuldade baixa; dor costas/pernas fraca => risco baixo
ativa_regra1 = np.fmin(dorCP_fraca, np.fmin(dorP_nivel_fraca, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra1 = np.fmin(ativa_regra1, risco_baixo)		#implicacao 