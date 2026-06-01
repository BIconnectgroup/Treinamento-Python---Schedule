# ============================================================
# AULA 3 - BackgroundScheduler: rodando em segundo plano
# ============================================================
# Na Aula 1 usamos o BlockingScheduler, que "trava" o programa.
# Agora vamos usar o BackgroundScheduler, que roda em paralelo —
# o programa continua executando outras coisas ao mesmo tempo.
#
# Isso é útil quando o agendador é apenas PARTE do programa.
# ============================================================

import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


def coletar_dados():
    agora = datetime.now().strftime("%H:%M:%S")
    print(f"  [AGENDADOR] Coletando dados às {agora}...")


# BackgroundScheduler roda em uma thread separada
scheduler = BackgroundScheduler()

scheduler.add_job(
    func=coletar_dados,
    trigger="interval",
    seconds=4,
    id="coleta",
)

# start() NÃO bloqueia — o programa continua abaixo
scheduler.start()

print("Programa principal iniciado!")
print("O agendador roda em segundo plano.\n")

# Simulamos o programa principal fazendo outras coisas
for i in range(1, 16):
    print(f"[PROGRAMA] Processando passo {i}/15...")
    time.sleep(1)

print("\nPrograma principal terminou. Parando agendador...")
scheduler.shutdown()
print("Agendador encerrado. Fim do programa.")
