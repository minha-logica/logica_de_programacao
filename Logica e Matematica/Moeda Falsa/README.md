## 🪙 Moeda Falsa

#### Dado um conjunto de moedas, deseja-se encontrar uma moeda falsa, que possui um peso menor que as demais moedas. 

***
## Contextualizando
Suponha que você está participando de um programa de TV e 
lhe é proposto o desafio de descobrir qual é a moeda falsa dentre
8 moedas de ouro, sabendo que, a moeda falsa pesa menos que as demais. Para isso,
a equipe de produção forneceu uma balança de dois pratos. Você só terá duas chances.
Se conseguir achar a moeda com menos de 2 pesagens em uma das 
chances você ganha as moedas de ouro. Com um pouco de sorte
e de lógica você poderia conseguir isso se pesasse a metade das moedas com a outra metade, 
eliminando a metade mais pesada. Você poderia 
repetir esse processo até encontrar a moeda mais leve ou a moeda falsa. Mas 
e se fossem um número `n` de moedas e você tivesse que escrever um algoritmo pra isso?


## Desafio
Considere uma lista `moedas` com *n* elementos representando as moedas. 
Escreva um programa que simule o processo de pesagem de uma balança de dois pratos. 
Sua missão é determinar a posição da moeda falsa com a menor quantidade de
pesagens possível. As moedas verdadeiras 
podem ser representadas por 2 e a moeda 
falsa por 1.

Exemplo:
```
[2, 2, 2, 2, 1]
```
Nesse exemplo, a moeda falsa está na última posição (pos=4)

Além disso, o programa deve informar a
quantidade de pesagens utilizadas
para chegar ao resultado, ou seja,
quantas comparações foram necessárias 
para encotrar a moeda falsa. 
***
### Importante
   * Não utilize funções internas para persquisar a moeda falsa.
   Exemplo:
```python
moedas.index(1)
```
   * Tente fazer com que a quantidade de pesagens seja menor que pelo menos metade da lista de moedas.
   


### Exemplos

**Moedas**
```
[1,2,2,2,2]
```
**Saída**
```
Moedas: [1,2,2,2,2]
Posição da moeda falsa: 0
Pesagens: 2
```

**Moedas**
```
[2,2,2,2,2,1,2]
```
**Saída**
```
Moedas: [2,2,2,2,2,1,2]
Posição da moeda falsa: 5
Pesagens: 2
```
**Moedas**
```
[2,1,2,2,2]
```
**Saída**
```
Moedas: [2,1,2,2,2]
Posição da moeda falsa: 1
Pesagens: 2
```
**Moedas**
```
[2,2,2,1,2,2,2]
```
**Saída**
```
Moedas: [2,2,2,1,2,2,2]
Posição da moeda falsa: 3
Pesagens: 1
```
**Moedas**
```
[2,1]
```
**Saída**
```
Moedas: [2,1]
Posição da moeda falsa: 1
Pesagens: 1
```
***

Dica: seu programa deve ser capaz de determinar uma moeda falsa em uma posição aleatória de uma lista com n elementos. Use isso para testar diferentes valores.

Solução disponível em `moedafalsa.py`
A resolução comentada desse exercício sairá em breve!


## Complementar

[Busca Binária](https://pt.m.wikipedia.org/wiki/Pesquisa_bin%C3%A1ria)

Obs: a resolução do problema é um pouco diferente da pesquisa binária que conhecemos, já que não podemos verificar diretamente se o elemento é igual a 1, mas sim fazer sucessivas comparações entre os elementos tal qual um balança de dois pratos o faria.
