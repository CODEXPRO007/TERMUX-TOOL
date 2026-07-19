#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
        ★ CORTEX TERMINAL STYLER — ALL-IN-ONE EDITION ★
   Author/Credit: Sabuj (CortexHost)
   Version: 6.0.0 | Full Termux Customization Suite
===================================================================

A single-file, all-in-one Termux environment customizer.
Covers themes, fonts, prompt, shell, plugins, productivity tools,
dev tools, backups, and system utilities.

No license gate, no network authentication, no device-ID gating —
this is a pure local customization tool. If you need to restrict
who runs it, wrap main() with your own check.
"""

import os
import sys
import json
import shutil
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
TERMUX_PROPS = os.path.join(TERMUX_DIR, "termux.properties")

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
    "13": {"name": "Gruvbox Dark", "config": "background = #282828\nforeground = #ebdbb2\ncursor = #fe8019\ncolor0 = #282828\ncolor1 = #cc241d\ncolor2 = #98971a\ncolor3 = #d79921\ncolor4 = #458588\ncolor5 = #b16286\ncolor6 = #689d6a\ncolor7 = #a89984\n"},
    "14": {"name": "Catppuccin Mocha", "config": "background = #1e1e2e\nforeground = #cdd6f4\ncursor = #f5e0dc\ncolor0 = #45475a\ncolor1 = #f38ba8\ncolor2 = #a6e3a1\ncolor3 = #f9e2af\ncolor4 = #89b4fa\ncolor5 = #f5c2e7\ncolor6 = #94e2d5\ncolor7 = #bac2de\n"},
}

ASCII_ART = f"""{COLORS['KALI']}
  ______________      __________________  ____ ___ ____  ____
 / ___/\\_  __ \\ \\    / /_  __ \\_  __ \\  \\/ /  |  |    \\_   /
/ /__   |  | \\/\\ \\  / / |  | \\/|  | \\/\\   /|  |  |  |  //  /_
\\___ \\  |__|    \\ \\/ /  |__|   |__|    \\_/ |____/|____/ \\____/
{COLORS['MATRIX']}┌────────────────────────────────────────────────────────┐
│           ★ ALL-IN-ONE ECOSYSTEM BY CORTEXHOST ★        │
│         Premium Terminal Customization Suite v6.0       │
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
    stdout = subprocess.DEVNULL if quiet else None
    stderr = subprocess.DEVNULL if quiet else None
    return subprocess.run(cmd, shell=True, stdout=stdout, stderr=stderr)

def is_installed(cmd):
    """Check if a command/package binary already exists on PATH."""
    return shutil.which(cmd) is not None

def load_settings():
    ensure_dirs()
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"auto_mode": True, "profile_name": "", "profile_host": ""}

def save_settings(data):
    ensure_dirs()
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def backup_file(path, name):
    ensure_dirs()
    dest = os.path.join(BACKUP_DIR, name)
    if os.path.exists(path) and not os.path.exists(dest):
        shutil.copy(path, dest)

def smart_install(pkg_name, binary_name=None):
    """
    Auto-package system: checks if a tool is already installed.
    - In AUTO mode: skips silently if present, installs if missing.
    - In MANUAL mode: asks the user before (re)installing.
    Returns True if the package is ready to use, False if skipped/failed.
    """
    settings = load_settings()
    auto_mode = settings.get("auto_mode", True)
    check_bin = binary_name or pkg_name

    if is_installed(check_bin):
        if auto_mode:
            print(f"{COLORS['DIM']}[=] {pkg_name} already installed — skipping.{COLORS['RESET']}")
            return True
        else:
            choice = input(f"{COLORS['YELLOW']}{pkg_name} is already installed. Reinstall? (y/N): {COLORS['RESET']}").strip().lower()
            if choice != "y":
                return True

    print(f"{COLORS['YELLOW']}[*] Installing {pkg_name}...{COLORS['RESET']}")
    result = run(f"pkg install {pkg_name} -y")
    ok = is_installed(check_bin)
    if ok:
        print(f"{COLORS['MATRIX']}[✓] {pkg_name} ready.{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}[-] {pkg_name} install may have failed — check output above.{COLORS['RESET']}")
    return ok

