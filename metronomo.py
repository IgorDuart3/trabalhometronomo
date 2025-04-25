import time
import threading
from sons import som_click

# Variáveis de estado
estado = {
    "rodando": False,
    "bpm": 60,
    "intervalo": 1.0,
    "thread": None
}

def atualizar_bpm(valor_bpm):
    estado["bpm"] = int(valor_bpm)
    estado["intervalo"] = 60.0 / estado["bpm"]
    print(f'BPM alterado para {estado["bpm"]}.')

def _loop_metronomo():
    while estado["rodando"]:
        som_click.play()
        time.sleep(estado["intervalo"])

def iniciar_metronomo():
    if not estado["rodando"]:
        estado["rodando"] = True
        estado["thread"] = threading.Thread(target=_loop_metronomo, daemon=True)
        estado["thread"].start()

def parar_metronomo():
    estado["rodando"] = False
    print("Metrônomo parado.")

def esta_rodando():
    return estado["rodando"]
