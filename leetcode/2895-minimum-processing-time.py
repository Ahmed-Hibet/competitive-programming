class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)

        max_time = 0
        for i in range(n):
            t = processorTime[i] + tasks[i*4]
            max_time = max(max_time, t)
        return max_time
