import matplotlib.pyplot as graph


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