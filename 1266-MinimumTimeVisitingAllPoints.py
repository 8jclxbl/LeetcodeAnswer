class Solution:
    def minTimeToVisitAllPoints(self, points):
        current = points[0]
        steps = 0
        for point in points[1:]:
            x_diff = abs(point[0] - current[0])
            y_diff = abs(point[1] - current[1])
            current = point
            steps += max(x_diff, y_diff)
        return steps
