import praw

def redditConnect():
    reddit = praw.Reddit(
        client_id="vZDRFX6xilbb22_qBJJYGw",
        client_secret="bPRv0EkK4vuHMLh2xYG-Pyt7o3h7dw",
        user_agent="bot",
        username="",  
        password="",  
    )

    print(reddit.read_only)
    return reddit

def printPost(redditCon, subreddit):
    for submission in redditCon.subreddit(subreddit).new(limit=10):
        print(submission.title)


if __name__ == '__main__':
    printPost(redditConnect(), 'KSI')
