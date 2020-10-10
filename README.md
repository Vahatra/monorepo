# monorepo

A monorepo for smart contracts and subgraphs.

### Smart Contracts

| Name                                          | Description                                     |
| --------------------------------------------- | ----------------------------------------------- |
| `@vahatra/contracts-v20`                      | TODO                                            |
| `@vahatra/contracts-v721`                     | TODO                                            |
| [`@vahatra/contracts-v1155`](/contracts/v115) | An ERC1155 token with a slightly modified event |

### Subgraphs for Grapnode

| Name                                           | Description        |
| ---------------------------------------------- | ------------------ |
| `@vahatra/subgraphs-v20`                       | TODO               |
| `@vahatra/subgraphs-v721`                      | TODO               |
| [`@vahatra/subgraphs-v1155`](/subgraphs/v1155) | Subgraph for v1155 |

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
