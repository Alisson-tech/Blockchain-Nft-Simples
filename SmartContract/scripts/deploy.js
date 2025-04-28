const hre = require("hardhat");

async function main() {
  const ItemNFT = await hre.ethers.getContractFactory("ItemNFT");
  const contract = await ItemNFT.deploy();
  

  console.log(`Contrato implantado em: ${contract.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
