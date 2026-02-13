import sqlite3

# 1. Conecta ao banco e cria a tabela de vendas
conexao = sqlite3.connect('vendas_empresa.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT
    )
''')

# 2. Função simples para cadastrar uma venda
def cadastrar_venda(produto, valor, data):
    cursor.execute("INSERT INTO vendas (produto, valor, data) VALUES (?, ?, ?)", (produto, valor, data))
    conexao.commit()
    print(f"✅ Venda de {produto} registrada com sucesso!")

# 3. Função para ver o total vendido (O que o patrão gosta de ver!)
def relatorio_vendas():
    print("\n--- RELATÓRIO DE VENDAS ---")
    cursor.execute("SELECT SUM(valor) FROM vendas")
    total = cursor.fetchone()[0]
    print(f"💰 Total faturado até agora: R$ {total if total else 0:.2f}")
    print("---------------------------\n")

# --- TESTANDO O SISTEMA ---
# Simulando o cadastro de algumas vendas
cadastrar_venda("Curso de Python", 150.00, "13/02/2026")
cadastrar_venda("Mentoria SQL", 250.00, "13/02/2026")

# Mostrando o resultado
relatorio_vendas()

conexao.close()
