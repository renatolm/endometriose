from __future__ import division
import numpy as np
import skfuzzy as fuzz
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def mamdani_defuzz(dism, disp, dor, cans):
	dismenorreia = dism
	dispareunia = disp
	dorNasCostasPernas = dor
	cansaco = cans

	print "entradas: dismenorreia "+str(dismenorreia)+" dispareunia "+str(dispareunia)+" dorcp "+str(dorNasCostasPernas)+" cansaco "+str(cansaco)

	def nivelLeve(entrada):
		if entrada == 0:
			return 1
		elif entrada >= 4:
			return 0
		else:
			return  1 - (entrada/4)

	def nivelModerado(entrada):
		if entrada == 5:
			return 1
		elif entrada < 5 and entrada > 1:
			return (entrada/4) - (1/4)
		elif entrada > 5 and entrada < 9:
			return -(entrada/4) + (9/4)
		else:
			return 0

	def nivelIntenso(entrada):
		if entrada == 10:
			return 1
		elif entrada <=6:
			return 0
		else:
			return (entrada/4) - (6/4)

	#Antecedentes
	dismenorreia_dominio = np.arange(0,11,1)		#nivel de dismenorreia (0 a 10)
	dispareunia_dominio = np.arange(0,11,1)		#nivel de dispareunia (0 a 10)
	dorNasCostasPernas_dominio = np.arange(0,11,1)		#nivel de dor nas costas/pernas (0 a 10)
	cansaco_dominio = np.arange(0,11,1)		#nivel de cansaco (0 a 10)

	#Consequente
	risco = np.arange(0,100,1)		#nivel de risco de endometriose (0 a 10)

	#Funcoes de pertinencia de dismenorreia
	dismenorreia_leve = fuzz.trimf(dismenorreia_dominio, [0,0,5])		#dismenorreia leve
	dismenorreia_moderada = fuzz.trimf(dismenorreia_dominio, [0,5,10])	#dismenorreia moderada
	dismenorreia_intensa = fuzz.trimf(dismenorreia_dominio, [5,10,10])	#dismenorreia intensa

	#Funcoes de pertinencia de dispareunia
	dispareunia_leve = fuzz.trimf(dispareunia_dominio, [0,0,5])			#dispareunia leve
	dispareunia_moderada = fuzz.trimf(dispareunia_dominio, [0,5,10])	#dispareunia moderada
	dispareunia_intensa = fuzz.trimf(dispareunia_dominio, [5,10,10])	#dispareunia intensa

	#Funcoes de pertinencia de Dor Nas Costas e Pernas
	dorCP_leve = fuzz.trimf(dorNasCostasPernas_dominio, [0,0,5])			#dor nas costas e/ou pernas leve
	dorCP_moderada = fuzz.trimf(dorNasCostasPernas_dominio, [0,5,10])		#dor nas costas e/ou pernas moderada
	dorCP_intensa = fuzz.trimf(dorNasCostasPernas_dominio, [5,10,10])		#dor nas costas e/ou pernas intensa

	#Funcoes de pertinencia de cansaco
	cansaco_leve = fuzz.trimf(cansaco_dominio, [0,0,5])				#cansaco leve
	cansaco_moderado = fuzz.trimf(cansaco_dominio, [0,5,10])		#cansaco moderada
	cansaco_intenso = fuzz.trimf(cansaco_dominio, [5,10,10])		#cansaco intensa

	#Funcoes de pertinencia do Risco de Endometriose
	risco_improvavel = fuzz.trimf(risco, [0,0,25])		#risco de endometriose baixo
	risco_poucoprovavel = fuzz.trimf(risco, [8,33,58])		#risco de endometriose medio
	risco_provavel = fuzz.trimf(risco, [42,67,92])		#risco de endometriose alto
	risco_muitoprovavel = fuzz.trimf(risco, [75,100,100])		#risco de endometriose alto


	## Simulando uma entrada
	dismenorreia_nivel_leve = nivelLeve(dismenorreia)		#faz a intersecao da entrada (10) com a funcao de pertinencia da dismenorreia leve
	dismenorreia_nivel_moderada = nivelModerado(dismenorreia)	#faz a intersecao da entrada (10) com a funcao de pertinencia da dismenorreia moderada
	dismenorreia_nivel_intensa = nivelIntenso(dismenorreia)		#faz a intersecao da entrada (10) com a funcao de pertinencia da dismenorreia intensa

	dispareunia_nivel_leve = nivelLeve(dispareunia)		#faz a intersecao da entrada (8) com a funcao de pertinencia da dispareunia leve
	dispareunia_nivel_moderada = nivelModerado(dispareunia)		#faz a intersecao da entrada (8) com a funcao de pertinencia da dispareunia moderada
	dispareunia_nivel_intensa = nivelIntenso(dispareunia)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dispareunia instensa

	dorCP_nivel_leve = nivelLeve(dorNasCostasPernas)		#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas leve
	dorCP_nivel_moderada = nivelModerado(dorNasCostasPernas)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas moderada
	dorCP_nivel_intensa = nivelIntenso(dorNasCostasPernas)	#faz a intersecao da entrada (8) com a funcao de pertinencia da dor nas costas/pernas intensa

	cansaco_nivel_leve = nivelLeve(cansaco)		#faz a intersecao da entrada (9) com a funcao de pertinencia de cansaco leve
	cansaco_nivel_moderado = nivelModerado(cansaco)		#faz a intersecao da entrada (9) com a funcao de pertinencia de cansaco moderado
	cansaco_nivel_intenso = nivelIntenso(cansaco)	#faz a intersecao da entrada com a funcao de pertinencia de cansaco intenso

	regras_ativas = []

	## Base de regras
	#Regra 1: dismenorreia leve; dispareunia leve; dor costas/pernas leve; cansaco leve => risco improvavel
	ativa_regra1 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra1 = np.fmin(ativa_regra1, risco_improvavel)		#implicacao
	if regra1.any() != 0:
		regras_ativas.append(1)

	#Regra 2: dismenorreia leve; dispareunia leve; dor costas/pernas leve; cansaco moderado => risco pouco provavel
	ativa_regra2 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra2 = np.fmin(ativa_regra2, risco_poucoprovavel)		#implicacao
	if regra2.any() != 0:
		regras_ativas.append(2)

	#Regra 3: dismenorreia leve; dispareunia leve; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra3 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra3 = np.fmin(ativa_regra3, risco_provavel)		#implicacao
	if regra3.any() != 0:
		regras_ativas.append(3)

	#Regra 4: dismenorreia leve; dispareunia leve; dor costas/pernas moderado; cansaco leve => risco pouco provavel
	ativa_regra4 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra4 = np.fmin(ativa_regra4, risco_poucoprovavel)		#implicacao
	if regra4.any() != 0:
		regras_ativas.append(4)

	#Regra 5: dismenorreia leve; dispareunia leve; dor costas/pernas moderado; cansaco moderado => risco pouco provavel
	ativa_regra5 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra5 = np.fmin(ativa_regra5, risco_poucoprovavel)		#implicacao
	if regra5.any() != 0:
		regras_ativas.append(5)

	#Regra 6: dismenorreia leve; dispareunia leve; dor costas/pernas moderado; cansaco intenso => risco provavel
	ativa_regra6 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra6 = np.fmin(ativa_regra6, risco_provavel)		#implicacao
	if regra6.any() != 0:
		regras_ativas.append(6)

	#Regra 7: dismenorreia leve; dispareunia leve; dor costas/pernas intenso; cansaco leve => risco provavel
	ativa_regra7 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra7 = np.fmin(ativa_regra7, risco_provavel)		#implicacao
	if regra7.any() != 0:
		regras_ativas.append(7)

	#Regra 8: dismenorreia leve; dispareunia leve; dor costas/pernas intenso; cansaco moderado => risco provavel
	ativa_regra8 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra8 = np.fmin(ativa_regra8, risco_provavel)		#implicacao
	if regra8.any() != 0:
		regras_ativas.append(8)

	#Regra 9: dismenorreia leve; dispareunia leve; dor costas/pernas intenso; cansaco intenso => risco provavel
	ativa_regra9 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra9 = np.fmin(ativa_regra9, risco_provavel)		#implicacao
	if regra9.any() != 0:
		regras_ativas.append(9)

	#Regra 10: dismenorreia leve; dispareunia moderado; dor costas/pernas leve; cansaco leve => risco pouco provavel
	ativa_regra10 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra10 = np.fmin(ativa_regra10, risco_poucoprovavel)		#implicacao
	if regra10.any() != 0:
		regras_ativas.append(10)

	#Regra 11: dismenorreia leve; dispareunia moderado; dor costas/pernas leve; cansaco moderado => risco provavel
	ativa_regra11 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra11 = np.fmin(ativa_regra11, risco_provavel)		#implicacao
	if regra11.any() != 0:
		regras_ativas.append(11)

	#Regra 12: dismenorreia leve; dispareunia moderado; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra12 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra12 = np.fmin(ativa_regra12, risco_provavel)		#implicacao
	if regra12.any() != 0:
		regras_ativas.append(12)

	#Regra 13: dismenorreia leve; dispareunia moderado; dor costas/pernas moderado; cansaco leve => risco pouco provavel
	ativa_regra13 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra13 = np.fmin(ativa_regra13, risco_poucoprovavel)		#implicacao
	if regra13.any() != 0:
		regras_ativas.append(13)

	#Regra 14: dismenorreia leve; dispareunia moderado; dor costas/pernas moderado; cansaco moderado => risco provavel
	ativa_regra14 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra14 = np.fmin(ativa_regra14, risco_provavel)		#implicacao
	if regra14.any() != 0:
		regras_ativas.append(14)

	#Regra 15: dismenorreia leve; dispareunia moderado; dor costas/pernas moderado; cansaco intenso => risco pouco provavel
	ativa_regra15 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra15 = np.fmin(ativa_regra15, risco_poucoprovavel)		#implicacao
	if regra15.any() != 0:
		regras_ativas.append(15)

	#Regra 16: dismenorreia leve; dispareunia moderado; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra16 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra16 = np.fmin(ativa_regra16, risco_poucoprovavel)		#implicacao
	if regra16.any() != 0:
		regras_ativas.append(16)

	#Regra 17: dismenorreia leve; dispareunia moderado; dor costas/pernas intenso; cansaco moderado => risco provavel
	ativa_regra17 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra17 = np.fmin(ativa_regra17, risco_provavel)		#implicacao
	if regra17.any() != 0:
		regras_ativas.append(17)

	#Regra 18: dismenorreia leve; dispareunia moderado; dor costas/pernas intenso; cansaco intenso => risco provavel
	ativa_regra18 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra18 = np.fmin(ativa_regra18, risco_provavel)		#implicacao
	if regra18.any() != 0:
		regras_ativas.append(18)

	#Regra 19: dismenorreia leve; dispareunia intenso; dor costas/pernas leve; cansaco leve => risco improvavel
	ativa_regra19 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra19 = np.fmin(ativa_regra19, risco_improvavel)		#implicacao
	if regra19.any() != 0:
		regras_ativas.append(19)

	#Regra 20: dismenorreia leve; dispareunia intenso; dor costas/pernas leve; cansaco moderado => risco pouco provavel
	ativa_regra20 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra20 = np.fmin(ativa_regra20, risco_poucoprovavel)		#implicacao
	if regra20.any() != 0:
		regras_ativas.append(20)

	#Regra 21: dismenorreia leve; dispareunia intenso; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra21 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra21 = np.fmin(ativa_regra21, risco_provavel)		#implicacao
	if regra21.any() != 0:
		regras_ativas.append(21)

	#Regra 22: dismenorreia leve; dispareunia intenso; dor costas/pernas moderado; cansaco leve => risco pouco provavel
	ativa_regra22 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra22 = np.fmin(ativa_regra22, risco_poucoprovavel)		#implicacao
	if regra22.any() != 0:
		regras_ativas.append(22)

	#Regra 23: dismenorreia leve; dispareunia intenso; dor costas/pernas moderado; cansaco moderado => risco provavel
	ativa_regra23 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra23 = np.fmin(ativa_regra23, risco_provavel)		#implicacao
	if regra23.any() != 0:
		regras_ativas.append(23)

	#Regra 24: dismenorreia leve; dispareunia intenso; dor costas/pernas moderado; cansaco intenso => risco provavel
	ativa_regra24 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra24 = np.fmin(ativa_regra24, risco_provavel)		#implicacao
	if regra24.any() != 0:
		regras_ativas.append(24)

	#Regra 25: dismenorreia leve; dispareunia intenso; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra25 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra25 = np.fmin(ativa_regra25, risco_poucoprovavel)		#implicacao
	if regra25.any() != 0:
		regras_ativas.append(25)

	#Regra 26: dismenorreia leve; dispareunia intenso; dor costas/pernas intenso; cansaco moderado => risco provavel
	ativa_regra26 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra26 = np.fmin(ativa_regra26, risco_provavel)		#implicacao
	if regra26.any() != 0:
		regras_ativas.append(26)

	#Regra 27: dismenorreia leve; dispareunia intenso; dor costas/pernas intenso; cansaco intenso => risco provavel
	ativa_regra27 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_leve, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra27 = np.fmin(ativa_regra27, risco_provavel)		#implicacao
	if regra27.any() != 0:
		regras_ativas.append(27)

	#Regra 28: dismenorreia moderado; dispareunia leve; dor costas/pernas leve; cansaco leve => risco pouco provavel
	ativa_regra28 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra28 = np.fmin(ativa_regra28, risco_poucoprovavel)		#implicacao
	if regra28.any() != 0:
		regras_ativas.append(28)

	#Regra 29: dismenorreia moderado; dispareunia leve; dor costas/pernas leve; cansaco moderado => risco pouco provavel
	ativa_regra29 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra29 = np.fmin(ativa_regra29, risco_poucoprovavel)		#implicacao
	if regra29.any() != 0:
		regras_ativas.append(29)

	#Regra 30: dismenorreia moderado; dispareunia leve; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra30 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra30 = np.fmin(ativa_regra30, risco_provavel)		#implicacao
	if regra30.any() != 0:
		regras_ativas.append(30)

	#Regra 31: dismenorreia moderado; dispareunia leve; dor costas/pernas moderado; cansaco leve => risco pouco provavel
	ativa_regra31 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra31 = np.fmin(ativa_regra31, risco_poucoprovavel)		#implicacao
	if regra31.any() != 0:
		regras_ativas.append(31)

	#Regra 32: dismenorreia moderado; dispareunia leve; dor costas/pernas moderado; cansaco moderado => risco provavel
	ativa_regra32 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra32 = np.fmin(ativa_regra32, risco_provavel)		#implicacao
	if regra32.any() != 0:
		regras_ativas.append(32)

	#Regra 33: dismenorreia moderado; dispareunia leve; dor costas/pernas moderado; cansaco intenso => risco provavel
	ativa_regra33 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra33 = np.fmin(ativa_regra33, risco_provavel)		#implicacao
	if regra33.any() != 0:
		regras_ativas.append(33)

	#Regra 34: dismenorreia moderado; dispareunia leve; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra34 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra34 = np.fmin(ativa_regra34, risco_poucoprovavel)		#implicacao
	if regra34.any() != 0:
		regras_ativas.append(34)

	#Regra 35: dismenorreia moderado; dispareunia leve; dor costas/pernas intenso; cansaco moderado => risco provavel
	ativa_regra35 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra35 = np.fmin(ativa_regra35, risco_provavel)		#implicacao
	if regra35.any() != 0:
		regras_ativas.append(35)

	#Regra 36: dismenorreia moderado; dispareunia leve; dor costas/pernas intenso; cansaco intenso => risco provavel
	ativa_regra36 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra36 = np.fmin(ativa_regra36, risco_provavel)		#implicacao
	if regra36.any() != 0:
		regras_ativas.append(36)

	#Regra 37: dismenorreia moderado; dispareunia moderado; dor costas/pernas leve; cansaco leve => risco pouco provavel
	ativa_regra37 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra37 = np.fmin(ativa_regra37, risco_poucoprovavel)		#implicacao
	if regra37.any() != 0:
		regras_ativas.append(37)

	#Regra 38: dismenorreia moderado; dispareunia moderado; dor costas/pernas leve; cansaco moderado => risco pouco provavel
	ativa_regra38 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra38 = np.fmin(ativa_regra38, risco_poucoprovavel)		#implicacao
	if regra38.any() != 0:
		regras_ativas.append(38)

	#Regra 39: dismenorreia moderado; dispareunia moderado; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra39 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra39 = np.fmin(ativa_regra39, risco_provavel)		#implicacao
	if regra39.any() != 0:
		regras_ativas.append(39)

	#Regra 40: dismenorreia moderado; dispareunia moderado; dor costas/pernas moderado; cansaco leve => risco provavel
	ativa_regra40 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra40 = np.fmin(ativa_regra40, risco_provavel)		#implicacao
	if regra40.any() != 0:
		regras_ativas.append(40)

	#Regra 41: dismenorreia moderado; dispareunia moderado; dor costas/pernas moderado; cansaco moderado => risco pouco provavel
	ativa_regra41 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra41 = np.fmin(ativa_regra41, risco_poucoprovavel)		#implicacao
	if regra41.any() != 0:
		regras_ativas.append(41)

	#Regra 42: dismenorreia moderado; dispareunia moderado; dor costas/pernas moderado; cansaco intenso => risco muito provavel
	ativa_regra42 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra42 = np.fmin(ativa_regra42, risco_muitoprovavel)		#implicacao
	if regra42.any() != 0:
		regras_ativas.append(42)

	#Regra 43: dismenorreia moderado; dispareunia moderado; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra43 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra43 = np.fmin(ativa_regra43, risco_poucoprovavel)		#implicacao
	if regra43.any() != 0:
		regras_ativas.append(43)

	#Regra 44: dismenorreia moderado; dispareunia moderado; dor costas/pernas intenso; cansaco moderado => risco muito provavel
	ativa_regra44 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra44 = np.fmin(ativa_regra44, risco_muitoprovavel)		#implicacao
	if regra44.any() != 0:
		regras_ativas.append(44)

	#Regra 45: dismenorreia moderado; dispareunia moderado; dor costas/pernas intenso; cansaco intenso => risco muito provavel
	ativa_regra45 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra45 = np.fmin(ativa_regra45, risco_muitoprovavel)		#implicacao
	if regra45.any() != 0:
		regras_ativas.append(45)

	#Regra 46: dismenorreia moderado; dispareunia intenso; dor costas/pernas leve; cansaco leve => risco provavel
	ativa_regra46 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra46 = np.fmin(ativa_regra46, risco_provavel)		#implicacao
	if regra46.any() != 0:
		regras_ativas.append(46)

	#Regra 47: dismenorreia moderado; dispareunia intenso; dor costas/pernas leve; cansaco moderado => risco provavel
	ativa_regra47 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra47 = np.fmin(ativa_regra47, risco_provavel)		#implicacao
	if regra47.any() != 0:
		regras_ativas.append(47)

	#Regra 48: dismenorreia moderado; dispareunia intenso; dor costas/pernas leve; cansaco intenso => risco pouco provavel
	ativa_regra48 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra48 = np.fmin(ativa_regra48, risco_poucoprovavel)		#implicacao
	if regra48.any() != 0:
		regras_ativas.append(48)

	#Regra 49: dismenorreia moderado; dispareunia intenso; dor costas/pernas moderado; cansaco leve => risco provavel
	ativa_regra49 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra49 = np.fmin(ativa_regra49, risco_provavel)		#implicacao
	if regra49.any() != 0:
		regras_ativas.append(49)

	#Regra 50: dismenorreia moderado; dispareunia intenso; dor costas/pernas moderado; cansaco moderado => risco provavel
	ativa_regra50 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra50 = np.fmin(ativa_regra50, risco_provavel)		#implicacao
	if regra50.any() != 0:
		regras_ativas.append(50)

	#Regra 51: dismenorreia moderado; dispareunia intenso; dor costas/pernas moderado; cansaco intenso => risco muito provavel
	ativa_regra51 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra51 = np.fmin(ativa_regra51, risco_muitoprovavel)		#implicacao
	if regra51.any() != 0:
		regras_ativas.append(51)

	#Regra 52: dismenorreia moderado; dispareunia intenso; dor costas/pernas intenso; cansaco leve => risco muito provavel
	ativa_regra52 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra52 = np.fmin(ativa_regra52, risco_muitoprovavel)		#implicacao
	if regra52.any() != 0:
		regras_ativas.append(52)

	#Regra 53: dismenorreia moderado; dispareunia intenso; dor costas/pernas intenso; cansaco moderado => risco muito provavel
	ativa_regra53 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra53 = np.fmin(ativa_regra53, risco_muitoprovavel)		#implicacao
	if regra53.any() != 0:
		regras_ativas.append(53)

	#Regra 54: dismenorreia moderado; dispareunia intenso; dor costas/pernas intenso; cansaco intenso => risco muito provavel
	ativa_regra54 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_moderada, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra54 = np.fmin(ativa_regra54, risco_muitoprovavel)		#implicacao
	if regra54.any() != 0:
		regras_ativas.append(54)

	#Regra 55: dismenorreia intenso; dispareunia leve; dor costas/pernas leve; cansaco leve => risco provavel
	ativa_regra55 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra55 = np.fmin(ativa_regra55, risco_provavel)		#implicacao
	if regra55.any() != 0:
		regras_ativas.append(55)

	#Regra 56: dismenorreia intenso; dispareunia leve; dor costas/pernas leve; cansaco moderado => risco provavel
	ativa_regra56 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra56 = np.fmin(ativa_regra56, risco_provavel)		#implicacao
	if regra56.any() != 0:
		regras_ativas.append(56)

	#Regra 57: dismenorreia intenso; dispareunia leve; dor costas/pernas leve; cansaco intenso => risco muito provavel
	ativa_regra57 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra57 = np.fmin(ativa_regra57, risco_muitoprovavel)		#implicacao
	if regra57.any() != 0:
		regras_ativas.append(57)

	#Regra 58: dismenorreia intenso; dispareunia leve; dor costas/pernas moderado; cansaco leve => risco provavel
	ativa_regra58 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra58 = np.fmin(ativa_regra58, risco_provavel)		#implicacao
	if regra58.any() != 0:
		regras_ativas.append(58)

	#Regra 59: dismenorreia intenso; dispareunia leve; dor costas/pernas moderado; cansaco moderado => risco muito provavel
	ativa_regra59 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra59 = np.fmin(ativa_regra59, risco_muitoprovavel)		#implicacao
	if regra59.any() != 0:
		regras_ativas.append(59)

	#Regra 60: dismenorreia intenso; dispareunia leve; dor costas/pernas moderado; cansaco intenso => risco muito provavel
	ativa_regra60 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra60 = np.fmin(ativa_regra60, risco_muitoprovavel)		#implicacao
	if regra60.any() != 0:
		regras_ativas.append(60)

	#Regra 61: dismenorreia intenso; dispareunia leve; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra61 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra61 = np.fmin(ativa_regra61, risco_poucoprovavel)		#implicacao
	if regra61.any() != 0:
		regras_ativas.append(61)

	#Regra 62: dismenorreia intenso; dispareunia leve; dor costas/pernas intenso; cansaco moderado => risco muito provavel
	ativa_regra62 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra62 = np.fmin(ativa_regra62, risco_muitoprovavel)		#implicacao
	if regra62.any() != 0:
		regras_ativas.append(62)

	#Regra 63: dismenorreia intenso; dispareunia leve; dor costas/pernas intenso; cansaco intenso => risco muito provavel
	ativa_regra63 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_leve)))		#composicao usando operador AND (minimo)
	regra63 = np.fmin(ativa_regra63, risco_muitoprovavel)		#implicacao
	if regra63.any() != 0:
		regras_ativas.append(63)

	#Regra 64: dismenorreia intenso; dispareunia moderado; dor costas/pernas leve; cansaco leve => risco provavel
	ativa_regra64 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra64 = np.fmin(ativa_regra64, risco_provavel)		#implicacao
	if regra64.any() != 0:
		regras_ativas.append(64)

	#Regra 65: dismenorreia intenso; dispareunia moderado; dor costas/pernas leve; cansaco moderado => risco provavel
	ativa_regra65 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra65 = np.fmin(ativa_regra65, risco_provavel)		#implicacao
	if regra65.any() != 0:
		regras_ativas.append(65)

	#Regra 66: dismenorreia intenso; dispareunia moderado; dor costas/pernas leve; cansaco intenso => risco provavel
	ativa_regra66 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra66 = np.fmin(ativa_regra66, risco_provavel)		#implicacao
	if regra66.any() != 0:
		regras_ativas.append(66)

	#Regra 67: dismenorreia intenso; dispareunia moderado; dor costas/pernas moderado; cansaco leve => risco provavel
	ativa_regra67 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra67 = np.fmin(ativa_regra67, risco_provavel)		#implicacao
	if regra67.any() != 0:
		regras_ativas.append(67)

	#Regra 68: dismenorreia intenso; dispareunia moderado; dor costas/pernas moderado; cansaco moderado => risco muito provavel
	ativa_regra68 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra68 = np.fmin(ativa_regra68, risco_muitoprovavel)		#implicacao
	if regra68.any() != 0:
		regras_ativas.append(68)

	#Regra 69: dismenorreia intenso; dispareunia moderado; dor costas/pernas moderado; cansaco intenso => risco muito provavel
	ativa_regra69 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra69 = np.fmin(ativa_regra69, risco_muitoprovavel)		#implicacao
	if regra69.any() != 0:
		regras_ativas.append(69)

	#Regra 70: dismenorreia intenso; dispareunia moderado; dor costas/pernas intenso; cansaco leve => risco provavel
	ativa_regra70 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra70 = np.fmin(ativa_regra70, risco_provavel)		#implicacao
	if regra70.any() != 0:
		regras_ativas.append(70)

	#Regra 71: dismenorreia intenso; dispareunia moderado; dor costas/pernas intenso; cansaco moderado => risco muito provavel
	ativa_regra71 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra71 = np.fmin(ativa_regra71, risco_muitoprovavel)		#implicacao
	if regra71.any() != 0:
		regras_ativas.append(71)

	#Regra 72: dismenorreia intenso; dispareunia moderado; dor costas/pernas intenso; cansaco intenso => risco muito provavel
	ativa_regra72 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_moderada)))		#composicao usando operador AND (minimo)
	regra72 = np.fmin(ativa_regra72, risco_muitoprovavel)		#implicacao
	if regra72.any() != 0:
		regras_ativas.append(72)

	#Regra 73: dismenorreia intenso; dispareunia intenso; dor costas/pernas leve; cansaco leve => risco pouco provavel
	ativa_regra73 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra73 = np.fmin(ativa_regra73, risco_poucoprovavel)		#implicacao
	if regra73.any() != 0:
		regras_ativas.append(73)

	#Regra 74: dismenorreia intenso; dispareunia intenso; dor costas/pernas leve; cansaco moderado => risco provavel
	ativa_regra74 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra74 = np.fmin(ativa_regra74, risco_provavel)		#implicacao
	if regra74.any() != 0:
		regras_ativas.append(74)

	#Regra 75: dismenorreia intenso; dispareunia intenso; dor costas/pernas leve; cansaco intenso => risco muito provavel
	ativa_regra75 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_leve, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra75 = np.fmin(ativa_regra75, risco_muitoprovavel)		#implicacao
	if regra75.any() != 0:
		regras_ativas.append(75)

	#Regra 76: dismenorreia intenso; dispareunia intenso; dor costas/pernas moderado; cansaco leve => risco provavel
	ativa_regra76 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra76 = np.fmin(ativa_regra76, risco_provavel)		#implicacao
	if regra76.any() != 0:
		regras_ativas.append(76)

	#Regra 77: dismenorreia intenso; dispareunia intenso; dor costas/pernas moderado; cansaco moderado => risco provavel
	ativa_regra77 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra77 = np.fmin(ativa_regra77, risco_provavel)		#implicacao
	if regra77.any() != 0:
		regras_ativas.append(77)

	#Regra 78: dismenorreia intenso; dispareunia intenso; dor costas/pernas moderado; cansaco intenso => risco muito provavel
	ativa_regra78 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_moderada, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra78 = np.fmin(ativa_regra78, risco_muitoprovavel)		#implicacao
	if regra78.any() != 0:
		regras_ativas.append(78)

	#Regra 79: dismenorreia intenso; dispareunia intenso; dor costas/pernas intenso; cansaco leve => risco pouco provavel
	ativa_regra79 = np.fmin(cansaco_nivel_leve, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra79 = np.fmin(ativa_regra79, risco_poucoprovavel)		#implicacao
	if regra79.any() != 0:
		regras_ativas.append(79)

	#Regra 80: dismenorreia intenso; dispareunia intenso; dor costas/pernas intenso; cansaco moderado => risco muito provavel
	ativa_regra80 = np.fmin(cansaco_nivel_moderado, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra80 = np.fmin(ativa_regra80, risco_muitoprovavel)		#implicacao
	if regra80.any() != 0:
		regras_ativas.append(80)

	#Regra 81: dismenorreia intenso; dispareunia intenso; dor costas/pernas intenso; cansaco intenso => risco muito provavel
	ativa_regra81 = np.fmin(cansaco_nivel_intenso, np.fmin(dorCP_nivel_intensa, np.fmin(dismenorreia_nivel_intensa, dispareunia_nivel_intensa)))		#composicao usando operador AND (minimo)
	regra81 = np.fmin(ativa_regra81, risco_muitoprovavel)		#implicacao
	if regra81.any() != 0:
		regras_ativas.append(81)

	print "regras ativas: "+str(regras_ativas)

	## Agregacao das regras
	agregacao = np.fmax(regra81,
		np.fmax(regra80,
		np.fmax(regra79,
		np.fmax(regra78,
		np.fmax(regra77,
		np.fmax(regra76,
		np.fmax(regra75,
		np.fmax(regra74,
		np.fmax(regra73,
		np.fmax(regra72,
		np.fmax(regra71,
		np.fmax(regra70,
		np.fmax(regra69,
		np.fmax(regra68,
		np.fmax(regra67,
		np.fmax(regra66,
		np.fmax(regra65,
		np.fmax(regra64,
		np.fmax(regra63,
		np.fmax(regra62,
		np.fmax(regra61,
		np.fmax(regra60,
		np.fmax(regra59,
		np.fmax(regra58,
		np.fmax(regra57,
		np.fmax(regra56,
		np.fmax(regra55,
		np.fmax(regra54,
		np.fmax(regra53,
		np.fmax(regra52,
		np.fmax(regra51,
		np.fmax(regra50,
		np.fmax(regra49,
		np.fmax(regra48,
		np.fmax(regra47,
		np.fmax(regra46,
		np.fmax(regra45,
		np.fmax(regra44,
		np.fmax(regra43,
		np.fmax(regra42,
		np.fmax(regra41,
		np.fmax(regra40,
		np.fmax(regra39,
		np.fmax(regra38,
		np.fmax(regra37,
		np.fmax(regra36,
		np.fmax(regra35,
		np.fmax(regra34,
		np.fmax(regra33,
		np.fmax(regra32,
		np.fmax(regra31,
		np.fmax(regra30,
		np.fmax(regra29,
		np.fmax(regra28,
		np.fmax(regra27,
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
		np.fmax(regra1, regra2))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))	#agregacao das regras

	risco0 = np.zeros_like(risco)	#variavel auxiliar para montar o grafico


	## Calculo do resultado defuzzificado
	risco_def = fuzz.defuzz(risco, agregacao, 'centroid')		#defuzzificacao pelo metodo centroide
	risco_ativacao = fuzz.interp_membership(risco, agregacao, risco_def)	#intersecao do risco defuzzificado com a funcao de pertinencia

	## Grafico da funcao de pertinencia resultante
	fig, ax0 = plt.subplots(figsize=(9.27,3.23))

	ax0.plot(risco, risco_improvavel, 'b', linewidth=0.5, label='I', linestyle='--')
	ax0.plot(risco, risco_poucoprovavel, 'g', linewidth=0.5, label='PP', linestyle='--')
	ax0.plot(risco, risco_provavel, 'y', linewidth=0.5, label='P', linestyle='--')
	ax0.plot(risco, risco_muitoprovavel, 'r', linewidth=1.5, label='MP', linestyle='--')
	ax0.legend(loc='upper center',bbox_to_anchor=(0.5, 1.05), ncol=4, fancybox=True, shadow=True)
	ax0.fill_between(risco, risco0, agregacao, facecolor='Orange', alpha=0.7)
	ax0.plot([risco_def, risco_def], [0, risco_ativacao], 'k', linewidth=1.5, alpha=0.9)
	plt.xticks(np.append(plt.xticks()[0],risco_def))
	plt.xlabel('risco (%)')
	ax0.set_title("Agregacao das regras e resultado defuzzificado")

	plt.tight_layout()
	#plt.show()
	plt.savefig('/home/endometriose/mysite/static/resultado.png')
	return risco_def

mamdani_defuzz(0,0,0,0)