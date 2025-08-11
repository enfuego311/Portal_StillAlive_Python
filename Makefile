# Portal Still Alive Credits - Makefile
# Provides easy commands for common project tasks

.PHONY: help setup test run clean install

# Default target
help:
	@echo "🎵 Portal Still Alive Credits - Available Commands"
	@echo "=================================================="
	@echo ""
	@echo "setup    - Run macOS setup and tests"
	@echo "test     - Test audio functionality"
	@echo "run      - Run the credits (with sound)"
	@echo "run-nosound - Run the credits (without sound)"
	@echo "clean    - Clean up temporary files"
	@echo "install  - Install dependencies (if needed)"
	@echo "help     - Show this help message"
	@echo ""

# Setup the project
setup:
	@echo "🔧 Setting up Portal Still Alive Credits..."
	@chmod +x setup_macos.sh
	@./setup_macos.sh

# Test audio functionality
test:
	@echo "🔊 Testing audio functionality..."
	@python3 test_audio.py

# Run the credits with sound
run:
	@echo "🎬 Running Portal Still Alive Credits..."
	@python3 still_alive_credit.py

# Run the credits without sound
run-nosound:
	@echo "🎬 Running Portal Still Alive Credits (no sound)..."
	@python3 still_alive_credit.py --no-sound

# Clean up temporary files
clean:
	@echo "🧹 Cleaning up project..."
	@python3 cleanup.py

# Install dependencies (minimal - mostly just Python)
install:
	@echo "📦 Checking dependencies..."
	@python3 -c "import sys; print(f'Python {sys.version}')"
	@echo "✅ No external dependencies required for basic functionality"
	@echo "   The script uses native system audio players"

# Quick start - setup and test
quickstart: setup test
	@echo ""
	@echo "🚀 Quick start complete! Run 'make run' to start the credits." 