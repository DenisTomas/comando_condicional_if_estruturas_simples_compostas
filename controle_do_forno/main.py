def medir_forno():
    umidade = float(input("Digite a umidade do ar interna do forno: "))
    temperatura = float(input("Digite a temperatura externa do forno: "))
    return umidade, temperatura

def decidir_procedimento(umidade, temperatura):
    if temperatura <= 20 and umidade >= 40:
        return "desumidificacao"
    return "coccao"

def desumidificacao():
    print("Início da desumidificação.")
    umidade = float(input("Digite a umidade do ar interna do forno após a desumidificação: "))
    temperatura = float(input("Digite a temperatura interna do forno após a desumidificação: "))
    if temperatura > 15 and umidade >= 40:
        print("Acionando somente o exaustor.")
    elif temperatura <= 15 and umidade >= 40:
        print("Acionando aquecimento do forno e exaustor de ar.")
        temperatura = float(input("Digite a temperatura interna do forno após o aquecimento: "))
    while umidade >= 5:
        umidade = float(input("Digite a umidade do ar interna do forno após a desumidificação: "))
    print("Desumidificação concluída.")

def coccao():
    print("Iniciando cocção.")
    umidade = float(input("Digite a umidade do ar interna do forno após a cocção: "))
    temperatura = float(input("Digite a temperatura interna do forno após a cocção: "))
    if umidade > 15:
        print("Acionando exaustor.")
    if temperatura < 200:
        print("Acionando aquecimento para a temperatura de 380°C.")
        temperatura = float(input("Digite a temperatura interna do forno após o aquecimento: "))
    while umidade >= 5:
        umidade = float(input("Digite a umidade do ar interna do forno após a cocção: "))
    print("Inserir conteúdo para cocção - quando concluir pressionar botão pronto")
    input("Pressione Enter para continuar...")
    print("Manter aquecimento a 380°C por 3 horas.")
    print("Cocção concluída.")

def main():
    umidade, temperatura = medir_forno()
    procedimento = decidir_procedimento(umidade, temperatura)
    
    if procedimento == "desumidificacao":
        desumidificacao()
    coccao()

if __name__ == "__main__":
    main()
