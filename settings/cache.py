import redis
import os


class Cache:
    def __init__(
        self,
        redis_host=os.environ.get("REDIS_HOST", "localhost"),
        redis_port=os.environ.get("REDIS_PORT", 6379),
    ):
        self.client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, timeout=None):
        self.client.set(key, value, timeout)


cache = Cache()
