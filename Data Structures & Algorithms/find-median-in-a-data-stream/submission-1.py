import bisect 
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        idx = bisect.bisect_left(self.nums, num)
        new_nums = self.nums[:idx]
        new_nums.append(num) 
        for i in range(idx, len(self.nums), 1): 
            new_nums.append(self.nums[i])
        self.nums = new_nums.copy()

    def findMedian(self) -> float:
        length = len(self.nums) 
        if length % 2 == 1: 
            return self.nums[length//2]
        else: 
            return (self.nums[length//2] + self.nums[(length//2)-1]) / 2
        