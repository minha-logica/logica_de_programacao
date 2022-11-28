## 🪙 Moeda Falsa

#### Dado um conjunto de moedas, sendo uma delas falsa, deseja-se saber através de uma balança qual a moeda falsa sabendo que seu peso é menor que as demais.

***

Seja uma lista com "n" elementos representando moedas. Escreva
um programa que determine a posição da
moeda falsa com a menor quantidade de
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
A resolução comentada desse exercício sai em breve!


## Complementar

[Busca Binária](https://pt.m.wikipedia.org/wiki/Pesquisa_bin%C3%A1ria)

Obs: a resolução do problema é um pouco diferente da pesquisa binária, já que não podemos verificar diretamente se o elemento é igual a 1, mas sim fazer sucessivas comparações entre os elementos tal qual um balança de dois pratos o faria.
