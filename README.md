# Insta-Hack Tool

## Features
- Advanced algorithm
- Multi-threaded core
- Secure handshake protocols
- 2FA Bypass

## Installation (Termux)

Follow these steps carefully to set up the environment in Termux:

1. **Setup Storage**
   ```bash
   termux-setup-storage
   ```

2. **Install Python and Git**
   ```bash
   pkg install python
   pkg install python-pip
   pkg install git
   ```

3. **Update System**
   ```bash
   pkg update && pkg upgrade
   ```

4. **Install Dependencies**
   ```bash
   pip install colorama
   pip install aiohttp
   pip install art
   pip install pycryptodome
   pip install requests
   ```
   *Alternative: `pip install -r requirements.txt` if you have the file.*

5. **Run the Tool**
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
