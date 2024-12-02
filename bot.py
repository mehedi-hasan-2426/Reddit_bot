import praw
import time
from datetime import datetime

def create_reddit_instance():
    """Create and return a Reddit instance using credentials."""
    return praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="python:beginner.project.helper:v1.0",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD"
    )

def generate_project_response():
    """Generate a response with beginner project suggestions."""
    return """Hello! Here are some beginner-friendly Python project ideas:

1. Number Guessing Game
- Create a game where the computer picks a random number and the player has to guess it
- Concepts: loops, conditionals, random numbers, user input
- Difficulty: Easy
- Extensions: Add hints, limit guesses, add multiple levels

2. File Organizer
- Script to organize files in a directory by extension or date
- Concepts: file operations, os module, datetime
- Difficulty: Easy-Medium
- Extensions: GUI interface, custom rules, scheduling

3. Personal Task Manager
- Command-line todo list manager
- Concepts: lists/dictionaries, file I/O, basic CRUD operations
- Difficulty: Medium
- Extensions: Due dates, priorities, SQLite database

4. Weather App
- Get weather data for a city using a free API
- Concepts: APIs, JSON, requests library
- Difficulty: Medium
- Extensions: 5-day forecast, weather alerts, multiple cities

5. Password Generator
- Generate strong random passwords
- Concepts: strings, random module, functions
- Difficulty: Easy
- Extensions: GUI, password strength checker, save encrypted passwords

Feel free to ask specific questions about any of these projects! Remember to:
1. Start small and add features gradually
2. Test each piece as you build it
3. Use Google and documentation when stuck
4. Ask for help on r/learnpython if needed

Good luck with your coding journey! 🐍"""

def monitor_subreddit(reddit, subreddit_name="learnpython"):
    """Monitor subreddit for posts about beginner projects."""
    subreddit = reddit.subreddit(subreddit_name)
    
    project_keywords = [
        "beginner project",
        "starter project",
        "project idea",
        "project suggestion",
        "what to build",
        "first project",
        "new to python",
        "learning python"
    ]
    
    print(f"Starting to monitor r/{subreddit_name} at {datetime.now()}")
    print("Looking for posts about beginner projects...")
    
    try:
        for submission in subreddit.stream.submissions():
            title_lower = submission.title.lower()
            selftext_lower = submission.selftext.lower()
            
            is_project_post = any(keyword in title_lower or keyword in selftext_lower 
                                for keyword in project_keywords)
            
            if is_project_post:
                try:
                    already_replied = any(
                        comment.author and comment.author.name == reddit.user.me().name 
                        for comment in submission.comments
                    )
                    
                    if not already_replied and not submission.archived:
                        print(f"\nFound relevant post: {submission.title}")
                        print("Submitting response...")
                        submission.reply(generate_project_response())
                        print("Response posted successfully!")
                        print("-" * 50)
                        
                        # Wait to avoid rate limiting
                        time.sleep(60)
                        
                except Exception as e:
                    print(f"Error responding to post: {e}")
                    time.sleep(60)
                    
    except Exception as e:
        print(f"Error monitoring subreddit: {e}")
        return

def main():
    print("Starting Reddit Bot...")
    try:
        reddit = create_reddit_instance()
        print(f"Successfully logged in as: {reddit.user.me()}")
        monitor_subreddit(reddit)
    except Exception as e:
        print(f"Error initializing bot: {e}")

if __name__ == "__main__":
    main()