def toggle_auto_mode():
    clear()
    settings = load_settings()
    current = settings.get("auto_mode", True)
    print(f"{COLORS['CYAN']}------- AUTO-INSTALL MODE -------{COLORS['RESET']}")
    print(f"Current mode: {COLORS['MATRIX'] if current else COLORS['YELLOW']}{'AUTO (skip if installed)' if current else 'MANUAL (ask every time)'}{COLORS['RESET']}")
    print("1) Auto  2) Manual")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    if c == "1":
        settings["auto_mode"] = True
    elif c == "2":
        settings["auto_mode"] = False
    save_settings(settings)
    print(f"{COLORS['MATRIX']}[+] Mode saved.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 1–4. THEME ENGINE
# ------------------------------------------------------------------
def apply_theme_by_key(choice):
    ensure_dirs()
    backup_file(COLOR_FILE, "colors.properties.bak")
    theme_data = THEMES[choice]
    with open(COLOR_FILE, "w") as f:
        f.write(theme_data["config"])
    run("termux-reload-settings", quiet=True)
    return theme_data["name"]

def theme_menu():
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['CYAN']}------- SELECT A THEME -------{COLORS['RESET']}")
    for k, v in THEMES.items():
        print(f"  {COLORS['YELLOW']}[{k.zfill(2)}]{COLORS['WHITE']} {v['name']}{COLORS['RESET']}")
    choice = input(f"\n{COLORS['CYAN']}Enter theme number: {COLORS['RESET']}").strip()
    if choice in THEMES:
        name = apply_theme_by_key(choice)
        print(f"\n{COLORS['MATRIX']}[+] Theme applied: {name}{COLORS['RESET']}")
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

