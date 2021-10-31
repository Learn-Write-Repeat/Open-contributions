require("dotenv").config();
const { ethers } = require("ethers");

const contract = require("../artifacts/contracts/EmotionalShapes.sol/EmotionalShapes.json");
const contractInterface = contract.abi;

// https://docs.ethers.io/v5/api/providers
const provider = ethers.getDefaultProvider("ropsten", {
  alchemy: process.env.DEV_API_URL,
});

// https://docs.ethers.io/v5/api/signer/#Wallet
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

//https://docs.ethers.io/v5/api/contract/contract
const emotionalShapes = new ethers.Contract(
  YOUR_NFT_ADDRESS,
  contractInterface,
  wallet
);

const main = () => {
  emotionalShapes
    .mint(process.env.PUBLIC_KEY)
    .then((transaction) => console.log(transaction))
    .catch((e) => console.log("something went wrong", e));
};

main();