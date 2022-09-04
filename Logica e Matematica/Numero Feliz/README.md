## 🧮 Número Feliz

#### Dado um número inteiro positivo verificar se é um número feliz ou infeliz.

* * *
Um número inteiro positivo é feliz se quando substituido pela soma do quadrado de cada um de seus dígitos assume eventualmente o valor 1. Por outro lado, se o número eventualmente atinge um dos valores que iniciou a sequência ele é considerado infeliz ou triste. 

Por exemplo, 13 é um número feliz 😁, pois 

    n = 13
    n = 1^2 + 3^2 = 10
    n = 1^2 + 0^2 = 1 (fim)

Já o 5 é infeliz😢, pois

    n = 5
    n = 5^2 = 25
    n = 2^2 + 5^2 = 29
    n = 2^2 + 9^2 = 85
    n = 8^2 + 5^2 = 89 (inicio)
    n = 8^2 + 9^2 = 145
    n = 1^2 + 4^2 + 5^2 = 42
    n = 4^2 + 2^2 = 20
    n = 2^2 + 0^2 = 4
    n = 4^2 = 16
    n = 1^2 + 6^2 = 37
    n = 3^2 + 7^2 = 58
    n = 5^2 + 8^2 = 89 (fim)

Note que no último exemplo a sequência termina quando *n* assume um dos valores anteriores, que no caso é o 89. Se continuássemos repetindo esse processo a sequência seria a mesma a partir do número 89, isto é, a sequência seria periódica.

Assim, sua missão é escrever um programa em Python ou em uma linguagem de sua preferência que receba um inteiro positivo *n* e informe ao usuário se esse número é feliz ou infeliz.


#### Exemplos:

**Entrada:**
```
13
```
**Saída:**
```
13 é feliz
```

* * *


**Entrada:**
```
4
```
**Saída:**
```
4 é infeliz
```
* * *

Dica: acesse o arquivo numerofeliz.py para ver o código de resolução somemte depois de tentar resolver o exercício.😅

Em breve a explicação completa do algorítmo em [Número Feliz](#)

Para saber mais sobre os Números Feliz acesse [String Fixer](https://stringfixer.com/pt/Happy_prime)