# ChatsApp: End-to-End Encryption (E2EE) Demonstration

**ChatsApp** is a multi-role web application designed to demonstrate the principles of End-to-End Encryption within the Energy Sector cloud context. It visualizes how data remains secure even when stored in a central database accessed by an administrator.

---

## 🛡️ Security Architecture

The system uses **Symmetric Encryption** (Fernet/AES-128) via the `cryptography` library.

1.  **Encryption at Source**: Messages are encrypted on the client or server-proxy *before* hitting the database.
2.  **Zero-Knowledge Storage**: The SQLite database only ever sees the base64-encoded ciphertext.
3.  **Key-Dependent Decryption**: Decryption is only possible if the viewer possesses the exact secret key generated for that session.

---

## 🖥️ The Three Interfaces

To properly demonstrate E2EE, the system provides three distinct perspectives:

### 1. User 1 Interface (`/`)
*   **Role**: Sender/Receiver A.
*   **Access**: Open [http://127.0.0.1:5000](http://127.0.0.1:5000).
*   **Feature**: Can send messages and unlock incoming messages using their session key.

### 2. User 2 Interface (`/`)
*   **Role**: Sender/Receiver B.
*   **Access**: Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a separate tab or incognito window.
*   **Feature**: Acts as the other end of the secure channel.

### 3. Admin Interface (`/admin`)
*   **Role**: Database Monitor / Server Admin.
*   **Access**: Open [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin).
*   **Feature**: Monitors the "Source Data". Every message is displayed as **Ciphertext**. This proves that the "Company" or "Cloud Provider" cannot read private communications.

---

## 🛠️ Technology Stack
*   **Backend**: Python 3.12 + Flask
*   **Logic**: `cryptography.fernet` (Symmetric AES)
*   **Database**: SQLite 3 (Persistent)
*   **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism), JavaScript ES6

---

## 🚀 Getting Started

### 1. Installation
Ensure you have Python installed, then run:
```bash
pip install flask cryptography
```

### 2. Execution
Start the secure server:
```bash
python app.py
```

### 3. Demonstration Script (The "Walkthrough")
1.  **Step 1**: Open **two** chat windows (User 1 and User 2) and **one** admin window side-by-side.
2.  **Step 2**: From User 1, send the message: `"Emergency Grid Protocol: Shutdown Substation-4"`.
3.  **Step 3**: Look at the **Admin Monitor**. You will see a string like `gAAAAABm...`. Explain that the grid controller (Admin) knows a message was sent but has **zero access** to the command details.
4.  **Step 4**: Go to **User 2**. Click the 🔓 icon. The message reveals itself. This confirms that only the authorized endpoints hold the decryption keys.

---

## 📁 File Structure
- `app.py`: Main Flask application and API routes.
- `encryption_utils.py`: Core cryptographic logic.
- `templates/`: HTML layouts (Index & Admin).
- `static/`: Premium CSS styles and JS frontend logic.
- `database.db`: The SQLite file containing encrypted records.
