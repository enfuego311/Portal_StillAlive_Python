#!/bin/bash

# Portal Still Alive Credits - macOS Setup Script
# This script helps set up the project on macOS

echo "🎵 Setting up Portal Still Alive Credits for macOS..."
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.6+ from python.org"
    echo "   Or use Homebrew: brew install python"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if the audio file exists
if [ ! -f "sa1.mp3" ]; then
    echo "❌ Audio file 'sa1.mp3' not found in current directory"
    echo "   Please ensure you have the audio file in the project directory"
    exit 1
fi

echo "✅ Audio file found: sa1.mp3"

# Test audio playback capability
echo ""
echo "🔊 Testing audio playback capability..."

# Check if afplay is available (should be on all macOS systems)
if command -v afplay &> /dev/null; then
    echo "✅ afplay found - audio playback should work"
else
    echo "❌ afplay not found - this is unusual on macOS"
    exit 1
fi

# Test terminal capabilities
echo ""
echo "🖥️  Checking terminal capabilities..."

# Check terminal size
if command -v tput &> /dev/null; then
    cols=$(tput cols)
    lines=$(tput lines)
    echo "✅ Terminal size: ${cols}x${lines}"
    
    if [ "$cols" -lt 80 ] || [ "$lines" -lt 24 ]; then
        echo "⚠️  Warning: Terminal size is smaller than recommended (80x24)"
        echo "   The display may not look optimal"
    fi
else
    echo "⚠️  Could not determine terminal size"
fi

# Check if terminal supports colors
if [ -t 1 ]; then
    echo "✅ Terminal supports colors and formatting"
else
    echo "⚠️  Terminal may not support colors"
fi

echo ""
echo "🎉 Setup complete! You can now run:"
echo "   python3 still_alive_credit.py"
echo ""
echo "Options:"
echo "   --no-sound    Run without audio"
echo "   --no-stay     Exit after completion"
echo ""
echo "Press Ctrl+C to exit during playback"
echo ""
echo "Enjoy the Portal credits! 🧪" 