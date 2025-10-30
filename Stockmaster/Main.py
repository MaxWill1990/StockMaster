import json
from pathlib import Path

ARQUIVO = Path("Estoque.json")

def carregar_estoque():
    if not ARQUIVO.exists():
        return []
    with ARQUIVO.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_estoque(estoque):
    with ARQUIVO.open("w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome vazio. Operação cancelada.")
        return
    try:
        preco = float(input("Preço (ex: 12.50): ").strip())
        quantidade = int(input("Quantidade (ex: 10): ").strip())
    except ValueError:
        print("Valor inválido. Use números para preço e quantidade.")
        return
    for p in estoque:
        if p["nome"].lower() == nome.lower():
            p["quantidade"] += quantidade
            p["preco"] = preco
            print("Produto existente atualizado.")
            salvar_estoque(estoque)
            return
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    estoque.append(produto)
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso.")

def listar_produtos(estoque):
    if not estoque:
        print("\nEstoque vazio.\n")
        return
    print("\n=== PRODUTOS NO ESTOQUE ===")
    total_valor = 0.0
    for i, p in enumerate(estoque, start=1):
        valor = p["preco"] * p["quantidade"]
        total_valor += valor
        print(f"{i}. {p['nome']} - R$ {p['preco']:.2f} - Qtde: {p['quantidade']} - Valor Total: R$ {valor:.2f}")
    print(f"Valor total do estoque: R$ {total_valor:.2f}\n")

def atualizar_estoque(estoque):
    listar_produtos(estoque)
    try:
        idx = int(input("Numero do produto para atualizar: ")) - 1
        if not (0 <= idx < len(estoque)):
            print("Índice inválido.")
            return
        nova_qtde = int(input("Nova quantidade (substitui a atual): "))
    except ValueError:
        print("Valor inválido.")
        return
    estoque[idx]["quantidade"] = nova_qtde
    salvar_estoque(estoque)
    print("Quantidade atualizada.")

def remover_produto(estoque):
    listar_produtos(estoque)
    try:
        idx = int(input("Numero do produto para remover: ")) - 1
        if not (0 <= idx < len(estoque)):
            print("Índice inválido.")
            return
    except ValueError:
        print("Valor inválido.")
        return
    produto = estoque.pop(idx)
    salvar_estoque(estoque)
    print(f"Produto '{produto['nome']}' removido.")

def buscar_produtos(estoque):
    termo = input("Buscar por nome: ").strip().lower()
    encontrados = [p for p in estoque if termo in p["nome"].lower()]
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
    print("\n=== RESULTADOS ===")
    for p in encontrados:
        print(f"{p['nome']} - R$ {p['preco']:.2f} - qtde: {p['quantidade']}")

def menu():
    estoque = carregar_estoque()
    while True:
        print("\n=== Estoque Mestre ===")
        print("1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Atualizar quantidade")
        print("4. Remover produto")
        print("5. Buscar produto")
        print("0. Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            listar_produtos(estoque)
        elif opcao == "2":
            adicionar_produto(estoque)
        elif opcao == "3":
            atualizar_estoque(estoque)
        elif opcao == "4":
            remover_produto(estoque)
        elif opcao == "5":
            buscar_produtos(estoque)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def menu():
    estoque = carregar_estoque()
    while True:
        print("\n=== StockMaster ===")
        print("1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Atualizar quantidade")
        print("4. Remover produto")
        print("5. Buscar produto")
        print("0. Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            listar_produtos(estoque)
        elif opcao == "2":
            adicionar_produto(estoque)
        elif opcao == "3":
            atualizar_estoque(estoque)
        elif opcao == "4":
            remover_produto(estoque)
        elif opcao == "5":
            buscar_produtos(estoque)
        elif opcao == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
