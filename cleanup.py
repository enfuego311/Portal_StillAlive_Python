#!/usr/bin/env python3
"""
Cleanup script for Portal Still Alive Credits project
Removes temporary files and helps maintain the project
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Clean up temporary files and organize the project"""
    print("🧹 Cleaning up Portal Still Alive Credits project...")
    print()
    
    # Files to remove (if they exist)
    temp_files = [
        "*.pyc",
        "__pycache__",
        ".DS_Store",
        "*.tmp",
        "*.log"
    ]
    
    # Remove Python cache files
    for pattern in temp_files:
        if pattern == "__pycache__":
            cache_dir = Path("__pycache__")
            if cache_dir.exists():
                shutil.rmtree(cache_dir)
                print(f"✅ Removed {cache_dir}")
        elif pattern == "*.pyc":
            for pyc_file in Path(".").glob("*.pyc"):
                pyc_file.unlink()
                print(f"✅ Removed {pyc_file}")
        elif pattern == ".DS_Store":
            ds_store = Path(".DS_Store")
            if ds_store.exists():
                ds_store.unlink()
                print(f"✅ Removed {ds_store}")
    
    # Check project structure
    print()
    print("📁 Project structure:")
    
    required_files = [
        "still_alive_credit.py",
        "sa1.mp3", 
        "README.md",
        "requirements.txt",
        "setup_macos.sh",
        "test_audio.py"
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")
    
    # Check for optional files
    print()
    print("🖼️  Media files:")
    media_files = ["still_alive_linux.jpg", "still_alive_informer213.jpg"]
    for file in media_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"⚠️  {file} (optional)")
    
    print()
    print("🎉 Cleanup complete!")
    print()
    print("To run the project:")
    print("  ./setup_macos.sh    # Setup and test")
    print("  python3 test_audio.py  # Test audio")
    print("  python3 still_alive_credit.py  # Run credits")

if __name__ == "__main__":
    cleanup_project() 