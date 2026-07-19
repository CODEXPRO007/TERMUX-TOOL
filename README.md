# Cortex Terminal Styler — All-in-One Edition

![Preview](https://github.com/CODEXPRO007/TERMUX-TOOL/raw/refs/heads/main/Screenshot_2026-07-19-20-13-40-00_84d3000e3f4017145260f7618db1d683.jpg)

A single-file, all-in-one **Termux customization suite** — themes, fonts, shell, prompt, productivity tools, backups, and system utilities, all from one interactive menu. No accounts, no license keys, no network gate — everything runs locally on your device.

Credit: **Sabuj (CortexHost)**

---

## ✨ Features (56 tools in one menu)

### 🧙 Guided Setup
- **Full Setup Wizard** — one flow that walks you through theme → username/hostname → optional background image → optional startup banner, then applies everything together
- **Auto-Install Mode toggle** — every installer checks if a tool is already present first. In **Auto** mode it silently skips what's already installed; in **Manual** mode it asks before reinstalling. No wasted re-downloads.

### 🎨 Appearance
- 14 built-in color themes (Kali, Dracula, Tokyo Night, Nord, Solarized, Gruvbox, Catppuccin, and more)
- Custom theme builder (enter your own hex codes)
- Random theme shuffler
- ANSI color palette previewer
- Nerd Font installer (FiraCode, Hack, JetBrainsMono, or custom URL) — verifies the download actually succeeded
- Terminal background image setter — **honest note:** stock Termux does not render picture backgrounds in the terminal itself (this is a Termux limitation, not a bug in the tool). The file still saves to `~/.termux/background.png` for forks/emulators that do support it; solid-color theming is handled by the Theme Picker instead
- Extra Keys row customizer, cursor style, cursor blink, terminal bell behavior (via `termux.properties`)

### 🐚 Shell & Prompt
- Zsh + Oh My Zsh + autosuggestions + syntax highlighting, one-click install
- Powerlevel10k theme installer
- Username/hostname prompt customizer (remembers your last values)
- Default shell switcher (bash / zsh / fish)
- Fish shell installer

### ⚡ Productivity Tools (all auto-package aware)
- `fzf` fuzzy finder with keybindings
- `zoxide` smarter `cd`
- `eza` modern `ls` replacement with icons
- `bat` syntax-highlighted `cat`
- `fastfetch` system info on login
- `ripgrep`, `fd`, `htop`, `tree`, `ncdu`, `lazygit`
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
- Custom MOTD (message of the day)
- Storage access setup (`termux-setup-storage`)
- Shell history tuning (size, dedup)
- Clipboard test (Termux:API)
- Notification test (Termux:API)
- `termux-api` package installer
- Package manager shortcuts: update/upgrade, autoclean, list, export/import package lists, install/uninstall by name
- Disk usage summary for your home directory

### 💾 Backup & Maintenance
- Full config backup to a single `.tar.gz`
- Export/import a shareable config bundle (hand your setup to a friend)
- Safe rollback (restore last backup)
- Hard purge (reset everything to defaults, with confirmation)
- Self-update from GitHub + custom update-source URL
- Current configuration viewer
- Dependency status check (see what's installed at a glance)
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

You'll get a numbered dashboard (01–56). Type the two-digit option number and hit Enter.

**New to the tool? Start with option `01` — Guided Full Setup Wizard.** It walks you through theme → username/hostname → optional background image → optional startup banner, in order, then applies everything in one shot.

Every destructive action (purge, rollback) asks for confirmation first, and most config-changing tools back up your existing file to `~/.termux_backup/` before touching it. Installers check what's already on your device first (option `24` switches this between **Auto** — skip silently if present — and **Manual** — ask before reinstalling).

## 📁 What it touches

| Path | Purpose |
|---|---|
| `~/.termux/colors.properties` | Theme colors |
| `~/.termux/font.ttf` | Custom font |
| `~/.termux/background.png` | Terminal background image |
| `~/.bashrc` / `~/.zshrc` | Shell config, prompt, banner |
| `~/.cortex_aliases` | Your custom aliases |
| `~/.tmux.conf` / `~/.vimrc` | tmux / vim configs |
| `~/.termux/termux.properties` | Extra keys, cursor style, bell behavior |
| `~/.termux_backup/` | Auto-backups before overwriting configs |
| `~/.cortex_styler/` | Tool's own settings (install mode, saved profile) |

## 🔄 Updating

Menu option **52** pulls the latest `styler.py` straight from this repo and restarts itself. Option **53** lets you point it at a different raw-file URL first.

## 🤝 Credits

Built and maintained by **Sabuj** (CortexHost). Community: https://t.me/codexx01

## 📜 License

Use, modify, and redistribute freely — just keep the credit line.
