#!/bin/bash

echo "🔧 Updating Kali Linux and installing base packages..."
sudo apt update && sudo apt upgrade -y

# CLI-based tools
echo "📦 Installing essential OSINT tools..."
sudo apt install -y \
  theharvester \
  spiderfoot \
  maltego \
  recon-ng \
  amass \
  shodan \
  exiftool \
  whois \
  dnsrecon \
  dnsenum \
  dig \
  whatweb \
  chromium \
  firefox-esr \
  git \
  python3-pip \
  curl

# Python tools
echo "🐍 Installing Holehe and Social Analyzer via pip..."
pip install holehe social-analyzer

# Cloning GitHub-based tools
echo "📁 Cloning useful GitHub OSINT repositories..."
mkdir -p ~/osint-tools
cd ~/osint-tools

git clone https://github.com/sherlock-project/sherlock
git clone https://github.com/smicallef/spiderfoot
git clone https://github.com/mxrch/GHunt

echo "✅ Done! All tools installed in ~/osint-tools"
echo "🧩 Don't forget to install browser extensions:"
echo "- uBlock Origin, Wappalyzer, NoScript, etc. (Firefox/Chromium)"
