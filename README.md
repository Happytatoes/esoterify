# Esoterify

A cryptographic composition toolkit for analyzing the security properties of cipher chaining.

## Overview

Esoterify allows users to compose multiple encryption algorithms into custom pipelines and analyze whether chaining ciphers actually improves security. Built to demystify encryption through transparent, step-by-step transformations.

## Features

- **Multiple Cipher Support**: Caesar, AES-256-CFB, ChaCha20, RSA
- **Transparent Operation**: View every transformation step (bytes, hex, encoding)
- **Cipher Composition**: Chain multiple encryptions in custom sequences
- **Key Management**: Built-in key storage and retrieval system
- **Security Analysis**: Benchmark and analyze composition effectiveness

## Supported Ciphers

### Symmetric Encryption
- **Caesar Cipher**: Classical substitution cipher with configurable shift
- **AES-256-CFB**: Industry-standard block cipher in Cipher Feedback mode
- **ChaCha20**: Modern stream cipher, optimized for software

### Asymmetric Encryption
- **RSA-2048**: Public-key encryption (manual implementation)

## Installation

### Prerequisites
- Python 3.10+
- Homebrew (macOS)

### Setup

# Install cryptography library
brew install cryptography

# Clone repository
git clone https://github.com/yourusername/esoterify.git
cd esoterify

# Run
python3 main.py

### Basic Operations
menu:
e - enter a message
v - view current message
r - run a single encryption or decryption
c - run a chain of encryptions or decryptions
k - view stored keys
m - view menu
q - quit program

**Important Limitations:**
- Keys are not persisted between sessions
- No secure key storage (educational tool only)
- RSA implementation is for demonstration, not production use
- Do not use for actual sensitive data

### Cipher Modes

- **AES-CFB**: Cipher Feedback mode, converts block cipher to stream cipher
- **No ECB mode**: ECB is insecure (identical plaintext blocks = identical ciphertext)
- **IV/Nonce requirement**: Ensures same plaintext encrypts differently each time

## Project Structure

esoterify/
├── main.py           # Menu loop and user interface
├── ciphers.py        # Encryption/decryption implementations
├── utils.py          # Helper functions (menus, key viewer)
└── globals.py        # Shared state (message, keys)

## License

MIT License - Educational purposes only. Not for production use.

## Author

Noah Wong
Computer Science @ UT Austin  

## Acknowledgments

- Cryptography primitives via the `cryptography` library

---

**Disclaimer**: This is an educational tool for understanding cryptographic principles. Do not use for protecting actual sensitive data. Use established, audited cryptographic libraries for production applications.