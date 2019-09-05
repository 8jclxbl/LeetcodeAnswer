class Solution:
    def merge(self, intervals):
        intervals = self.quicksort(intervals)
        print(intervals)
        changed = True
        while 1:
            l = len(intervals)
            temp = []
            changed = False
            i = 0
            while i < l:
                if i + 1 >= l:
                    temp.append(intervals[i])
                    break
                if intervals[i][1] >= intervals[i+1][0]:
                    changed = True
                    if intervals[i][1] >= intervals[i+1][1]:
                        temp.append(intervals[i])
                    else:
                        temp.append([intervals[i][0],intervals[i+1][1]])
                    i += 2
                else:
                    temp.append(intervals[i])
                    i += 1
                
            print(temp)
            if not changed:return intervals
            intervals = temp

                
    def partition(self,intervals):
        piv = intervals[0][0]
        s = 0
        l = len(intervals)
        i = 1
        while i < l:
            if intervals[i][0] < piv:
                s += 1
                intervals[i],intervals[s] = intervals[s],intervals[i]
            if intervals[i][0] == piv:
                if intervals[i][1] < intervals[0][1]:
                    intervals[i],intervals[0] = intervals[0],intervals[i]
                    
            i += 1
        return intervals[1:s + 1], [intervals[0]], intervals[s + 1:]
    
    def quicksort(self,intervals):
        if len(intervals) <= 1:return intervals
        else:
            left,mid,right = self.partition(intervals)
            return self.quicksort(left) + mid + self.quicksort(right)

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]))