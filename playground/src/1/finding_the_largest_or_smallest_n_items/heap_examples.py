import heapq

nums = [1, 8, 5, -3, 9, 0, 7, 4, -7]
heap = list(nums)
print(nums)
print(list(nums))
heapq.heapify(heap)
print(heap)
popped = heapq.heappop(heap)
print(popped)
print(heap)
heapq.heappush(heap, 5)
print(heap)

print("Minimum of 4,12,43.3,19 and 100 is : ",end="")
print (min( 4,12,43.3,19,100 ) )