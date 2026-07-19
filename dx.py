#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
      ★ CORTEX TERMINAL STYLER ECOSYSTEM & ONLINE AUTH ★
  Author/Credit: Sabuj (CortexHost) & CodexModz
  Version: 4.0.0 | Mega Production Engine & Auto-Update
===================================================================
"""

import os
import sys
import json
import hashlib
import platform
import subprocess
import requests

# CONSTANTS & ENDPOINTS
API_URL = "https://bbx.cortexhost.in/connect"
GAME_IDENTIFIER = "PUBG"  # AUTO-PASS WITH NO USER PROMPT REQUIRED
GITHUB_RAW_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/styler.py"
TELEGRAM_LINK = "https://t.me/codexx01"

# DIRECTORY SPECIFICATIONS
TERMUX_DIR = os.path.expanduser("~/.termux")
BASHRC_PATH = os.path.expanduser("~/.bashrc")
ZSHRC_PATH = os.path.expanduser("~/.zshrc")
BACKUP_DIR = os.path.expanduser("~/.termux_backup")

# MULTI-VARIANCE ANSI COLORS FRAMEWORK
COLORS = {
    "CYAN": "\033[1;36m",
    "PURPLE": "\033[1;35m",
    "BLUE": "\033[1;34m",
    "GREEN": "\033[1;32m",
    "RED": "\033[1;31m",
    "YELLOW": "\033[1;33m",
    "WHITE": "\033[1;37m",
    "KALI": "\033[38;5;39m",
    "MATRIX": "\033[38;5;46m",
    "ARCH": "\033[38;5;51m",
    "BLACKARCH": "\033[38;5;196m",
    "PARROT": "\033[38;5;121m",
    "RESET": "\033[0m",
    "BLINK": "\033[5m"
}

# PRE-COMPILED CORE INTERFACE DESIGN ARRAYS
THEMES = {
    "1": {
        "name": "Kali Linux OffSec (Official Look)",
        "config": "background = #0f1015\nforeground = #c5cdd8\ncursor = #839edb\ncolor0 = #1d2026\ncolor1 = #f07178\ncolor2 = #c3e88d\ncolor3 = #ffcb6b\ncolor4 = #82aaff\ncolor5 = #c792ea\ncolor6 = #89ddff\ncolor7 = #ffffff\n"
    },
    "2": {
        "name": "Cyberpunk Neon (Dark Theme)",
        "config": "background = #0d1117\nforeground = #c9d1d9\ncursor = #58a6ff\ncolor0 = #161b22\ncolor1 = #ff7b72\ncolor2 = #7ee787\ncolor3 = #d2a8ff\ncolor4 = #6cb6ff\ncolor5 = #db61a2\ncolor6 = #388bfd\ncolor7 = #ffffff\n"
    },
    "3": {
        "name": "Matrix Blood (Dark Red)",
        "config": "background = #050000\nforeground = #ff3333\ncursor = #ff0000\ncolor0 = #100000\ncolor1 = #ff0000\ncolor2 = #00ff00\ncolor3 = #ffff00\ncolor4 = #0000ff\ncolor5 = #ff00ff\ncolor6 = #00ffff\ncolor7 = #ffffff\n"
    },
    "4": {
        "name": "Dracula Classic Pro",
        "config": "background = #282a36\nforeground = #f8f8f2\ncursor = #f8f8f0\ncolor0 = #21222c\ncolor1 = #ff5555\ncolor2 = #50fa7b\ncolor3 = #f1fa8c\ncolor4 = #bd93f9\ncolor5 = #ff79c6\ncolor6 = #8be9fd\ncolor7 = #f8f8f2\n"
    },
    "5": {
        "name": "Ghost RGB Custom Edition",
        "config": "background = #0f0f13\nforeground = #a9b1d6\ncursor = #7aa2f7\ncolor0 = #1d202f\ncolor1 = #f7768e\ncolor2 = #9ece6a\ncolor3 = #e0af68\ncolor4 = #7aa2f7\ncolor5 = #bb9af3\ncolor6 = #7dcfff\ncolor7 = #c0caf5\n"
    },
    "6": {
        "name": "Arch Linux Cyber Cyan Node",
        "config": "background = #0a0f14\nforeground = #eaeaea\ncursor = #00aaff\ncolor0 = #222222\ncolor1 = #ff5555\ncolor2 = #55ff55\ncolor3 = #ffff55\ncolor4 = #00aaff\ncolor5 = #ff55ff\ncolor6 = #55ffff\ncolor7 = #ffffff\n"
    },
    "7": {
        "name": "BlackArch Stealth Tactical (Deep Crimson)",
        "config": "background = #000000\nforeground = #dcdcdc\ncursor = #ff0000\ncolor0 = #1a1a1a\ncolor1 = #ff1a1a\ncolor2 = #1aff1a\ncolor3 = #ffff1a\ncolor4 = #1a1aff\ncolor5 = #ff1aff\ncolor6 = #1affff\ncolor7 = #ffffff\n"
    },
    "8": {
        "name": "Parrot OS Security Core Layout",
        "config": "background = #0c1013\nforeground = #a0aab3\ncursor = #00e5ff\ncolor0 = #182226\ncolor1 = #ff4365\ncolor2 = #00e5ff\ncolor3 = #ffe600\ncolor4 = #0066ff\ncolor5 = #9b5de5\ncolor6 = #00f5d4\ncolor7 = #ffffff\n"
    },
    "9": {
        "name": "Ubuntu Canonical Server Vanilla Minimal",
        "config": "background = #300a24\nforeground = #ffffff\ncursor = #df4814\ncolor0 = #2c001e\ncolor1 = #f1592a\ncolor2 = #82be00\ncolor3 = #ffce00\ncolor4 = #0087b4\ncolor5 = #b900b4\ncolor6 = #00b4b4\ncolor7 = #ffffff\n"
    }
}

ASCII_ART = f"""{COLORS['KALI']}
  ______________      __________________  ____ ___ ____  ____ 
 / ___/\_  __ \ \    / /_  __ \_  __ \  \/ /  |  |    \_   / 
