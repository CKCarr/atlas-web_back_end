Notes on Caching and Learning Objectives
---
___
Cache replacement policies - FIFO

Cache replacement policies - LIFO

Cache replacement policies - LRU

Cache replacement policies - MRU

Cache replacement policies - LFU

Learning Objectives

What a caching system is

What FIFO means

What LIFO means

What LRU means

What MRU means

What LFU means

What is the purpose of a caching system

What limits a caching system have
___
Let's dive into the world of caching systems and their various replacement policies. Understanding these concepts is essential for software development, especially when dealing with performance optimization and resource management.

What is a Caching System?

Definition:
 A caching system temporarily stores data so that future requests for that data can be served faster. The data stored in a cache might be the result of an earlier computation or a duplicate of data stored elsewhere.

Purpose:
The primary purpose of caching is to improve data retrieval performance by reducing the time it takes to access data from the primary storage location, which is often slower.

How it Works:
When data is first read or computed, it is stored in the cache. Subsequent requests can be served from the cache if the data is still there, leading to faster response times.

Cache Replacement Policies
When the cache is full, the system must decide which items to discard to make room for new ones. This decision is guided by a cache replacement policy. Each policy has its own way of determining which items to evict.

FIFO (First-In, First-Out)

Concept: The first items put into the cache are the first ones to be removed.
Usage: It's simple and easy to implement but doesn't consider how frequently or recently items are accessed.
LIFO (Last-In, First-Out)

Concept:
The most recently added items are removed first.
Usage: Rarely used in caching because it tends to remove items that might still be needed.
LRU (Least Recently Used)

Concept:
Evicts the items that haven't been accessed for the longest time.
Usage: More effective than FIFO or LIFO in many scenarios since it's based on the assumption that items used recently are more likely to be used again.
MRU (Most Recently Used)

Concept:
Removes the most recently used items.
Usage: Can be useful in specific scenarios where the most recently used items are less likely to be used again soon.
LFU (Least Frequently Used)

Concept:
 Keeps track of how often items are accessed and removes those with the lowest count.
Usage: Good for scenarios where long-term usage patterns are more important than recent access.

Limits of a Caching System

Size Limitations:
 The size of the cache is limited, meaning it can only store a finite amount of data.

Stale Data:
 If the source data changes and the cache isn't updated, it can return outdated information.

Complexity:
 Implementing and maintaining an efficient cache can be complex, especially when dealing with consistency and synchronization in distributed systems.

Conclusion

Understanding these caching policies helps you design systems that efficiently manage data, balancing between memory usage and performance. Each policy has its context where it excels, and the choice often depends on the specific requirements and behavior of your system. Remember, the ultimate goal of a caching system is to reduce access time and improve system performance.

