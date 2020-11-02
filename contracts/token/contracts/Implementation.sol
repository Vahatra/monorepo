// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/introspection/IERC1820Registry.sol";
import "./interfaces/ITokenRecipient.sol";
import "./interfaces/ITokenSender.sol";
import "./Initializable.sol";
import "./MixinNF.sol";
import "./SwapVerifier.sol";

/// @title Token contract
/// @notice This contract holds implementation logic for all token management
// contract Token is SwapVerifier, MixinNF, Initializable, Pausable, AccessControl {
contract Token is AccessControl {

}
