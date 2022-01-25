# Função de calcular em Lambda
def Calc(valor1, valor2):
	
	# Varíavel para calcuar em lambda
	calculo = lambda a, b: a + b
	
	# Mostrar o resultado
	print("O resultado é:", calculo(valor1, valor2))

# Enquant for verdadeiro
while True:
	
	# Pedir para digitar dois valores inteiros
	print("Olá, digite dois valores para somar.")
	
	# Varíaveis para guardar os valores
	perg = int(input(": "))
	
	perg2 = int(input(": "))
 	
 	# Chamar a função passando os parâmetros das varíaveis
	Calc(perg, perg2)
	
	# Perguntar se deseja continuar
	print("Você deseja continuar? (S/N)")
	
	# Receber a resposta
	perg3 = input(": ")
	
	# Se a resposta for sim
	if perg == "S" or perg == "s":
		
		# Continuar
		continue
	
	# Caso contrário continuar
	else:
		
		# Enecerrar o programa
		break
