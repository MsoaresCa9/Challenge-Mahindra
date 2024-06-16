import matplotlib.pyplot as plt
import numpy as np
import os
import keyboard

# Data das proximas corridas
data_corridas = [
    "13 de janeiro de 2024",
    "26 de janeiro de 2024",
    "27 de janeiro de 2024",
    "10 de fevereiro de 2024",
    "24 de fevereiro de 2024",
    "16 de março de 2024",
    "30 de março de 2024",
    "13 de abril de 2024",
    "14 de abril de 2024",
    "27 de abril de 2024",
    "25 de maio de 2024",
    "8 de junho de 2024",
    "29 de junho de 2024",
    "20 de julho de 2024",
    "21 de julho de 2024"
]
#local onde sera as prximas corridas
local_corridas = [
    "México",
    "Arábia Saudita",
    "Arábia Saudita",
    "A ser confirmado",
    "A ser confirmado",
    "Brasil",
    "Japão",
    "Itália",
    "Itália",
    "Mônaco",
    "A ser cofirmado",
    "Indonésia",
    "Estados Unidos (EUA)",
    "Reino Unido",
    "Reino Unido",
]
#Equipes presentes na formula-e
equipes_formula_e = {
    "Audi Sport ABT Schaeffler": ["Lucas di Grassi", "René Rast"],
    "BMW i Andretti Motorsport": ["António Félix da Costa", "Alexander Sims"],
    "DS Techeetah": ["Jean-Éric Vergne", "André Lotterer"],
    "Envision Virgin Racing": ["Sam Bird", "Robin Frijns"],
    "Jaguar TCS Racing": ["Mitch Evans", "James Calado"],
    "Mahindra Racing": ["Jérôme d'Ambrosio", "Pascal Wehrlein"],
    "Mercedes-EQ Formula E Team": ["Stoffel Vandoorne", "Nyck de Vries"],
    "NIO 333 FE Team": ["Oliver Turvey", "Tom Blomqvist"],
    "Porsche Formula E Team": ["André Lotterer", "Pascal Wehrlein"],
    "Rokit Venturi Racing": ["Felipe Massa", "Edoardo Mortara"],
    "TAG Heuer Porsche Formula E Team": ["Neel Jani", "André Lotterer"]
}

def mostrar_data_corridas():
    print("As próximas corridas da Fórmula E serão em:")
    for i, data in enumerate(data_corridas):
        print(f"{i+1}. {data} - {local_corridas[i]}")

def gerar_grafico_interativo():
    # Velocidades máximas de carros de Fórmula 1 e Fórmula E em diferentes circuitos
    velocidades_f1 = {
        "Monza": 370,
        "Silverstone": 360,
        "Montréal": 350,
        "Spa": 340,
        "São Paulo": 320,
        "Austin": 310,
        "Melbourne": 300,
        "Bahrain": 290,
        "Shanghai": 280
    }

    velocidades_fe = {
        "Roma": 220,
        "Paris": 210,
        "Berlim": 200,
        "Nova York": 190,
        "Londres": 180,
        "Marrakech": 170,
        "Santiago": 160,
        "México": 150,
        "Hong Kong": 140,
        "Ad Diriyah": 130
    }

    # Média de velocidade de cada equipe
    media_velocidade_f1 = np.mean(list(velocidades_f1.values()))
    media_velocidade_fe = np.mean(list(velocidades_fe.values()))

    # Criar o gráfico
    plt.figure(figsize=(10, 6))

    plt.plot(list(velocidades_f1.keys()), list(velocidades_f1.values()), label='Fórmula 1')
    plt.plot(list(velocidades_fe.keys()), list(velocidades_fe.values()), label='Fórmula E')

    plt.axhline(y=media_velocidade_f1, color='r', linestyle='--', label='Média Fórmula 1')
    plt.axhline(y=media_velocidade_fe, color='g', linestyle='--', label='MédFórmula E')

    plt.xlabel('Circuito')
    plt.ylabel('Velocidade (Km/h)')
    plt.title('Comparação de velocidades entre Fórmula 1 e Fórmula E')
    plt.legend()

    plt.show()
#função que mostra as equipes
def mostrar_equipes_formula_e():
    print("Equipes da Fórmula E:")
    for equipe in equipes_formula_e:
        print(f"{equipe}: {', '.join(equipes_formula_e[equipe])}")
#função para direcionar para o site da formul-e
def redirect_formula_e_website():
    print("Você será redirecionado para o site oficial da Fórmula E...")
    import webbrowser
    webbrowser.open("https://www.fiaformulae.com/pt-br")
#função para limpar console
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
#função principal que ofere as opções o usuario
def main():
    keyboard.add_hotkey('ctrl', limpar_console)
    while True:
        print("Selecione uma opção:")
        print("1. Data das corridas")
        print("2. Gerar gráfico interativo")
        print("3. Equipes da Fórmula E")
        print("4. Saber mais sobre a Fórmula E")
        opcao = input("Opção: ")

        if opcao == "1":
            mostrar_data_corridas()
        elif opcao == "2":
            gerar_grafico_interativo()
        elif opcao == "3":
            mostrar_equipes_formula_e()
            while True:
                equipe_escolhida = input("Qual equipe você deseja saber mais sobre? ")
                if equipe_escolhida in equipes_formula_e:
                    print(f"Equipe {equipe_escolhida}: {', '.join(equipes_formula_e[equipe_escolhida])}")
                    break
                else:
                    print("Opção inválida. Por favor, digite novamente.")
        elif opcao == "4":
            redirect_formula_e_website()
        else:
            print("Opção inválida. Por favor, digite novamente.")
            continue
#pergunta ao usuario se ele deseja mais algumma informação
        while True:
            resposta = input("Deseja saber mais alguma informação? (Sim/Não): ")
            if resposta.lower() == "sim":
                break
            elif resposta.lower() == "não":
                limpar_console()
                return
            else:
                print("Opção inválida. Por favor, digite 'Sim' ou 'Não'.")
                limpar_console()

if __name__ == "__main__":
    main()