const { deployProxy, upgradeProxy } = require('@openzeppelin/truffle-upgrades');
const EIP712 = require('../utils/EIP712.js');
const Token = artifacts.require("Token");

contract("Token contract test", async accounts => {

    const create = async (_creator, _uri, _isNF, _data) => {
        await instance.createTokenType(_uri, _isNF, _data, {
            from: _creator,
        });
    };

    const mintFungible = async (_operator, _to, _id, _amounts, _data, _operatorData) => {
        await instance.mintFungible(_to, _id, _amounts, _data, _operatorData, {
            from: _operator,
        });
    };

    const mintNonFungible = async (_operator, _to, _id, _data, _operatorData) => {
        await instance.mintNonFungible(_to, _id, _data, _operatorData, {
            from: _operator,
        });
    };

    const send = async (_from, _to, _ids, _amounts, _data) => {
        await instance.transfer(_to, _ids, _amounts, _data, {
            from: _from,
        });
    };

    const operatorSend = async (_operator, _from, _to, _ids, _amounts, _data, _operatorData) => {
        await instance.transfer(_from, _to, _ids, _amounts, _data, _operatorData, {
            from: _operator,
        });
    };

    const swap = async (_sender, _swap, _nonce, _expiry, _v, _r, _s, _data) => {
        await instance.swap(_swap, _nonce, _v, _r, _s, _data, {
            from: _sender,
        });
    };

    const burn = async (_from, _ids, _amounts, _data) => {
        await instance.transfer(_to, _ids, _amounts, _data, {
            from: _from,
        });
    };

    const operatorBurn = async (_operator, _from, _ids, _amounts, _data, _operatorData) => {
        await instance.transfer(_from, _to, _ids, _amounts, _data, _operatorData, {
            from: _operator,
        });
    };

    let instance;
    let fungible;
    let nonFungible;

    before(async () => {
        instance = await deployProxy(Token, [1]);
        EIP712_DOMAIN_HASH = await instance.EIP712_DOMAIN_HASH();
    });


    it("NOT IMPLEMENTED", async () => {
        throw 'not implemented';
    });

    it("should create a fungible token", async () => {
        fungible = await create(accounts[0], "api.uri.token", false, "");
        assert.isNotNull(fungible, 'No returned type');
        console.log("Token type created ", fungible);
    });

    it("should create a non-fungible token", async () => {
        nonFungible = await create(accounts[0], "api.uri.token", true, "");
        assert.isNotNull(nonFungible, 'No returned type.');
        console.log("Token type created ", nonFungible);
    });

    it("should mint 10 fungible token", async () => {
        await mintFungible(accounts[0], [accounts[0]], fungible, [10], "", "");
        let balance = await instance.balanceOf.call(accounts[0], fungible);
        assert.equal(balance, 10);
        console.log("10 token type ", fungible, " minted");
    });

    it("should mint a non-fungible token", async () => {
        await mintNonFungible(accounts[0], [accounts[0]], nonFungible, "", "");
        let balance = await instance.balanceOf.call(accounts[0], nonFungible);
        assert.equal(balance, 5);
        console.log("1 token type ", fungible, " minted");
    });

    it("should send 5 fungible tokens", async () => {
        await send(accounts[0], accounts[1], [fungible], [5], "");
        let balance = await instance.balanceOf.call(accounts[0], fungible);
        assert.equal(balance, 5);
    });

    it("should swap 2 fungible tokens for 1 non-fungible token", async () => {
        const name = 'Vahatra';
        const chainId = 5777;
        const domain = { name, chainId, verifyingContract: instance.address };
        const types = {
            Swap: [
                { name: 'sender', type: 'address' },
                { name: 'senderTokenIds', type: 'uint256[]' },
                { name: 'senderTokenAmounts', type: 'uint256[]' },
                { name: 'signerTokenIds', type: 'uint256[]' },
                { name: 'signerTokenAmounts', type: 'uint256[]' }
            ]
        };
        const nonce = 0;
        const expiry = 10e9;
        const swapData = {
            sender: accounts[0],
            senderTokenIds: [fungible],
            senderTokenAmounts: [2],
            signerTokenIds: [nonFungible],
            signerTokenAmounts: [1]
        };
        const { v, r, s } = await EIP712.sign(domain, 'Swap', swapData, types, pk);
        await Swap(accounts[0], swapData, nonce, expiry, v, r, s, "");
        let balance = await instance.balanceOf.call(accounts[0], nonFungible);
        assert.equal(balance, 1);
    });
});