import { ethereum } from "@graphprotocol/graph-ts";
import { GraphTransfer } from "../generated/Contract/Contract";
import { Block, Transfer, Mint, Burn } from "../generated/schema";

export function handleBlock(block: ethereum.Block): void {
  let b = new Block(block.hash.toHex());

  b.hash = block.hash;
  b.parentHash = block.parentHash;
  b.unclesHash = block.unclesHash;
  b.author = block.author;
  b.stateRoot = block.stateRoot;
  b.transactionsRoot = block.transactionsRoot;
  b.receiptsRoot = block.receiptsRoot;
  b.number = block.number;
  b.gasUsed = block.gasUsed;
  b.gasLimit = block.gasLimit;
  b.timestamp = block.timestamp;
  b.difficulty = block.difficulty;
  b.totalDifficulty = block.totalDifficulty;
  b.size = block.size;

  b.save();
}

export function handleGraphTransfer(event: GraphTransfer): void {
  let sender = event.params._sender.toHex();
  let receiver = event.params._receiver.toHex();

  if (sender == "0x0000000000000000000000000000000000000000") {
    let m = new Mint(event.params._id.toHex());

    m._receiver = event.params._receiver;
    m._token = event.params._token;
    m._amount = event.params._value;
    m.timestamp = event.block.timestamp;

    m.save();
  } else if (receiver == "0x0000000000000000000000000000000000000000") {
    let b = new Burn(event.params._id.toHex());

    b._sender = event.params._sender;
    b._token = event.params._token;
    b._amount = event.params._value;
    b.timestamp = event.block.timestamp;

    b.save();
  } else {
    let t = new Transfer(event.params._id.toHex());

    t._sender = event.params._sender;
    t._receiver = event.params._receiver;
    t._token = event.params._token;
    t._amount = event.params._value;
    t.timestamp = event.block.timestamp;

    t.save();
  }
}
