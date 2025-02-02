import os

# Estrutura do curso "Frontend Web3"
estrutura = {
    "mod1": {
        "nome": "Introdução a Web3",
        "aulas": [
            "Introdução a web3",
            "O que é Criptografia",
            "O que é uma Wallet",
            "O que é um Dapp",
        ],
    },
    "mod2": {
        "nome": "Arquitetura de Dapp",
        "aulas": [
            "Login e connect Wallet",
            "Interação com blockchains (Leituras)",
            "Interação com blockchains (Escrita)",
            "Construindo nosso primeiro Dapp (Configuração | React)",
        ],
    },
    "mod3": {
        "nome": "Ethers.js",
        "aulas": [
            "Connect Wallet",
            "Interagindo com smartcontracts (Read)",
            "Interagindo com smartcontracts (Write)",
            "Capturando Erros e Exceções",
            "Capturando Eventos",
        ],
    },
    "mod4": {
        "nome": "RainbowKit e Wagmi",
        "aulas": [
            "Connect Wallet",
            "Mint de NFTs (depois do login)",
            "Dashboard (visualizar os NFTs)",
        ],
    },
    "mod5": {
        "nome": "NFTs e ERC721",
        "aulas": [
            "O que é IPFS: Usar Helia para se conectar, guardar e recuperar arquivos",
            "O que é indexação de dados: conectar com The Graph",
            "NFT Traits",
            "Integrando tudo: Marketplace de NFT",
        ],
    },
    "mod6": {
        "nome": "Siwe",
        "aulas": [
            "Conceitos de login, autenticação, identificação, autorização, sessão e JWT",
            "Sign-in with Ethereum: Login com frontend + backend",
            "Sign-in with Ethereum: Logout com frontend + backend",
        ],
    },
}

# Criar estrutura de diretórios e arquivos
for mod, dados in estrutura.items():
    modulo_path = os.path.join(os.getcwd(), mod)
    os.makedirs(modulo_path, exist_ok=True)

    for idx, aula in enumerate(dados["aulas"], start=1):
        aula_path = os.path.join(modulo_path, f"aula{idx}")
        os.makedirs(aula_path, exist_ok=True)
        roteiro_path = os.path.join(aula_path, "README.md")

        with open(roteiro_path, "w", encoding="utf-8") as f:
            f.write(f"# {aula}\n\nConteúdo da aula {idx} do módulo {dados['nome']}.")

print("Estrutura de aulas criada com sucesso!")
