// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ItemNFT is ERC721 {
    uint256 public nextTokenId;
    mapping(uint256 => string) public tokenURIs;

    address public owner;

    constructor() ERC721("ItemNFT", "ITM") {
        owner = msg.sender; 
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Voce nao tem permissao para criar tokens.");
        _;
    }

    function mintItem(address to, string memory uri) external onlyOwner {
        uint256 tokenId = nextTokenId;
        _mint(to, tokenId);
        tokenURIs[tokenId] = uri;
        nextTokenId++;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        return tokenURIs[tokenId];
    }
}
