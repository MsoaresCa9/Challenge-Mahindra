import matplotlib.pyplot as plt
import numpy as np
import os
import keyboard

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
    print("Equipes da Fórmula E:")
    for equipe in equipes_formula_e:
        print(f"{equipe}: {', '.join(equipes_formula_e[equipe])}")

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

    escolha = input("Digite o número da sua escolha: ")

    if escolha.isdigit() and 1 <= int(escolha) <= len(equipes_formula_e):
        equipe_favorita = list(equipes_formula_e.keys())[int(escolha) - 1]
        print(f"Informações sobre a equipe {equipe_favorita}:")
        # Informações sobre a equipe
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

        equipe_data = equipe_info[equipe_favorita]
        print(f"Pais: {equipe_data['pais']}")
        print(f"Ano de criação: {equipe_data['ano_criacao']}")
        print(f"Títulos: {equipe_data['titulos']}")
        print(f"Seguidores: {equipe_data['seguidores']}")
        print(f"Instagram: @{equipe_data['instagram']}")

        # Curiosidades sobre a equipe
        equipe_curiosidades = {
            "Audi Sport ABT Schaeffler": [
                "A equipe Audi Sport ABT Schaeffler é uma das mais bem-sucedidas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2017 e 2018."
            ],
            "BMW i Andretti Motorsport": [
                "A equipe BMW i Andretti Motorsport é uma das mais novas da Fórmula E.",
                "Eles conquistaram o título de equipes em 2020."
            ],
            "DS Techeetah": [
                "A equipe DS Techeetah é uma das mais bem-sucedidas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2019 e 2020."
            ],
            "Envision Virgin Racing": [
                "A equipe Envision Virgin Racing é uma das mais antigas da Fórmula E.",
                "Eles conquistaram o título de equipes em 2019."
            ],
            "Jaguar TCS Racing": [
                "A equipe Jaguar TCS Racing é uma das mais novas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2020."
            ],
            "Mahindra Racing": [
                "A equipe Mahindra Racing é uma das mais antigas da Fórmula E.",
                "Eles conquistaram o título de equipes em 2017."
            ],
            "Mercedes-EQ Formula E Team": [
                "A equipe Mercedes-EQ Formula E Team é uma das mais bem-sucedidas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2020 e 2021."
            ],
            "NIO 333 FE Team": [
                "A equipe NIO 333 FE Team é uma das mais antigas da Fórmula E.",
                "Eles conquistaram o título de equipes em 2018."
            ],
            "Porsche Formula E Team": [
                "A equipe Porsche Formula E Team é uma das mais bem-sucedidas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2021."
            ],
            "Rokit Venturi Racing": [
                "A equipe Rokit Venturi Racing é uma das mais antigas da Fórmula E.",
                "Eles conquistaram o título de equipes em 2019."
            ],
            "TAG Heuer Porsche Formula E Team": [
                "A equipe TAG Heuer Porsche Formula E Team é uma das mais bem-sucedidas da Fórmula E.",
                "Eles conquistaram o título de pilotos em 2021."
            ]
        }

        while True:
            continuar = input("Você deseja continuar utilizando o programa? (sim/não): ")
            if continuar.casefold() == "sim":
                # Continuar mostrando informações sobre as equipes
                mostrar_informacoes_equipe_favorita()
                break
            elif continuar.casefold() == "não":
                # Voltar ao menu principal
                print("Você escolheu voltar ao menu principal.")
                # Chamar a função do menu principal aqui
                main()
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
        else:
            print("Opção inválida. Por favor, escolha novamente.")

        continuar = input("Você deseja continuar utilizando o programa? (Sim/Não): ")
        while True:
            if continuar.lower() == "sim":
                break
            elif continuar.lower() == "não":
                print("Você escolheu sair do programa. Até logo!")
                exit()
            else:
                print("Opção inválida. Por favor, escolha novamente.")
                continuar = input("Você deseja continuar utilizando o programa? (Sim/Não): ")

        limpar_console()

if __name__ == "__main__":
    main()
