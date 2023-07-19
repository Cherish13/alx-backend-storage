## 0x02. Redis basic

### Redis Basic
This project contains tasks for learning to use the Redis NoSQL data storage application through Python3.

### Tasks

### Task 0
Writing strings to Redis
* Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

* Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

* Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

### Task 1
Reading from Redis and recovering original type
* Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

* In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

* Remember to conserve the original Redis.get behavior if the key does not exist.

* Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.

### Task 2
 Incrementing values
 * Familiarize yourself with the INCR command and its python equivalent.

In this task, we will implement a system to count how many times methods of the Cache class are called.

### Task 3
Familiarize yourself with redis commands RPUSH, LPUSH, LRANGE, etc.
* In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.

### Task 4
In this tasks, we will implement a replay function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20