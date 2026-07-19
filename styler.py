#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
        ★ CORTEX TERMINAL STYLER — ALL-IN-ONE EDITION ★
   Author/Credit: Sabuj (CortexHost)
   Version: 5.0.0 | Full Termux Customization Suite
===================================================================

A single-file, all-in-one Termux environment customizer.
Covers themes, fonts, prompt, shell, plugins, productivity tools,
backups, and system utilities — no license gate, no network auth.
Plug your own access-control layer in front of main() if you need one.
"""

import os
import sys
import json
import shutil
import hashlib
import platform
import subprocess

# ------------------------------------------------------------------
# CONSTANTS & PATHS
# ------------------------------------------------------------------
GITHUB_RAW_URL = "https://raw.githubusercontent.com/CODEXPRO007/TERMUX-TOOL/main/styler.py"
TELEGRAM_LINK = "https://t.me/codexx01"

HOME = os.path.expanduser("~")
TERMUX_DIR = os.path.join(HOME, ".termux")
BASHRC_PATH = os.path.join(HOME, ".bashrc")
ZSHRC_PATH = os.path.join(HOME, ".zshrc")
TMUX_CONF = os.path.join(HOME, ".tmux.conf")
VIMRC_PATH = os.path.join(HOME, ".vimrc")
BACKUP_DIR = os.path.join(HOME, ".termux_backup")
CONFIG_DIR = os.path.join(HOME, ".cortex_styler")
SETTINGS_FILE = os.path.join(CONFIG_DIR, "settings.json")
ALIASES_FILE = os.path.join(HOME, ".cortex_aliases")

FONT_DIR = TERMUX_DIR
COLOR_FILE = os.path.join(TERMUX_DIR, "colors.properties")
FONT_FILE = os.path.join(TERMUX_DIR, "font.ttf")
BG_FILE = os.path.join(TERMUX_DIR, "background.png")

# ------------------------------------------------------------------
# ANSI COLOR FRAMEWORK
# ------------------------------------------------------------------
COLORS = {
    "CYAN": "\033[1;36m", "PURPLE": "\033[1;35m", "BLUE": "\033[1;34m",
    "GREEN": "\033[1;32m", "RED": "\033[1;31m", "YELLOW": "\033[1;33m",
    "WHITE": "\033[1;37m", "KALI": "\033[38;5;39m", "MATRIX": "\033[38;5;46m",
    "ARCH": "\033[38;5;51m", "BLACKARCH": "\033[38;5;196m", "PARROT": "\033[38;5;121m",
    "RESET": "\033[0m", "BLINK": "\033[5m", "DIM": "\033[2m", "BOLD": "\033[1m",
}

THEMES = {
    "1": {"name": "Kali Linux OffSec", "config": "background = #0f1015\nforeground = #c5cdd8\ncursor = #839edb\ncolor0 = #1d2026\ncolor1 = #f07178\ncolor2 = #c3e88d\ncolor3 = #ffcb6b\ncolor4 = #82aaff\ncolor5 = #c792ea\ncolor6 = #89ddff\ncolor7 = #ffffff\n"},
    "2": {"name": "Cyberpunk Neon", "config": "background = #0d1117\nforeground = #c9d1d9\ncursor = #58a6ff\ncolor0 = #161b22\ncolor1 = #ff7b72\ncolor2 = #7ee787\ncolor3 = #d2a8ff\ncolor4 = #6cb6ff\ncolor5 = #db61a2\ncolor6 = #388bfd\ncolor7 = #ffffff\n"},
    "3": {"name": "Matrix Blood", "config": "background = #050000\nforeground = #ff3333\ncursor = #ff0000\ncolor0 = #100000\ncolor1 = #ff0000\ncolor2 = #00ff00\ncolor3 = #ffff00\ncolor4 = #0000ff\ncolor5 = #ff00ff\ncolor6 = #00ffff\ncolor7 = #ffffff\n"},
    "4": {"name": "Dracula Classic Pro", "config": "background = #282a36\nforeground = #f8f8f2\ncursor = #f8f8f0\ncolor0 = #21222c\ncolor1 = #ff5555\ncolor2 = #50fa7b\ncolor3 = #f1fa8c\ncolor4 = #bd93f9\ncolor5 = #ff79c6\ncolor6 = #8be9fd\ncolor7 = #f8f8f2\n"},
    "5": {"name": "Ghost RGB Custom", "config": "background = #0f0f13\nforeground = #a9b1d6\ncursor = #7aa2f7\ncolor0 = #1d202f\ncolor1 = #f7768e\ncolor2 = #9ece6a\ncolor3 = #e0af68\ncolor4 = #7aa2f7\ncolor5 = #bb9af3\ncolor6 = #7dcfff\ncolor7 = #c0caf5\n"},
    "6": {"name": "Arch Linux Cyber Cyan", "config": "background = #0a0f14\nforeground = #eaeaea\ncursor = #00aaff\ncolor0 = #222222\ncolor1 = #ff5555\ncolor2 = #55ff55\ncolor3 = #ffff55\ncolor4 = #00aaff\ncolor5 = #ff55ff\ncolor6 = #55ffff\ncolor7 = #ffffff\n"},
    "7": {"name": "BlackArch Stealth Tactical", "config": "background = #000000\nforeground = #dcdcdc\ncursor = #ff0000\ncolor0 = #1a1a1a\ncolor1 = #ff1a1a\ncolor2 = #1aff1a\ncolor3 = #ffff1a\ncolor4 = #1a1aff\ncolor5 = #ff1aff\ncolor6 = #1affff\ncolor7 = #ffffff\n"},
    "8": {"name": "Parrot OS Security Core", "config": "background = #0c1013\nforeground = #a0aab3\ncursor = #00e5ff\ncolor0 = #182226\ncolor1 = #ff4365\ncolor2 = #00e5ff\ncolor3 = #ffe600\ncolor4 = #0066ff\ncolor5 = #9b5de5\ncolor6 = #00f5d4\ncolor7 = #ffffff\n"},
    "9": {"name": "Ubuntu Canonical Vanilla", "config": "background = #300a24\nforeground = #ffffff\ncursor = #df4814\ncolor0 = #2c001e\ncolor1 = #f1592a\ncolor2 = #82be00\ncolor3 = #ffce00\ncolor4 = #0087b4\ncolor5 = #b900b4\ncolor6 = #00b4b4\ncolor7 = #ffffff\n"},
    "10": {"name": "Nord Frost", "config": "background = #2e3440\nforeground = #d8dee9\ncursor = #88c0d0\ncolor0 = #3b4252\ncolor1 = #bf616a\ncolor2 = #a3be8c\ncolor3 = #ebcb8b\ncolor4 = #81a1c1\ncolor5 = #b48ead\ncolor6 = #88c0d0\ncolor7 = #e5e9f0\n"},
    "11": {"name": "Solarized Dark", "config": "background = #002b36\nforeground = #839496\ncursor = #93a1a1\ncolor0 = #073642\ncolor1 = #dc322f\ncolor2 = #859900\ncolor3 = #b58900\ncolor4 = #268bd2\ncolor5 = #d33682\ncolor6 = #2aa198\ncolor7 = #eee8d5\n"},
    "12": {"name": "Tokyo Night", "config": "background = #1a1b26\nforeground = #a9b1d6\ncursor = #c0caf5\ncolor0 = #15161e\ncolor1 = #f7768e\ncolor2 = #9ece6a\ncolor3 = #e0af68\ncolor4 = #7aa2f7\ncolor5 = #bb9af3\ncolor6 = #7dcfff\ncolor7 = #a9b1d6\n"},
}

ASCII_ART = f"""{COLORS['KALI']}
  ______________      __________________  ____ ___ ____  ____
 / ___/\\_  __ \\ \\    / /_  __ \\_  __ \\  \\/ /  |  |    \\_   /