def randomize_theme():
    import random
    clear()
    key = random.choice(list(THEMES.keys()))
    name = apply_theme_by_key(key)
    print(f"{COLORS['MATRIX']}[+] Random theme applied: {name}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 5–7. FONT & BACKGROUND
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
        return False
    ensure_dirs()
    backup_file(FONT_FILE, "font.ttf.bak")
    run(f'curl -fL "{url}" -o "{FONT_FILE}"')
    ok = os.path.exists(FONT_FILE) and os.path.getsize(FONT_FILE) > 1000
    if ok:
        run("termux-reload-settings", quiet=True)
        print(f"\n{COLORS['MATRIX']}[+] Font installed and applied.{COLORS['RESET']}")
    else:
        print(f"\n{COLORS['RED']}[-] Download failed or file too small — check the URL.{COLORS['RESET']}")
    pause()
    return ok

def set_background_image():
    """
    IMPORTANT: The stock Termux app renders a plain terminal — it does not
    support picture/image backgrounds inside colors.properties or any other
    config file. That's almost certainly why it "wasn't working" before —
    it isn't a bug in this tool, it's a Termux limitation.

    What actually works:
      - Solid/gradient-style backgrounds via theme colors (use Theme Picker).
      - True image wallpapers need Termux:Styling (font/color picker only,
        no images either) or a separate terminal emulator that supports
        it, or running a GUI (Termux:X11 / VNC) where you set an Android
        wallpaper behind a transparent terminal window.
    This function is kept as a placeholder that explains that clearly and
    still saves the file for tools/forks that do read background.png.
    """
    clear()
    print(f"{COLORS['YELLOW']}------- TERMINAL BACKGROUND IMAGE -------{COLORS['RESET']}")
    print(f"{COLORS['DIM']}Note: stock Termux does not render image backgrounds in the")
    print(f"terminal itself — only solid theme colors (see Theme Picker).")
    print(f"This will still save the file to ~/.termux/background.png in case")
    print(f"you're using a fork/emulator that supports it.{COLORS['RESET']}\n")
    url = input(f"{COLORS['WHITE']}Image URL (png/jpg), blank to skip: {COLORS['RESET']}").strip()
    if not url:
        print(f"{COLORS['YELLOW']}[*] Skipped.{COLORS['RESET']}")
        pause()
        return
    ensure_dirs()
    run(f'curl -fL "{url}" -o "{BG_FILE}"')
    ok = os.path.exists(BG_FILE) and os.path.getsize(BG_FILE) > 1000
    run("termux-reload-settings", quiet=True)
    if ok:
        print(f"\n{COLORS['MATRIX']}[+] Image saved to ~/.termux/background.png{COLORS['RESET']}")
    else:
        print(f"\n{COLORS['RED']}[-] Download failed — check the URL and your connection.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 8. GUIDED FULL SETUP WIZARD
# ------------------------------------------------------------------
def full_setup_wizard():
    """
    Step-by-step: pick a theme -> set your name/host -> optionally set a
    background image -> optionally add a startup banner -> apply everything
    together in one go, then show a summary.
    """
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['CYAN']}========== GUIDED FULL SETUP WIZARD =========={COLORS['RESET']}")
    print(f"{COLORS['DIM']}This walks through every core setting once, then applies it all.{COLORS['RESET']}\n")

    # Step 1: theme
    print(f"{COLORS['WHITE']}Step 1/4 — Theme{COLORS['RESET']}")
    for k, v in THEMES.items():
        print(f"  [{k.zfill(2)}] {v['name']}")
    theme_choice = input(f"{COLORS['CYAN']}Pick a theme number [1]: {COLORS['RESET']}").strip() or "1"
    if theme_choice not in THEMES:
        theme_choice = "1"

    # Step 2: name/host
    print(f"\n{COLORS['WHITE']}Step 2/4 — Prompt identity{COLORS['RESET']}")
    settings = load_settings()
    default_name = settings.get("profile_name") or "Sabuj"
    default_host = settings.get("profile_host") or "Cortex"
    name = input(f"{COLORS['CYAN']}Username [{default_name}]: {COLORS['RESET']}").strip() or default_name
    host = input(f"{COLORS['CYAN']}Hostname [{default_host}]: {COLORS['RESET']}").strip() or default_host

    # Step 3: background
    print(f"\n{COLORS['WHITE']}Step 3/4 — Background image (optional){COLORS['RESET']}")
    print(f"{COLORS['DIM']}Stock Termux won't render this in-terminal, but it'll be saved for forks that do.{COLORS['RESET']}")
    bg_url = input(f"{COLORS['CYAN']}Image URL (blank to skip): {COLORS['RESET']}").strip()

    # Step 4: banner
    print(f"\n{COLORS['WHITE']}Step 4/4 — Startup banner{COLORS['RESET']}")
    want_banner = input(f"{COLORS['CYAN']}Add a startup banner to .bashrc? (y/N): {COLORS['RESET']}").strip().lower() == "y"

    # Apply everything
    print(f"\n{COLORS['YELLOW']}[*] Applying your full setup...{COLORS['RESET']}")
    theme_name = apply_theme_by_key(theme_choice)
    print(f"{COLORS['MATRIX']}  [✓] Theme: {theme_name}{COLORS['RESET']}")

    ps1_text = (f"export PS1='{COLORS['CYAN']}┌─[{COLORS['WHITE']}{name}{COLORS['CYAN']}@"
                f"{COLORS['GREEN']}{host}{COLORS['CYAN']}]─[{COLORS['YELLOW']}\\w{COLORS['CYAN']}]\\n"
                f"└─{COLORS['CYAN']}>>{COLORS['RESET']} '")
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(f"\n{ps1_text}\n")
    print(f"{COLORS['MATRIX']}  [✓] Prompt: {name}@{host}{COLORS['RESET']}")

    settings["profile_name"] = name
    settings["profile_host"] = host
    save_settings(settings)

    if bg_url:
        ensure_dirs()
        run(f'curl -fL "{bg_url}" -o "{BG_FILE}"')
        if os.path.exists(BG_FILE) and os.path.getsize(BG_FILE) > 1000:
            print(f"{COLORS['MATRIX']}  [✓] Background image saved.{COLORS['RESET']}")
        else:
            print(f"{COLORS['RED']}  [-] Background download failed.{COLORS['RESET']}")

    if want_banner:
        inject_banner(silent=True)
        print(f"{COLORS['MATRIX']}  [✓] Startup banner added.{COLORS['RESET']}")

    run("termux-reload-settings", quiet=True)
    print(f"\n{COLORS['MATRIX']}========== SETUP COMPLETE =========={COLORS['RESET']}")
    print(f"{COLORS['DIM']}Restart Termux (or run `source ~/.bashrc`) to see everything.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 9–13. SHELL / PROMPT
# ------------------------------------------------------------------
def enable_autosuggestions():
    clear()
    print(f"{COLORS['YELLOW']}[*] Setting up zsh + oh-my-zsh + plugins...{COLORS['RESET']}")
    smart_install("zsh")
    smart_install("git")
    smart_install("ncurses-utils")
    omz = os.path.join(HOME, ".oh-my-zsh")
    if not os.path.exists(omz):
        run(f'git clone https://github.com/ohmyzsh/ohmyzsh.git "{omz}"')
    else:
        print(f"{COLORS['DIM']}[=] oh-my-zsh already present — skipping clone.{COLORS['RESET']}")
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
    smart_install("zsh")
    smart_install("git")
    p10k = os.path.join(HOME, ".oh-my-zsh/custom/themes/powerlevel10k")
    if not os.path.exists(p10k):
        run(f'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "{p10k}"')
    else:
        print(f"{COLORS['DIM']}[=] Powerlevel10k already cloned.{COLORS['RESET']}")
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
    settings = load_settings()
    new_user = input(f"{COLORS['WHITE']}Custom Username [{settings.get('profile_name') or 'Sabuj'}]: {COLORS['RESET']}").strip() or settings.get("profile_name") or "Sabuj"
    new_host = input(f"{COLORS['WHITE']}Custom Hostname [{settings.get('profile_host') or 'Cortex'}]: {COLORS['RESET']}").strip() or settings.get("profile_host") or "Cortex"
    ps1_text = (f"export PS1='{COLORS['CYAN']}┌─[{COLORS['WHITE']}{new_user}{COLORS['CYAN']}@"
                f"{COLORS['GREEN']}{new_host}{COLORS['CYAN']}]─[{COLORS['YELLOW']}\\w{COLORS['CYAN']}]\\n"
                f"└─{COLORS['CYAN']}>>{COLORS['RESET']} '")
    backup_file(BASHRC_PATH, "bashrc.bak")
    with open(BASHRC_PATH, "a") as f:
        f.write(f"\n{ps1_text}\n")
    settings["profile_name"] = new_user
    settings["profile_host"] = new_host
    save_settings(settings)
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
    smart_install(shell)
    run(f"chsh -s {shell}")
    print(f"\n{COLORS['MATRIX']}[✓] Default shell set to {shell}.{COLORS['RESET']}")
    pause()

def install_fish_shell():
    clear()
    smart_install("fish")
    print(f"\n{COLORS['MATRIX']}[✓] Fish ready. Use 'Switch Default Shell' to make it default.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 14–22. PRODUCTIVITY TOOLS (auto-package aware)
# ------------------------------------------------------------------
def install_fzf():
    clear()
    if smart_install("fzf"):
        snippet = '\n# fzf keybindings\n[ -f /data/data/com.termux/files/usr/share/examples/fzf/key-bindings.bash ] && source /data/data/com.termux/files/usr/share/examples/fzf/key-bindings.bash\n'
        backup_file(BASHRC_PATH, "bashrc.bak")
        with open(BASHRC_PATH, "a") as f:
            f.write(snippet)
        print(f"{COLORS['MATRIX']}[✓] fzf ready with keybindings.{COLORS['RESET']}")
    pause()

def install_zoxide():
    clear()
    if smart_install("zoxide"):
        backup_file(BASHRC_PATH, "bashrc.bak")
        with open(BASHRC_PATH, "a") as f:
            f.write('\neval "$(zoxide init bash)"\n')
        print(f"{COLORS['MATRIX']}[✓] zoxide ready — use `z <dir>` to jump around.{COLORS['RESET']}")
    pause()

def install_eza():
    clear()
    if smart_install("eza"):
        backup_file(ALIASES_FILE, "cortex_aliases.bak")
        with open(ALIASES_FILE, "a") as f:
            f.write("\nalias ls='eza --icons'\nalias ll='eza -la --icons'\nalias lt='eza --tree --icons'\n")
        print(f"{COLORS['MATRIX']}[✓] eza ready with ls/ll/lt aliases.{COLORS['RESET']}")
    pause()

def install_bat():
    clear()
    if smart_install("bat"):
        with open(ALIASES_FILE, "a") as f:
            f.write("\nalias cat='bat --paging=never'\n")
        print(f"{COLORS['MATRIX']}[✓] bat ready with cat alias.{COLORS['RESET']}")
    pause()

def install_fastfetch():
    clear()
    if smart_install("fastfetch"):
        backup_file(BASHRC_PATH, "bashrc.bak")
        with open(BASHRC_PATH, "a") as f:
            f.write("\nfastfetch\n")
        print(f"{COLORS['MATRIX']}[✓] fastfetch set to run on login.{COLORS['RESET']}")
    pause()

def install_ripgrep():
    clear()
    smart_install("ripgrep", binary_name="rg")
    print(f"{COLORS['MATRIX']}[✓] ripgrep ready — use `rg <pattern>`.{COLORS['RESET']}")
    pause()

def install_fd():
    clear()
    smart_install("fd", binary_name="fd")
    print(f"{COLORS['MATRIX']}[✓] fd ready — use `fd <name>`.{COLORS['RESET']}")
    pause()

def install_htop():
    clear()
    smart_install("htop")
    print(f"{COLORS['MATRIX']}[✓] htop ready — run `htop` for a live process view.{COLORS['RESET']}")
    pause()

def install_tree():
    clear()
    smart_install("tree")
    print(f"{COLORS['MATRIX']}[✓] tree ready — run `tree` to view folder structure.{COLORS['RESET']}")
    pause()

def install_ncdu():
    clear()
    smart_install("ncdu")
    print(f"{COLORS['MATRIX']}[✓] ncdu ready — run `ncdu` for interactive disk usage.{COLORS['RESET']}")
    pause()

def install_lazygit():
    clear()
    smart_install("lazygit")
    print(f"{COLORS['MATRIX']}[✓] lazygit ready — run `lazygit` inside a repo.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 25. ALIAS MANAGER
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
# 26–27. MOTD / BANNER / WEATHER
# ------------------------------------------------------------------
def inject_banner(silent=False):
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
    if not silent:
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

def set_motd():
    clear()
    print(f"{COLORS['CYAN']}------- CUSTOM MOTD (MESSAGE OF THE DAY) -------{COLORS['RESET']}")
    text = input(f"{COLORS['WHITE']}One-line MOTD text: {COLORS['RESET']}").strip()
    if not text:
        print(f"{COLORS['RED']}[-] Nothing entered.{COLORS['RESET']}")
        pause()
        return
    motd_path = os.path.join(os.path.dirname(shutil.which("bash") or "/data/data/com.termux/files/usr/bin/bash"), "..", "etc", "motd")
    motd_path = os.path.normpath(motd_path)
    try:
        with open(motd_path, "w") as f:
            f.write(text + "\n")
        print(f"{COLORS['MATRIX']}[+] MOTD updated at {motd_path}{COLORS['RESET']}")
    except Exception as e:
        print(f"{COLORS['RED']}[-] Could not write MOTD: {e}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 28–31. GIT / SSH / DEV TOOLS
# ------------------------------------------------------------------
def git_config_wizard():
    clear()
    print(f"{COLORS['CYAN']}------- GIT CONFIG WIZARD -------{COLORS['RESET']}")
    smart_install("git")
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
    smart_install("nodejs", binary_name="node")
    print(f"{COLORS['MATRIX']}[✓] Node.js ready.{COLORS['RESET']}")
    pause()

def setup_python_venv():
    clear()
    print(f"{COLORS['YELLOW']}[*] Setting up a Python virtual environment...{COLORS['RESET']}")
    smart_install("python")
    path = input("Venv folder name [venv]: ").strip() or "venv"
    run(f"python3 -m venv {path}")
    print(f"\n{COLORS['MATRIX']}[✓] Venv created at ./{path} — activate with `source {path}/bin/activate`{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 32–33. TMUX / VIM
# ------------------------------------------------------------------
def install_tmux():
    clear()
    if smart_install("tmux"):
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
        print(f"{COLORS['MATRIX']}[✓] tmux ready with mouse support + styled status bar.{COLORS['RESET']}")
    pause()

def install_vim_config():
    clear()
    if smart_install("vim"):
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
        print(f"{COLORS['MATRIX']}[✓] vim configured (line numbers, search, indenting).{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 34–38. TERMUX.PROPERTIES CUSTOMIZATION
# ------------------------------------------------------------------
def _read_props():
    if os.path.exists(TERMUX_PROPS):
        with open(TERMUX_PROPS) as f:
            return f.read()
    return ""

def _write_prop(key, value):
    ensure_dirs()
    backup_file(TERMUX_PROPS, "termux.properties.bak")
    content = _read_props()
    lines = [l for l in content.splitlines() if not l.strip().startswith(key)]
    lines.append(f"{key} = {value}")
    with open(TERMUX_PROPS, "w") as f:
        f.write("\n".join(lines) + "\n")
    run("termux-reload-settings", quiet=True)

def customize_extra_keys():
    clear()
    print(f"{COLORS['CYAN']}------- EXTRA KEYS ROW CUSTOMIZER -------{COLORS['RESET']}")
    print("1) Coding row (ESC TAB CTRL ALT - / | HOME UP END)")
    print("2) Minimal row (ESC / - HOME UP END DOWN)")
    print("3) Custom (type your own keys, comma separated)")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    presets = {
        "1": '[["ESC","TAB","CTRL","ALT","-","/","|","HOME","UP","END"],["FN","CTRL","ALT","LEFT","DOWN","RIGHT","PGUP","PGDN"]]',
        "2": '[["ESC","/","-","HOME","UP","END","DOWN"]]',
    }
    if c in presets:
        value = presets[c]
    else:
        keys = input("Enter keys comma-separated (e.g. ESC,TAB,-,/,HOME): ").strip()
        key_list = [f'"{k.strip()}"' for k in keys.split(",") if k.strip()]
        value = f'[[{",".join(key_list)}]]'
    _write_prop("extra-keys", value)
    print(f"\n{COLORS['MATRIX']}[+] Extra keys row updated.{COLORS['RESET']}")
    pause()

def toggle_cursor_style():
    clear()
    print(f"{COLORS['CYAN']}------- CURSOR STYLE -------{COLORS['RESET']}")
    print("1) Block\n2) Underline\n3) Bar")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    styles = {"1": "block", "2": "underline", "3": "bar"}
    style = styles.get(c, "block")
    _write_prop("terminal-cursor-style", style)
    print(f"\n{COLORS['MATRIX']}[+] Cursor style set to {style}.{COLORS['RESET']}")
    pause()

def toggle_cursor_blink():
    clear()
    print(f"{COLORS['CYAN']}------- CURSOR BLINK -------{COLORS['RESET']}")
    c = input("Enable blinking cursor? (y/N): ").strip().lower()
    _write_prop("terminal-cursor-blink-rate", "500" if c == "y" else "0")
    print(f"\n{COLORS['MATRIX']}[+] Cursor blink {'enabled' if c == 'y' else 'disabled'}.{COLORS['RESET']}")
    pause()

def toggle_bell():
    clear()
    print(f"{COLORS['CYAN']}------- TERMINAL BELL -------{COLORS['RESET']}")
    print("1) Vibrate\n2) Beep\n3) Ignore (silent)")
    c = input(f"{COLORS['CYAN']}Choice: {COLORS['RESET']}").strip()
    modes = {"1": "vibrate", "2": "beep", "3": "ignore"}
    mode = modes.get(c, "ignore")
    _write_prop("bell-character", mode)
    print(f"\n{COLORS['MATRIX']}[+] Bell behavior set to {mode}.{COLORS['RESET']}")
    pause()

def reset_termux_properties():
    clear()
    confirm = input(f"{COLORS['RED']}Reset termux.properties to defaults? (y/N): {COLORS['RESET']}").strip().lower()
    if confirm == "y" and os.path.exists(TERMUX_PROPS):
        os.remove(TERMUX_PROPS)
        run("termux-reload-settings", quiet=True)
        print(f"{COLORS['MATRIX']}[+] termux.properties reset.{COLORS['RESET']}")
    else:
        print("Cancelled.")
    pause()


# ------------------------------------------------------------------
# 39–40. SYSTEM UTILITIES
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
    print(f"\n{COLORS['MATRIX']}[✓] Copied (requires Termux:API app + package installed).{COLORS['RESET']}")
    pause()

def notification_test():
    clear()
    print(f"{COLORS['CYAN']}------- NOTIFICATION TEST -------{COLORS['RESET']}")
    run('termux-notification --title "Cortex Styler" --content "Notifications are working!"', quiet=True)
    print(f"\n{COLORS['MATRIX']}[✓] Sent (requires Termux:API app + package installed).{COLORS['RESET']}")
    pause()

def install_termux_api_package():
    clear()
    print(f"{COLORS['YELLOW']}[*] Installing termux-api package (also install the Termux:API app from F-Droid/Play){COLORS['RESET']}")
    smart_install("termux-api")
    print(f"{COLORS['MATRIX']}[✓] termux-api package ready.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 41–45. PACKAGE MANAGEMENT
# ------------------------------------------------------------------
def package_shortcuts():
    while True:
        clear()
        print(f"{COLORS['CYAN']}------- PACKAGE MANAGER SHORTCUTS -------{COLORS['RESET']}")
        print("1) Update + Upgrade all\n2) Autoclean cache\n3) List installed packages")
        print("4) Export package list\n5) Import package list\n6) Install a package by name")
        print("7) Uninstall a package by name\n8) Back")
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
        elif c == "6":
            pkg = input("Package name: ").strip()
            if pkg:
                smart_install(pkg)
        elif c == "7":
            pkg = input("Package name to remove: ").strip()
            if pkg:
                run(f"pkg uninstall {pkg} -y")
        else:
            return
        pause()

def disk_usage_summary():
    clear()
    print(f"{COLORS['CYAN']}------- HOME DIRECTORY DISK USAGE -------{COLORS['RESET']}\n")
    run(f'du -sh "{HOME}"/* 2>/dev/null | sort -rh | head -n 20')
    pause()


# ------------------------------------------------------------------
# 46–48. BACKUP / RESTORE / RESET
# ------------------------------------------------------------------
def backup_all():
    clear()
    print(f"{COLORS['YELLOW']}[*] Creating full dotfiles backup archive...{COLORS['RESET']}")
    ensure_dirs()
    archive = os.path.join(BACKUP_DIR, "cortex_full_backup.tar.gz")
    targets = " ".join(f'"{p}"' for p in [TERMUX_DIR, BASHRC_PATH, ZSHRC_PATH, TMUX_CONF, VIMRC_PATH, ALIASES_FILE] if os.path.exists(p))
    if targets:
        run(f'tar -czf "{archive}" {targets} 2>/dev/null')
        print(f"\n{COLORS['MATRIX']}[✓] Backup saved to {archive}{COLORS['RESET']}")
    else:
        print(f"\n{COLORS['RED']}[-] Nothing found to back up yet.{COLORS['RESET']}")
    pause()

def export_config_bundle():
    clear()
    print(f"{COLORS['YELLOW']}[*] Exporting a shareable config bundle...{COLORS['RESET']}")
    ensure_dirs()
    bundle = os.path.join(HOME, "cortex_config_bundle.tar.gz")
    targets = " ".join(f'"{p}"' for p in [COLOR_FILE, ALIASES_FILE, TMUX_CONF, VIMRC_PATH, SETTINGS_FILE] if os.path.exists(p))
    if targets:
        run(f'tar -czf "{bundle}" {targets} 2>/dev/null')
        print(f"\n{COLORS['MATRIX']}[✓] Bundle saved to {bundle} — share this file to hand off your setup.{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}[-] Nothing to bundle yet.{COLORS['RESET']}")
    pause()

def import_config_bundle():
    clear()
    print(f"{COLORS['CYAN']}------- IMPORT CONFIG BUNDLE -------{COLORS['RESET']}")
    path = input("Path to .tar.gz bundle: ").strip()
    if os.path.exists(path):
        run(f'tar -xzf "{path}" -C "{HOME}"')
        run("termux-reload-settings", quiet=True)
        print(f"{COLORS['MATRIX']}[✓] Bundle imported.{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}[-] File not found.{COLORS['RESET']}")
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
        os.path.join(BACKUP_DIR, "termux.properties.bak"): TERMUX_PROPS,
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
# 49. SELF-UPDATE
# ------------------------------------------------------------------
def execute_auto_update():
    clear()
    print(f"{COLORS['YELLOW']}[*] Checking for updates on GitHub...{COLORS['RESET']}")
    print(f"{COLORS['DIM']}Source: {GITHUB_RAW_URL}{COLORS['RESET']}\n")
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_RAW_URL, timeout=10) as resp:
            if resp.status == 200:
                data = resp.read().decode("utf-8")
                current_path = os.path.abspath(__file__)
                backup_file(current_path, "styler.py.bak")
                with open(current_path, "w", encoding="utf-8") as f:
                    f.write(data)
                print(f"{COLORS['MATRIX']}[✓] Updated successfully. Restarting...{COLORS['RESET']}")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print(f"{COLORS['RED']}[-] Update check failed (status {resp.status}).{COLORS['RESET']}")
    except Exception as e:
        print(f"{COLORS['RED']}[-] Update unavailable: {e}{COLORS['RESET']}")
    pause()

def set_update_source():
    global GITHUB_RAW_URL
    clear()
    print(f"{COLORS['CYAN']}------- SET UPDATE SOURCE URL -------{COLORS['RESET']}")
    print(f"Current: {GITHUB_RAW_URL}")
    url = input(f"{COLORS['WHITE']}New raw GitHub URL (blank to keep current): {COLORS['RESET']}").strip()
    if url:
        settings = load_settings()
        settings["update_url"] = url
        save_settings(settings)
        print(f"{COLORS['MATRIX']}[+] Saved. Will be used next time the tool starts.{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# 50. SETTINGS / DIAGNOSTICS / ABOUT
# ------------------------------------------------------------------
def view_current_config():
    clear()
    print(f"{COLORS['CYAN']}------- CURRENT CONFIGURATION -------{COLORS['RESET']}")
    print(f"Colors file      : {'present' if os.path.exists(COLOR_FILE) else 'not set'}")
    print(f"Font file        : {'present' if os.path.exists(FONT_FILE) else 'not set'}")
    print(f"Background image : {'present' if os.path.exists(BG_FILE) else 'not set'}")
    print(f".bashrc          : {'present' if os.path.exists(BASHRC_PATH) else 'not set'}")
    print(f".zshrc           : {'present' if os.path.exists(ZSHRC_PATH) else 'not set'}")
    print(f"Aliases          : {'present' if os.path.exists(ALIASES_FILE) else 'not set'}")
    print(f"termux.properties: {'present' if os.path.exists(TERMUX_PROPS) else 'not set'}")
    print(f"Backups dir      : {BACKUP_DIR if os.path.exists(BACKUP_DIR) else 'none yet'}")
    settings = load_settings()
    print(f"Auto-install mode: {'AUTO' if settings.get('auto_mode', True) else 'MANUAL'}")
    print(f"Saved profile    : {settings.get('profile_name') or '(none)'}@{settings.get('profile_host') or '(none)'}")
    pause()

def dependency_status():
    clear()
    print(f"{COLORS['CYAN']}------- DEPENDENCY STATUS -------{COLORS['RESET']}\n")
    tools = ["git", "zsh", "fish", "tmux", "vim", "fzf", "zoxide", "eza", "bat",
             "fastfetch", "rg", "fd", "htop", "tree", "ncdu", "lazygit", "node", "python3"]
    for t in tools:
        state = f"{COLORS['MATRIX']}installed" if is_installed(t) else f"{COLORS['RED']}missing"
        print(f"  {t.ljust(12)} : {state}{COLORS['RESET']}")
    pause()

def about_screen():
    clear()
    print(ASCII_ART)
    print(f"\n{COLORS['WHITE']}Cortex Terminal Styler — All-in-One Edition v6.0.0{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}Credit: Sabuj (CortexHost){COLORS['RESET']}")
    print(f"{COLORS['CYAN']}Community: {TELEGRAM_LINK}{COLORS['RESET']}")
    pause()


# ------------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------------
MENU_ITEMS = [
    ("01", "Guided Full Setup Wizard (theme+name+bg+banner)", full_setup_wizard),
    ("02", "Theme Picker (14 built-in themes)", theme_menu),
    ("03", "Custom Theme Builder", create_custom_theme),
    ("04", "Random Theme", randomize_theme),
    ("05", "Preview ANSI Color Palette", preview_color_palette),
    ("06", "Install Nerd Font", install_nerd_font),
    ("07", "Set Terminal Background Image", set_background_image),
    ("08", "Enable Zsh + Autosuggestions + Syntax Highlighting", enable_autosuggestions),
    ("09", "Install Powerlevel10k Theme", install_powerlevel10k),
    ("10", "Customize Username/Hostname Prompt", customize_host_prompt),
    ("11", "Switch Default Shell", switch_default_shell),
    ("12", "Install Fish Shell", install_fish_shell),
    ("13", "Install fzf (fuzzy finder)", install_fzf),
    ("14", "Install zoxide (smarter cd)", install_zoxide),
    ("15", "Install eza (modern ls)", install_eza),
    ("16", "Install bat (better cat)", install_bat),
    ("17", "Install fastfetch (system info)", install_fastfetch),
    ("18", "Install ripgrep", install_ripgrep),
    ("19", "Install fd", install_fd),
    ("20", "Install htop", install_htop),
    ("21", "Install tree", install_tree),
    ("22", "Install ncdu", install_ncdu),
    ("23", "Install lazygit", install_lazygit),
    ("24", "Toggle Auto-Install Mode (auto/manual)", toggle_auto_mode),
    ("25", "Alias Manager", alias_manager),
    ("26", "Deploy Startup Banner (.bashrc)", inject_banner),
    ("27", "Add Weather Widget to Login", toggle_weather_widget),
    ("28", "Set Custom MOTD", set_motd),
    ("29", "Git Config Wizard", git_config_wizard),
    ("30", "Generate SSH Key", generate_ssh_key),
    ("31", "Install Node.js + npm", install_node),
    ("32", "Setup Python venv", setup_python_venv),
    ("33", "Install tmux + styled config", install_tmux),
    ("34", "Install vim + sane config", install_vim_config),
    ("35", "Customize Extra Keys Row", customize_extra_keys),
    ("36", "Cursor Style (block/underline/bar)", toggle_cursor_style),
    ("37", "Cursor Blink Toggle", toggle_cursor_blink),
    ("38", "Terminal Bell Behavior", toggle_bell),
    ("39", "Reset termux.properties", reset_termux_properties),
    ("40", "Setup Storage Access", setup_storage),
    ("41", "Tune Shell History", configure_history),
    ("42", "Clipboard Tool Test", clipboard_tool),
    ("43", "Notification Test", notification_test),
    ("44", "Install termux-api package", install_termux_api_package),
    ("45", "Package Manager Shortcuts", package_shortcuts),
    ("46", "Disk Usage Summary", disk_usage_summary),
    ("47", "Full Config Backup (tar.gz)", backup_all),
    ("48", "Export Shareable Config Bundle", export_config_bundle),
    ("49", "Import Config Bundle", import_config_bundle),
    ("50", "Safe Rollback (Restore Backup)", rollback),
    ("51", "Hard Purge (Reset Everything)", purge),
    ("52", "Check for Online Updates", execute_auto_update),
    ("53", "Set Update Source URL", set_update_source),
    ("54", "View Current Configuration", view_current_config),
    ("55", "Dependency Status Check", dependency_status),
    ("56", "About / Credits", about_screen),
]

def display_menu():
    clear()
    print(ASCII_ART)
    settings = load_settings()
    mode = "AUTO" if settings.get("auto_mode", True) else "MANUAL"
    print(f"\n{COLORS['DIM']}Install mode: {mode}  (option 24 to change){COLORS['RESET']}")
    print(f"{COLORS['KALI']}┌────────────────────{COLORS['WHITE']} CORE CONTROL DASHBOARD {COLORS['KALI']}────────────────────┐{COLORS['RESET']}")
    for code, label, _ in MENU_ITEMS:
        print(f"  {COLORS['CYAN']}[{code}]{COLORS['WHITE']} {label}{COLORS['RESET']}")
    print(f"  {COLORS['RED']}[00]{COLORS['WHITE']} Exit{COLORS['RESET']}")
    print(f"{COLORS['KALI']}└──────────────────────────────────────────────────────────────┘{COLORS['RESET']}")

def main():
    ensure_dirs()
    actions = {code: fn for code, _, fn in MENU_ITEMS}
    while True:
        display_menu()
        choice = input(f"\n{COLORS['YELLOW']}Select an option [00-56]: {COLORS['RESET']}").strip().zfill(2)
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
