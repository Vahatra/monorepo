// const { deployProxy } = require('@openzeppelin/truffle-upgrades');

const Token = artifacts.require("Token");

// module.exports = async function (deployer) {
//   const instance = await deployProxy(Token, [1], { deployer });
//   console.log('Deployed', instance.address);
// };

module.exports = function (deployer) {
  deployer.deploy(Token, 1);
};