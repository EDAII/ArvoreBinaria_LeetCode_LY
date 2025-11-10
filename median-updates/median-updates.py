import heapq

def median(s, x):
    max_heap = []
    min_heap = []
    count = {}
    
    def rebalance():
        while len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        while len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
    
    def get_median():
        total = sum(count.values())
        if total == 0:
            return None
        
        max_heap.clear()
        min_heap.clear()
        
        for num, freq in count.items():
            for _ in range(freq):
                if not max_heap or num <= -max_heap[0]:
                    heapq.heappush(max_heap, -num)
                else:
                    heapq.heappush(min_heap, num)
                rebalance()
        
        if len(max_heap) == len(min_heap):
            med = (-max_heap[0] + min_heap[0]) / 2
            if med == int(med):
                return int(med)
            return med
        else:
            return -max_heap[0]
    
    for i in range(len(s)):
        op = s[i]
        val = x[i]
        
        if op == 'r':
            if val not in count or count[val] == 0:
                print("Wrong!")
            else:
                count[val] -= 1
                if count[val] == 0:
                    del count[val]
                
                med = get_median()
                if med is None:
                    print("Wrong!")
                else:
                    print(med)
        else:
            count[val] = count.get(val, 0) + 1
            med = get_median()
            print(med)

N = int(input())
s = []
x = []
for i in range(0, N):
    tmp = input().strip().split(' ')
    a, b = [xx for xx in tmp]
    s.append(a)
    x.append(int(b))
median(s, x)