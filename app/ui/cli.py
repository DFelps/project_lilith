class CLI:
    def print_banner(self, name: str) -> None:
        print(f"\n{name} pronta. Digite sua mensagem. Use 'sair' para encerrar.\n")

    def read_input(self) -> str:
        return input("Você: ").strip()

    def show_response(self, text: str) -> None:
        print(f"Lilith: {text}\n")
