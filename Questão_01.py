#!/usr/bin/env python3

'''
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
'''

def asterisk():
	number = eval(input("Digite um número: ")) #Recebendo um número inteiro na variável number
	aux = 1 #Variável auxiliar 
	for i in range(number-1, -1, -1): #laço que inicia do tamanho da variável number -1 e vai decrescendo em 1 ponto
		print(" "*i,"*"*aux) #Imprime na tela a quantidade de espaço (valor máximo do laço) e a quantidade de * que vai aumentando a cada interação com a váriavel auxiliar
		aux+=1 #Incremento da variável auxíliar em 1 ponto a cada interação
#Iniciando o programa
asterisk()