Fifteen Puzzle
======

* [Project goal](#project-goal)
* [Introduction](#introduction)
* [Implementation description](#implementation-description)
* [What is needed to run the application](#what-is-needed-to-run-the-application)
* [Results](#results)
* [Conclusions](#conclusions)


Project goal
-------
A console application that uses 3 different graph searching algorithms: DFS, BFS and A* in purpose of solving any initial form of a puzzle loaded from a file.


Introduction
-------
Fifteen is a puzzle game whose board with size of 4x4 consists of a randomly filled tiles with numbers from 1 to 15 and one empty field.
Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically. The goal of the game is to set blocks in ascending order of numbers, just like the picture below:
<br />
<br />
<img src="https://rosettacode.org/mw/images/thumb/7/79/15_puzzle.png/300px-15_puzzle.png" alt="An image that represents correctly solved puzzle" width="250" height="250"/>

Finding a solution to this game comes down to searching the tree, where the root is the initial state of the board
and the following vertices are child states resulted from performing the specified plate shift.
Searching the indicated tree is carried out using 3 different strategies:

### Breadth First Search (BFS)
It starts at the tree root and explores all nodes at the present depth, if it doesn't find a solution to the puzzle at the given level
it is moving on to the nodes at the next depth level. Child nodes that were visited but not explored are stored in the FIFO queue.

### Depth First Search (DFS)

### A* Search (ASTR)


Implementation description 
-------


What is needed to run the application
-------


Results
-------


Conclusions
-------


