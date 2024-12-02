# Reddit Python Project Helper Bot

A Reddit bot that automatically responds to posts asking for beginner Python project ideas in r/learnpython.

## Features

- Monitors r/learnpython subreddit for new posts
- Detects posts asking about beginner projects using keyword matching
- Provides curated responses with project suggestions
- Includes difficulty levels and learning concepts for each project
- Avoids duplicate responses

## Setup

1. Install required packages:
```bash
pip install praw requests
```

2. Create a Reddit App:
- Go to https://www.reddit.com/prefs/apps
- Click "create another app..."
- Select "script"
- Fill in name and description
- Set redirect URI to http://localhost:8080
- Note your client_id and client_secret

3. Create a config.py file with your credentials:
```python
client_id = "your_client_id"
client_secret = "your_client_secret"
username = "your_reddit_username"
password = "your_reddit_password"
```

## Usage

Run the bot:
```bash
python bot.py
```

The bot will:
1. Connect to Reddit using your credentials
2. Monitor r/learnpython for new posts
3. Respond to relevant posts about beginner projects
4. Print status messages to the console

## Project Structure

```
reddit_bot_helper/
├── bot.py             # Main bot code
├── config.py          # Configuration and credentials
└── .gitignore         # Git ignore file
```

## Configuration

The bot looks for these keywords in posts:
- "beginner project"
- "starter project"
- "project idea"
- "project suggestion"
- "what to build"
- "first project"
- "new to python"
- "learning python"

## Security Notes

- Never commit your config.py file
- Keep your Reddit credentials secure
- Monitor the bot's activity regularly

## Contributing

Feel free to:
1. Fork the repository
2. Create a new branch
3. Submit pull requests with improvements

## License

This project is available under the MIT License.
