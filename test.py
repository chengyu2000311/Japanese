def safe_solution(f, cafe):
    from collections import defaultdict, Counter
    graph = defaultdict(Counter)
    for i in range(len(f)):
        fra = f[i]
        safe = cafe[i]
        graph[fra][safe] += 1

    res = 0
    for count in graph.values():
        unsafe = count[0]
        safe = count[1]
        res += safe * unsafe + safe * (safe - 1) // 2
    
    return res 

from typing import List
def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    import heapq
    from collections import Counter
    left_count = Counter()
    right_count = Counter()
    min_heap = nums[:k]
    max_heap = [-x for x in nums[:k]]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    size = k // 2
    mid = 0
    res = []
    for _ in range(size):
        heapq.heappop(min_heap)
        heapq.heappop(max_heap)
    
    if k % 2 != 0 and min_heap:
        mid = heapq.heappop(min_heap)
        heapq.heappop(max_heap)
        res.append(mid)

    for right in range(k, len(nums)):
        left = right - k 
        left, right = nums[left], nums[right]
        left_max, right_min = -max_heap[0], min_heap[0]
        # pop first
        print("left max", left_max, "right_min", right_min)
        if left_max >= left:
            left_count[left] += 1
        elif right_min <= left:
            right_count[left] += 1
        
        print(left_count, right_count)
        while max_heap and left_count[-max_heap[0]]:
            ele = -heapq.heappop(max_heap)
            left_count[ele] -= 1
        
        while min_heap and right_count[min_heap[0]]:
            ele = heapq.heappop(min_heap)
            right_count[ele] -= 1

        print(max_heap, min_heap)
        if left_max >= right:
            heapq.heappush(max_heap, -right)
        elif right_min <= right:
            heapq.heappush(min_heap, right)
        # append then
        if k % 2 != 0:
            if left_max < right < right_min:
                mid = right
            elif len(min_heap) > size:
                mid = heapq.heappop(min_heap)
            elif len(max_heap) > size:
                mid = -heapq.heappop(max_heap)
            res.append(mid)
        
        if k % 2 == 0:
            if len(min_heap) > size:
                res.append(heapq.heappop(min_heap))
            if len(max_heap) > size:
                res.append(-heapq.heappop(max_heap))
            else:
                res.append((min_heap[0] + -max_heap[0]) // 2)
    return res


print(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))