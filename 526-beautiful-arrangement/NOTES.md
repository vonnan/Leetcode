```
nums = [i for i in range(1, N + 1)]
self.res = 0
def helper(nums, tmp):
if not nums:
self.res += 1
else:
for i in range(len(nums)):
if nums[i] % (len(tmp) + 1) == 0 or (len(tmp) + 1) % nums[i] == 0:
helper(nums[:i] + nums[i + 1:], tmp + [nums[i]])
helper(nums, [])
return self.res
```