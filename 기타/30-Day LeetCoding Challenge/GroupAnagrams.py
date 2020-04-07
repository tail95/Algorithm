class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = dict()
        for st in strs:
            tst = tuple(sorted(st))
            answer[tst].append(st)

        ret = list(answer.values())
        return ret

    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)  # default dict 로 기본값이 list로 설정
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()