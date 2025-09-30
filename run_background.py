#!/usr/bin/env python3
"""
Background service runner for Auto Code Generator
Runs the code generator as a background daemon on macOS
"""

import os
import sys
import time
import signal
import subprocess
import logging
from pathlib import Path

# Set up logging
log_file = Path(__file__).parent / 'background_service.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BackgroundService:
    def __init__(self):
        self.running = True
        self.script_path = Path(__file__).parent / 'auto_code_generator.py'
        self.process = None
        
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"Received signal {signum}, shutting down...")
        self.running = False
        if self.process:
            self.process.terminate()
        sys.exit(0)
    
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def start_service(self):
        """Start the background service"""
        logger.info("Starting Auto Code Generator background service...")
        self.setup_signal_handlers()
        
        try:
            # Start the main script
            self.process = subprocess.Popen([
                sys.executable, 
                str(self.script_path)
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            logger.info(f"Service started with PID: {self.process.pid}")
            
            # Monitor the process
            while self.running:
                if self.process.poll() is not None:
                    # Process died, restart it
                    logger.warning("Process died, restarting...")
                    self.process = subprocess.Popen([
                        sys.executable, 
                        str(self.script_path)
                    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    logger.info(f"Service restarted with PID: {self.process.pid}")
                
                time.sleep(10)  # Check every 10 seconds
                
        except KeyboardInterrupt:
            logger.info("Service stopped by user")
        except Exception as e:
            logger.error(f"Service error: {e}")
        finally:
            if self.process:
                self.process.terminate()
                logger.info("Service terminated")

def main():
    service = BackgroundService()
    service.start_service()

if __name__ == "__main__":
    main()
