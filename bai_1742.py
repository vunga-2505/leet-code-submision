class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * 46
        for i in range(lowLimit, highLimit+1):
            box_num = sum(int(digit) for digit in str(i))
            boxes[box_num] += 1
        max_balls = max(boxes)
        return max_balls