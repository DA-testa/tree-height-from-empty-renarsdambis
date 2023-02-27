import sys
import threading
import numpy

def compute_height(n, parents):
    """
    Computes the height of a tree given its number of nodes and parent array.
    """
    # Create a dictionary to store each node's parent and its children
    tree = {i: [] for i in range(n)}
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    # Compute the height of the tree using DFS
    def dfs(node):
        if not tree[node]:
            return 0
        heights = []
        for child in tree[node]:
            heights.append(dfs(child))
        return max(heights) + 1

    return dfs(root)

def main():
    # Get input from the user
    filename = input("Enter the input file name: ")
    while 'a' in filename:
        filename = input("Please enter a file name without the letter 'a': ")
    try:
        with open(filename) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    except:
        print("Error: File not found or invalid input")
        return

    # Compute the height of the tree and output the result
    print("Height of the tree:", compute_height(n, parents))

if __name__ == '__main__':
    # Increase recursion limit and stack size
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)

    # Start the main function in a new thread
    threading.Thread(target=main).start()
