from functools import wraps
import time

def retry(max_retries: int = 1, delay: int = 2, exceptions=(Exception,)):
    """
    Retry decorator to retry a function upon exception.

    Args:
        max_retries (int): Number of retries.
        delay (int): Delay in seconds between retries.
        exceptions (tuple): Exception types to catch.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < max_retries:
                        print(f"[Retry] Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"[Retry] Final attempt failed: {e}")
                        raise
        return wrapper
    return decorator