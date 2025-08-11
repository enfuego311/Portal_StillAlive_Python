#!/usr/bin/env python3
"""
Audio Test Script for Portal Still Alive Credits
Tests audio playback functionality on macOS
"""

import platform
import subprocess
import sys
from pathlib import Path

def test_audio_playback():
    """Test audio playback functionality"""
    print("🎵 Testing audio playback on", platform.system())
    print()
    
    # Check if audio file exists
    audio_file = Path("sa1.mp3")
    if not audio_file.exists():
        print("❌ Audio file 'sa1.mp3' not found")
        return False
    
    print("✅ Audio file found:", audio_file)
    
    # Test based on platform
    system = platform.system()
    
    if system == "Darwin":  # macOS
        print("🖥️  Testing macOS audio playback...")
        try:
            # Test afplay
            result = subprocess.run(["afplay", str(audio_file)], 
                                  capture_output=True, text=True, timeout=3)
            if result.returncode == 0:
                print("✅ afplay test successful")
                return True
            else:
                print("❌ afplay test failed")
                return False
        except subprocess.TimeoutExpired:
            print("✅ afplay started successfully (stopped after 3 seconds)")
            return True
        except Exception as e:
            print(f"❌ afplay test error: {e}")
            return False
    
    elif system == "Linux":
        print("🐧 Testing Linux audio playback...")
        # Test mpg123
        try:
            result = subprocess.run(["mpg123", "--version"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ mpg123 available")
                return True
            else:
                print("❌ mpg123 not available")
                return False
        except FileNotFoundError:
            print("❌ mpg123 not installed")
            return False
    
    elif system == "Windows":
        print("🪟 Testing Windows audio playback...")
        try:
            import winsound
            print("✅ winsound module available")
            return True
        except ImportError:
            print("❌ winsound module not available")
            return False
    
    else:
        print(f"❌ Unsupported platform: {system}")
        return False

def main():
    """Main test function"""
    print("=" * 50)
    print("Portal Still Alive - Audio Test")
    print("=" * 50)
    print()
    
    success = test_audio_playback()
    
    print()
    print("=" * 50)
    if success:
        print("🎉 Audio test PASSED! You can run the main script.")
        print("   python3 still_alive_credit.py")
    else:
        print("❌ Audio test FAILED! Check the issues above.")
    print("=" * 50)

if __name__ == "__main__":
    main() 