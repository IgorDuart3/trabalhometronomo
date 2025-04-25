from tkinter import *
from tkinter import messagebox
import metronomo

def criar_interface():
    app = Tk()
    app.title("Metrônomo")
    app.geometry("500x300")

    bpm_label = Label(app, text="BPM:")
    bpm_label.pack(pady=5)

    bpm_entry = Entry(app)
    bpm_entry.insert(0, str(60))
    bpm_entry.pack(pady=5)

    play_pause_button = Button(app, text="Play")

    def atualizar_bpm_callback():
        valor = bpm_entry.get()
        try:
            valor_int = int(valor)
            if valor_int < 30 or valor_int > 300:
                messagebox.showwarning("BPM inválido", "Por favor, insira um valor entre 30 e 300.")
                return False
            metronomo.atualizar_bpm(valor_int)
            return True
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
            return False

    def play_pause_callback():
        if metronomo.esta_rodando():
            metronomo.parar_metronomo()
            play_pause_button.config(text="Play")
        else:
            if atualizar_bpm_callback():  # Só inicia se o BPM for válido
                metronomo.iniciar_metronomo()
                play_pause_button.config(text="Pause")

    atualizar_bpm_button = Button(app, text="Atualizar BPM", command=atualizar_bpm_callback)
    atualizar_bpm_button.pack(pady=10)

    play_pause_button.config(command=play_pause_callback)
    play_pause_button.pack(pady=20)

    return app
