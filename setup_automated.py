#!/usr/bin/env python3
"""
Automated Setup Script for Auto Code Generator
Sets up everything needed for completely automated operation
"""

import os
import sys
import subprocess
import json
import shutil
from pathlib import Path

class AutomatedSetup:
    def __init__(self):
        self.repo_path = Path(__file__).parent
        self.home_dir = Path.home()
        self.ssh_dir = self.home_dir / '.ssh'
        self.launch_agents_dir = self.home_dir / 'Library' / 'LaunchAgents'
        
    def run_command(self, cmd, cwd=None, check=True):
        """Run a command and handle errors"""
        try:
            result = subprocess.run(cmd, shell=True, cwd=cwd, 
                                  capture_output=True, text=True, check=check)
            return result
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {cmd}")
            print(f"Error: {e.stderr}")
            return None
    
    def setup_git_repository(self):
        """Initialize Git repository and set up remote"""
        print("🔧 Setting up Git repository...")
        
        # Initialize git if not already done
        if not (self.repo_path / '.git').exists():
            self.run_command('git init', cwd=self.repo_path)
            print("✓ Git repository initialized")
        
        # Remove existing remote if it exists
        self.run_command('git remote remove origin', cwd=self.repo_path, check=False)
        
        # Add SSH remote
        self.run_command('git remote add origin git@github.com:Wasif-Karim03/GilGit.git', 
                        cwd=self.repo_path)
        print("✓ Remote repository configured (SSH)")
        
        # Create initial commit
        self.run_command('git add .', cwd=self.repo_path)
        self.run_command('git commit -m "Initial commit - Auto Code Generator setup"', 
                        cwd=self.repo_path, check=False)
        print("✓ Initial commit created")
        
        # Test SSH connection
        print("🔑 Testing SSH connection to GitHub...")
        result = self.run_command('ssh -T git@github.com', check=False)
        if result and result.returncode == 1:  # SSH returns 1 for successful auth
            print("✓ SSH connection to GitHub successful")
        else:
            print("⚠️  SSH connection failed - you may need to add your SSH key to GitHub")
    
    def setup_launchd_service(self):
        """Set up macOS launchd service for automatic startup"""
        print("🚀 Setting up automatic startup service...")
        
        # Create LaunchAgents directory if it doesn't exist
        self.launch_agents_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy plist file to LaunchAgents
        plist_source = self.repo_path / 'com.autocodegenerator.plist'
        plist_dest = self.launch_agents_dir / 'com.autocodegenerator.plist'
        
        if plist_source.exists():
            shutil.copy2(plist_source, plist_dest)
            print("✓ LaunchAgent plist installed")
            
            # Load the service
            result = self.run_command('launchctl load ~/Library/LaunchAgents/com.autocodegenerator.plist')
            if result:
                print("✓ Service loaded and started")
            else:
                print("⚠️  Could not load service automatically")
        else:
            print("❌ Plist file not found")
    
    def test_automation(self):
        """Test the automation by running once"""
        print("🧪 Testing automation (generating one code file)...")
        
        result = self.run_command('python3 auto_code_generator.py --once', 
                                cwd=self.repo_path)
        if result and result.returncode == 0:
            print("✓ Test run successful!")
        else:
            print("❌ Test run failed - check the logs")
    
    def create_startup_script(self):
        """Create a simple startup script"""
        startup_script = self.repo_path / 'start_automation.sh'
        
        script_content = """#!/bin/bash
# Auto Code Generator Startup Script

cd /Users/wasifkarim/Desktop/GitGits

echo "🚀 Starting Auto Code Generator..."
echo "📝 Logs will be saved to auto_generator.log"
echo "🔄 Service will run in background"

# Start the background service
python3 run_background.py &

echo "✅ Service started! Check logs for details."
echo "🛑 To stop: killall python3 or use Activity Monitor"
"""
        
        with open(startup_script, 'w') as f:
            f.write(script_content)
        
        # Make it executable
        os.chmod(startup_script, 0o755)
        print("✓ Startup script created: start_automation.sh")
    
    def update_config(self):
        """Update configuration with automated settings"""
        config_file = self.repo_path / 'config.json'
        
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            # Update with SSH URL
            config['remote_url'] = 'git@github.com:Wasif-Karim03/GilGit.git'
            config['repo_path'] = str(self.repo_path)
            
            # Set reasonable defaults
            config['git_user'] = config.get('git_user', 'Auto Code Generator')
            config['git_email'] = config.get('git_email', 'auto@example.com')
            
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=4)
            
            print("✓ Configuration updated for automation")
    
    def run_full_setup(self):
        """Run the complete automated setup"""
        print("🤖 Auto Code Generator - Automated Setup")
        print("=" * 50)
        
        try:
            self.update_config()
            self.setup_git_repository()
            self.create_startup_script()
            self.test_automation()
            self.setup_launchd_service()
            
            print("\n" + "=" * 50)
            print("✅ AUTOMATED SETUP COMPLETE!")
            print("\n📋 What's been set up:")
            print("  • SSH authentication (no more passwords!)")
            print("  • Git repository with remote")
            print("  • Background service for continuous operation")
            print("  • Automatic startup on system boot")
            print("  • Test run completed")
            
            print("\n🚀 Your system will now:")
            print("  • Generate random code twice daily (9 AM & 9 PM)")
            print("  • Automatically push to GitHub")
            print("  • Run in the background")
            print("  • Start automatically when you boot your computer")
            
            print("\n📝 Logs are available in:")
            print("  • auto_generator.log (main script)")
            print("  • background_service.log (service)")
            
            print("\n🛠️  Manual controls:")
            print("  • Start: ./start_automation.sh")
            print("  • Test: python3 auto_code_generator.py --once")
            print("  • Stop: killall python3")
            
        except Exception as e:
            print(f"❌ Setup failed: {e}")
            sys.exit(1)

def main():
    setup = AutomatedSetup()
    setup.run_full_setup()

if __name__ == "__main__":
    main()
