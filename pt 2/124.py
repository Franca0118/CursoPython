# exercicio da aula
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
erros = 0
input("Precione enter para começar o questionario")
for i in perguntas:
    print(i['Pergunta'])
    for j,k in enumerate(i["Opções"]):
        print(f"{j+1}) {k}")
    while True:
        try:
            # ao inves to try, eu poderia ter usado .isdigit() e is not None
            resp = input("Qual a respota?")
            resp = int(resp)
            if resp > 0 and resp <= 4 : break
            else: print("Nao foi encontrada esta opção")
        except:
            print("Resposta invalida, tente novamente")
    if i['Opções'][resp-1] == i['Resposta']:
        acertos+=1 
    else:
        erros+=1 
print("Fim do formulario")
print("Acertos:",acertos,"\nErros:",erros)
    