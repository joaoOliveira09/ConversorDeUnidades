def converter_temperatura():
    print("\n1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print("Temperatura em Fahrenheit:", fahrenheit)
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperatura em Celsius:", celsius)
    else:
        print("Opção inválida!")

def converter_comprimento():
    print("\n1. Metros para Pés")
    print("2. Pés para Metros")
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == '1':
        metros = float(input("Digite o valor em metros: "))
        pes = metros * 3.281
        print("Valor em pés:", pes)
    elif opcao == '2':
        pes = float(input("Digite o valor em pés: "))
        metros = pes / 3.281
        print("Valor em metros:", metros)
    else:
        print("Opção inválida!")

def converter_peso():
    print("\n1. Quilogramas para Libras")
    print("2. Libras para Quilogramas")
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == '1':
        quilogramas = float(input("Digite o valor em quilogramas: "))
        libras = quilogramas * 2.205
        print("Valor em libras:", libras)
    elif opcao == '2':
        libras = float(input("Digite o valor em libras: "))
        quilogramas = libras / 2.205
        print("Valor em quilogramas:", quilogramas)
    else:
        print("Opção inválida!")

def main():
    while True:
        print("\n=== Aplicação de Conversão de Unidades ===")
        print("1. Conversão de Temperatura")
        print("2. Conversão de Comprimento")
        print("3. Conversão de Peso")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            converter_temperatura()
        elif opcao == '2':
            converter_comprimento()
        elif opcao == '3':
            converter_peso()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

print("Bem-vindo à Aplicação de Conversão de Unidades!")
main()
