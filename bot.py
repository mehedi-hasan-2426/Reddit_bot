import praw
import time
from datetime import datetime
from config import client_id, client_secret, username, password

def create_reddit_instance():
    """Create and return a Reddit instance."""
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent="python:beginner.project.helper:v1.0 (by /u/your_username)"
    )

def main():
    print("Starting Reddit Bot...")
    try:
        reddit = create_reddit_instance()
        print(f"Successfully logged in as: {reddit.user.me()}")
        # Just to test if it works
        subreddit = reddit.subreddit("learnpython")
        print(f"Connected to r/learnpython")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()