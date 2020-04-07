class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = dict()
        for st in strs:
            k = answer.keys()
            tst = tuple(sorted(st))
            if tst in k:
                answer[tst].append(st)
            else:
                answer[tst] = [st]
        return list(answer.values())


    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list) # 기본값이 list인 defaultdict 생성
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()