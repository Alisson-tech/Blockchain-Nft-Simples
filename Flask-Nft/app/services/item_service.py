from app.Blockchain.item_NFT import ItemNFTContract
from app.models.item_model import Item

fake_db = []

def create_item(data):
    item = Item(
        name=data.get("name"),
        description=data.get("description"),
        initial_price=data.get("initial_price"),
        owner=data.get("owner")
    )
    fake_db.append(item)

    contract = ItemNFTContract()
    tx_hash = contract.mint(item)

    return tx_hash

def get_all_items():
    return [item.to_dict() for item in fake_db]