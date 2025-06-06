import praw

class AnomalyScraper:
    def __init__(self, client_id, client_secret, username, password, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=user_agent
        )

    def scan(self, subreddit="MandelaEffect", limit=25):
        anomalies = []
        for post in self.reddit.subreddit(subreddit).hot(limit=limit):
            anomalies.append({
                "title": post.title,
                "content": post.selftext,
                "score": post.score,
                "url": post.url
            })
        return anomalies
