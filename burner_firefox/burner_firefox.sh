#!/bin/bash

# === CONFIGURATION ===
PROFILE_NAME="burner-$(date +%s)"
FIREFOX_CMD=$(which firefox)

# Check if Firefox is installed
if [ -z "$FIREFOX_CMD" ]; then
  echo "❌ Firefox is not installed or not in PATH."
  exit 1
fi

echo "🌀 Creating Firefox burner profile: $PROFILE_NAME"
firefox -CreateProfile "$PROFILE_NAME"

# Find profile folder
PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*.$PROFILE_NAME" | head -n 1)

if [ -z "$PROFILE_DIR" ]; then
  echo "❌ Failed to find profile directory."
  exit 1
fi

echo "📁 Profile created at: $PROFILE_DIR"

# Download latest arkenfox user.js
echo "🌐 Downloading hardened user.js from arkenfox..."
curl -sSL https://raw.githubusercontent.com/arkenfox/user.js/master/user.js -o "$PROFILE_DIR/user.js"

# Launch Firefox with that profile
echo "🚀 Launching Firefox with burner profile..."
firefox -no-remote -P "$PROFILE_NAME" &
