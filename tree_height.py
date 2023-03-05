import sys
import threading
import numpy

def compute_height(n, parents):
    # Create an array to store the height of each node
    heights = [0] * n
    
    # Traverse the tree starting from each node to compute its height
    for i in range(n):
        node = i
        height = 0
        while node != -1:
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = parents[node]
        heights[i] = height
    
    # The height of the tree is the maximum height of its nodes
    return max(heights)


def main():
    # Read input from the keyboard
    n = int(input())
    parents = list(map(int, input().split()))
    
    # Compute the height of the tree and output the result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
