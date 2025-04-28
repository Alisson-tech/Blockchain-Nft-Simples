from web3 import Web3
from flask import current_app
from app.models.item_model import Item

class ItemNFTContract:
    def __init__(self):
        # Inicializando a conexão com a blockchain
        self.web3 = Web3(Web3.HTTPProvider(current_app.config['WEB3_PROVIDER']))
        self.contract = self.web3.eth.contract(address=current_app.config['CONTRACT_ADDRESS'],
                                               abi=current_app.config['ABI'])
        self.account = self.web3.eth.account.from_key(current_app.config['PRIVATE_KEY'])

    def mint(self, item: Item):
        to_address = item.owner
        uri = self.create_token_uri(item)

        txn = self.contract.functions.mintItem(to_address, uri).build_transaction({
            'from': self.account.address,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('20', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
        })

        signed_txn = self.web3.eth.account.sign_transaction(txn, private_key=current_app.config['PRIVATE_KEY'])
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return self.web3.to_hex(tx_hash)

    @staticmethod
    def create_token_uri(item: Item):
        return f"ipfs://example/{item.name}/{item.owner}/{item.initial_price}"