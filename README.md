# Insta-Hack Tool

## Features
- Advanced algorithm
- Multi-threaded core
- Secure handshake protocols
- 2FA Bypass

## Installation (Termux)

Follow these steps to install and run the tool on Termux:

1. **Update and Install Basics**
   ```bash
   pkg update && pkg upgrade -y
   pkg install git python -y
   termux-setup-storage
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/sackone-ctv/insta-hack-termux
   cd insta-hack-termux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tool**
   ```bash
   python main.py
   ```

## Usage
Enter the target username when prompted. The tool will attempt to recover the password.
Duration: 5-6 minutes per session.

## Troubleshooting (Termux)
If you encounter errors while installing `pycryptodome` (e.g. "command 'aarch64-linux-android-clang' failed"), run this command to install the necessary compilers:

```bash
pkg install clang libffi
```
Then try running `pip install pycryptodome` again.

<br><br><br><br>
<sub style="color: grey; font-size: 0.8em; opacity: 0.5;">
*Note: This tool is a simulation designed for educational demonstration and does not perform any actual security intrusion.*
</sub>
