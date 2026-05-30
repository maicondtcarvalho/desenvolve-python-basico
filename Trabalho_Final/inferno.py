import csv
import os

ARQUIVO_USUARIOS = "usuarios.txt"
ARQUIVO_PRODUTOS = "produtos.txt"
USUARIO_LOGADO = None


def inicializar_arquivos():
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["admin", "123", "admin"])
            writer.writerow(["cliente", "123", "cliente"])

    if not os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Teclado", "120.0", "10"])
            writer.writerow(["2", "Mouse", "50.0", "15"])
            writer.writerow(["3", "Monitor", "899.0", "5"])


def ler_usuarios():
    usuarios = {}
    with open(ARQUIVO_USUARIOS, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                login, senha, tipo = row
                usuarios[login] = {"senha": senha, "tipo": tipo}
    return usuarios


def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for login, dados in usuarios.items():
            writer.writerow([login, dados["senha"], dados["tipo"]])


def cadastrar_usuario():
    usuarios = ler_usuarios()

    login = input("Login: ")
    senha = input("Senha: ")

    if login in usuarios:
        print("Usuário já existe.")
        return

    tipo = "cliente"
    if USUARIO_LOGADO and USUARIO_LOGADO["tipo"] == "admin":
        tipo_digitado = input("Tipo (admin/cliente): ").lower()
        if tipo_digitado in ["admin", "cliente"]:
            tipo = tipo_digitado

    usuarios[login] = {"senha": senha, "tipo": tipo}
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso.")


def login():
    global USUARIO_LOGADO

    usuarios = ler_usuarios()

    login = input("Login: ")
    senha = input("Senha: ")

    if login in usuarios and usuarios[login]["senha"] == senha:
        USUARIO_LOGADO = {"login": login, "tipo": usuarios[login]["tipo"]}
        print("Login realizado.")
    else:
        print("Login inválido.")


def excluir_usuario():
    usuarios = ler_usuarios()
    login = input("Usuário para excluir: ")

    if login in usuarios:
        del usuarios[login]
        salvar_usuarios(usuarios)
        print("Usuário excluído.")
    else:
        print("Usuário não encontrado.")


def ler_produtos():
    produtos = []
    with open(ARQUIVO_PRODUTOS, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                produtos.append({
                    "codigo": row[0],
                    "nome": row[1],
                    "preco": float(row[2]),
                    "quantidade": int(row[3])
                })
    return produtos


def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for p in produtos:
            writer.writerow([p["codigo"], p["nome"], p["preco"], p["quantidade"]])


def cadastrar_produto():
    produtos = ler_produtos()

    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    produtos.append({
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

    salvar_produtos(produtos)
    print("Produto cadastrado.")


def listar_produtos():
    produtos = ler_produtos()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for p in produtos:
        print(
            f"Código: {p['codigo']} | "
            f"Nome: {p['nome']} | "
            f"Preço: R$ {p['preco']:.2f} | "
            f"Qtd: {p['quantidade']}"
        )


def buscar_produto():
    produtos = ler_produtos()
    nome = input("Nome do produto: ").lower()

    encontrado = False

    for p in produtos:
        if nome in p["nome"].lower():
            print(p)
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")


def atualizar_produto():
    produtos = ler_produtos()
    codigo = input("Código do produto: ")

    for p in produtos:
        if p["codigo"] == codigo:
            p["nome"] = input("Novo nome: ")
            p["preco"] = float(input("Novo preço: "))
            p["quantidade"] = int(input("Nova quantidade: "))
            salvar_produtos(produtos)
            print("Produto atualizado.")
            return

    print("Produto não encontrado.")


def excluir_produto():
    produtos = ler_produtos()
    codigo = input("Código do produto: ")

    novos = [p for p in produtos if p["codigo"] != codigo]

    salvar_produtos(novos)
    print("Produto excluído.")


def ordenar_por_nome():
    produtos = sorted(ler_produtos(), key=lambda x: x["nome"])
    for p in produtos:
        print(p)


def ordenar_por_preco():
    produtos = sorted(ler_produtos(), key=lambda x: x["preco"])
    for p in produtos:
        print(p)


inicializar_arquivos()

while True:
    print("\n1 - Login")
    print("2 - Cadastrar usuário")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        login()

        while USUARIO_LOGADO:
            print("\n--- MENU PRODUTOS ---")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Buscar produto")
            print("4 - Atualizar produto")
            print("5 - Excluir produto")
            print("6 - Ordenar por nome")
            print("7 - Ordenar por preço")

            if USUARIO_LOGADO["tipo"] == "admin":
                print("8 - Excluir usuário")

            print("0 - Logout")

            escolha = input("Escolha: ")

            if escolha == "1":
                cadastrar_produto()
            elif escolha == "2":
                listar_produtos()
            elif escolha == "3":
                buscar_produto()
            elif escolha == "4":
                atualizar_produto()
            elif escolha == "5":
                excluir_produto()
            elif escolha == "6":
                ordenar_por_nome()
            elif escolha == "7":
                ordenar_por_preco()
            elif escolha == "8" and USUARIO_LOGADO["tipo"] == "admin":
                excluir_usuario()
            elif escolha == "0":
                USUARIO_LOGADO = None

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "0":
        break