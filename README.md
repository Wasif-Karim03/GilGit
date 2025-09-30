# Auto Code Generator 🤖

An automated Python script that generates random code in multiple programming languages and pushes it to a GitHub repository twice daily.

## Features

- 🎲 Generates random code in Python, JavaScript, C++, Java, and HTML
- ⏰ Runs automatically twice daily (9:00 AM and 9:00 PM)
- 🔄 Automatically commits and pushes to GitHub
- 📝 Comprehensive logging
- ⚙️ Configurable settings
- 🎯 No external dependencies (uses Python standard library)

## Quick Start

### 1. Setup

```bash
# Clone or download this repository
cd GitGits

# Run the setup script
python setup.py
```

The setup script will:
- Initialize a Git repository (if needed)
- Create a `.gitignore` file
- Configure your Git settings
- Set up your GitHub repository connection

### 2. Configuration

Edit `config.json` to customize your settings:

```json
{
    "repo_path": ".",
    "git_user": "Your Name",
    "git_email": "your.email@example.com", 
    "remote_url": "https://github.com/yourusername/your-repo.git",
    "schedule": {
        "morning_time": "09:00",
        "evening_time": "21:00"
    }
}
```

### 3. Test Run

Test the script once to make sure everything works:

```bash
python auto_code_generator.py --once
```

### 4. Start the Scheduler

Run the script to start the automatic scheduler:

```bash
python auto_code_generator.py
```

The script will now run continuously and generate code twice daily at the specified times.

## Generated Code Types

The script randomly generates code in the following languages:

- **Python** (.py) - Functions, algorithms, and utilities
- **JavaScript** (.js) - Web development functions
- **C++** (.cpp) - System programming and algorithms  
- **Java** (.java) - Object-oriented programming examples
- **HTML** (.html) - Web pages with CSS styling

## File Structure

```
GitGits/
├── auto_code_generator.py  # Main script
├── config.json            # Configuration file
├── setup.py              # Setup script
├── requirements.txt      # Dependencies (none required)
├── README.md            # This file
└── auto_generated_*.ext # Generated code files
```

## Logging

The script creates detailed logs in `auto_generator.log` including:
- Code generation timestamps
- Git operation results
- Error messages and debugging information

## Scheduling Options

### Option 1: Run Continuously (Recommended)
```bash
python auto_code_generator.py
```
The script runs continuously and checks every minute for scheduled times.

### Option 2: Use System Cron (Linux/macOS)
Add to your crontab (`crontab -e`):
```bash
0 9,21 * * * cd /path/to/GitGits && python auto_code_generator.py --once
```

### Option 3: Use Task Scheduler (Windows)
Create a scheduled task to run the script with `--once` flag twice daily.

## Troubleshooting

### Common Issues

1. **Git authentication errors**: Make sure you have proper GitHub credentials configured
2. **Repository not found**: Verify the remote URL in `config.json`
3. **Permission denied**: Ensure you have write access to the repository

### Debug Mode

Check the log file for detailed information:
```bash
tail -f auto_generator.log
```

## Customization

### Adding New Languages

To add support for new programming languages, extend the `generate_random_code()` method in `auto_code_generator.py`:

```python
def generate_rust_code(self) -> str:
    """Generate random Rust code"""
    return """// Auto-generated Rust code
fn main() {
    println!("Hello from auto-generated Rust!");
}
"""
```

### Changing Schedule

Modify the times in the `run_scheduler()` method:
```python
morning_time = (8, 30)  # 8:30 AM
evening_time = (20, 0)  # 8:00 PM
```

## Requirements

- Python 3.6+
- Git installed and configured
- GitHub repository with push access

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the auto code generator!

---

**Happy Coding!** 🚀
