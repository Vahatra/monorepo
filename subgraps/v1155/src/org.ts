import { ethereum } from "@graphprotocol/graph-ts";
import {
  GraphOrg,
  GraphOrgStatus,
  GraphOrgTransact,
} from "../generated/Org/Org";
import { Org, Block } from "../generated/schema";

export function handleGraphOrg(event: GraphOrg): void {
  let o = new Org(event.params._org.toHex());
  o._org = event.params._org;
  o._name = event.params._name;
  o._role = event.params._role;
  o._status = event.params._status;

  o.save();
}

export function handleGraphOrgStatus(event: GraphOrgStatus): void {
  let o = Org.load(event.params._org.toHex());
  o._status = event.params._status;

  o.save();
}

export function handleGraphOrgTransact(event: GraphOrgTransact): void {
  let o = Org.load(event.params._org.toHex());
  o._txCount = event.params._txCount;

  o.save();
}

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