/ /__   |  | \\/\\ \\  / / |  | \\/|  | \\/\\   /|  |  |  |  //  /_
\\___ \\  |__|    \\ \\/ /  |__|   |__|    \\_/ |____/|____/ \\____/
{COLORS['MATRIX']}┌────────────────────────────────────────────────────────┐
│           ★ ALL-IN-ONE ECOSYSTEM BY CORTEXHOST ★        │
│         Premium Terminal Customization Suite v5.0       │
└────────────────────────────────────────────────────────┘{COLORS['RESET']}"""


# ------------------------------------------------------------------
# CORE HELPERS
# ------------------------------------------------------------------
def clear():
    os.system("clear")

def pause():
    input(f"\n{COLORS['WHITE']}Press [Enter] to return...{COLORS['RESET']}")

def ensure_dirs():
    for d in (TERMUX_DIR, BACKUP_DIR, CONFIG_DIR):
        os.makedirs(d, exist_ok=True)

def run(cmd, quiet=False):
    """Run a shell command, streaming output unless quiet."""
    stdout = subprocess.DEVNULL if quiet else None
    stderr = subprocess.DEVNULL if quiet else None
    return subprocess.run(cmd, shell=True, stdout=stdout, stderr=stderr)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_settings(data):
    ensure_dirs()
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_device_id():
    """Local-only device fingerprint, used purely for display in About/diagnostics."""
    try:
        if os.path.exists("/proc/sys/kernel/random/boot_id"):
            with open("/proc/sys/kernel/random/boot_id", "r") as f:
                boot_id = f.read().strip()
            return hashlib.sha256(boot_id.encode()).hexdigest()[:16]
    except Exception:
        pass
    fallback = platform.processor() + platform.machine() + platform.node()
    return hashlib.md5(fallback.encode()).hexdigest()[:16]

def backup_file(path, name):
    ensure_dirs()
    dest = os.path.join(BACKUP_DIR, name)
    if os.path.exists(path) and not os.path.exists(dest):
        shutil.copy(path, dest)


# ------------------------------------------------------------------
# 1–3. THEME ENGINE
# ------------------------------------------------------------------
def apply_theme(choice):
    ensure_dirs()
    backup_file(COLOR_FILE, "colors.properties.bak")
    theme_data = THEMES[choice]
    with open(COLOR_FILE, "w") as f:
        f.write(theme_data["config"])
    run("termux-reload-settings", quiet=True)
    print(f"\n{COLORS['MATRIX']}[+] Theme applied: {theme_data['name']}{COLORS['RESET']}")
    pause()

def theme_menu():
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['CYAN']}------- SELECT A THEME -------{COLORS['RESET']}")
    for k, v in THEMES.items():
        print(f"  {COLORS['YELLOW']}[{k.zfill(2)}]{COLORS['WHITE']} {v['name']}{COLORS['RESET']}")
    choice = input(f"\n{COLORS['CYAN']}Enter theme number: {COLORS['RESET']}").strip()
    if choice in THEMES:
        apply_theme(choice)
    else:
        print(f"{COLORS['RED']}[-] Invalid theme number.{COLORS['RESET']}")
        pause()

def create_custom_theme():
    clear()
    print(f"{COLORS['CYAN']}------- CUSTOM THEME BUILDER -------{COLORS['RESET']}")
    print(f"{COLORS['DIM']}Enter hex codes (e.g. #1a1b26). Leave blank for default.{COLORS['RESET']}\n")
    fields = {
        "background": "#0d1117", "foreground": "#c9d1d9", "cursor": "#58a6ff",
        "color0": "#161b22", "color1": "#ff5555", "color2": "#50fa7b",
        "color3": "#f1fa8c", "color4": "#82aaff", "color5": "#c792ea",
        "color6": "#89ddff", "color7": "#ffffff",
    }
    lines = []
    for key, default in fields.items():
        val = input(f"{COLORS['WHITE']}{key} [{default}]: {COLORS['RESET']}").strip() or default
        lines.append(f"{key} = {val}")
    ensure_dirs()
    backup_file(COLOR_FILE, "colors.properties.bak")
    with open(COLOR_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")
    run("termux-reload-settings", quiet=True)
    print(f"\n{COLORS['MATRIX']}[+] Custom theme saved and applied.{COLORS['RESET']}")
    pause()

def preview_color_palette():
    clear()
    print(f"{COLORS['CYAN']}------- ANSI COLOR SWATCH TEST -------{COLORS['RESET']}\n")
    for name, code in COLORS.items():
        if name in ("RESET", "BLINK", "DIM", "BOLD"):
            continue
        print(f"{code}████ {name}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 4–5. FONT & BACKGROUND
# ------------------------------------------------------------------
def install_nerd_font():
    clear()
    print(f"{COLORS['YELLOW']}------- NERD FONT INSTALLER -------{COLORS['RESET']}")
    print("1) FiraCode Nerd Font\n2) Hack Nerd Font\n3) JetBrainsMono Nerd Font\n4) Custom URL")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    urls = {
        "1": "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/FiraCode/Regular/FiraCodeNerdFont-Regular.ttf",
        "2": "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Regular/HackNerdFont-Regular.ttf",
        "3": "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/JetBrainsMono/Ligatures/Regular/JetBrainsMonoNerdFont-Regular.ttf",
    }
    url = urls.get(c) or input(f"{COLORS['WHITE']}Paste font URL: {COLORS['RESET']}").strip()
    if not url:
        print(f"{COLORS['RED']}[-] No URL provided.{COLORS['RESET']}")
        pause()
        return
    ensure_dirs()
    backup_file(FONT_FILE, "font.ttf.bak")
    run(f'curl -L "{url}" -o "{FONT_FILE}"')
    run("termux-reload-settings", quiet=True)
    print(f"\n{COLORS['MATRIX']}[+] Font installed and applied.{COLORS['RESET']}")
    pause()

def set_background_image():
    clear()
    print(f"{COLORS['YELLOW']}------- TERMINAL BACKGROUND IMAGE -------{COLORS['RESET']}")
    url = input(f"{COLORS['WHITE']}Image URL (png/jpg): {COLORS['RESET']}").strip()
    if not url:
        print(f"{COLORS['RED']}[-] No URL provided.{COLORS['RESET']}")
        pause()
        return
    ensure_dirs()
    run(f'curl -L "{url}" -o "{BG_FILE}"')
    run("termux-reload-settings", quiet=True)
    print(f"\n{COLORS['MATRIX']}[+] Background image set.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 6–7. SHELL / PROMPT
# ------------------------------------------------------------------
def enable_autosuggestions():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing zsh + oh-my-zsh + plugins...{COLORS['RESET']}")
    run("pkg install zsh git ncurses-utils -y")
    omz = os.path.join(HOME, ".oh-my-zsh")
    if not os.path.exists(omz):
        run(f'git clone https://github.com/ohmyzsh/ohmyzsh.git "{omz}"')
    sug = os.path.join(omz, "custom/plugins/zsh-autosuggestions")
    high = os.path.join(omz, "custom/plugins/zsh-syntax-highlighting")
    if not os.path.exists(sug):
        run(f'git clone https://github.com/zsh-users/zsh-autosuggestions "{sug}"')
    if not os.path.exists(high):
        run(f'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "{high}"')

    backup_file(ZSHRC_PATH, "zshrc.bak")
    zsh_config = """export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
