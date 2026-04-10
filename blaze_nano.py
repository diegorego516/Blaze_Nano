import nanoleafapi

def main_menu():
    print("1. criar funcionalidades para o editor de texto")
    print("2. adicionar formatação para textos")
    print("3. implementar funcionalidades para variáveis em programação no editor de texto")
    print("4. incrementos de funcionalidades para adicionar novas funcionalidades e funcionar direto do terminal com outras configurações")
    print("5. adicionar correções quentes para resolver erros de programação e segurança no editor de texto/código")

    escolha = input("Escolha qual opção que você quer (1-5): ")
    # em vez de colocar def funções e outras funcionalidades feias e sem sentido
    criar_editor()
    if escolha == "1":
        exit(0)
    elif escolha == "8":
        exit(0)

    int = input("Escolha a opção de (1-5): ")
    def criar_editor():
        print("Criando editor de texto...")

if __name__ == "__main__":
    main_menu()
