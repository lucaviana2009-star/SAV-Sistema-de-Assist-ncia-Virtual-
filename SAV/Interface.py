import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

from SAV_project import perguntar_ia


# ---------------------- Funções ----------------------

def enviar():

    pergunta = entrada.get().strip()

    if not pergunta:
        return

    entrada.delete(0, tk.END)

    chat.config(state="normal")

    chat.insert(tk.END, "\n👤 Você\n", "user_title")
    chat.insert(tk.END, f"{pergunta}\n\n", "user")

    chat.insert(tk.END, "🤖 SAV\n", "bot_title")

    chat.config(state="disabled")
    chat.see(tk.END)

    def atualizar_texto(pedaco):

        chat.config(state="normal")
        chat.insert(tk.END, pedaco, "bot")
        chat.config(state="disabled")

        chat.see(tk.END)
        janela.update_idletasks()

    perguntar_ia(
        pergunta,
        callback=atualizar_texto
    )

    chat.config(state="normal")
    chat.insert(tk.END, "\n\n")
    chat.config(state="disabled")


def enviar_thread():
    Thread(target=enviar, daemon=True).start()


# ---------------------- Janela ----------------------

janela = tk.Tk()

janela.title("SAV AI")
janela.geometry("950x700")
janela.configure(bg="#111827")


# ---------------------- Cabeçalho ----------------------

topo = tk.Frame(
    janela,
    bg="#1F2937",
    height=60
)

topo.pack(fill="x")

titulo = tk.Label(
    topo,
    text="SAV AI",
    font=("Segoe UI", 18, "bold"),
    bg="#1F2937",
    fg="white"
)

titulo.pack(side="left", padx=20, pady=12)

status = tk.Label(
    topo,
    text="🟢 Online",
    font=("Segoe UI", 10),
    bg="#1F2937",
    fg="#4ADE80"
)

status.pack(side="right", padx=20)


# ---------------------- Chat ----------------------

chat = scrolledtext.ScrolledText(
    janela,
    wrap=tk.WORD,
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 11),
    relief="flat",
    padx=15,
    pady=15,
    state="disabled",
)

chat.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(15, 10)
)

chat.tag_config(
    "user_title",
    foreground="#60A5FA",
    font=("Segoe UI", 11, "bold")
)

chat.tag_config(
    "bot_title",
    foreground="#22C55E",
    font=("Segoe UI", 11, "bold")
)

chat.tag_config(
    "user",
    foreground="white"
)

chat.tag_config(
    "bot",
    foreground="#E5E7EB"
)


# ---------------------- Barra inferior ----------------------

bottom = tk.Frame(
    janela,
    bg="#111827"
)

bottom.pack(fill="x", padx=15, pady=15)


entrada = tk.Entry(
    bottom,
    font=("Segoe UI", 12),
    bg="#374151",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entrada.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10,
    padx=(0, 10)
)


entrada.bind(
    "<Return>",
    lambda event: enviar_thread()
)


botao = tk.Button(
    bottom,
    text="Enviar ➜",
    command=enviar_thread,
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    font=("Segoe UI", 11, "bold"),
    padx=20,
    pady=8
)

botao.pack(side="right")


janela.mainloop()