source $ZSH/oh-my-zsh.sh
[ -f ~/.cortex_aliases ] && source ~/.cortex_aliases
PROMPT='%F{cyan}┌─[%F{white}%n%F{cyan}@%F{green}%m%F{cyan}]─[%F{yellow}%~%F{cyan}]
└─%F{cyan}>>%f '
"""
    with open(ZSHRC_PATH, "w") as f:
        f.write(zsh_config)
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write("\nexec zsh\n")
    print(f"\n{COLORS['MATRIX']}[✓] Zsh, autosuggestions & syntax highlighting configured.{COLORS['RESET']}")
    pause()

def install_powerlevel10k():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing Powerlevel10k...{COLORS['RESET']}")
    run("pkg install zsh git -y")
    p10k = os.path.join(HOME, ".oh-my-zsh/custom/themes/powerlevel10k")
    if not os.path.exists(p10k):
        run(f'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "{p10k}"')
    backup_file(ZSHRC_PATH, "zshrc.bak")
    if os.path.exists(ZSHRC_PATH):
        with open(ZSHRC_PATH, "r") as f:
            content = f.read()
        content = content.replace('ZSH_THEME="agnoster"', 'ZSH_THEME="powerlevel10k/powerlevel10k"')
        with open(ZSHRC_PATH, "w") as f:
            f.write(content)
    print(f"\n{COLORS['MATRIX']}[✓] Powerlevel10k installed. Run `p10k configure` after restart.{COLORS['RESET']}")
    pause()

def customize_host_prompt():
    clear()
    print(f"{COLORS['CYAN']}------- PROMPT CUSTOMIZER -------{COLORS['RESET']}")
    new_user = input(f"{COLORS['WHITE']}Custom Username [Sabuj]: {COLORS['RESET']}").strip() or "Sabuj"
    new_host = input(f"{COLORS['WHITE']}Custom Hostname [Cortex]: {COLORS['RESET']}").strip() or "Cortex"
    ps1_text = (f"export PS1='{COLORS['CYAN']}┌─[{COLORS['WHITE']}{new_user}{COLORS['CYAN']}@"
                f"{COLORS['GREEN']}{new_host}{COLORS['CYAN']}]─[{COLORS['YELLOW']}\\w{COLORS['CYAN']}]\\n"
                f"└─{COLORS['CYAN']}>>{COLORS['RESET']} '")
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(f"\n{ps1_text}\n")
    print(f"\n{COLORS['MATRIX']}[✓] Prompt updated: {new_user}@{new_host}{COLORS['RESET']}")
    pause()

def switch_default_shell():
    clear()
    print(f"{COLORS['CYAN']}------- SWITCH DEFAULT SHELL -------{COLORS['RESET']}")
    print("1) bash\n2) zsh\n3) fish")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    shells = {"1": "bash", "2": "zsh", "3": "fish"}
    shell = shells.get(c)
    if not shell:
        print(f"{COLORS['RED']}[-] Invalid choice.{COLORS['RESET']}")
        pause()
        return
    run(f"pkg install {shell} -y")
    run(f"chsh -s {shell}")
    print(f"\n{COLORS['MATRIX']}[✓] Default shell set to {shell}.{COLORS['RESET']}")
    pause()

def install_fish_shell():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing fish shell...{COLORS['RESET']}")
    run("pkg install fish -y")
    print(f"\n{COLORS['MATRIX']}[✓] Fish installed. Use option to switch default shell.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 8–12. PRODUCTIVITY TOOLS
# ------------------------------------------------------------------
def install_fzf():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing fzf (fuzzy finder)...{COLORS['RESET']}")
    run("pkg install fzf -y")
    snippet = '\n# fzf keybindings\n[ -f /data/data/com.termux/files/usr/share/examples/fzf/key-bindings.bash ] && source /data/data/com.termux/files/usr/share/examples/fzf/key-bindings.bash\n'
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(snippet)
    print(f"\n{COLORS['MATRIX']}[✓] fzf installed with keybindings.{COLORS['RESET']}")
    pause()

def install_zoxide():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing zoxide (smarter cd)...{COLORS['RESET']}")
    run("pkg install zoxide -y")
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write('\neval "$(zoxide init bash)"\n')
    print(f"\n{COLORS['MATRIX']}[✓] zoxide installed. Use `z <dir>` to jump around.{COLORS['RESET']}")
    pause()

def install_eza():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing eza (modern ls)...{COLORS['RESET']}")
    run("pkg install eza -y")
    backup_file(ALIASES_FILE, "cortex_aliases.bak")
    with open(ALIASES_FILE, "a") as f:
        f.write("\nalias ls='eza --icons'\nalias ll='eza -la --icons'\nalias lt='eza --tree --icons'\n")
    print(f"\n{COLORS['MATRIX']}[✓] eza installed with ls/ll/lt aliases.{COLORS['RESET']}")
    pause()

def install_bat():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing bat (better cat)...{COLORS['RESET']}")
    run("pkg install bat -y")
    with open(ALIASES_FILE, "a") as f:
        f.write("\nalias cat='bat --paging=never'\n")
    print(f"\n{COLORS['MATRIX']}[✓] bat installed with cat alias.{COLORS['RESET']}")
    pause()

def install_fastfetch():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing fastfetch (system info)...{COLORS['RESET']}")
    run("pkg install fastfetch -y")
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write("\nfastfetch\n")
    print(f"\n{COLORS['MATRIX']}[✓] fastfetch installed and set to run on login.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 13. ALIAS MANAGER
# ------------------------------------------------------------------
def alias_manager():
    while True:
        clear()
        print(f"{COLORS['CYAN']}------- ALIAS MANAGER -------{COLORS['RESET']}")
        print("1) List aliases\n2) Add alias\n3) Remove alias\n4) Back")
        c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
        if c == "1":
            if os.path.exists(ALIASES_FILE):
                with open(ALIASES_FILE) as f:
                    print(f.read() or "(empty)")
            else:
                print("(no aliases file yet)")
            pause()
        elif c == "2":
            name = input("Alias name: ").strip()
            cmd = input("Command it runs: ").strip()
            if name and cmd:
                with open(ALIASES_FILE, "a") as f:
                    f.write(f"alias {name}='{cmd}'\n")
                print(f"{COLORS['MATRIX']}[+] Alias added.{COLORS['RESET']}")
            pause()
        elif c == "3":
            name = input("Alias name to remove: ").strip()
            if os.path.exists(ALIASES_FILE):
                with open(ALIASES_FILE) as f:
                    lines = [l for l in f if not l.startswith(f"alias {name}=")]
                with open(ALIASES_FILE, "w") as f:
                    f.writelines(lines)
                print(f"{COLORS['MATRIX']}[+] Alias removed (if it existed).{COLORS['RESET']}")
            pause()
        else:
            return


# ------------------------------------------------------------------
# 14–15. MOTD / BANNER
# ------------------------------------------------------------------
def inject_banner():
    banner_text = f"""
