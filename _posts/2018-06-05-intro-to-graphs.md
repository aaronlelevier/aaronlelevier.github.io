---
layout: post
title: Intro to Graphs
tags: [Graphs, Algorithms, Data Structures, Neo4j]
---

The goal of this blog post is to distill down my learning of Graph Theory. The following learning took about 8 hours of my time, so if I can give it to someone in a single blog post with links for further reading, then I hope that I'm adding value to the reader.

I initially did this research before getting into [Neo4j](https://neo4j.com/), the most widely used graph database. I like to use motivation of doing something new to also learn new things in that area, so it becomes a richer learning experience.

At the time of this writing, the [AWS Neptune](https://aws.amazon.com/neptune/) graph database has recently been made publicly available, so this blog post is potentially more relevant.

# What is a Graph?

A [Graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) is a finite [set](https://en.wikipedia.org/wiki/Set_theory) of connected [nodes](https://en.wikipedia.org/wiki/Vertex_(graph_theory)). These nodes are connected by [edges](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#edge).

In the below graph. Each number is a node. Each line connecting them is an edge.

![Imgur](https://i.imgur.com/iE31kn3.png)

## Nodes

A [node](https://en.wikipedia.org/wiki/Vertex_(graph_theory)) is a connected object in the graph. They can also called a *vertex* (singular) or *vertices* (plural).

Nodes should have a unique identifier, such as a name or id. They can also store any other amout of arbitrary information. In a social graph, for example, a node would be a person. In a computer network, different machines would be nodes, their IP address or host name could be a unique identifier of the node.

## Edges

An [edge](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#edge) is the connection between two nodes.

An edge can also be called an *arc* or a *line*.

Edges can be *directed* or *undirected* (more on this later).

Edges can store information as well. In the case of a social graph, they may store information like how long two people have been connected. In a computer network graph, they could store connection protocols.

## Incidents

![Imgur](https://i.imgur.com/TiWWQpR.png)

### Incident vertices

*Incident vertices* are vertices that an edge connects. In the above graph, edge `e`'s incident vertices are `{U,V}`

### Incident edge

An *incident edge* is the edge that connects a pair of vertices. Above, `{U,V}`'s incident edge is `e`

Wikipedia Reference: [https://proofwiki.org/wiki/Definition:Incident_(Graph_Theory)/Undirected_Graph)](https://proofwiki.org/wiki/Definition:Incident_(Graph_Theory)/Undirected_Graph)

Stack Overflow reference: [https://stackoverflow.com/a/16886038](https://stackoverflow.com/a/16886038)

# Types of Graphs

There are two main types of graphs. Undirected and Directed. This section discusses these in more detail.

## Undirected Graph

![Imgur](https://i.imgur.com/Kt78Dph.jpg)

[Undirected graphs](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph) are connected graphs, but their is no direction to those connections. There isn't a direction though between the nodes.

An example of this is **LinkedIn**. People have connections, or edges in graph theory terminology, but there is not direction to the relationships.

Undirected graphs can be represented as a list of unordered pairs that represent all connections making up the graph.

## Unidirectional Graphs

![Imgur](https://i.imgur.com/xpuQ40X.png)

There are 2 types of [directed graphs](https://en.wikipedia.org/wiki/Directed_graph). The first is a unidirectional graph. This type of directed graph has relationships that go in a single direction. 

An example of this would be an organizational hierarchy. An employee has a boss, or maybe more than one if he or she is so lucky, but you can't be someone's boss and that person also be your boss.

Directed graphs can be represented as a list of ordered pairs.

Here, *edges* can be called directed edges, arrows, or directed (arcs, lines).

This type of graph is also known as an *oriented graph*.

## Bidirectional Graphs

![Imgur](https://i.imgur.com/CZHWvtP.png)

A [bidirectional graph](https://en.wikipedia.org/wiki/Bidirected_graph) is a directed graph, where edges can be directed in both directions.

An example of this is Twitter. In Twitter you can follow someone, and they can follow you. In this case the relationship could be in both directions, but not necessarily.

# Graph Matricies

Different types of matrices can be used to represent a single graph's information. These matricies can be used to compute different information and for performant lookups.

It is importatant to note that a single matrix may or may not be an [isomophism](https://en.wikipedia.org/wiki/Isomorphism) of the graph. This means that all information about the graph may not be represented in a single matrix. Diagonal matrices, for example, tell the number of incoming edges per node, but not which nodes are connected.

## Adjacency Matrix

![Imgur](https://i.imgur.com/L84sNRM.gif)

An [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) is a square matrix that tells which nodes are connected by displaying a `1` if connected, or `0` if not connected.

In an *undirected* graph, as the above pictures, this matrix is symmetric.

For *directed graphs*, the adjacency matrix will have a `1` denoting the direction of the incoming edge, otherwise `0`, so the matrix is most likely not symmetric.

### Coding challenge example

I came accross an *adjacency matrix* in a coding challenge as part of a job interview. The challenge was to take a `3x3` matrix of unique random values from `1-9`. And, then be able to accept a sequence of values, and say how many steps it takes to traverse back and forth on this random `3x3` grid where positions to traverse is a random sequence as well. An adjacent position is `1` step, otherwise it's `2` steps.

Here's a concrete example of this problem:

```
# Rando 3x3 grid
[[2, 5, 9],
 [1, 8, 3],
 [4, 6, 7]]
 
How may steps does it take to traverse [2, 5, 8, 3, 4]?
 
Can you take any random grid and also random sequence and comput this?
```

This can be solved by loading the random 3x3 data into an *adjacency matrix*. The adjacent positions in the grid are connections, or `1`'s, otherwise they are `0`'s. An adjacency matrix can be used as a lookup to solve how many steps it takes.

And *adjacency list* could also be used.

## Degree Matrix

![Imgur](https://i.imgur.com/LjEt3p3.png)

A [degree matrix](https://en.wikipedia.org/wiki/Degree_matrix) is a diagonal matrix that says the degree of the vertices. The degree of a vertex is the number of it's incidence edges. The vertices are plotted on the rows and columns.

In the above matrix, vertex `1` in the top left most position has a degree of `4` *incidence edges*, edge `2` has degree of `3`, and so on.

## Incidence Matrix

![Imgur](https://i.imgur.com/hWR9bX0.png)

### Inidence Matrix of above graph

The columns are the edges, and the rows are the nodes. Edge `e1` in column `1` is the incidence edge of vertices `{1,2}`, `e2` is the incidence edge for vertices `{1,3}`, and so on.

```
[[1, 1, 1, 0],
 [1, 0, 0, 0],
 [0, 1, 0, 1],
 [0, 0, 1, 1]]
```

A [incidence matrix](https://en.wikipedia.org/wiki/Incidence_matrix) is a matrix that says which edges connect which nodes by plotting the incidence edges as `1`'s, otherwise `0`'s.

Incidence matrices are square if the number of vertices equals the number of nodes, otherwise they're non-square.

### Directed Incidence Matrix

For *unidirectional graphs* these are represented with a `-1` for outgoing edges, `1` for incoming edges, otherwise `0`.

For a *bidirectional graph* they follow the same rules as a unidirectional incidence matrix, except for incoming and outgoing endges between nodes, the data is represented by a `2`

## Adjacency List

![Imgur](https://i.imgur.com/hWR9bX0.png)

### Adjacency list of the above graph

The rows represent a node and the columns are the connected nodes values.

```
[[2, 3, 4],
 [1],
 [1, 4],
 [1, 3]]
```

An [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list) is a list of nodes' adjancent nodes. The first element, `[2, 3, 4]`, is node `1`'s adjacent nodes, the second element, `[1]`, is node `2`'s adjacent nodes, and so on.

# Continued Reading

[Graph Data Structure And Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)

- comprehensive list of graph algorithms

[Neo4j Graph Algorithms](https://github.com/neo4j-contrib/neo4j-graph-algorithms)

- Neo4j at the time of this writing has 300+ algorithms for use with it's graph database

[Directed Acyclic Graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

- These are one particularly interesting naturally occuring type of *unidirectional graph* that is used in project management, and there are software frameworks that implement them as well.

## Example Graph Project

![Imgur](https://i.imgur.com/4yJh6XE.png)

This is from a demo project that I did. It's a *Bidirectional Graph* of my Github followers using  Neo4j, D3.js, and Python Multithreading. Here's the link if anyone's interested:

[https://github.com/aaronlelevier/neo4j-github-followers](https://github.com/aaronlelevier/neo4j-github-followers)

## Conclusion

Graphs are very interesting. They appear in so many places like social networks, machine learning, decision trees, and a lot more. This is really just a quick introduction. There are many sub-types of graphs within the above three main categories of graphs mentioned.

This research was originally part of my pre-research in order to learn more about graphs before trying out [Neo4j](https://neo4j.com/), the largest graph database platform. I first saw Neo4j as recommended experience to have on a job posting, and I didn't know what it was, so I started to look into it. This research was in my spiral notebook, so now it's public for other's if they're intersted.

Thank you for reading. Happy coding!

