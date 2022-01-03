#!/usr/bin/env python3
import praw
from kafka_producer import producer

from config import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, CRYPTO_SUBS


class RedditStreamer():
    def __init__(self, listener):
        self.reddit = praw.Reddit(
            user_agent="The Watcher",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=USERNAME,
            password=PASSWORD,
        )
        self.listener = listener

    def stream(self):
        subreddit = self.reddit.subreddit("+".join(CRYPTO_SUBS))
        for comment in subreddit.stream.comments():
            message = dict(
                date=comment.created_utc,
                author=comment.author.name,
                body=comment.body
            )
            self.listener.send(topic="RedditStreamer", value=message)


if __name__ == "__main__":
    reddit = RedditStreamer(listener=producer)
    reddit.stream()