clear
echo -e "{COLORS['KALI']}============================================================={COLORS['RESET']}"
echo -e "{COLORS['MATRIX']}       ⚡ TERMINAL SUBSYSTEM — POWERED BY CORTEX ⚡          {COLORS['RESET']}"
echo -e "{COLORS['BLUE']}       Environment designed by Sabuj                         {COLORS['RESET']}"
echo -e "{COLORS['KALI']}============================================================={COLORS['RESET']}"
echo ""
"""
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(banner_text)
    print(f"\n{COLORS['MATRIX']}[+] Startup banner added to .bashrc{COLORS['RESET']}")
    pause()

def toggle_weather_widget():
    clear()
    print(f"{COLORS['CYAN']}------- WEATHER WIDGET ON LOGIN -------{COLORS['RESET']}")
    city = input(f"{COLORS['WHITE']}City name (blank = auto-detect): {COLORS['RESET']}").strip()
    line = f'curl -s "wttr.in/{city}?format=3" 2>/dev/null\n' if city else 'curl -s "wttr.in?format=3" 2>/dev/null\n'
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(line)
    print(f"\n{COLORS['MATRIX']}[+] Weather widget added to login shell.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 16–19. GIT / SSH / DEV TOOLS
# ------------------------------------------------------------------
def git_config_wizard():
    clear()
    print(f"{COLORS['CYAN']}------- GIT CONFIG WIZARD -------{COLORS['RESET']}")
    run("pkg install git -y")
    name = input("Git user.name: ").strip()
    email = input("Git user.email: ").strip()
    if name:
        run(f'git config --global user.name "{name}"')
    if email:
        run(f'git config --global user.email "{email}"')
    run("git config --global init.defaultBranch main")
    run("git config --global alias.st status")
    run("git config --global alias.co checkout")
    run("git config --global alias.br branch")
    run("git config --global alias.cm 'commit -m'")
    print(f"\n{COLORS['MATRIX']}[✓] Git configured with name/email + handy aliases (st/co/br/cm).{COLORS['RESET']}")
    pause()

def generate_ssh_key():
    clear()
    print(f"{COLORS['CYAN']}------- SSH KEY GENERATOR -------{COLORS['RESET']}")
    email = input("Email for key comment: ").strip() or "user@termux"
    run(f'ssh-keygen -t ed25519 -C "{email}" -f {HOME}/.ssh/id_ed25519')
    print(f"\n{COLORS['MATRIX']}[✓] SSH key generated at ~/.ssh/id_ed25519(.pub){COLORS['RESET']}")
    pause()

def install_node():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing Node.js + npm...{COLORS['RESET']}")
    run("pkg install nodejs -y")
    print(f"\n{COLORS['MATRIX']}[✓] Node.js installed.{COLORS['RESET']}")
    pause()

def setup_python_venv():
    clear()
    print(f"{COLORS['YELLOW']}[*] Setting up a Python virtual environment...{COLORS['RESET']}")
    run("pkg install python -y")
    path = input("Venv folder name [venv]: ").strip() or "venv"
    run(f"python3 -m venv {path}")
    print(f"\n{COLORS['MATRIX']}[✓] Venv created at ./{path} — activate with `source {path}/bin/activate`{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 20–22. TMUX / VIM
# ------------------------------------------------------------------
def install_tmux():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing tmux with a clean config...{COLORS['RESET']}")
    run("pkg install tmux -y")
    backup_file(TMUX_CONF, "tmux.conf.bak")
    config = """set -g mouse on
