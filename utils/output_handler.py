import json
import os
from datetime import datetime
from typing import List, Dict

from utils.logger import get_logger


logger = get_logger()

def get_json_filename() -> str:
    """Generates a timestamped JSON file path for storing social media posts.

    Returns:
        str: A string representing the full file path in the 'data/' directory,
            with the filename formatted as 'posts-YYYY-MM-DD-HH-MM-SS.json'.
    """
    return os.path.join("data", f"posts{datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')}.json")

def save_to_json(posts: List[Dict[str, str]], filename: str = get_json_filename()) -> None:
    """
    Saves a list of posts to a JSON file.

    Args:
        posts (List[Dict[str, str]]): List of dicts containing 'original' and 'rewritten' fields.
        filename (str): Path to the output file.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved {len(posts)} posts to {filename}")
    except Exception as e:
        logger.error(f"Failed to write JSON: {e}")

def print_to_console(posts: List[Dict[str, str]]) -> None:
    """
    Prints all rewritten posts to the console.

    Args:
        posts (List[Dict[str, str]]): List of dicts containing 'original' and 'rewritten' fields.
    """
    for i, post in enumerate(posts, start=1):
        print(f"\n{i}. {post['rewritten']}\n→ {post['original']['link']}\n---")
