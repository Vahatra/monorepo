# monorepo

A monorepo for blockchain related projects.

## Pinned

[`@vahatra/contracts-token`](/contracts/token) -- **`WIP`**

[`@vahatra/dapp`](/dapp) -- **`WIP`**

Just a bunch of ideas put together, may change to something completly different.

**Main contracts:**

- [`Account.sol`](/contracts/token/contracts/Account.sol)
  - Contract that holds the implementation logic for all account management functionality (addAccount, updateAccountStatus, authorizeOperator, revokeOperator,...).
  - Register, add sub-accounts.
  - Set an account status to Active, Suspended or Blacklisted.
  - Authorize, revoke an operator.
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0xB087A133F176a6B2Ca5e7ed8C0ABE10c9508287c](https://rinkeby.etherscan.io/dapp/0xb087a133f176a6b2ca5e7ed8c0abe10c9508287c#readContract)
- [`Token.sol`](/contracts/token/contracts/Token.sol)
  - Contract that holds the implementation logic for all token management functionality (create, mintFungible, mintNonFungible, send, operatorSend, swap,...).
  - Split-Bit ID/Type similar to `0x's ERC1155 implementation`.
  - Mint Fungible or Non-Fungible tokens with a granularity constraint for Fungible tokens.
  - Introspection on send/burn using the `ERC1820`, similiar to the `ERC777`.
  - Use a third party operator to send/burn tokens.
  - Swap tokens in one transaction using offline signing and on-chain verification (`ERC712`).
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0xC826aF0C93870bDF9B2eed05A8d4888b12E1d4e8](https://rinkeby.etherscan.io/dapp/0xc826af0c93870bdf9b2eed05a8d4888b12e1d4e8#readContract)
- [`Implementation.sol`](/contracts/token/contracts/Implementation.sol)
  - Wrapper arround the `Token` and `Account` contract.
  - ### `RINKEBY` [0xE1bfD8706D9f6d5d2a3249f4B4d75b57bf95D5c7](https://rinkeby.etherscan.io/dapp/0xe1bfd8706d9f6d5d2a3249f4b4d75b57bf95d5c7#writeContract)

**DApp:**

Built with `Django/DRF` and `React`.

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