set -g status-bg colour234
set -g status-fg colour137
set -g status-left '#[fg=cyan]#S '
set -g status-right '#[fg=yellow]%H:%M '
setw -g window-status-current-style fg=black,bg=cyan
"""
    with open(TMUX_CONF, "w") as f:
        f.write(config)
    print(f"\n{COLORS['MATRIX']}[✓] tmux installed with mouse support + styled status bar.{COLORS['RESET']}")
    pause()

def install_vim_config():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing vim with a basic sane config...{COLORS['RESET']}")
    run("pkg install vim -y")
    backup_file(VIMRC_PATH, "vimrc.bak")
    config = """syntax on
set number
set relativenumber
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set ignorecase
set smartcase
set incsearch
set hlsearch
colorscheme desert
"""
    with open(VIMRC_PATH, "w") as f:
        f.write(config)
    print(f"\n{COLORS['MATRIX']}[✓] vim configured (line numbers, search, indenting).{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 23–26. SYSTEM UTILITIES
# ------------------------------------------------------------------
def setup_storage():
    clear()
    print(f"{COLORS['YELLOW']}[*] Requesting Termux storage permission...{COLORS['RESET']}")
    run("termux-setup-storage")
    print(f"\n{COLORS['MATRIX']}[✓] Storage access requested — approve the Android prompt.{COLORS['RESET']}")
    pause()

def configure_history():
    clear()
    print(f"{COLORS['CYAN']}------- SHELL HISTORY TUNING -------{COLORS['RESET']}")
    size = input("HISTSIZE [10000]: ").strip() or "10000"
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(f"\nexport HISTSIZE={size}\nexport HISTFILESIZE={size}\nexport HISTCONTROL=ignoredups:erasedups\n")
    print(f"\n{COLORS['MATRIX']}[✓] History size set to {size}, duplicates ignored.{COLORS['RESET']}")
    pause()

def clipboard_tool():
    clear()
    print(f"{COLORS['CYAN']}------- CLIPBOARD TEST -------{COLORS['RESET']}")
    text = input("Text to copy to clipboard: ").strip()
    run(f'termux-clipboard-set "{text}"', quiet=True)
    print(f"\n{COLORS['MATRIX']}[✓] Copied to clipboard (if Termux:API is installed).{COLORS['RESET']}")
    pause()

def notification_test():
    clear()
    print(f"{COLORS['CYAN']}------- NOTIFICATION TEST -------{COLORS['RESET']}")
    run('termux-notification --title "Cortex Styler" --content "Notifications are working!"', quiet=True)
    print(f"\n{COLORS['MATRIX']}[✓] Sent (requires Termux:API installed).{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 27–30. PACKAGE MANAGEMENT
# ------------------------------------------------------------------
def package_shortcuts():
    while True:
        clear()
        print(f"{COLORS['CYAN']}------- PACKAGE MANAGER SHORTCUTS -------{COLORS['RESET']}")
        print("1) Update + Upgrade all\n2) Autoclean cache\n3) List installed packages\n4) Export package list\n5) Import package list\n6) Back")
        c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
        if c == "1":
            run("pkg update && pkg upgrade -y")
        elif c == "2":
            run("pkg autoclean && pkg clean")
        elif c == "3":
            run("pkg list-installed")
        elif c == "4":
            path = os.path.join(HOME, "cortex_packages.txt")
            run(f"pkg list-installed > {path}")
            print(f"{COLORS['MATRIX']}[+] Exported to {path}{COLORS['RESET']}")
        elif c == "5":
            path = input("Path to package list file: ").strip()
            if os.path.exists(path):
                run(f"xargs -a {path} pkg install -y")
        else:
            return
        pause()


# ------------------------------------------------------------------
# 31–33. BACKUP / RESTORE / RESET
# ------------------------------------------------------------------
def backup_all():
    clear()
    print(f"{COLORS['YELLOW']}[*] Creating full dotfiles backup archive...{COLORS['RESET']}")
    ensure_dirs()
    archive = os.path.join(BACKUP_DIR, "cortex_full_backup.tar.gz")
    targets = " ".join(p for p in [TERMUX_DIR, BASHRC_PATH, ZSHRC_PATH, TMUX_CONF, VIMRC_PATH, ALIASES_FILE] if os.path.exists(p))
    if targets:
        run(f'tar -czf "{archive}" {targets} 2>/dev/null')
        print(f"\n{COLORS['MATRIX']}[✓] Backup saved to {archive}{COLORS['RESET']}")
    else:
        print(f"\n{COLORS['RED']}[-] Nothing found to back up yet.{COLORS['RESET']}")
    pause()

def rollback():
    clear()
    if not os.path.exists(BACKUP_DIR):
        print(f"{COLORS['RED']}[-] No backups found.{COLORS['RESET']}")
        pause()
        return
    mapping = {
        os.path.join(BACKUP_DIR, "colors.properties.bak"): COLOR_FILE,
        os.path.join(BACKUP_DIR, "bashrc.bak"): BASHRC_PATH,
        os.path.join(BACKUP_DIR, "zshrc.bak"): ZSHRC_PATH,
        os.path.join(BACKUP_DIR, "tmux.conf.bak"): TMUX_CONF,
        os.path.join(BACKUP_DIR, "vimrc.bak"): VIMRC_PATH,
        os.path.join(BACKUP_DIR, "font.ttf.bak"): FONT_FILE,
        os.path.join(BACKUP_DIR, "cortex_aliases.bak"): ALIASES_FILE,
    }
    restored = 0
    for src, dst in mapping.items():
        if os.path.exists(src):
            shutil.copy(src, dst)
            restored += 1
    run("termux-reload-settings", quiet=True)
    print(f"{COLORS['MATRIX']}[+] Restored {restored} config file(s) from backup.{COLORS['RESET']}")
    pause()

def purge():
    clear()
    confirm = input(f"{COLORS['RED']}This wipes ALL styler configs (theme, prompt, aliases). Type YES to confirm: {COLORS['RESET']}").strip()
    if confirm != "YES":
        print("Cancelled.")
        pause()
        return
    for p in (TERMUX_DIR, BASHRC_PATH, ZSHRC_PATH, ALIASES_FILE, TMUX_CONF, VIMRC_PATH):
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)
        elif os.path.exists(p):
            os.remove(p)
    print(f"\n{COLORS['YELLOW']}[*] All styler configs wiped. System reset to defaults.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 34. SELF-UPDATE
# ------------------------------------------------------------------
def execute_auto_update():
    clear()
    print(f"{COLORS['YELLOW']}[*] Checking for updates on GitHub...{COLORS['RESET']}")
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_RAW_URL, timeout=10) as resp:
            if resp.status == 200:
                data = resp.read().decode("utf-8")
                current_path = os.path.abspath(__file__)
                with open(current_path, "w", encoding="utf-8") as f:
                    f.write(data)
                print(f"{COLORS['MATRIX']}[✓] Updated successfully. Restarting...{COLORS['RESET']}")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print(f"{COLORS['RED']}[-] Update check failed (status {resp.status}).{COLORS['RESET']}")
    except Exception as e:
        print(f"{COLORS['RED']}[-] Update unavailable: {e}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 35. SETTINGS / DIAGNOSTICS / ABOUT
# ------------------------------------------------------------------
def view_current_config():
    clear()
    print(f"{COLORS['CYAN']}------- CURRENT CONFIGURATION -------{COLORS['RESET']}")
    print(f"Colors file : {'present' if os.path.exists(COLOR_FILE) else 'not set'}")
    print(f"Font file   : {'present' if os.path.exists(FONT_FILE) else 'not set'}")
    print(f"Background  : {'present' if os.path.exists(BG_FILE) else 'not set'}")
    print(f".bashrc     : {'present' if os.path.exists(BASHRC_PATH) else 'not set'}")
    print(f".zshrc      : {'present' if os.path.exists(ZSHRC_PATH) else 'not set'}")
    print(f"Aliases     : {'present' if os.path.exists(ALIASES_FILE) else 'not set'}")
    print(f"Backups dir : {BACKUP_DIR if os.path.exists(BACKUP_DIR) else 'none yet'}")
    pause()

def about_screen():
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['WHITE']}Cortex Terminal Styler — All-in-One Edition v5.0.0{COLORS['RESET']}")
    print(f"{COLORS['DIM']}Local device tag: {get_device_id()}{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}Credit: Sabuj (CortexHost){COLORS['RESET']}")
    print(f"{COLORS['CYAN']}Community: {TELEGRAM_LINK}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------------
MENU_ITEMS = [
    ("01", "Theme Picker (12 built-in themes)", theme_menu),
    ("02", "Custom Theme Builder", create_custom_theme),
    ("03", "Preview ANSI Color Palette", preview_color_palette),
    ("04", "Install Nerd Font", install_nerd_font),
    ("05", "Set Terminal Background Image", set_background_image),
    ("06", "Enable Zsh + Autosuggestions + Syntax Highlighting", enable_autosuggestions),
    ("07", "Install Powerlevel10k Theme", install_powerlevel10k),
    ("08", "Customize Username/Hostname Prompt", customize_host_prompt),
    ("09", "Switch Default Shell", switch_default_shell),
    ("10", "Install Fish Shell", install_fish_shell),
    ("11", "Install fzf (fuzzy finder)", install_fzf),
    ("12", "Install zoxide (smarter cd)", install_zoxide),
    ("13", "Install eza (modern ls)", install_eza),
    ("14", "Install bat (better cat)", install_bat),
    ("15", "Install fastfetch (system info)", install_fastfetch),
    ("16", "Alias Manager", alias_manager),
    ("17", "Deploy Startup Banner (.bashrc)", inject_banner),
    ("18", "Add Weather Widget to Login", toggle_weather_widget),
    ("19", "Git Config Wizard", git_config_wizard),
    ("20", "Generate SSH Key", generate_ssh_key),
    ("21", "Install Node.js + npm", install_node),
    ("22", "Setup Python venv", setup_python_venv),
    ("23", "Install tmux + styled config", install_tmux),
    ("24", "Install vim + sane config", install_vim_config),
    ("25", "Setup Storage Access", setup_storage),
    ("26", "Tune Shell History", configure_history),
    ("27", "Clipboard Tool Test", clipboard_tool),
    ("28", "Notification Test", notification_test),
    ("29", "Package Manager Shortcuts", package_shortcuts),
    ("30", "Full Config Backup (tar.gz)", backup_all),
    ("31", "Safe Rollback (Restore Backup)", rollback),
    ("32", "Hard Purge (Reset Everything)", purge),
    ("33", "Check for Online Updates", execute_auto_update),
    ("34", "View Current Configuration", view_current_config),
    ("35", "About / Credits", about_screen),
]

def display_menu():
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['KALI']}┌────────────────────{COLORS['WHITE']} CORE CONTROL DASHBOARD {COLORS['KALI']}────────────────────┐{COLORS['RESET']}")
    for code, label, _ in MENU_ITEMS:
        print(f"  {COLORS['CYAN']}[{code}]{COLORS['WHITE']} {label}{COLORS['RESET']}")
    print(f"  {COLORS['RED']}[00]{COLORS['WHITE']} Exit{COLORS['RESET']}")
    print(f"{COLORS['KALI']}└──────────────────────────────────────────────────────────────┘{COLORS['RESET']}")

def main():
    ensure_dirs()
    actions = {code: fn for code, _, fn in MENU_ITEMS}
    while True:
        display_menu()
        choice = input(f"\n{COLORS['YELLOW']}Select an option [00-35]: {COLORS['RESET']}").strip().zfill(2)
        if choice == "00":
            print(f"{COLORS['BLUE']}[*] Goodbye!{COLORS['RESET']}")
            break
        fn = actions.get(choice)
        if fn:
            try:
                fn()
            except KeyboardInterrupt:
                print(f"\n{COLORS['RED']}[!] Cancelled.{COLORS['RESET']}")
                pause()
            except Exception as e:
                print(f"\n{COLORS['RED']}[!] Error: {e}{COLORS['RESET']}")
                pause()
        else:
            print(f"{COLORS['RED']}[!] Invalid option.{COLORS['RESET']}")
            pause()

if __name__ == "__main__":
    main()
