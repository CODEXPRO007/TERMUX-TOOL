# Cortex Terminal Styler — All-in-One Edition

![Preview](https://github.com/CODEXPRO007/TERMUX-TOOL/raw/refs/heads/main/Screenshot_2026-07-19-20-13-40-00_84d3000e3f4017145260f7618db1d683.jpg)

A single-file, all-in-one **Termux customization suite** — themes, fonts, shell, prompt, productivity tools, backups, and system utilities, all from one interactive menu. No accounts, no license keys, no network gate — everything runs locally on your device.

Credit: **Sabuj (CortexHost)**

---

## ✨ Features (35 tools in one menu)

### 🎨 Appearance
- 12 built-in color themes (Kali, Dracula, Tokyo Night, Nord, Solarized, and more)
- Custom theme builder (enter your own hex codes)
- ANSI color palette previewer
- Nerd Font installer (FiraCode, Hack, JetBrainsMono, or custom URL)
- Terminal background image setter

### 🐚 Shell & Prompt
- Zsh + Oh My Zsh + autosuggestions + syntax highlighting, one-click install
- Powerlevel10k theme installer
- Username/hostname prompt customizer
- Default shell switcher (bash / zsh / fish)
- Fish shell installer

### ⚡ Productivity Tools
- `fzf` fuzzy finder with keybindings
- `zoxide` smarter `cd`
- `eza` modern `ls` replacement with icons
- `bat` syntax-highlighted `cat`
- `fastfetch` system info on login
- Alias manager (add / list / remove your own shortcuts)

### 🧑‍💻 Dev Tools
- Git config wizard (name, email, default branch, handy aliases)
- SSH key generator (ed25519)
- Node.js + npm installer
- Python venv quick setup
- tmux installer with a styled status bar config
- vim installer with a sane default config

### 🛠 System Utilities
- Startup banner designer for `.bashrc`
- Weather widget on login (via wttr.in)
- Storage access setup (`termux-setup-storage`)
- Shell history tuning (size, dedup)
- Clipboard test (Termux:API)
- Notification test (Termux:API)
- Package manager shortcuts: update/upgrade, autoclean, list, export/import package lists

### 💾 Backup & Maintenance
- Full config backup to a single `.tar.gz`
- Safe rollback (restore last backup)
- Hard purge (reset everything to defaults, with confirmation)
- Self-update from GitHub
- Current configuration viewer
- About / credits screen

---

## 📦 Installation

```bash
pkg update && pkg upgrade -y
pkg install python git zsh wget -y
git clone https://github.com/CODEXPRO007/TERMUX-TOOL.git
cd TERMUX-TOOL
chmod +x styler.py
python3 styler.py
```

## ▶️ Usage

Just run:

```bash
python3 styler.py
```

You'll get a numbered dashboard (01–35). Type the two-digit option number and hit Enter. Every destructive action (purge, rollback) asks for confirmation first, and most config-changing tools back up your existing file to `~/.termux_backup/` before touching it.

## 📁 What it touches

| Path | Purpose |
|---|---|
| `~/.termux/colors.properties` | Theme colors |
| `~/.termux/font.ttf` | Custom font |
| `~/.termux/background.png` | Terminal background image |
| `~/.bashrc` / `~/.zshrc` | Shell config, prompt, banner |
| `~/.cortex_aliases` | Your custom aliases |
| `~/.tmux.conf` / `~/.vimrc` | tmux / vim configs |
| `~/.termux_backup/` | Auto-backups before overwriting configs |
| `~/.cortex_styler/` | Tool's own settings |

## 🔄 Updating

Menu option **33** pulls the latest `styler.py` straight from this repo and restarts itself.

## 🤝 Credits

Built and maintained by **Sabuj** (CortexHost). Community: https://t.me/codexx01

## 📜 License

Use, modify, and redistribute freely — just keep the credit line.
