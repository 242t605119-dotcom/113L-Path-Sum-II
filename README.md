# LeetCode 113 - Path Sum II

## Problem

Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values is equal to `targetSum`.

A root-to-leaf path starts at the root and ends at a leaf node.

A leaf node is a node that has no left or right child.

## Example 1

### Input

```text
root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
```

### Output

```text
[[5,4,11,2],[5,8,4,5]]
```

### Explanation

There are two root-to-leaf paths whose values add up to `22`:

```text
5 → 4 → 11 → 2
```

and

```text
5 → 8 → 4 → 5
```

Both paths have a sum of:

```text
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

## Example 2

### Input

```text
root = [1,2,3]
targetSum = 5
```

### Output

```text
[]
```

There is no root-to-leaf path whose sum equals `5`.

## Example 3

### Input

```text
root = []
targetSum = 0
```

### Output

```text
[]
```

## Approach

This problem can be solved using **Depth-First Search (DFS)** with recursion.

While traversing the tree, maintain the current path and the remaining target sum.

When a node is visited:

1. Add its value to the current path.
2. Subtract its value from the target sum.
3. Continue searching through the left and right subtrees.
4. If a leaf is reached and the remaining sum is `0`, store the current path.
5. Remove the current node from the path before returning to the previous node.

The last step is called **backtracking** and allows the same path list to be reused for different branches.

## Algorithm

1. Start DFS from the root.
2. If the current node is `None`, stop.
3. Add the current node to the current path.
4. Subtract its value from the remaining target sum.
5. If the node is a leaf and the remaining sum is `0`, save the path.
6. Otherwise, continue recursively through both children.
7. Remove the current node from the path.
8. Return all valid paths.

## Complexity

* **Time Complexity:** `O(n²)` in the worst case because complete paths may need to be copied.
* **Space Complexity:** `O(n)` for the recursion stack, current path, and stored paths.

## LeetCode Details

**Problem Number:** 113
**Problem Name:** Path Sum II
**Difficulty:** Medium
**Topics:** Binary Tree, Depth-First Search, Recursion, Backtracking

## Language

Python 3

## File

`solution.py`

## Author

T.Nandhini
