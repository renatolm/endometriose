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
dorP_nivel_fraca = fuzz.interp_membership(dorPelvica, dorP_fraca, 9)	#faz a intersecao da entrada (9) com a funcao de pertinencia da dor pelvica fraca
dorP_nivel_media = fuzz.interp_membership(dorPelvica, dorP_media, 9)	#faz a intersecao da entrada (9) com a funcao de pertinencia da dor pelvica media
dorP_nivel_forte = fuzz.interp_membership(dorPelvica, dorP_forte, 9)	#faz a intersecao da entrada (9) com a funcao de pertinencia da dor pelvica forte

#Nivel de dificuldade para engravidar 7
dificuldade_nivel_baixa = fuzz.interp_membership(dificuldadeEngravidar, dific_baixa, 7)	#faz a intersecao da entrada (7) com a funcao de pertinencia da dificuldade baixa
dificuldade_nivel_media = fuzz.interp_membership(dificuldadeEngravidar, dific_media, 7)	#faz a intersecao da entrada (7) com a funcao de pertinencia da dificuldade media
dificuldade_nivel_alta = fuzz.interp_membership(dificuldadeEngravidar, dific_alta, 7)	#faz a intersecao da entrada (7) com a funcao de pertinencia da dificuldade alta

#Nivel de dor nas costas/pernas 8
dorCP_nivel_fraca = fuzz.interp_membership(dorNasCostasPernas, dorCP_fraca, 8)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas fraca
dorCP_nivel_media = fuzz.interp_membership(dorNasCostasPernas, dorCP_media, 8)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas media
dorCP_nivel_forte = fuzz.interp_membership(dorNasCostasPernas, dorCP_forte, 8)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas forte


## Base de regras
#Regra 1: dor pelvica fraca; dificuldade baixa; dor costas/pernas fraca => risco baixo
ativa_regra1 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_fraca, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra1 = np.fmin(ativa_regra1, risco_baixo)		#implicacao 

#Regra 2: dor pelvica media; dificuldade baixa; dor costas/pernas fraca => risco baixo
ativa_regra2 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_media, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra2 = np.fmin(ativa_regra2, risco_baixo)		#implicacao 

#Regra 3: dor pelvica forte; dificuldade baixa; dor costas/pernas fraca => risco medio
ativa_regra3 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_forte, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra3 = np.fmin(ativa_regra3, risco_medio)		#implicacao 

#Regra 4: dor pelvica fraca; dificuldade media; dor costas/pernas fraca => risco baixo
ativa_regra4 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_fraca, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra4 = np.fmin(ativa_regra4, risco_baixo)		#implicacao 

#Regra 5: dor pelvica media; dificuldade media; dor costas/pernas fraca => risco medio
ativa_regra5 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_media, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra5 = np.fmin(ativa_regra5, risco_medio)		#implicacao 

#Regra 6: dor pelvica forte; dificuldade media; dor costas/pernas fraca => risco medio
ativa_regra6 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_forte, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra6 = np.fmin(ativa_regra6, risco_medio)		#implicacao 

#Regra 7: dor pelvica fraca; dificuldade alta; dor costas/pernas fraca => risco medio
ativa_regra7 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_fraca, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra7 = np.fmin(ativa_regra7, risco_medio)		#implicacao 

#Regra 8: dor pelvica media; dificuldade alta; dor costas/pernas fraca => risco medio
ativa_regra8 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_media, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra8 = np.fmin(ativa_regra8, risco_medio)		#implicacao 

