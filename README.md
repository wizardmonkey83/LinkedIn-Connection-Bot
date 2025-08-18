# LinkedIn-Connection-Bot
A Python/Selenium script that automates sending LinkedIn connection requests based on user criteria. It logs in headlessly (or with UI), scrolls through suggestions, and sends a configurable number of invites with randomized delays to mimic human behavior.


## Features
- Headless or headed ChromeDriver support
- Configurable invites per run
- Randomized delays to reduce bot-detection risk


## Prerequisites
- Python 3.8+
- Google Chrome (for ChromeDriver)
- Git (for cloning this repo)


## Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/wizardmonkey83/LinkedIn-Connection-Bot
   cd LinkedIn-Connection-Bot
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    -- for macOS/Linux
   .\venv\Scripts\activate     -- for Windows
   ```

5. Install dependencies:
   ```
   pip install -r requiriements.txt
   ```


## Configuration
1. Create a .env file in the project root:
   ```
   LINKEDIN_USER=youremail@example.com
   LINKEDIN_PASS=yoursuperdupersecurepassword
   ```

3. Make sure you put .env into .gitignore to keep it secure

## Usage
With your venv activated and .env configured, simply run: ```python main.py```

## Notes
There should be a few updates to this bot in the future in order to add operations and make it more robust

Happy networking!

  
