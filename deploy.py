#!/usr/bin/env python3
"""
Deployment script for VibeType API
Supports multiple hosting platforms
"""
import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import openai
        import tiktoken
        import sklearn
        import numpy
        print("✅ All dependencies are available")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def setup_environment():
    """Setup environment variables"""
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY not set. Please set it before running the API.")
        print("   You can set it with: export OPENAI_API_KEY='your-key-here'")
        return False
    
    print("✅ Environment variables configured")
    return True

def run_local():
    """Run the API locally"""
    print("🚀 Starting VibeType API locally...")
    print("📡 API will be available at: http://localhost:8000")
    print("📚 API docs at: http://localhost:8000/docs")
    
    try:
        subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    except KeyboardInterrupt:
        print("\n👋 API stopped")

def create_dockerfile():
    """Create a Dockerfile for containerized deployment"""
    dockerfile_content = """# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
    
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    print("✅ Dockerfile created")

def create_docker_compose():
    """Create docker-compose.yml for easy deployment"""
    compose_content = """version: '3.8'

services:
  vibetype-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
"""
    
    with open("docker-compose.yml", "w") as f:
        f.write(compose_content)
    print("✅ docker-compose.yml created")

def main():
    """Main deployment function"""
    print("🎯 VibeType API Deployment")
    print("=" * 40)
    
    if not check_dependencies():
        print("\n📦 Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    if not setup_environment():
        print("\n❌ Please set up your environment variables first")
        return
    
    print("\n🚀 Choose deployment option:")
    print("1. Run locally")
    print("2. Create Docker files")
    print("3. Both")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice in ["1", "3"]:
        run_local()
    
    if choice in ["2", "3"]:
        create_dockerfile()
        create_docker_compose()
        print("\n🐳 Docker files created!")
        print("To run with Docker:")
        print("  docker build -t vibetype-api .")
        print("  docker run -p 8000:8000 -e OPENAI_API_KEY=your-key vibetype-api")
        print("\nOr with docker-compose:")
        print("  docker-compose up --build")

if __name__ == "__main__":
    main() 