# monorepo

A monorepo for blockchain related projects.

## Pinned

[`@vahatra/contracts-token`](/contracts/token)

**`WIP`**

Just a bunch of ideas put together, may change to something completly different.

**Main contracts:**

- [`Account.sol`](/contracts/token/contracts/Account.sol)
  - Contract that holds the implementation logic for all account management functionality (addAccount, updateAccountStatus, authorizeOperator, revokeOperator,...).
  - Register, add sub-accounts.
  - Set an account status to Active, Suspended or Blacklisted.
  - Authorize, revoke an operator.
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0xAEebA704a11DBB627dFFe14084edb263dAbD9C51](https://rinkeby.etherscan.io/address/0xaeeba704a11dbb627dffe14084edb263dabd9c51#readContract)
- [`Token.sol`](/contracts/token/contracts/Token.sol)
  - Contract that holds the implementation logic for all token management functionality (create, mintFungible, mintNonFungible, send, operatorSend, swap,...).
  - Split-Bit ID/Type similar to `0x's ERC1155 implementation`.
  - Mint Fungible or Non-Fungible tokens with a granularity constraint for Fungible tokens.
  - Introspection on send/burn using the `ERC1820`, similiar to the `ERC777`.
  - Use a third party operator to send/burn tokens.
  - Swap tokens in one transaction using offline signing and on-chain verification (`ERC712`).
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0x1d112108b341F7be0Ef3Df928E70dFD8e80a2493](https://rinkeby.etherscan.io/address/0x1d112108b341f7be0ef3df928e70dfd8e80a2493#readContract)
- [`Implementation.sol`](/contracts/token/contracts/Implementation.sol)
  - Wrapper arround the `Token` and `Account` contract.
  - ### `RINKEBY` [0xe82d666F1A813E7EDce46b7cD8d4f8F89bAdB803](https://rinkeby.etherscan.io/address/0xe82d666f1a813e7edce46b7cd8d4f8f89badb803#writeContract)

**Ideas:**

- zk-SNARK
- GSN

## Smart Contracts

| Name                                           | Description                                               |
| ---------------------------------------------- | --------------------------------------------------------- |
| `@vahatra/contracts-v20`                       | TODO                                                      |
| `@vahatra/contracts-v721`                      | TODO                                                      |
| [`@vahatra/contracts-v1155`](/contracts/v1155) | A token based (not compatible) on the ERC1155.            |
| [`@vahatra/contracts-token`](/contracts/token) | A token inspired by (not compatible) the ERC1155, ERC777. |

## Subgraphs for Grapnode (The Graph)

| Name                                           | Description        |
| ---------------------------------------------- | ------------------ |
| `@vahatra/subgraphs-v20`                       | TODO               |
| `@vahatra/subgraphs-v721`                      | TODO               |
| [`@vahatra/subgraphs-v1155`](/subgraphs/v1155) | Subgraph for v1155 |

## DApp

| Name                                 | Description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| [`@vahatra/dapp-token`](/dapp/token) | WIP: DApp for [`@vahatra/contracts-token`](/contracts/token) |

## zk-SNARK

| Name                                    | Description            |
| --------------------------------------- | ---------------------- |
| [`@vahatra/snark-test`](/zk-snark/test) | Testing circom/snarkjs |

## Usage

Using [`lerna`](https://github.com/lerna/lerna) and [`yarn`](https://yarnpkg.com/getting-started/usage) for dependency management.

```bash
brew install yarn # macOs
choco install yarn # windows
# or
npm install -g yarn
```

```bash
yarn install
```

```bash
lerna bootstrap # installing dependencies
```

```bash
lerna link # linking local dependencies
```
