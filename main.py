import matplotlib.pyplot as graph

'''
*** a)Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos. ***

---> No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00. <----

---> No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente. <----

---> Após 2 períodos(s), o montante será de R$12113.69. <----
---> Após 3 períodos(s), o montante será de R$13179.11. <----
---> Após 4 períodos(s), o montante será de R$14250.27. <----
---> Após 5 períodos(s), o montante será de R$15327.22. <----

---> final: 120 meses - R$187.303,05. <----

---------------------------------------------------------

*** b) Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais. ***
-----------------------------------------------------------
'''

def aporte():
  valor_inicial = float(input("Informe o valor inicial: "))
  rendimento = float(input("Informe o rendimento por período: "))
  aporte_mensal = float(input("Informe o aporte a cada período: "))
  periodo = int(input("Informe o total de períodos: "))

  rend = (valor_inicial * rendimento)/100
  semi_total = valor_inicial + rend
  total=semi_total+ aporte_mensal

  print(f'\n-Valor inicial: R${valor_inicial}')
  print(f'-Rendimento por período (%): {rendimento}')
  print(f'-Aporte a cada período: R${aporte_mensal}')
  print(f'-Total de períodos: {periodo} \n')

  #lista para o gráfico 
  global listax 
  global listay 
  listax = []
  listay = []
  
  for x in range(1,periodo+1):
    #print(x)
    aporte_mensal=+ aporte_mensal

    rend = (valor_inicial  * rendimento)/100
    semi_total = valor_inicial + rend
    #print(semi_total)
    total=semi_total + aporte_mensal

    total_arrendodado = "%2.2f" % round(total,2)

    #total_texto = str(total_arrendodado).replace('.',',')

    print(f'Após {x} períodos(s), o montante será de R${total_arrendodado}.')

    valor_inicial = total

    #lista para o gráfico 
    listax.append(int(x))
    listay.append(float(total_arrendodado))

    
aporte()

def grafico():

      x = listax
      y = listay
      

      graph.title("Gráfico da hipótese de Einstein à prova")
      graph.xlabel('Períodos')
      graph.ylabel('Montante em R$')

      graph.plot(x,y)
      graph.show()
      
      
grafico()