#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()

def cache_result(expires=10):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Check if the URL is already cached
            cached_result = redis_client.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode()

            # Invoke the original function if the URL is not cached
            result = func(url)

            # Cache the result with the specified expiration time
            redis_client.set(f"cache:{url}", result, ex=expires)

            return result
        return wrapper
    return decorator

@cache_result()
def get_page(url: str) -> str:
    # Simulate slow response using slowwly.robertomurray.co.uk
    response = requests.get(url)
    return response.text
