#!/usr/bin/env python3
"""
This module contains the Cache class and supporting functions
for managing data storage and retrieval in Redis.
"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to manage storing and retrieving data in Redis.
    Includes features like counting calls, storing call history,
    and replaying method history.
    """

    def __init__(self):
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count how many times a method is called.
        The count is stored in Redis.
        
        Args:
            method (Callable): The method being wrapped.
        
        Returns:
            Callable: The wrapped method with call counting.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs of a method.
        
        Args:
            method (Callable): The method being wrapped.
        
        Returns:
            Callable: The wrapped method with input/output history stored.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = method.__qualname__ + ":inputs"
            output_key = method.__qualname__ + ":outputs"

            self._redis.rpush(input_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(result))

            return result
        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        
        Args:
            data (Union[str, bytes, int, float]): The data to store.
        
        Returns:
            str: The key where the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally convert it using a given function.
        
        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable]): Optional function to convert the data.
        
        Returns:
            Union[str, bytes, int, float]: The retrieved data, optionally converted.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve a string value from Redis.
        
        Args:
            key (str): The key to retrieve.
        
        Returns:
            str: The retrieved string value.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer value from Redis.
        
        Args:
            key (str): The key to retrieve.
        
        Returns:
            int: The retrieved integer value.
        """
        return self.get(key, fn=int)

    @staticmethod
    def replay(method: Callable) -> None:
        """
        Display the history of calls to a method.
        
        Args:
            method (Callable): The method to replay the history of.
        
        Returns:
            None: Displays the history of method calls.
        """
        self = method.__self__
        redis = self._redis

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        inputs = redis.lrange(input_key, 0, -1)
        outputs = redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_, output in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{input_.decode('utf-8')}) -> {output.decode('utf-8')}")


if __name__ == "__main__":
    cache = Cache()

    # Store some values
    key1 = cache.store("Hello, Redis!")
    key2 = cache.store(1234)

    # Retrieve values with type conversion
    print(cache.get_str(key1))  # Should print "Hello, Redis!"
    print(cache.get_int(key2))  # Should print 1234

    # Replay the history of the store method
    Cache.replay(cache.store)
