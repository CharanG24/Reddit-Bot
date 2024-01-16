Overview
The Reddit Bot: Post Printer is a simple Python script designed to fetch and print posts from specified subreddits. The bot utilizes the Reddit API to retrieve posts and outputs them in a readable format.

Features
Fetches the latest posts from specified subreddits.
Prints post details, including title, author, and URL.
Customizable subreddit list.

Set up Reddit API credentials:

Create a Reddit App at https://www.reddit.com/prefs/apps.

Obtain the client_id, client_secret, user_agent, username, and password.

Update the config.py file with your credentials:

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'your_user_agent'
USERNAME = 'your_username'
PASSWORD = 'your_password'
