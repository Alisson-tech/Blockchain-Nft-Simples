require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.20",
  networks: {
    ganache: {
      url: "http://127.0.0.1:7545",
      accounts: [
        "0x157b3952e66e4c99a9119fa2799acfd241361786da901adac3e47463460f84e3"
      ]
    }
  }
};