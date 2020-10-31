# monorepo

A monorepo for blockchain related projects.

### Smart Contracts

| Name                                           | Description                                                                                                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@vahatra/contracts-v20`                       | TODO                                                                                                                                                                |
| `@vahatra/contracts-v721`                      | TODO                                                                                                                                                                |
| [`@vahatra/contracts-v1155`](/contracts/v1155) | A token based on the ERC1155.                                                                                                                                       |
| [`@vahatra/contracts-token`](/contracts/token) | A token based (not compatible) on ERC1155, ERC777. Other features: AccessControl, Pausable, Upgradable, Split-Bit, Token Swap in one transaction (offline signing). |

### Subgraphs for Grapnode

| Name                                           | Description        |
| ---------------------------------------------- | ------------------ |
| `@vahatra/subgraphs-v20`                       | TODO               |
| `@vahatra/subgraphs-v721`                      | TODO               |
| [`@vahatra/subgraphs-v1155`](/subgraphs/v1155) | Subgraph for v1155 |

### DApp

| Name                                 | Description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| [`@vahatra/dapp-token`](/dapp/token) | WIP: DApp for [`@vahatra/contracts-token`](/contracts/token) |

### zk-SNARK

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
