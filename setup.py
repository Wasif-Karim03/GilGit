#!/usr/bin/env python3
"""
Setup script for Auto Code Generator
Helps initialize the repository and configure settings
"""

import os
import json
import subprocess
import sys

def setup_repository():
    """Initialize Git repository if not already initialized"""
    if not os.path.exists('.git'):
        print("Initializing Git repository...")
        subprocess.run(['git', 'init'], check=True)
        print("✓ Git repository initialized")
    else:
        print("✓ Git repository already exists")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
auto_generator.log

# Temporary files
*.tmp
*.temp
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("✓ .gitignore created")

def configure_repository():
    """Configure repository settings"""
    print("\n=== Repository Configuration ===")
    
    # Get user input
    git_user = input("Enter your Git username: ").strip()
    git_email = input("Enter your Git email: ").strip()
    remote_url = input("Enter your GitHub repository URL: ").strip()
    
    # Update config.json
    config_file = 'config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    
    config['git_user'] = git_user
    config['git_email'] = git_email
    config['remote_url'] = remote_url
    
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)
    
    print("✓ Configuration saved to config.json")
    
    # Setup Git config
    if git_user:
        subprocess.run(['git', 'config', 'user.name', git_user], check=True)
    if git_email:
        subprocess.run(['git', 'config', 'user.email', git_email], check=True)
    
    print("✓ Git configuration updated")

def setup_remote():
    """Setup remote repository"""
    remote_url = input("\nEnter your GitHub repository URL (or press Enter to skip): ").strip()
    
    if remote_url:
        try:
            # Remove existing origin if it exists
            subprocess.run(['git', 'remote', 'remove', 'origin'], 
                         capture_output=True)
            
            # Add new origin
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)
            print("✓ Remote repository configured")
            
            # Create initial commit
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', 'Initial commit - Auto Code Generator setup'], check=True)
            print("✓ Initial commit created")
            
            # Push to remote
            try:
                subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
                print("✓ Initial push completed")
            except subprocess.CalledProcessError:
                print("⚠ Could not push to remote. Make sure the repository exists and you have access.")
                
        except subprocess.CalledProcessError as e:
            print(f"✗ Error setting up remote: {e}")

def main():
    """Main setup function"""
    print("🚀 Auto Code Generator Setup")
    print("=" * 40)
    
    try:
        setup_repository()
        create_gitignore()
        configure_repository()
        setup_remote()
        
        print("\n" + "=" * 40)
        print("✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Make sure your GitHub repository exists")
        print("2. Run: python auto_code_generator.py --once  (to test)")
        print("3. Run: python auto_code_generator.py  (to start scheduler)")
        print("\nThe script will generate random code twice daily at 9:00 AM and 9:00 PM")
        
    except Exception as e:
        print(f"✗ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
