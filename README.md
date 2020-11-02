# monorepo

A monorepo for blockchain related projects.

## Pinned

[`@vahatra/contracts-token`](/contracts/token)

**`WIP`**

Just a bunch of ideas put together, may change to something completly different.

**Main contracts:**

- [`Account.sol`](/contracts/token/contracts/Account.sol)
  - Contract that holds the implementation logic for all account management functionality (addAccount, updateAccountStatus, authorizeOperator, revokeOperator,...).
  - Add an account or sub-account.
  - Set an account status to Active, Suspended or Blacklisted.
  - Authorize, revoke an operator.
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0x24AA4FFC6CE2826bC0D1abB4Eb391CfE4be57593](https://rinkeby.etherscan.io/address/0x24aa4ffc6ce2826bc0d1abb4eb391cfe4be57593#readContract)
- [`Token.sol`](/contracts/token/contracts/Token.sol)
  - Contract that holds the implementation logic for all token management functionality (create, mintFungible, mintNonFungible, send, operatorSend, swap,...).
  - Split-Bit ID/Type similar to `0x's ERC1155 implementation`.
  - Mint Fungible or Non-Fungible tokens with a granularity constraint for Fungible tokens.
  - Introspection on send/burn using the `ERC1820`, similiar to the `ERC777`.
  - Use a third party operator to send/burn tokens.
  - Swap tokens in one transaction using offline signing and on-chain verification (`ERC712`).
  - Can only be called by the `Implementation` contract expect for some `public view` functions.
  - ### `RINKEBY` [0x00004908AC9F162640a4875ca4723A8A82c3B500](https://rinkeby.etherscan.io/address/0x00004908ac9f162640a4875ca4723a8a82c3b500#readContract)
- [`Implementation.sol`](/contracts/token/contracts/Implementation.sol)
  - Wrapper arround the `Token` and `Account` contract.
  - ### `RINKEBY` [0x3D3075F680E05F788c38B77f4e8C9737cBB05bE2](https://rinkeby.etherscan.io/address/0x3d3075f680e05f788c38b77f4e8c9737cbb05be2#writeContract)

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
