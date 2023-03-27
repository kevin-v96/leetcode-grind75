#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [], [], []
        for number in nums:
            if number < 0:
                n.append(number)
            elif number > 0:
                p.append(number)
            else:
                z.append(number)

        #lookups are quicker with sets
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res