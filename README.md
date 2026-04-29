# ChatsApp - E2EE for Energy Apps

A modern End-to-End Encryption (E2EE) demonstration tool built for the Energy Sector.

## Features
- **Symmetric Encryption**: Uses the industry-standard Fernet (AES) algorithm via Python's `cryptography` library.
- **SQLite Persistence**: Stores encrypted data locally.
- **Premium UI**: A sleek, dark-mode dashboard with real-time feedback.
- **Key Management**: Dynamic key generation.

## Setup
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Initialize the database (optional, `app.py` does this automatically):
    ```bash
    python init_db.py
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
4.  Open `http://127.0.0.1:5000` in your browser.

## How to use
1.  **Generate a Key**: Click "Generate New Key" and copy the value.
2.  **Encrypt**: Enter a title and your message, paste your key, and Click "Encrypt & Store".
3.  **Stored Messages**: You will see the encrypted ciphertext appear in the right-hand panel.
4.  **Decrypt**: Click on any encrypted message, paste the **original key**, and click "Unlock Access" to reveal the plaintext.
