import mysql.connector

config = {
    'user': 'mpretoufabc',
    'password': 'yr8v1xRa8Fw8UC',
    'host': 'mpretoufabc.mysql.pythonanywhere-services.com',
    'database': 'mpretoufabc$default'
}

def inserir_test(dados):
    try:
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            # Extrai os nomes das colunas e os valores do dicionário
            colunas = ", ".join(dados.keys())
            valores = tuple(dados.values())
            placeholders = ", ".join(["%s"] * len(dados))

            # Monta e executa a query
            query = f"INSERT INTO tests ({colunas}) VALUES ({placeholders})"
            cursor.execute(query, valores)
            conn.commit()
            print("Dados inseridos com sucesso na tabela 'tests'.")
    except mysql.connector.Error as e:
        print(f"Erro ao inserir dados na tabela 'tests': {e}")

if __name__ == "__main__":
    dados = {
        "initials": "MP",
        "idade": 28,
        "profession": "Engenheiro de Software",
        "created_at": "2025-10-28",
        "nota_0": 8,
        "nota_1": 7,
        "nota_2": 9,
        "nota_3": 6,
        "nota_4": 8,
        "nota_5": 7,
        "nota_6": 9,
        "nota_7": 8,
        "nota_8": 7,
        "nota_9": 8
    }

    inserir_test(dados)
