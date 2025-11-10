from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = sum(count)
        median_pos1 = (total - 1) // 2
        median_pos2 = total // 2
        cum = 0
        median_left = median_right = 0

        for i, c in enumerate(count):
            cum += c
            if cum - 1 >= median_pos1 and median_left == 0:
                median_left = i
            if cum - 1 >= median_pos2:
                median_right = i
                break

        median = (median_left + median_right) / 2

        return [
            float(next(i for i, c in enumerate(count) if c > 0)),  
            float(next(i for i in reversed(range(len(count))) if count[i] > 0)),  # max
            float(sum(i*c for i, c in enumerate(count)) / total),  # mean
            float(median),  # median
            float(max(range(len(count)), key=count.__getitem__))  # mode
        ]
