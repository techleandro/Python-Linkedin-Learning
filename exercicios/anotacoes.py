#ESTRUTURAS DE DADOS

#conjuntos (sets) são estruturas de valores únicos declarados por chaves, modificaveis, não da pra acessar por índice porque a ordem não importa, tem que chamar pelo conteúdo de cada elemento
exemplo = {'a', 'b', 'c', 'c'}
print(exemplo)
#retorna sem o segundo c

#--------------------------------------

#dicionarios são estruturas chave - valor declarados por chaves, modificáveis e não únicos

exemplo2 = {
    'a':'primeira letra',
    'b':'segunda letra',
    'c':'terceira letra'
}
print(exemplo2)

#--------------------------------------

# tuplas são estruturas não modificáveis e repetíveis declarados por parênteses, mais estáveis e preferíveis do que listas por alocarem apenas o espaço definido na memória

exemplo3 = ('a', 'b', 'c')
print (exemplo3)
#exemplo3.append() da erro, você só pode verificar e chamar coisas, e não modificar, pode se acessar usando índice

#--------------------------------------

#listas são modificáveis e não únicas declaradas por chaves
exemplo4 = ['a', 'b', 'c']
print(exemplo4)

#--------------------------------------

#as estruturas de dados se misturam, você pode ter uma lista de tuplas, lista de listas, lista de dicionários, lista de conjuntos
#dicionários de listas, dicionários de tuplas e assim por diante...
#vai de saber o uso e a função de cada uma

#--------------------------------------

#range gera um objeto iteravel, entao pra visualizar todos os elementos tem que usar um método que passe um por um, como o list

#--------------------------------------
#string format você usa para usar variáveis e afins dentro de uma string
#f'{variavel, função, estrutura de controle ou o que quer que seja}'
from datetime import datetime

print (f'Data e horário atual: {datetime.now()}')

#no for loop pode usar if e elif e não precisa de else, no operador ternário precisa de else na última condição

#estruturas de repetição for e while

#continue passa pra proxima checagem
#pass vai pro final do loop
#break força a saída do loop