# monorepo

A monorepo for blockchain related projects.

## Pinned

[`@vahatra/contracts-token`](/contracts/token)

`WIP`

A token based (not compatible) on ERC1155, ERC777.

Features:

- AccessControl using `@openzeppelin/contracts/access/AccessControl` .
- Pausable using `@openzeppelin/contracts/utils/Pausable` .
- Upgradable using `@openzeppelin/contracts/proxy/Initializable.sol` .
- Split-Bit ID/Type similar to `0x's ERC1155 implementation` .
- Token Swap in one transaction using offline signing and on-cahin verification.

Ideas:

- zk-SNARK
- GSN

### `RINKEBY` [0x0f8aE7D251BAeD14c60C9E381e55393B608609D1](https://rinkeby.etherscan.io/address/0x0f8ae7d251baed14c60c9e381e55393b608609d1#code)

## Smart Contracts

| Name                                           | Description                                                                                                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@vahatra/contracts-v20`                       | TODO                                                                                                                                                                |
| `@vahatra/contracts-v721`                      | TODO                                                                                                                                                                |
| [`@vahatra/contracts-v1155`](/contracts/v1155) | A token based on the ERC1155.                                                                                                                                       |
| [`@vahatra/contracts-token`](/contracts/token) | A token based (not compatible) on ERC1155, ERC777. Other features: AccessControl, Pausable, Upgradable, Split-Bit, Token Swap in one transaction (offline signing). |

## Subgraphs for Grapnode

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
