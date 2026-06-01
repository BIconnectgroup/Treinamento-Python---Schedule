# ============================================================
# AULA 4 - Projeto Prático: Monitor de Arquivos de Relatório
# ============================================================
# Cenário real: uma pasta recebe arquivos CSV ao longo do dia.
# Nosso programa vai:
#   - A cada 10 segundos: verificar se chegaram arquivos novos
#   - A cada 30 segundos: gerar um resumo do que foi processado
#   - Uma vez ao dia (simulado aqui): limpar arquivos antigos
#
# Para testar: crie arquivos .csv na pasta "relatorios/"
# enquanto o programa roda e veja ele detectar automaticamente.
# ============================================================

import os
import time
from pathlib import Path
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# Pasta onde os relatórios chegam
PASTA_RELATORIOS = Path("relatorios")
PASTA_RELATORIOS.mkdir(exist_ok=True)  # cria a pasta se não existir

# Memória simples: quais arquivos já foram processados
arquivos_processados = set()
contador_processados = 0


def verificar_novos_arquivos():
    """Roda a cada 10 segundos: detecta arquivos CSV novos."""
    global contador_processados

    arquivos_atuais = set(PASTA_RELATORIOS.glob("*.csv"))
    novos = arquivos_atuais - arquivos_processados

    if novos:
        for arquivo in sorted(novos):
            agora = datetime.now().strftime("%H:%M:%S")
            tamanho = arquivo.stat().st_size
            print(f"[{agora}] NOVO ARQUIVO: {arquivo.name} ({tamanho} bytes)")
            arquivos_processados.add(arquivo)
            contador_processados += 1
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        print(f"[{agora}] Verificando... nenhum arquivo novo.")


def gerar_resumo():
    """Roda a cada 30 segundos: mostra um resumo geral."""
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"\n{'='*45}")
    print(f"  RESUMO — {agora}")
    print(f"  Arquivos processados: {contador_processados}")
    print(f"  Arquivos na pasta:    {len(list(PASTA_RELATORIOS.glob('*.csv')))}")
    print(f"{'='*45}\n")


def limpar_pasta():
    """Simula uma limpeza diária (aqui: 60 segundos para testar)."""
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] LIMPEZA: removendo arquivos CSV antigos...")

    removidos = 0
    for arquivo in PASTA_RELATORIOS.glob("*.csv"):
        arquivo.unlink()  # apaga o arquivo
        removidos += 1
        arquivos_processados.discard(arquivo)

    print(f"[{agora}] LIMPEZA: {removidos} arquivo(s) removido(s).\n")


# ---- Configurando o agendador ----
scheduler = BackgroundScheduler()

scheduler.add_job(
    func=verificar_novos_arquivos,
    trigger="interval",
    seconds=10,
    id="verificador",
    next_run_time=datetime.now(),  # roda imediatamente na primeira vez
)

scheduler.add_job(
    func=gerar_resumo,
    trigger="interval",
    seconds=30,
    id="resumo",
)

scheduler.add_job(
    func=limpar_pasta,
    trigger="interval",
    seconds=60,  # em produção seria: trigger="cron", hour=2 (às 2h da manhã)
    id="limpeza",
)

print("Monitor de Relatórios iniciado!")
print(f"Pasta monitorada: {PASTA_RELATORIOS.resolve()}")
print("\nCrie arquivos .csv na pasta 'relatorios/' para testar.")
print("Pressione Ctrl+C para parar.\n")

scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrando monitor...")
    scheduler.shutdown()
    print("Monitor encerrado.")
