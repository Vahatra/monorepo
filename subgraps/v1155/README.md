# @wylog/subgraphs-tracerchain

Subgraph for `@wylog/contracts-tracerchain`

## First setup:

### **Dependencies**

Use `lerna`.

OR

Install graph-cli globaly:

```bash
# Yarn (recommended)
yarn global add @graphprotocol/graph-cli
```

### **Contract**

Compile and migrate `@wylog/contracts-tracerchain/GraphToken.sol` to the running service `node_rpc` of `wylog-backend`:

```bash
truffle compile
truffle migrate
# or Use lerna.

OR

# use RemixIDE
```

### **Subgraph**

Set the deployed smartcontract address in the [subgraph.yaml](../tracerchain/subgraph.yaml) file.

```bash
source:
      address: "__HERE__"
      abi: Contract
```

Then

```bash
yarn codegen # code generation
yarn create-local # subgraph creation
yarn deploy-local # deployement
# or Use lerna.
```
