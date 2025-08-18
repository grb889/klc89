#!/bin/bash

echo "🧼 Starting Kali OSINT cleanup..."

# 1. Clear APT cache
echo "🔹 Cleaning APT cache..."
sudo apt clean

# 2. Remove orphaned packages
echo "🔹 Removing unused packages..."
sudo apt autoremove -y

# 3. Clear GUI thumbnail cache
echo "🔹 Clearing thumbnail cache..."
rm -rf ~/.cache/thumbnails/*

# 4. Trim journal logs older than 7 days
echo "🔹 Pruning journal logs (older than 7 days)..."
sudo journalctl --vacuum-time=7d

# 5. Remove any bash history backups
echo "🔹 Removing bash history backups..."
rm -f ~/.bash_history.*

# 6. Clear Downloads folder
echo "🔹 Cleaning ~/Downloads directory..."
rm -rf ~/Downloads/*

echo "✅ Cleanup complete. Your system is fresh and lean!"
