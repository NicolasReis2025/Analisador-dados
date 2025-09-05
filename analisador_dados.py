def calcularDesvioPadraoAlturas(alturas):
    media = sum(alturas) / len(alturas)
    variancia =  sum((i - media)**2 for i in alturas) / (len(alturas) - 1)
    return variancia ** 0.5

def calcularMediaIdades(idades):
    return sum(idades) / len(idades)

def calcularIMC(peso, altura):
    return peso / (altura**2)

def calcularMedianaPesos(pesos):
    lista_ordenada = sorted(pesos)
    n = len(lista_ordenada)

    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        meio1 = lista_ordenada[n // 2 - 1]
        meio2 = lista_ordenada[n // 2]
        return (meio1 + meio2) / 2
    
def main():
    nomes = []
    idades = []
    pesos = []
    alturas = []
    Imc = []

    quantidade_alunos = int(input("Digite a quantidade de alunos: "))
    i = 0
    for _ in range(quantidade_alunos):
        print(f"{i+1}# pessoa: ")
        try:
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
            peso = float(input("Peso: "))
            altura = float(input("Altura: "))
            print("-="*10)
        except ValueError:
            print("ERRO: digite uma entrada válida! ")
            continue

        nomes.append(nome)    
        idades.append(idade)
        pesos.append(peso)
        alturas.append(altura)
        Imc.append(calcularIMC(peso, altura))
        i += 1

    if not nomes:
        print("Nenhum aluno inserido!") 
        return

    media_idades = calcularMediaIdades(idades)
    desvio_padrao_alturas = calcularDesvioPadraoAlturas(alturas)
    mediana_pesos = calcularMedianaPesos(pesos)
    maior_imc = max(Imc)
    menor_imc = min(Imc)
    print(f"\nAlunos cadastrados: ")
    
    for i in range(quantidade_alunos):
        print(f"Nome: {nomes[i]} | Idade: {idades[i]} | Altura: {alturas[i]:.2f} | peso: {pesos[i]:.2f} | Imc: {Imc[i]:.2f}\n")
        print("=-"*10)
    
    print("\n=== Análise de desempenhos ===")

    print(f"Média de idades dos alunos: {media_idades:.2f}\n")
    print(f"Mediana do peso: {mediana_pesos:.2f}\n")
    print(f"Desvio padrão das alturas: {desvio_padrao_alturas:.2f}\n")
    print("Maior imc:")
    print(f"nome: {nomes[Imc.index(maior_imc)]} | Imc: {maior_imc:.2f}\n")
    print("menor imc: ")
    print(f"Nome: {nomes[Imc.index(menor_imc)]} | Imc: {menor_imc:.2f}\n")

if __name__ == "__main__":
    main()