/ /__   |  | \/\ \  / / |  | \/|  | \/\   /|  |  |  |  //  /_ 
\___ \  |__|    \ \/ /  |__|   |__|    \_/ |____/|____/ \____/
{COLORS['MATRIX']}┌────────────────────────────────────────────────────────┐
│             ★ ECOSYSTEM BY CORTEXHOST ★                │
│       Premium Terminal Dynamic Security Ecosystem       │
└────────────────────────────────────────────────────────┘{COLORS['RESET']}"""

def get_hwid():
    """Generates a stable unique device identifier from the Termux environment."""
    try:
        if os.path.exists("/proc/sys/kernel/random/boot_id"):
            with open("/proc/sys/kernel/random/boot_id", "r") as f:
                boot_id = f.read().strip()
            return hashlib.sha256(boot_id.encode('utf-8')).hexdigest()[:24]
    except Exception:
        pass
    
    fallback_str = platform.processor() + platform.machine() + platform.node()
    return hashlib.md5(fallback_str.encode('utf-8')).hexdigest()[:24]

def trigger_telegram_redirect():
    """Launches the native browser node or Telegram handler to route to the channel."""
    print(f"{COLORS['PURPLE']}[*] Opening official verification channel node: {TELEGRAM_LINK}{COLORS['RESET']}")
    try:
        # Utilizing explicit termux-open system hooks to launch external applications
        subprocess.run(f"termux-open {TELEGRAM_LINK}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        # Fallback to pure shell command sequence
        os.system(f"am start -a android.intent.action.VIEW -d {TELEGRAM_LINK} > /dev/null 2>&1")

def execute_auto_update():
    """Fetches the latest execution script array from remote server repository."""
    print(f"\n{COLORS['YELLOW']}[*] Checking for online framework repository iterations...{COLORS['RESET']}")
    try:
        response = requests.get(GITHUB_RAW_URL, timeout=10)
        if response.status_code == 200:
            current_script_path = os.path.abspath(__file__)
            # Overwriting active runtime matrix safely
            with open(current_script_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"{COLORS['MATRIX']}[✓] Complete update downloaded successfully. Program environment synchronized.{COLORS['RESET']}")
            print(f"{COLORS['YELLOW']}[*] Relaunching system suite instances...{COLORS['RESET']}")
            os.execv(sys.executable, ['python3'] + sys.argv)
        else:
            print(f"{COLORS['RED']}[-] Update check error: Repository target not found (Status Code: {response.status_code}).{COLORS['RESET']}")
    except Exception as e:
        print(f"{COLORS['RED']}[-] Remote network pipeline unavailable: {e}{COLORS['RESET']}")
    input("\nPress [Enter] to resume standard processing loops...")

def authenticate():
    """Executes auto-mapped verification against the backend routing engine."""
    os.system("clear")
    print(ASCII_ART)
    print(f"\n{COLORS['YELLOW']}[*] Initializing Secure Cyber Authentication Loop...{COLORS['RESET']}")
    
    hwid = get_hwid()
    print(f"{COLORS['KALI']}[+] Hardware Device Signature : {COLORS['MATRIX']}{hwid}{COLORS['RESET']}")
    print(f"{COLORS['KALI']}[+] Target Routing Scope     : {COLORS['WHITE']}{GAME_IDENTIFIER} (Auto-Injected){COLORS['RESET']}\n")
    
    user_key = input(f"{COLORS['CYAN']}🔑 ENTER YOUR LICENSE KEY : {COLORS['RESET']}").strip()
    if not user_key:
        print(f"{COLORS['RED']}[-] License verification string cannot be empty.{COLORS['RESET']}")
        sys.exit(1)
        
    payload = {
        'game': GAME_IDENTIFIER,
        'user_key': user_key,
        'serial': hwid
    }
    
    print(f"\n{COLORS['YELLOW']}[*] Dispatching payloads to Cortex Verification Gateway...{COLORS['RESET']}")
    try:
        response = requests.post(API_URL, data=payload, timeout=15)
        if response.status_code != 200:
            print(f"{COLORS['RED']}[-] Gateway Integrity Exception (HTTP Status: {response.status_code}){COLORS['RESET']}")
            sys.exit(1)
            
        res_data = response.json()
        
        if res_data.get('status') is True:
            auth_payload = res_data.get('data', {})
            credit = auth_payload.get('credit', 'Sabuj Systems')
            modname = auth_payload.get('modname', 'Cortex Mainframe')
            exp_date = auth_payload.get('expired_date', 'Lifetime')
            
            print(f"\n{COLORS['MATRIX']}◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢")
            print(f"  [✓] CRITICAL ACCESS GRANTED SUCCESSFUL")
            print(f"  ⚡ Operator System : {credit}")
            print(f"  ⚡ Mainframe Node  : {modname}")
            print(f"  ⚡ Session Lease   : {exp_date}")
            print(f"◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢{COLORS['RESET']}")
            
            # TRIGGER TELEGRAM POPUP/REDIRECT UPON SUCCESSFUL SYSTEM ACCESS
            trigger_telegram_redirect()
            
            input(f"\n{COLORS['WHITE']}Press [Enter] to boot terminal controller panel...{COLORS['RESET']}")
            return True
        else:
            reason = res_data.get('reason', 'INVALID LICENSE SIGNATURE DEPLOYED')
            print(f"\n{COLORS['RED']}❌ Access Denied: {reason}{COLORS['RESET']}")
            sys.exit(1)
            
    except requests.exceptions.RequestException as e:
        print(f"{COLORS['RED']}[-] Connection Exception: Authentication node unreachable ({e}){COLORS['RESET']}")
        sys.exit(1)
    except ValueError:
        print(f"{COLORS['RED']}[-] Protocol Format Exception: Server returned corrupted data layout.{COLORS['RESET']}")
        sys.exit(1)

def display_menu():
    os.system("clear")
    print(ASCII_ART)
    print(f"\n{COLORS['KALI']}┌────────────────────────{COLORS['WHITE']} CORE CONTROL DASHBOARD {COLORS['KALI']}────────────────────────┐")
    print(f"│  {COLORS['CYAN']}[01]{COLORS['WHITE']} Inject Kali Linux OffSec Theme (Premium UI)                {COLORS['KALI']}│")
    print(f"│  {COLORS['CYAN']}[02]{COLORS['WHITE']} Inject Cyberpunk Neon Visual Array                         {COLORS['KALI']}│")
    print(f"│  {COLORS['CYAN']}[03]{COLORS['WHITE']} Inject Matrix Blood Dark Core                              {COLORS['KALI']}│")
    print(f"│  {COLORS['CYAN']}[04]{COLORS['WHITE']} Inject Dracula Classic Pro Theme                           {COLORS['KALI']}│")
    print(f"│  {COLORS['CYAN']}[05]{COLORS['WHITE']} Inject Ghost RGB Custom Edition Style                      {COLORS['KALI']}│")
    print(f"│  {COLORS['ARCH']}[06]{COLORS['WHITE']} Inject Arch Linux Cyber Cyan Node                          {COLORS['KALI']}│")
    print(f"│  {COLORS['BLACKARCH']}[07]{COLORS['WHITE']} Inject BlackArch Stealth Tactical (Crimson)                 {COLORS['KALI']}│")
    print(f"│  {COLORS['PARROT']}[08]{COLORS['WHITE']} Inject Parrot OS Security Core Theme                        {COLORS['KALI']}│")
    print(f"│  {COLORS['YELLOW']}[09]{COLORS['WHITE']} Inject Ubuntu Canonical Server Vanilla Theme                {COLORS['KALI']}│")
    print(f"│  ----------------------------------------------------------------------  │")
    print(f"│  {COLORS['MATRIX']}[10]{COLORS['WHITE']} Enable Fish-Style Autosuggestions & Advanced Syntax        {COLORS['KALI']}│")
    print(f"│  {COLORS['MATRIX']}[11]{COLORS['WHITE']} Customize Live Terminal Shell Username & Hostname           {COLORS['KALI']}│")
    print(f"│  {COLORS['PURPLE']}[12]{COLORS['WHITE']} Deploy Premium Root Startup Banner (.bashrc)               {COLORS['KALI']}│")
    print(f"│  {COLORS['GREEN']}[13]{COLORS['WHITE']} Safe State Rollback (Restore Saved Configuration)          {COLORS['KALI']}│")
    print(f"│  {COLORS['RED']}[14]{COLORS['WHITE']} Hard Factory Purge (Clean Installs & Reset Native)         {COLORS['KALI']}│")
    print(f"│  {COLORS['BLUE']}[15]{COLORS['BLINK']} Force Synchronize Online Remote Auto-Updates               {COLORS['KALI']}│")
    print(f"│  {COLORS['WHITE']}[16] Exit Terminal Automation Engine                              {COLORS['KALI']}│")
    print(f"└────────────────────────────────────────────────────────────────────────┘{COLORS['RESET']}")

def apply_theme(choice):
    if not os.path.exists(TERMUX_DIR):
        os.makedirs(TERMUX_DIR)
    
    color_file = os.path.join(TERMUX_DIR, "colors.properties")
    if os.path.exists(color_file) and not os.path.exists(os.path.join(BACKUP_DIR, "colors.properties.bak")):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        subprocess.run(f"cp {color_file} {os.path.join(BACKUP_DIR, 'colors.properties.bak')}", shell=True)

    theme_data = THEMES[choice]
    with open(color_file, "w") as f:
        f.write(theme_data['config'])
        
    os.system("termux-reload-settings")
    print(f"\n{COLORS['MATRIX']}[+] Layer deployed successfully: {theme_data['name']}{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def enable_autosuggestions():
    """Installs and structures elite interactive connection shell dependencies."""
    print(f"\n{COLORS['YELLOW']}[*] Downloading terminal interactive syntax highlighting system...{COLORS['RESET']}")
    
    # Installing packages required for terminal text connectivity and code arrow matching
    subprocess.run("pkg install zsh git ncurses-utils -y", shell=True)
    
    oh_my_zsh_path = os.path.expanduser("~/.oh-my-zsh")
    if not os.path.exists(oh_my_zsh_path):
        print(f"{COLORS['BLUE']}[*] Compiling environment base architecture...{COLORS['RESET']}")
        subprocess.run('git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh', shell=True)

    # Injecting connection node scripts for arrow suggestions (Fish-like)
    sug_path = os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
    high_path = os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
    
    if not os.path.exists(sug_path):
        subprocess.run('git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions', shell=True)
    if not os.path.exists(high_path):
        subprocess.run('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting', shell=True)

    # Creating dynamic zsh configuration mapping with syntax arrow structures
    zsh_config = """
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh
# Code connection mapping arrows setup
PROMPT='%F{cyan}┌─[%F{white}%n%F{cyan}@%F{green}%m%F{cyan}]─[%F{yellow}%~%F{cyan}]
└─%F{cyan}>>%f '
"""
    with open(ZSHRC_PATH, "w") as f:
        f.write(zsh_config)

    # Update shell configuration environment execution paths
    with open(BASHRC_PATH, "w") as f:
        f.write("exec zsh\n")

    print(f"\n{COLORS['MATRIX']}[✓] Linux code node tracking arrows & fish autosuggestions configured successfully!{COLORS['RESET']}")
    print(f"{COLORS['YELLOW']}[*] Restart Termux application to experience elite workspace execution.{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def customize_host_prompt():
    """Modifies the target username string values inside the dynamic shell execution state."""
    print(f"\n{COLORS['CYAN']}------- PROMPT CUSTOMIZER INTERFACE -------{COLORS['RESET']}")
    new_user = input(f"{COLORS['WHITE']}Enter New Custom Username [Default: Sabuj]: {COLORS['RESET']}").strip() or "Sabuj"
    new_host = input(f"{COLORS['WHITE']}Enter New Custom Hostname [Default: Cortex]: {COLORS['RESET']}").strip() or "Cortex"

    # Injecting dynamic runtime PS1 parameters into Bash initialization contexts
    ps1_text = f"export PS1='{COLORS['CYAN']}┌─[{COLORS['WHITE']}{new_user}{COLORS['CYAN']}@{COLORS['GREEN']}{new_host}{COLORS['CYAN']}]─[{COLORS['YELLOW']}\\w{COLORS['CYAN']}]\\n└─{COLORS['CYAN']}>>{COLORS['RESET']} '"
    
    if os.path.exists(BASHRC_PATH):
        with open(BASHRC_PATH, "a") as f:
            f.write(f"\n{ps1_text}\n")
            
    print(f"\n{COLORS['MATRIX']}[✓] Shell profile parameters hardcoded: {new_user}@{new_host}{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def inject_banner():
    banner_text = f"""
