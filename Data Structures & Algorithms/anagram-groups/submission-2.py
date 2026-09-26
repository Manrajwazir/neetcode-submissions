class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            count = [0] * 26
            for l in s:
                index = ord(l) - ord('a')
                count[index] += 1
            tuple_key = tuple(count)
            if tuple_key in hashMap:
                hashMap[tuple_key].append(s)
            else:
                hashMap[tuple_key] = [s]


        return list(hashMap.values())
