import customtkinter
from main import tocar_musica


def buscar_musica():
    musica = entrada_musica.get()

    if musica.strip():  # evita campo vazio
        tocar_musica(musica)


def main():
    global entrada_musica

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    janela = customtkinter.CTk()
    janela.geometry("400x250")
    janela.title("Spotify Automation")

    titulo = customtkinter.CTkLabel(
        janela,
        text="Escolha sua música",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=20)

    entrada_musica = customtkinter.CTkEntry(
        janela,
        placeholder_text="Digite o nome da música",
        width=250
    )
    entrada_musica.pack(pady=10)

    botao = customtkinter.CTkButton(
        janela,
        text="Tocar Música",
        command=buscar_musica
    )
    botao.pack(pady=10)

    janela.mainloop()


if __name__ == "__main__":
    main()