// const { deployProxy } = require('@openzeppelin/truffle-upgrades');

const Token = artifacts.require("Token");
const Account = artifacts.require("Account");
const Implementation = artifacts.require(
  "Implementation"
);

module.exports = function (deployer) {
  deployer
    .deploy(Token, 1)
    .then(function () {
      return deployer.deploy(Account, 5, 1);
    })
    .then(function () {
      return deployer.deploy(
        Implementation,
        Account.address,
        Token.address
      );
    });
};
