## ⏰ Conversor de Segundos

#### Dado um número inteiro positivo que representa a quantidade de segundos exibir uma mensagem para o usuário com esse valor convertido em dias, horas, minutos e segundos.

* * *
Sabemos que 1 minuto equivale a 60 segundo e 1 hora é equivalente a 60 minutos. Assim, podemos representar o tempo a partir de multiplos do segundo.
    
    1 minuto = 60 s
    1 hora   = 60 x 1 minuto = 60 x 60 s   = 3600 s
    1 dia    = 24 x 1 hora   = 24 x 3600 s = 86400 s


Sua tarefa é escrever um programa em Python que dado um valor inteiro *n* em segundos converta-o em dias, horas, minutos e segundos. 

Por exemplo, para *n* = 3500 temos

    dias  = 3500 // 86400 = 0
    resto = 3500 % 86400  = 3500
    horas = resto // 3400 = 3500 // 3400 = 1
    resto = 3500 %  3400  = 100
    minutos = resto // 60 = 100 // 60 = 1
    resto   = resto %  60 = 100 %  60 = 40
    #Saída
    0 dia(s), 1 hora(s), 1 minuto(s) e 40 segundo(s) 

Note que '//' representa a divisão inteira e '%' representa o resto da divisão assim como no Python. Se ficou com dúvida reveja o conceito de [divisão euclidiana](https://pt.wikipedia.org/wiki/Divis%C3%A3o_euclidiana). Uma dica: você pode usar a função interna `divmode` que recebe dois valores e retorna a divisão inteira e o resto da divisão ao mesmo tempo.
```Python
divisao, resto = divmod(7,4)
print(f"A divisão é {divisao} e o resto é {resto}")
#A divisão é 1 e o resto é 3
```


#### Exemplos:

**N:**
```
86400*2 + 2*3600 + 3*60 + 30
```
**Saída:**
```
2 dia(s), 2 hora(s), 3 minuto(s) e 30 segundo(s)
```

* * *


**N:**
```
97275
```
**Saída:**
```
1 dia(s), 3 hora(s), 1 minuto(s) e 15 segundo(s)
```
* * *

**N:**
```
3950
```
**Saída:**
```
0 dia(s), 1 hora(s), 5 minuto(s) e 50 segundo(s)
```
* * *


Dica: acesse o arquivo conversordesegundos.py para ver o código de resolução somemte depois de tentar resolver o exercício.😅

Vá mais além: quando terminar o desafio tente usar a mesma ideia para converter segundos em semanas, meses e anos. Você também pode tentar converter qualquer umas dessas unidade de tempo em outras.

Em breve uma explicação mais detalhada do algorítmo em [Conversor de Segundos](#)