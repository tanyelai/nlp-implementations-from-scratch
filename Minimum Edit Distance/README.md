## Minimum Edit Distance Algorithm
How do we find minimum edit distance? We can think it's kind of a search task, 
in which we are searching for the shortest path -*a sequence of edits*- from one string to another.\
<br />
 ![image](https://user-images.githubusercontent.com/44132720/132943359-0cee527e-f733-4a8e-ba1d-330102daf65b.png)\
<br />
The space of all possible edits is enormous, so we cannot search naively. However, lots of distinct edit paths will end up in the same state (string), 
so rather than recomputing all those paths, we could just remember the shortest path to a state each time we saw it.
To do that, we use dynamic programming.\
<br />
Let's assume that we define the minimum edit distance between two strings. Given two strings, the source string X of length n and the target string Y of length m. 
Therefore, our edit distance between X, and Y is thus distance[n,m].\
We'll use dynamic programming to compute distance[n,m] bottom up, combining solutions to subproblems.\
<br />

![image](https://user-images.githubusercontent.com/44132720/132943371-45e34352-ada1-43fe-bc50-933c35be1b93.png)
<br />
<br />
<br />

Bottom up:\
• We compute distance(i,j) for small i,j\
• And compute larger distance(i,j) based on previously computed smaller values\
• i.e., compute distance(i,j) for all i(0 < i < n)  and j(0 < j < m)

![image](https://user-images.githubusercontent.com/44132720/132943352-a9c6b729-d1bd-4321-b172-3bf4c8d533d6.png)

<br />
<br />

## Backtrace for computing alignments

Edit distance is not sufficient
- We often need to align each character of the two strings to each other

We do this by keeping a " backtrace "\
Every time we enter a cell, remember where we came from and when we reach the end, 
- Trace back the path from the lower right corner to read off the alignment for our case.

## Adding backtrace to Minimum Edit Distance

![image](https://user-images.githubusercontent.com/44132720/132943659-7d5c5947-6490-4c7f-b8bb-67736e177f24.png)

<br />

## After adding backtrace my outputs for "intention" to "execution"

![image](https://user-images.githubusercontent.com/44132720/132994861-86157961-7c93-4b04-a65e-f1ebd25df444.png)

<br />

## Performance
Time: O(n\*m)\
Space: O(n\*m)\
Backtrace: O(n+m)
<br />


## Weighted Edit Distance

Why would we add weights to the computation?
- Spell Correction: some letters are more likely to be mistyped than others
- Biology: certain kinds of deletions or insertions are more likely than others

#### Confusion matrix for spelling errors

![image](https://user-images.githubusercontent.com/44132720/132943896-ad51db65-d8bd-4f94-bf14-29c7e6ad99a1.png)

<br />

#### Pseudocode for weighted edit distance

![image](https://user-images.githubusercontent.com/44132720/132943921-91cfb619-4d1a-4078-a24a-d8917566da00.png)


