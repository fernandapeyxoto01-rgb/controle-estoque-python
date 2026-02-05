import json
import os

ARQUIVO = "estoque.json"


# 🔹 Carregar estoque do arquivo
def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# 🔹 Salvar estoque no arquivo
def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=2)


# 🔹 Adicionar item
def adicionar_item(estoque):
    item = input("Nome do item: ").strip().lower()
    qtd = input("Quantidade: ").strip()

    if not qtd.isdigit():
        print("Quantidade inválida.")
        return

    qtd = int(qtd)
    estoque[item] = estoque.get(item, 0) + qtd
    salvar_estoque(estoque)

    print(f"{qtd} unidade(s) de '{item}' adicionada(s).")


# 🔹 Remover item
def remover_item(estoque):
    item = input("Nome do item: ").strip().lower()
    qtd = input("Quantidade: ").strip()

    if not qtd.isdigit():
        print("Quantidade inválida.")
        return

    qtd = int(qtd)

    if item not in estoque:
        print("Item não encontrado.")
        return

    estoque[item] -= qtd

    if estoque[item] <= 0:
        del estoque[item]
        print(f"'{item}' removido do estoque.")
    else:
        print(f"{qtd} unidade(s) removida(s) de '{item}'.")

    salvar_estoque(estoque)


# 🔹 Menu principal
def menu():
    estoque = carregar_estoque()

    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Ver estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_item(estoque)

        elif opcao == "2":
            remover_item(estoque)

        elif opcao == "3":
            print("Estoque atual:", estoque)

        elif opcao == "0":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida.")


# 🔹 Executar sistema
menu()
