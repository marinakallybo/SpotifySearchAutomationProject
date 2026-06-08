import customtkinter
from main import tocar_musica


def buscar_musica():
    musica = entrada_musica.get().strip()

    if musica:
        tocar_musica(musica)


def main():
    global entrada_musica

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    janela = customtkinter.CTk()
    janela.geometry("500x400")
    janela.title("Spotify Automation")
    janela.resizable(False, False)

    frame = customtkinter.CTkFrame(
        janela,
        corner_radius=20
    )
    frame.pack(
        padx=30,
        pady=30,
        fill="both",
        expand=True
    )

    titulo = customtkinter.CTkLabel(
        frame,
        text="🎵 Spotify Search",
        font=("Poppins", 28, "bold")
    )
    titulo.pack(pady=(25, 10))

    subtitulo = customtkinter.CTkLabel(
        frame,
        text="Type the song you want to play",
        font=("Poppins", 14)
    )
    subtitulo.pack(pady=(0, 20))

    entrada_musica = customtkinter.CTkEntry(
        frame,
        placeholder_text="Ex: Marina Sena - Desmitificar",
        width=320,
        height=40,
        corner_radius=12,
        font=("Poppins", 14)
    )
    entrada_musica.pack(pady=10)

    botao = customtkinter.CTkButton(
        frame,
        text="Play Music",
        command=buscar_musica,
        width=180,
        height=40,
        corner_radius=12,
        font=("Poppins", 15, "bold")
    )
    botao.pack(pady=20)

    janela.bind("<Return>", lambda event: buscar_musica())

    janela.mainloop()


if __name__ == "__main__":
    main()