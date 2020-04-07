import collections
class Solution:
    def countElements(self, arr: List[int]) -> int:    
        answer = 0
        counting = collections.defaultdict(int)
        for num in arr:
            counting[num] += 1
        keys = counting.keys()
        for k,v in counting.items():
            if k+1 in keys:
                answer += counting[k]
        return answer