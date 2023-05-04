################### Atividade 1 - Transcrição portugol para código ###################
print('################# Atividade 1 - Transcrição portugol para código #################')

indice = 13
soma = 0
k = 0

while(k<indice):
    k += 1
    soma += k

print(f'Resultado do while: {soma}')
print('')

################### Atividade 2 - Fibonacci ###################
print('################### Atividade 2 - Fibonacci ###################')

numero = int(input('Informe um número: '))
print('')

fibonacci = [0, 1]

tamanhoArray = len(fibonacci)
ultimoEleArray = fibonacci[(tamanhoArray-1)]
penultimoEleArray = fibonacci[(tamanhoArray-2)]

while ultimoEleArray < numero:
    aux = ultimoEleArray + penultimoEleArray
    fibonacci.append(aux)
    penultimoEleArray = ultimoEleArray
    ultimoEleArray = aux
    print(f'Sequência de Fibonacci: {fibonacci}')

print('')
if(numero in fibonacci):
    print(f'O número informado "{numero}" existe na sequência de Fibonacci')
    print('')
else:
    print(f'O número informado "{numero}" não existe na sequência de Fibonacci!')
    print('')
    
################### Atividade 3 - E-mail não recebido ###################
print('################### Atividade 3 - E-mail não recebido ###################')
print('')

################### Atividade 4 - Faturamentos ###################
print('################### Atividade 4 - Faturamentos ###################')

fatEstados = [
    {'Estado': 'SP', 'Faturamento': 67836.43},
    {'Estado': 'RJ', 'Faturamento': 36678.66},
    {'Estado': 'MG', 'Faturamento': 29229.88},
    {'Estado': 'ES', 'Faturamento': 27165.48},
    {'Estado': 'Outros', 'Faturamento': 19849.53}
]

totalFaturamento = 0
percentualEstado = 0

for fat in fatEstados:
    totalFaturamento += round(fat['Faturamento'], 2)

print(f'Faturamento total: {totalFaturamento}')
for fat in fatEstados:
    aux = round(((100 * fat['Faturamento'])/totalFaturamento),2)
    print(f'Percentual de faturamento de {fat["Estado"]}: {aux}%')
    
print('')

################### Atividade 5 - Inversão de string ###################
print('################### Atividade 5 - Inversão de string ###################')

entrada = input('Escreva algo: ')
entrada = entrada.lower()
print('')
tamanhoString = len(entrada)
tamanhoString -=1
aux1 = []
aux2 = []
aux3 = 0

for letra in entrada:
    aux1.append(letra)

while (tamanhoString) >= aux3:
    aux2.append(aux1[tamanhoString])
    tamanhoString -= 1

aux3 = str(aux3)
aux3 = ''

for letra in aux2:
    aux3 += letra

print(f'Palavra invertida: {aux3}')