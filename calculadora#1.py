valor_investimento=float(input("informe o valor inicial: "))
juros=int(input("Informe o Juros ao ano do investimento: "))
tempo=int(input("diga quanto você investira?: "))

while True:
    operação=(input("Informe qual operação deseja efetuar se é Juros simplês (JS) ou Juros composto" 
                    "diga apenas as siglas JS ou JC: "))
    if operação.upper() == "JS" or operação.upper() == "JC":
        for x in range(1, tempo+1):
            if operação.upper() == "JS":
                resultado= valor_investimento + valor_investimento * (juros / 100) * x
                print(f"o valor do rendimento bruto no tempo {x}: R$ {resultado: .2f}")
            else:
                resultado= valor_investimento * (1 + juros / 100) ** x
            print(f"o valor do rendimento bruto no tempo {x}: R$ {resultado: .2f}")
            break
        else:
            print("essa operação que você solicitou não existe,   tente novamente: ")