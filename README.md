# Esoterify

**Esoterify** is an interactive educational tool designed to demystify the world of cryptography. By breaking down complex algorithms into human-readable steps, it allows users to see exactly how their data transforms from plain text into high-level ciphertext.

---

## Features

* **Four Distinct Ciphers:** Supports Caesar, RSA, AES, and ChaCha20.
* **Chain Mode:** Layer multiple encryptions (e.g., Caesar -> AES -> RSA) to see how layers affect data complexity.
* **Step-by-Step Transparency:** Every transformation is printed to the console—see the ASCII values, the Hex bytes, and the Base64 encoding in real-time.
* **Automatic Key Management:** Stored keys are tracked and indexed for easy decryption within the same session.

---

## How to Use

Prerequisites:
Ensure you have the Python cryptography library installed:
pip install cryptography

Running the Program:
1. Launch the application: python main.py
2. Enter a message using the 'e' command.
3. Run a transformation with 'r' or create a Chain with 'c'.
4. Decrypt by following the prompts and selecting the stored key generated during the encryption phase.

---

## Technical Architecture

Esoterify is built with a modular structure for easy expansion:
* main.py: The UI engine and main loop.
* ciphers.py: The mathematical core containing all algorithm logic.
* globals.py: State management for the current message and key store.
* utils.py: Interface helpers and key visualization.

---

## Learn More
For a deep dive into the math behind these ciphers, including the "diminishing returns" of multiple encryption rounds and the RSA prime factor logic, visit:
👉 happytatoes.com/writings/esoterify.html

---
Disclaimer: Esoterify is an educational tool. While it uses industry-standard libraries, it is intended for learning purposes and not for securing high-sensitivity production data.