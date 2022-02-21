#!/usr/bin/env python3
import re #importando a biblioteca de expressão regular

def check_passw(password):
	while True:
		#Usando expressão regular para checar os requisitos mínimos da senha
		digit_error = re.search(r"\d", password) is None
		lowercase_error = re.search(r"[a-z]", password) is None
		uppercase_error = re.search(r"[A-Z]", password) is None
		specialCharacter_error = re.search(r"[!@#$%^&*()-+]", password) is None
		space_error = re.search(r"\s", password) is not None
		
		#Caso algum erro seja encontrado retorna a respectiva ajuda
		if len(password)<6: print(f"Você digitou {len(password)} caracteres e a senha precisa ser no mímino 6 caracteres")
		if digit_error: print("Sua senha deve conter no mínimo 1 digito: ")
		if lowercase_error: print("Sua senha deve conter no mínimo 1 letra em minúsculo: ")
		if uppercase_error: print("Sua senha deve conter no mínimo 1 letra em maiúsculo: ")
		if specialCharacter_error: print("Sua senha deve conter no mínimo 1 caractere especial.\nOs caracteres especiais são: !@#$%^&*()-+\n")
		elif space_error: print("Sua senha não deve ter espaços: ")
		
		else: print("Valid password!"); break #se a seja estiver com os requisitos mínimos acaba o programa
		
		'''
		Verifica se o usuário quer continuar com a senha anterior se se prefere digitar uma nova
		'''
		cont = eval(input("Digite 1 para continuar escrevendo a senha anterior\nOu outro número para escrever uma nova senha"))
		if cont == 1:
			newpassword = input(f"Digite mais {6-(len(password))} caracteres: ")
			password = password+newpassword
			print(f"Sua senha é: {password}")
		else:
			password = input("Digite uma senha válida: ")
			print(f"Sua senha é: {password}")

#Iniciando o programa
password = input("Digite sua senha: ")
check_passw(password)