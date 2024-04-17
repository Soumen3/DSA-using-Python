# Import heapq module for priority queue operations
import heapq

# Define a function that takes an array of integers and an integer k as parameters
def top_k_frequent(nums, k):
  # Create an empty hash table to store the frequency of each element
  freq = {}
  # Iterate over the array and update the frequency of each element in the hash table
  for num in nums:
    freq[num] = freq.get(num, 0) + 1
  # Create an empty priority queue (min-heap) to store the k most frequent elements
  pq = []
  # Iterate over the hash table and push each element-frequency pair into the priority queue
  for num, count in freq.items():
    # If the priority queue has less than k elements, push the pair into the queue
    if len(pq) < k:
      heapq.heappush(pq, (count, num))
    # Else, compare the current pair with the minimum pair in the queue
    else:
      # If the current pair has a higher frequency than the minimum pair, pop the minimum pair and push the current pair
      if count > pq[0][0]:
        heapq.heappop(pq)
        heapq.heappush(pq, (count, num))
  # Create an empty list to store the answer
  ans = []
  # Pop all the pairs from the priority queue and append the elements to the answer list
  while pq:
    ans.append(heapq.heappop(pq)[1])
  # Return the answer list in any order
  return ans

# Test the function with some examples
nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k)) # Output: [1,2]

nums = [1]
k = 1
print(top_k_frequent(nums, k)) # Output: [1]
