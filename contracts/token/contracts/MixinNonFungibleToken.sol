// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

contract MixinNonFungibleToken {
    /// Use a split bit implementation.
    /// Store the type in the upper 128 bits..
    uint256 internal constant TYPE_MASK = uint256(uint128(~0)) << 128;

    /// ..and the non-fungible index in the lower 128
    uint256 internal constant NF_INDEX_MASK = uint128(~0);

    /// The top bit is a flag to tell if this is a NFI.
    uint256 internal constant TYPE_NF_BIT = 1 << 255;

    /// mapping of nft to owner
    mapping(uint256 => address) internal nfOwners;

    /// @dev Returns true if token is non-fungible
    function isNonFungible(uint256 id) public pure returns (bool) {
        return id & TYPE_NF_BIT == TYPE_NF_BIT;
    }

    /// @dev Returns true if token is fungible
    function isFungible(uint256 id) public pure returns (bool) {
        return id & TYPE_NF_BIT == 0;
    }

    /// @dev Returns index of non-fungible token
    function getNonFungibleIndex(uint256 id) public pure returns (uint256) {
        return id & NF_INDEX_MASK;
    }

    /// @dev Returns base type of non-fungible token
    function getNonFungibleBaseType(uint256 id) public pure returns (uint256) {
        return id & TYPE_MASK;
    }

    /// @dev Returns true if input is base-type of a non-fungible token
    function isNonFungibleBaseType(uint256 id) public pure returns (bool) {
        // A base type has the NF bit but does not have an index.
        return (id & TYPE_NF_BIT == TYPE_NF_BIT) && (id & NF_INDEX_MASK == 0);
    }

    /// @dev Returns true if input is a non-fungible token
    function isNonFungibleItem(uint256 id) public pure returns (bool) {
        // A base type has the NF bit but does has an index.
        return (id & TYPE_NF_BIT == TYPE_NF_BIT) && (id & NF_INDEX_MASK != 0);
    }

    /// @dev returns owner of a non-fungible token
    function ownerOf(uint256 id) public view returns (address) {
        return nfOwners[id];
    }
}
