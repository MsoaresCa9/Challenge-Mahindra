import matplotlib.pyplot as plt
import numpy as np
import os
import keyboard
import pandas as pd

# Data das próximas corridas
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

# Local onde serão as próximas corridas
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

# Equipes presentes na Fórmula E
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

def mostrar_equipes_formula_e():
    df = pd.DataFrame(list(equipes_formula_e.items()), columns=["Equipe", "Pilotos"])
    print(df)

def redirect_formula_e_website():
    print("Você será redirecionado para o site oficial da Fórmula E...")
    url = "https://www.fiaformulae.com/pt-br"
    os.system(f"start {url}" if os.name == "nt" else f"open {url}")

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_informacoes_equipe_favorita():
    print("Escolha uma equipe da Fórmula E:")
    for i, equipe in enumerate(equipes_formula_e):
        print(f"{i+1}. {equipe}")

    while True:
        escolha = input("Digite o número da sua escolha: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(equipes_formula_e):
            equipe_favorita = list(equipes_formula_e.keys())[int(escolha) - 1]
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    equipe_info = {
        "Audi Sport ABT Schaeffler": {
            "pais": "Alemanha",
            "ano_criacao": 2009,
            "titulos": 4,
            "seguidores": 100000,
            "instagram": "audisport"
        },
        "BMW i Andretti Motorsport": {
            "pais": "EUA",
            "ano_criacao": 2013,
            "titulos": 2,
            "seguidores": 50000,
            "instagram": "bmwiandrettimotorsport"
        },
        "DS Techeetah": {
            "pais": "China",
            "ano_criacao": 2016,
            "titulos": 3,
            "seguidores": 80000,
            "instagram": "dstecheetah"
        },
        "Envision Virgin Racing": {
            "pais": "Reino Unido",
            "ano_criacao": 2013,
            "titulos": 1,
            "seguidores": 40000,
            "instagram": "envisionvirginracing"
        },
        "Jaguar TCS Racing": {
            "pais": "Reino Unido",
            "ano_criacao": 2016,
            "titulos": 1,
            "seguidores": 30000,
            "instagram": "jaguarracing"
        },
        "Mahindra Racing": {
            "pais": "Índia",
            "ano_criacao": 2014,
            "titulos": 1,
            "seguidores": 20000,
            "instagram": "mahindraracing"
        },
        "Mercedes-EQ Formula E Team": {
            "pais": "Alemanha",
            "ano_criacao": 2019,
            "titulos": 2,
            "seguidores": 150000,
            "instagram": "mercedeseq"
        },
        "NIO 333 FE Team": {
            "pais": "China",
            "ano_criacao": 2014,
            "titulos": 0,
            "seguidores": 10000,
            "instagram": "nio333fe"
        },
        "Porsche Formula E Team": {
            "pais": "Alemanha",
            "ano_criacao": 2019,
            "titulos": 1,
            "seguidores": 120000,
            "instagram": "porscheformulae"
        },
        "Rokit Venturi Racing": {
            "pais": "Mônaco",
            "ano_criacao": 2014,
            "titulos": 0,
            "seguidores": 15000,
            "instagram": "rokitventuriracing"
        },
        "TAG Heuer Porsche Formula E Team": {
            "pais": "Alemanha",
            "ano_criacao": 2019,
            "titulos": 1,
            "seguidores": 100000,
            "instagram": "tagheuerporsche"
        }
    }

    print(f"Informações sobre a equipe {equipe_favorita}:")
    equipe_data = equipe_info[equipe_favorita]
    print(f"Pais: {equipe_data['pais']}")
    print(f"Ano de criação: {equipe_data['ano_criacao']}")
    print(f"Títulos: {equipe_data['titulos']}")
    print(f"Seguidores: {equipe_data['seguidores']}")
    print(f"Instagram: @{equipe_data['instagram']}")

    while True:
        continuar = input("Você deseja continuar utilizando o programa? (sim/não): ")
        if continuar.casefold() == "sim":
            break
        elif continuar.casefold() == "não":
            print("Você escolheu sair do programa. Até logo!")
            exit()
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def adicionar_equipe():
    equipe_nome = input("Digite o nome da equipe: ")
    equipe_pilotos = input("Digite os pilotos da equipe (separados por vírgula): ")
    equipe_pilotos = [piloto.strip() for piloto in equipe_pilotos.split(",")]
    equipes_formula_e[equipe_nome] = equipe_pilotos
    print("Equipe adicionada com sucesso!")

def atualizar_equipe():
    equipe_nome = input("Digite o nome da equipe que deseja atualizar: ")
    if equipe_nome in equipes_formula_e:
        equipe_pilotos = input("Digite os novos pilotos da equipe (separados por vírgula): ")
        equipe_pilotos = [piloto.strip() for piloto in equipe_pilotos.split(",")]
        equipes_formula_e[equipe_nome] = equipe_pilotos
        print("Equipe atualizada com sucesso!")
    else:
        print("Equipe não encontrada.")

def excluir_equipe():
    equipe_nome = input("Digite o nome da equipe que deseja excluir: ")
    if equipe_nome in equipes_formula_e:
        del equipes_formula_e[equipe_nome]
        print("Equipe excluída com sucesso!")
    else:
        print("Equipe não encontrada.")

def funcionario_menu():
    while True:
        print("Menu do Funcionário:")
        print("1. Adicionar equipe")
        print("2. Atualizar equipe")
        print("3. Excluir equipe")
        print("4. Voltar ao menu principal")

        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            adicionar_equipe()
        elif escolha == "2":
            atualizar_equipe()
        elif escolha == "3":
            excluir_equipe()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def main():
    while True:
        print("Seja bem-vindo ao programa de Fórmula E!")
        print("Escolha uma opção:")
        print("1. Mostrar próximas corridas")
        print("2. Gerar gráfico interativo")
        print("3. Mostrar equipes da Fórmula E")
        print("4. Redirecionar para o site oficial da Fórmula E")
        print("5. Mostrar informações sobre a equipe favorita")
        print("6. Sair do programa")
        print("7. Funcionário")

        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            mostrar_data_corridas()
        elif escolha == "2":
            gerar_grafico_interativo()
        elif escolha == "3":
            mostrar_equipes_formula_e()
        elif escolha == "4":
            redirect_formula_e_website()
        elif escolha == "5":
            mostrar_informacoes_equipe_favorita()
        elif escolha == "6":
            print("Você escolheu sair do programa. Até logo!")
            exit()
        elif escolha == "7":
            funcionario_menu()
        else:
            print("Opção inválida. Por favor, escolha novamente.")

        continuar = input("Você deseja continuar utilizando o programa? (sim/não): ")
        while True:
            if continuar.lower() == "sim":
                break
            elif continuar.lower() == "não":
                print("Você escolheu sair do programa. Até logo!")
                exit()
            else:
                print("Opção inválida. Por favor, escolha novamente.")
                continuar = input("Você deseja continuar utilizando o programa? (sim/não): ")

        limpar_console()

if __name__ == "__main__":
    main()
