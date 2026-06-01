# ============================================================
# AULA 1 - Introdução ao APScheduler
# ============================================================
# O APScheduler permite agendar tarefas para rodar
# automaticamente em horários ou intervalos definidos.
#
# Exemplo do dia a dia: imagine que você precisa enviar
# um relatório por e-mail toda segunda-feira às 8h.
# Com APScheduler, o Python faz isso sozinho
# ============================================================

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# Criamos o "agendador" — ele é quem controla os horários
scheduler = BlockingScheduler()


# Esta é a tarefa que queremos executar automaticamente
def dizer_ola():
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] Olá Will! Esta mensagem aparece a cada 5 segundos.")


# Adicionamos a tarefa ao agendador
# interval = intervalo de tempo entre cada execução
scheduler.add_job(
    func=dizer_ola,       # qual função executar
    trigger="interval",   # tipo: por intervalo de tempo
    seconds=5,            # a cada 5 segundos
    id="tarefa_ola",      # nome único para identificar a tarefa
)

print("Agendador iniciado! Pressione Ctrl+C para parar.\n")

# start() inicia o agendador e BLOQUEIA o programa aqui
# (o programa fica rodando até você pressionar Ctrl+C)
try:
    scheduler.start()
except KeyboardInterrupt:
    print("\nAgendador parado pelo usuário.")
