# ============================================================
# AULA 2 - Os 3 tipos de gatilho (trigger) do APScheduler
# ============================================================
# O APScheduler tem 3 formas de definir QUANDO uma tarefa roda:
#
#   1. interval  → a cada X segundos/minutos/horas
#   2. date      → uma única vez em data/hora específica
#   3. cron      → igual ao agendador do Linux/Mac (ex: todo dia às 9h)
#
# Neste arquivo veremos exemplos dos 3 tipos juntos.
# ============================================================

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

scheduler = BlockingScheduler()


# ----------------------------------------------------------
# GATILHO 1: interval — repete em intervalos fixos
# ----------------------------------------------------------
def tarefa_intervalo():
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] [INTERVAL] Executando a cada 3 segundos")


scheduler.add_job(
    func=tarefa_intervalo,
    trigger="interval",
    seconds=3,
    id="intervalo",
)


# ----------------------------------------------------------
# GATILHO 2: date — executa UMA única vez
# ----------------------------------------------------------
def tarefa_unica():
    print("[DATE] Esta tarefa rodou apenas uma vez!")


# Vamos agendar para daqui a 7 segundos
momento_unico = datetime.now() + timedelta(seconds=7)

scheduler.add_job(
    func=tarefa_unica,
    trigger="date",
    run_date=momento_unico,
    id="unica_vez",
)


# ----------------------------------------------------------
# GATILHO 3: cron — agendamento estilo calendário
# ----------------------------------------------------------
def tarefa_cron():
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] [CRON] Executando todo dia nesse segundo específico")


# Rode todo dia, a cada minuto, no segundo 0
# (para ver funcionar rápido durante o teste)
scheduler.add_job(
    func=tarefa_cron,
    trigger="cron",
    second=0,   # no segundo 0 de cada minuto
    id="cron",
)

print("Agendador iniciado com 3 tarefas diferentes!")
print("  - INTERVAL: a cada 3 segundos")
print("  - DATE: uma única vez daqui a 7 segundos")
print("  - CRON: a cada início de minuto")
print("\nPressione Ctrl+C para parar.\n")

try:
    scheduler.start()
except KeyboardInterrupt:
    print("\nAgendador parado pelo usuário.")
