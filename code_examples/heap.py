import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)
# Remove element from the heap
heapq.heappop(H)
print(H)
# Replace an element
heapq.heapreplace(H,6)
print(H)