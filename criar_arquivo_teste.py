# ============================================================
# Script auxiliar para testar o projeto prático (Aula 4)
# ============================================================
# Execute este script em um terminal separado enquanto o
# 04_projeto_pratico.py está rodando.
# Ele cria um arquivo CSV novo a cada 8 segundos.
# ============================================================

import time
from pathlib import Path
from datetime import datetime

PASTA = Path("relatorios")
PASTA.mkdir(exist_ok=True)

print("Criando arquivos CSV de teste a cada 8 segundos...")
print("Pressione Ctrl+C para parar.\n")

contador = 1
try:
    while True:
        nome = f"relatorio_{datetime.now().strftime('%H%M%S')}_{contador}.csv"
        arquivo = PASTA / nome

        # Cria um CSV simples com alguns dados fictícios
        conteudo = "data,vendedor,valor\n"
        conteudo += f"2026-06-01,Ana,1500.00\n"
        conteudo += f"2026-06-01,Bruno,2300.50\n"

        arquivo.write_text(conteudo)
        print(f"Arquivo criado: {nome}")

        contador += 1
        time.sleep(8)
except KeyboardInterrupt:
    print("\nParado.")