clear
echo -e "{COLORS['KALI']}============================================================={COLORS['RESET']}"
echo -e "{COLORS['MATRIX']}       ⚡ KALI TERMINAL SUBSYSTEM - POWERED BY CORTEX ⚡     {COLORS['RESET']}"
echo -e "{COLORS['BLUE']}       Mainframe Architecture Designed Globally By Sabuj     {COLORS['RESET']}"
echo -e "{COLORS['KALI']}============================================================={COLORS['RESET']}"
echo -e "{COLORS['GREEN']}[✓] Terminal Security System Status: ACTIVE & ENCRYPTED{COLORS['RESET']}"
echo ""
"""
    if os.path.exists(BASHRC_PATH) and not os.path.exists(os.path.join(BACKUP_DIR, "bashrc.bak")):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        subprocess.run(f"cp {BASHRC_PATH} {os.path.join(BACKUP_DIR, 'bashrc.bak')}", shell=True)

    with open(BASHRC_PATH, "a") as f:
        f.write(banner_text)
        
    print(f"\n{COLORS['MATRIX']}[+] Advanced startup binary hooks added to .bashrc workspace.{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def rollback():
    if not os.path.exists(BACKUP_DIR):
        print(f"\n{COLORS['RED']}[-] Error: No historical state snapshot trees located on local path.{COLORS['RESET']}")
        input("\nPress [Enter] to return...")
        return
        
    bak_colors = os.path.join(BACKUP_DIR, "colors.properties.bak")
    bak_bashrc = os.path.join(BACKUP_DIR, "bashrc.bak")
    
    if os.path.exists(bak_colors):
        subprocess.run(f"cp {bak_colors} {os.path.join(TERMUX_DIR, 'colors.properties')}", shell=True)
    if os.path.exists(bak_bashrc):
        subprocess.run(f"cp {bak_bashrc} {BASHRC_PATH}", shell=True)
        
    os.system("termux-reload-settings")
    print(f"\n{COLORS['MATRIX']}[+] Configuration snapshots restored to system root cleanly.{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def purge():
    if os.path.exists(TERMUX_DIR):
        subprocess.run(f"rm -rf {TERMUX_DIR}", shell=True)
    if os.path.exists(BASHRC_PATH):
        subprocess.run(f"rm -f {BASHRC_PATH}", shell=True)
    if os.path.exists(ZSHRC_PATH):
        subprocess.run(f"rm -f {ZSHRC_PATH}", shell=True)
        
    print(f"\n{COLORS['YELLOW']}[*] Stylers wiped out. System configurations set back to clean defaults.{COLORS['RESET']}")
    input("\nPress [Enter] to return...")

def main():
    if authenticate():
        while True:
            display_menu()
            choice = input(f"{COLORS['YELLOW']}Execute Command Matrix [01-16]: {COLORS['RESET']}").strip()
            if choice in ["1", "01", "2", "02", "3", "03", "4", "04", "5", "05", "6", "06", "7", "07", "8", "08", "9", "09"]:
                # Mapping uniform length variations
                normalized_choice = choice.lstrip('0') if len(choice) > 1 and choice != "00" else choice
                apply_theme(normalized_choice)
            elif choice == "10":
                enable_autosuggestions()
            elif choice == "11":
                customize_host_prompt()
            elif choice == "12":
                inject_banner()
            elif choice == "13":
                rollback()
            elif choice == "14":
                purge()
            elif choice == "15":
                execute_auto_update()
            elif choice == "16":
                print(f"{COLORS['BLUE']}[*] Interface session decoupled. System safe shutdown.{COLORS['RESET']}")
                break
            else:
                print(f"{COLORS['RED']}[!] Array Index Error: Command selection out of bounds.{COLORS['RESET']}")

if __name__ == "__main__":
    main()
