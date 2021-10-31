---
layout: post
title: Thoughts on the InfoQ talk Netflix Networking Beating the Speed of Light with Intelligent Request Routing
tags: [Networking, Netflix, InfoQ, Talks]
---

This blog is about my thoughts on the InfoQ talk:
*Netflix Networking: Beating the Speed of Light with Intelligent Request Routing*<sub>1</sub>. This is a top notch talk. Even if you are not into networking, you can learn something from the methodologies discussed in this talk. After listening to this talk, I was like "wow!", and so I just want to share some thoughts on the talk as they relate to myself and other learning.

## Summary

The talk is 38 minutes long including Q&A, so let me first summarize the talk. The talk is about improving Netflix streaming speeds using networking by intelligently either connecting to the Cloud or a CDN endpoint. This is done by using an agent installed on Netflix clients to measure and compare DNS Resolver response times, and then this data is aggregated and analyzed, and DNS is updated to direct the client to either the Cloud or CDN, whichever is faster.

## Thoughts

I listened to this talk while driving, and did not see all the diagrams, so my summary may be overly vague for certain points. With that said, what really impressed me about this talk is that the speakers used their knowledge of networking and the empirical process to make hypotheses, prototype, analyze results, and then repeat. 

I am currently reading the book *TCP Illustrated*<sub>2</sub> and am about two thirds done. Having some of the networking knowledge from the book, I was impressed how they use Anycast addresses<sub>3</sub> networking for the CDN to provide the best service based upon location.

They also discussed how they have about 200k DNS Resolver<sub>4</sub> IPs that they store when they build the DNS map that is used for the intelligent routing, and this data pipeline refreshes every 10 minutes. This was a pretty interesting statistic after reading the DNS chapter in *TCP Illustrated*<sub>2</sub>, also because Internet routes change over time, so the mapping must be updated on some interval.

Building in a failure mode to the service. This was a particularly interesting point that the service will fall back to the default if it fails. They noted how this is critical for the service to be resilient and make the change on such a large scale.

## Beyond Networking

The part in the talk about time to integrate their service and make it to production was also super interesting. They did experiments in production to analyze traffic before their service went live, then did Canary tests, A/B tests, and progressive rollouts.

## Conclusion

I recommend this talk. Even the Q&A was really good.

## References

[1] - [Netflix Networking: Beating the Speed of Light with Intelligent Request Routing](https://youtu.be/7AO4t7G8Bmk)

[2] - [TCP Illustrated](https://en.wikipedia.org/wiki/TCP/IP_Illustrated)

[3] - [Anycast Address Networking](https://en.wikipedia.org/wiki/Anycast)

[4] - [DNS Resolver](https://en.wikipedia.org/wiki/Domain_Name_System#DNS_resolvers)

