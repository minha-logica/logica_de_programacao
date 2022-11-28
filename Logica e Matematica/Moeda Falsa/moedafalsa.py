from math import log2
from random import randint

def moeda_falsa(moedas):
    posicao = 0
    ultima_pesagem = int(log2(len(moedas)))
    pesagens = 1
    while pesagens <= ultima_pesagem:
        tamanho = len(moedas)
        metade, resto = divmod(tamanho, 2)        
        soma = metade + resto
             
        prato_1 = moedas[:metade]          
        prato_2 = moedas[metade + resto:]
        
        peso_prato_1 = sum(prato_1)
        peso_prato_2 = sum(prato_2)
        
        if peso_prato_1 == peso_prato_2:
            posicao += metade
            break 
            
        if peso_prato_1 > peso_prato_2:       
            posicao += soma
            moedas = prato_2[:]                                
        else:            
            moedas = prato_1[:]
        
        if len(prato_1)==1:                       
            break                    
        pesagens += 1     
    return posicao, pesagens

quantidade = 7
peso_falso = 1
peso_verdadeiro = 2
moedas = [peso_verdadeiro]*quantidade
moedas[randint(0,quantidade-1)] = peso_falso
posicao, pesagens = moeda_falsa(moedas)                        
print("Moedas: ", moedas)              
print("Posição da moeda falsa: ", posicao)
print("Pesagens: ", pesagens)
