from utils.fetch_news import fetch_latest_ft_articles
from utils.logger import get_logger
from utils.rewrite_post import rewrite_as_social_post
from utils.output_handler import (print_to_console, save_to_json,)

logger = get_logger()

def main():
    try:
        articles = fetch_latest_ft_articles(limit=5)
    except Exception as e:
        logger.error(f"Extraction of latest articles failed: {e}")

    if not articles:
        logger.warning("No articles found to process.")
        return None

    rewritten_posts = []
    for i, article in enumerate(articles, start=1):
        logger.info(f"Rewriting article {i}: {article['title']}")

        try:
            rewritten_post = rewrite_as_social_post(article)
            rewritten_posts.append({
                "original": article,
                "rewritten": rewritten_post
            })
            logger.info(f"Rewritten Post {i} generated.")
        except Exception as e:
            logger.error(f"GPT rewriting failed for article {i}: {e}")
    print_to_console(rewritten_posts)
    save_to_json(rewritten_posts)

if __name__ == "__main__":
    main()
