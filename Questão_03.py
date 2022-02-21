#!/usr/bin/env python3

palavra = 'ifailuhkqq'

def extNum(elem, tam2):
	tmp=[]
	cont = tam2
	tam1 =0
	for i in range(len(elem)):
		a =(elem[tam1:tam2])
		if len(a) == cont:
			tmp.append(a)
		tam1+=1
		tam2+=1
	return tmp

def anagramaPerfeito(palavra):
	for letra in range(len(palavra)-1,-1,-1):
		return (palavra[letra])

tmp2 = []

for i in range(len(palavra)):
	tmp2.append(extNum(palavra, i+1))
	#print(tmp2)
cont =0
l=[]
sortedTmp =[]
sorted2 = []
tmp3 = []
contador = 0
for i in tmp2:
	for j in i:
		sortedTmp.append("".join(sorted(j)))
sortedTmp.sort()
for i in range(len(sortedTmp)-1):
	if (sortedTmp[i] == sortedTmp[i + 1]):
		cont+=1

print(cont)
