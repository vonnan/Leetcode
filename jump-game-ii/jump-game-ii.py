class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([0])
        seen = set([])
        jump, n= 0, len(nums)
        while q:
            m = len(q)
            for _ in range(m):
                pos = q.popleft()
                if pos >= n-1:
                    return jump
                for j in range(pos + 1, pos + nums[pos] + 1):
                    if j >= n-1:
                        return jump + 1
                    if j not in seen:
                        seen.add(j)
                        q.append(j)
            jump += 1
        return jump
        