#Regra 9: dor pelvica forte; dificuldade alta; dor costas/pernas fraca => risco alto
ativa_regra9 = np.fmin(dorCP_nivel_fraca, np.fmin(dorP_nivel_forte, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra9 = np.fmin(ativa_regra9, risco_alto)		#implicacao 

#Regra 10: dor pelvica fraca; dificuldade baixa; dor costas/pernas media => risco baixo
ativa_regra10 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_fraca, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra10 = np.fmin(ativa_regra10, risco_baixo)		#implicacao 

#Regra 11: dor pelvica media; dificuldade baixa; dor costas/pernas media => risco medio
ativa_regra11 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_media, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra11 = np.fmin(ativa_regra11, risco_medio)		#implicacao 

#Regra 12: dor pelvica forte; dificuldade baixa; dor costas/pernas media => risco medio
ativa_regra12 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_forte, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra12 = np.fmin(ativa_regra12, risco_medio)		#implicacao 

#Regra 13: dor pelvica fraca; dificuldade media; dor costas/pernas media => risco medio
ativa_regra13 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_fraca, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra13 = np.fmin(ativa_regra13, risco_medio)		#implicacao 

#Regra 14: dor pelvica media; dificuldade media; dor costas/pernas media => risco alto
ativa_regra14 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_media, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra14 = np.fmin(ativa_regra14, risco_alto)		#implicacao 

#Regra 15: dor pelvica forte; dificuldade media; dor costas/pernas media => risco alto
ativa_regra15 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_forte, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra15 = np.fmin(ativa_regra15, risco_alto)		#implicacao 

#Regra 16: dor pelvica fraca; dificuldade alta; dor costas/pernas media => risco medio
ativa_regra16 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_fraca, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra16 = np.fmin(ativa_regra16, risco_medio)		#implicacao 

#Regra 17: dor pelvica media; dificuldade alta; dor costas/pernas media => risco alto
ativa_regra17 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_media, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra17 = np.fmin(ativa_regra17, risco_alto)		#implicacao 

#Regra 18: dor pelvica forte; dificuldade alta; dor costas/pernas media => risco alto
ativa_regra18 = np.fmin(dorCP_nivel_media, np.fmin(dorP_nivel_forte, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra18 = np.fmin(ativa_regra18, risco_alto)		#implicacao 

#Regra 19: dor pelvica fraca; dificuldade baixa; dor costas/pernas forte => risco baixo
ativa_regra19 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_fraca, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra19 = np.fmin(ativa_regra19, risco_baixo)		#implicacao 

#Regra 20: dor pelvica media; dificuldade baixa; dor costas/pernas forte => risco medio
ativa_regra20 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_media, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra20 = np.fmin(ativa_regra20, risco_medio)		#implicacao 

#Regra 21: dor pelvica forte; dificuldade baixa; dor costas/pernas forte => risco medio
ativa_regra21 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_forte, dificuldade_nivel_baixa))		#composicao usando operador AND (minimo)
regra21 = np.fmin(ativa_regra21, risco_medio)		#implicacao 

#Regra 22: dor pelvica fraca; dificuldade media; dor costas/pernas forte => risco medio
ativa_regra22 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_fraca, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra22 = np.fmin(ativa_regra22, risco_medio)		#implicacao 

#Regra 23: dor pelvica media; dificuldade media; dor costas/pernas forte => risco medio
ativa_regra23 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_media, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra23 = np.fmin(ativa_regra23, risco_medio)		#implicacao 

#Regra 24: dor pelvica forte; dificuldade media; dor costas/pernas forte => risco alto
ativa_regra24 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_forte, dificuldade_nivel_media))		#composicao usando operador AND (minimo)
regra24 = np.fmin(ativa_regra24, risco_alto)		#implicacao 

#Regra 25: dor pelvica fraca; dificuldade alta; dor costas/pernas forte => risco medio
ativa_regra25 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_fraca, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra25 = np.fmin(ativa_regra25, risco_medio)		#implicacao 

#Regra 26: dor pelvica media; dificuldade alta; dor costas/pernas forte => risco alto
ativa_regra26 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_media, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra26 = np.fmin(ativa_regra26, risco_alto)		#implicacao 

#Regra 27: dor pelvica forte; dificuldade alta; dor costas/pernas forte => risco alto
ativa_regra27 = np.fmin(dorCP_nivel_forte, np.fmin(dorP_nivel_forte, dificuldade_nivel_alta))		#composicao usando operador AND (minimo)
regra27 = np.fmin(ativa_regra27, risco_alto)		#implicacao 


## Agregacao das regras
agregacao = np.fmax(regra27, 
	np.fmax(regra26, 
	np.fmax(regra25, 
	np.fmax(regra24, 
	np.fmax(regra23, 
	np.fmax(regra22, 
	np.fmax(regra21, 
	np.fmax(regra20, 
	np.fmax(regra19, 
	np.fmax(regra18, 
	np.fmax(regra17, 
	np.fmax(regra16, 
	np.fmax(regra15, 
	np.fmax(regra14, 
	np.fmax(regra13, 
	np.fmax(regra12, 
	np.fmax(regra11,
	np.fmax(regra10,
	np.fmax(regra9, 
	np.fmax(regra8, 
	np.fmax(regra7, 
	np.fmax(regra6, 
	np.fmax(regra5, 
	np.fmax(regra4,
	np.fmax(regra3, 
	np.fmax(regra1, regra2))))))))))))))))))))))))))	#agregacao das regras

risco0 = np.zeros_like(risco)	#variavel auxiliar para montar o grafico


## Calculo do resultado defuzzificado
risco_def = fuzz.defuzz(risco, agregacao, 'centroid')		#defuzzificacao pelo metodo centroide
risco_ativacao = fuzz.interp_membership(risco, agregacao, risco_def)	#intersecao do risco defuzzificado com a funcao de pertinencia

## Grafico da funcao de pertinencia resultante
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(risco, risco_baixo, 'b', linewidth=0.5, linestyle='--')
ax0.plot(risco, risco_medio, 'g', linewidth=0.5, linestyle='--')
ax0.plot(risco, risco_alto, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(risco, risco0, agregacao, facecolor='Orange', alpha=0.7)
ax0.plot([risco_def, risco_def], [0, risco_ativacao], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title("Agregacao das regras e resultado defuzzificado")

plt.tight_layout()
plt.show()