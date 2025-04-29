# SmartContract & Flask-Python

Este projeto implementa um contrato inteligente (Smart Contract) para criar um token de item na blockchain utilizando Solidity, juntamente com uma API em Flask para interagir com o contrato e cadastrar tokens de item na blockchain. A comunicação com a blockchain é feita utilizando a biblioteca Web3.js, e Ganache é usado para rodar uma blockchain local durante o desenvolvimento.

## Estrutura do Projeto

O projeto contém duas pastas principais:

- `SmartContract`: Contém o código em Solidity para a criação do contrato inteligente de itemToken.
- `Flask-Python`: Contém a API em Flask que interage com a blockchain para criar e gerenciar tokens de itens.

## Requisitos

### Pré-requisitos

- Ganache para rodar a blockchain localmente.
- Node.js e Hardhat para compilar e implantar o contrato inteligente.
- Python e Flask para a API.
- Web3.py para a comunicação com a blockchain no Flask.

## Instalação

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

