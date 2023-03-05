import sys
import threading

# Increase the recursion limit and stack size to handle large trees
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

def build_tree(parents):
    n = len(parents)
    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    return tree, root

def compute_height(tree, root):
    if not tree[root]:
        return 1
    heights = []
    for child in tree[root]:
        heights.append(compute_height(tree, child))
    return 1 + max(heights)

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))

    # Build tree and compute height
    tree, root = build_tree(parents)
    height = compute_height(tree, root)

    # Output result
    print(height)

# Start the main thread
threading.Thread(target=main).start()
