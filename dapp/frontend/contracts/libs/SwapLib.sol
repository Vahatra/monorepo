// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

library SwapLib {
    using SwapLib for Swap;

    struct Swap {
        address sender;
        uint256[] senderTokenIds;
        uint256[] senderTokenAmounts;
        uint256[] signerTokenIds;
        uint256[] signerTokenAmounts;
    }
}
