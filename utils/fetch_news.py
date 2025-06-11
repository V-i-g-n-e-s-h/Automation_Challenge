from typing import (List, Dict,)

import feedparser

import const
from .logger import get_logger
from .retry import retry


logger = get_logger()

@retry(max_retries=1, delay=2, exceptions=(Exception,))
def fetch_latest_ft_articles(limit: int = 3) -> List[Dict[str, str]]:
    """
    Fetch latest articles from Financial Times RSS.

    Returns a list of dicts with 'title' and 'summary' keys.
    """
    logger.info("Extracting latest feed from Financial Times")
    feed = feedparser.parse(const.FEED_URL)
    articles = []

    if limit > 10:
        logger.warning("System can only fetch upto 10 documents from the cite.")

    for entry in feed.entries[:limit]:
        title = entry.get("title", "").strip()
        summary = entry.get("summary", "").strip()
        link = entry.get("link", "").strip()

        if title:
            articles.append({
                "title": title,
                "summary": summary,
                "link": link
            })

    return articles
