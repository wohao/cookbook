import heapq 
nums = [1,8,12,23,7,-4,-5,90]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

heapq.heapify(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))