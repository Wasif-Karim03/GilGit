#!/usr/bin/env python3
"""
Automatic Code Generator and Git Pusher
Generates random code twice daily and pushes to GitHub repository
"""

import os
import random
import datetime
import subprocess
import json
import time
from typing import List, Dict
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('auto_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AutoCodeGenerator:
    def __init__(self, config_file: str = 'config.json'):
        """Initialize the code generator with configuration"""
        self.config = self.load_config(config_file)
        self.repo_path = self.config.get('repo_path', '.')
        self.git_user = self.config.get('git_user')
        self.git_email = self.config.get('git_email')
        self.remote_url = self.config.get('remote_url')
        
    def load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found!")
            return {}
    
    def generate_random_code(self) -> str:
        """Generate random code in various programming languages"""
        languages = [
            self.generate_python_code,
            self.generate_javascript_code,
            self.generate_cpp_code,
            self.generate_java_code,
            self.generate_html_code
        ]
        
        generator = random.choice(languages)
        return generator()
    
    def generate_python_code(self) -> str:
        """Generate random Python code"""
        functions = [
            "def calculate_fibonacci(n):",
            "def binary_search(arr, target):",
            "def bubble_sort(data):",
            "def merge_sort(arr):",
            "def quick_sort(arr):",
            "def factorial(n):",
            "def is_prime(num):",
            "def reverse_string(text):",
            "def count_vowels(text):",
            "def find_max(arr):"
        ]
        
        function = random.choice(functions)
        code = f"""#!/usr/bin/env python3
# Auto-generated code at {datetime.datetime.now()}

{function}
    \"\"\"Auto-generated function\"\"\"
    # Random implementation
    result = {random.randint(1, 100)}
    for i in range({random.randint(1, 10)}):
        result += {random.randint(1, 50)}
    return result

# Test the function
if __name__ == "__main__":
    test_result = {function.split()[1].split('(')[0]}({random.randint(1, 20)})
    print(f"Result: {{test_result}}")
"""
        return code
    
    def generate_javascript_code(self) -> str:
        """Generate random JavaScript code"""
        functions = [
            "function calculateSum(a, b)",
            "function findAverage(numbers)",
            "function reverseArray(arr)",
            "function capitalizeWords(str)",
            "function countOccurrences(arr, target)",
            "function generateRandomString(length)",
            "function validateEmail(email)",
            "function shuffleArray(arr)",
            "function findLongestWord(str)",
            "function isPalindrome(str)"
        ]
        
        function = random.choice(functions)
        code = f"""// Auto-generated JavaScript code at {datetime.datetime.now()}

{function} {{
    // Auto-generated function
    const randomNumber = {random.randint(1, 100)};
    const multiplier = {random.randint(1, 10)};
    
    return randomNumber * multiplier;
}}

// Test the function
console.log("Auto-generated result:", {function.split()[1].split('(')[0]}({random.randint(1, 20)}));
"""
        return code
    
    def generate_cpp_code(self) -> str:
        """Generate random C++ code"""
        functions = [
            "int calculatePower(int base, int exponent)",
            "int findGCD(int a, int b)",
            "bool isEven(int number)",
            "int sumArray(int arr[], int size)",
            "int findMax(int arr[], int size)",
            "void printPattern(int n)",
            "int factorial(int n)",
            "bool isPalindrome(int num)",
            "int countDigits(int num)",
            "int reverseNumber(int num)"
        ]
        
        function = random.choice(functions)
        code = f"""// Auto-generated C++ code at {datetime.datetime.now()}
#include <iostream>
#include <vector>
#include <algorithm>

{function} {{
    // Auto-generated function
    int result = {random.randint(1, 100)};
    for (int i = 0; i < {random.randint(1, 10)}; i++) {{
        result += {random.randint(1, 50)};
    }}
    return result;
}}

int main() {{
    // Test the function
    auto result = {function.split()[1].split('(')[0]}({random.randint(1, 20)});
    std::cout << "Auto-generated result: " << result << std::endl;
    return 0;
}}
"""
        return code
    
    def generate_java_code(self) -> str:
        """Generate random Java code"""
        classes = [
            "Calculator",
            "StringProcessor",
            "NumberUtils",
            "ArrayHelper",
            "MathOperations",
            "DataValidator",
            "TextAnalyzer",
            "RandomGenerator",
            "SortingUtils",
            "SearchAlgorithms"
        ]
        
        class_name = random.choice(classes)
        methods = [
            "public int processData(int input)",
            "public String manipulateText(String text)",
            "public boolean validateInput(String input)",
            "public int calculateResult(int a, int b)",
            "public void printResults()"
        ]
        
        method = random.choice(methods)
        code = f"""// Auto-generated Java code at {datetime.datetime.now()}
public class {class_name} {{
    
    {method} {{
        // Auto-generated method
        int result = {random.randint(1, 100)};
        for (int i = 0; i < {random.randint(1, 10)}; i++) {{
            result += {random.randint(1, 50)};
        }}
        return result;
    }}
    
    public static void main(String[] args) {{
        {class_name} instance = new {class_name}();
        System.out.println("Auto-generated result: " + 
                          instance.{method.split()[1].split('(')[0]}({random.randint(1, 20)}));
    }}
}}
"""
        return code
    
    def generate_html_code(self) -> str:
        """Generate random HTML code"""
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'yellow', 'teal']
        color = random.choice(colors)
        
        code = f"""<!DOCTYPE html>
<!-- Auto-generated HTML at {datetime.datetime.now()} -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auto-Generated Page</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: {color};
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: {color};
            text-align: center;
        }}
        .random-number {{
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Auto-Generated HTML Page</h1>
        <p>This page was automatically generated at {datetime.datetime.now()}.</p>
        <div class="random-number">Random Number: {random.randint(1, 1000)}</div>
        <p>Generated with love by the Auto Code Generator!</p>
    </div>
</body>
</html>"""
        return code
    
    def save_code_to_file(self, code: str, filename: str = None) -> str:
        """Save generated code to a file"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            extensions = ['.py', '.js', '.cpp', '.java', '.html']
            ext = random.choice(extensions)
            filename = f"auto_generated_{timestamp}{ext}"
        
        filepath = os.path.join(self.repo_path, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            logger.info(f"Code saved to {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error saving code to {filepath}: {e}")
            return None
    
    def setup_git_config(self):
        """Setup Git configuration if not already set"""
        try:
            if self.git_user:
                subprocess.run(['git', 'config', 'user.name', self.git_user], 
                             cwd=self.repo_path, check=True)
            if self.git_email:
                subprocess.run(['git', 'config', 'user.email', self.git_email], 
                             cwd=self.repo_path, check=True)
            logger.info("Git configuration updated")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error setting up git config: {e}")
    
    def git_add_commit_push(self, filepath: str):
        """Add, commit, and push the generated code to GitHub"""
        try:
            # Add file to git
            subprocess.run(['git', 'add', filepath], cwd=self.repo_path, check=True)
            
            # Commit with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = f"Auto-generated code at {timestamp}"
            subprocess.run(['git', 'commit', '-m', commit_message], 
                         cwd=self.repo_path, check=True)
            
            # Push to remote
            if self.remote_url:
                subprocess.run(['git', 'push', 'origin', 'main'], 
                             cwd=self.repo_path, check=True)
                logger.info(f"Successfully pushed {filepath} to GitHub")
            else:
                logger.warning("No remote URL configured, commit made locally only")
                
        except subprocess.CalledProcessError as e:
            logger.error(f"Error in git operations: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during git operations: {e}")
    
    def generate_and_push(self):
        """Main method to generate code and push to GitHub"""
        logger.info("Starting code generation and push process...")
        
        # Setup git config
        self.setup_git_config()
        
        # Generate random code
        code = self.generate_random_code()
        
        # Save to file
        filepath = self.save_code_to_file(code)
        if not filepath:
            logger.error("Failed to save code to file")
            return
        
        # Git operations
        self.git_add_commit_push(filepath)
        
        logger.info("Code generation and push process completed!")
    
    def run_scheduler(self):
        """Run the scheduler to generate code twice daily"""
        logger.info("Starting scheduler for twice-daily code generation...")
        
        # Schedule times: 11:40 AM and 12:10 PM
        morning_time = (11, 40)  # 11:40 AM
        evening_time = (12, 10)  # 12:10 PM
        
        while True:
            current_time = datetime.datetime.now().time()
            current_hour_min = (current_time.hour, current_time.minute)
            
            # Check if it's time to generate code
            if current_hour_min == morning_time or current_hour_min == evening_time:
                logger.info(f"Trigger time reached: {current_time}")
                self.generate_and_push()
                
                # Sleep for a minute to avoid multiple triggers
                time.sleep(60)
            
            # Check every minute
            time.sleep(60)

def main():
    """Main entry point"""
    generator = AutoCodeGenerator()
    
    # Check if we should run once or start scheduler
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--once':
        generator.generate_and_push()
    else:
        generator.run_scheduler()

if __name__ == "__main__":
    main()
