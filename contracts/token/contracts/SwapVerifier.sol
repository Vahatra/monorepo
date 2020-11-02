// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "./libs/SwapLib.sol";

/// @title Contract for verifying the signature of a token swap transaction.
contract SwapVerifier {
    using SwapLib for SwapLib.Swap;

    /// @dev Mapping of nonces to avoid replays.
    mapping(address => uint256) public signerNonces;

    /// @dev EIP712
    string public constant name = "Vahatra";
    bytes32 public constant SWAP_TYPEHASH = keccak256(
        "Swap(address sender,uint256[] senderTokenIds,uint256[] senderTokenAmounts,uint256[] signerTokenIds,uint256[] signerTokenAmounts)"
    );
    bytes32 public constant EIP712_DOMAIN_TYPEHASH = keccak256(
        "EIP712Domain(string name,uint256 chainId,address verifyingContract)"
    );
    bytes32 public DOMAIN_SEPARATOR = keccak256(
        abi.encode(EIP712_DOMAIN_TYPEHASH, keccak256(bytes(name)), getChainId(), address(this))
    );

    /// @notice Verifies the signature and returns the signer.
    /// @param _swap    Swap data
    /// @param _nonce   Contract state required to match the signature
    /// @param _expiry  Time at which to expire the signature
    /// @param _v       Recovery byte of the signature
    /// @param _r       Half of the ECDSA signature pair
    /// @param _s       Half of the ECDSA signature pair
    function swapVerify(
        SwapLib.Swap memory _swap,
        uint256 _nonce,
        uint256 _expiry,
        uint8 _v,
        bytes32 _r,
        bytes32 _s
    ) public returns (address signer_) {
        signer_ = ecrecover(hashSwap(_swap), _v, _r, _s);
        require(signer_ != address(0), "INVALID_SIGNER");
        require(_nonce == signerNonces[signer_]++, "INVALID_NONCE");
        require(now <= _expiry, "SIGNATURE_EXPIRED");
    }

    function getChainId() internal pure returns (uint256) {
        uint256 chainId;
        assembly {
            chainId := chainid()
        }
        return chainId;
    }

    function hashSwap(SwapLib.Swap memory _swap) private view returns (bytes32) {
        return
            keccak256(
                abi.encodePacked(
                    "\\x19\\x01",
                    DOMAIN_SEPARATOR,
                    keccak256(
                        abi.encode(
                            SWAP_TYPEHASH,
                            _swap.sender,
                            _swap.senderTokenIds,
                            _swap.senderTokenAmounts,
                            _swap.signerTokenIds,
                            _swap.signerTokenAmounts
                        )
                    )
                )
            );
    }
}
