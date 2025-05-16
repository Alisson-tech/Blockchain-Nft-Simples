# 💠 SmartContract & Flask-Python

Este projeto demonstra a integração entre um **Smart Contract** desenvolvido em **Solidity** e uma **API em Flask**, que interage com a blockchain para criar e gerenciar tokens de item. A blockchain local é executada com **Ganache**, e a comunicação é feita utilizando a biblioteca **Web3.py** no backend e **Hardhat** no ambiente de desenvolvimento.

---

## 🗂 Estrutura do Projeto

O repositório está dividido em duas pastas principais:

- `SmartContract`: Código em Solidity responsável pelo contrato inteligente `ItemToken`.
- `Flask-Python`: API em Flask responsável por interagir com a blockchain e registrar tokens.

---

## 🔧 Requisitos

### Pré-requisitos instalados:

- [Ganache](https://trufflesuite.com/ganache/) (blockchain local)
- [Node.js](https://nodejs.org/)
- [Hardhat](https://hardhat.org/)
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Web3.py](https://web3py.readthedocs.io/)

---

## ⚙️ Instalação

### 1. SmartContract

1. Clone este repositório.
2. Navegue até a pasta `SmartContract`.
3. Instale as dependências do Hardhat:

```bash
npm init -y
npm install --save-dev hardhat
```
4. Compile o contrato com Hardhat:

```bash
npx hardhat compile
```

### 2. Flask-Python

1. Navegue até a pasta Flask-Python.
2. Crie e ative um ambiente virtual Python:
   
```bash
python3 -m venv venv
source venv/bin/activate 
```

3. Instale as dependências do Flask e Web3.py:

```bash
pip install -r requirements.txt
```

## Execução
### 1. Rodando Ganache

1. Abra o **Ganache** e crie uma nova blockchain local.
2. Conecte-se à blockchain local utilizando a URL RPC fornecida (ex: `http://127.0.0.1:7545`).

## Implantando o Contrato

Para implantar o contrato inteligente na blockchain local do Ganache, utilize o Hardhat:

```bash
npx hardhat run scripts/deploy.js --network ganache
```

### 2. Configurando a API Flask

1. Navegue até a pasta Flask-Python.
2. Crie um arquivo de configuração (por exemplo, config.py) para conectar à blockchain local utilizando a URL RPC do Ganache.
3. Execute a API Flask:

```bash
flask run
```
O servidor estará rodando na porta 5000 por padrão.

### 3. Implantando o Contrato
Para implantar o contrato inteligente na blockchain local do Ganache, utilize o Hardhat:

```bash
npx hardhat run scripts/deploy.js --network ganache
```

## Como Funciona

A API Flask oferece um ponto de entrada para cadastrar tokens de itens na blockchain.
A comunicação entre a API e a blockchain ocorre através da biblioteca Web3.py, que interage diretamente com o contrato inteligente.

Com isso, é possível registrar tokens personalizados na blockchain, enviando dados como:

- Nome
- Descrição
- Preço inicial
- Proprietário (endereço Ethereum)

### Requisição para Cadastrar Token
Para cadastrar um token de item, faça uma requisição POST para o endpoint /api/items/ com o corpo da requisição contendo as informações do token:

Exemplo de requisição:

```bash
curl -X POST http://127.0.0.1:5000/api/items/ -H "Content-Type: application/json" -d "{\"name\":\"LucasHouse\",\"description\":\"Escritura da Casa\",\"initial_price\":400000,\"owner\":\"0x35ae815027a2DA0595ad9Ac782583fDCfb2bB100\"}"
```
Explicação da Requisição

- name: Nome do item (exemplo: "LucasHouse").
- description: Descrição do item (exemplo: "Escritura da Casa").
- initial_price: Preço inicial do item (exemplo: 400000).
- owner: Endereço do proprietário do item na blockchain (exemplo: "0x35ae815027a2DA0595ad9Ac782583fDCfb2bB100").

  
Essa requisição faz com que a API Flask interaja com o contrato inteligente e registre o token de item na blockchain.

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Abra um pull request ou issue caso tenha sugestões.

