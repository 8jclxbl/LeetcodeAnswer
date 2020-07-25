class Solution:
    def numTeams(self, rating):
        rating_length = len(rating)
        i = 0
        count = 0
        while i < rating_length - 2:
            sa = rating[i]
            j = i + 1
            while j < rating_length - 1:
                sb = rating[j]
                k = j + 1
                if sb > sa:
                    while k < rating_length:
                        if rating[k] > sb:
                            count += 1
                            print(sa,sb,rating[k])
                        k += 1
                elif sb < sa:
                    while k < rating_length:
                        if rating[k] < sb:
                            count += 1
                            print(sa,sb,rating[k])
                        k += 1
                j += 1
            i += 1
        return count

    def numTeams_(self, rating):
        rating_length = len(rating)
        i = 0
        count = 0
        while i < rating_length:
            cur = rating[i]

            left_greater = 0
            left_less = 0

            right_greater = 0
            right_less = 0

            for j in range(i):
                if rating[j] < cur:
                    left_less += 1
                elif rating[j] > cur:
                    left_greater += 1

            for j in range(i + 1,rating_length):
                if rating[j] < cur:
                    right_less += 1
                elif rating[j] > cur:
                    right_greater += 1

            count += left_less * right_greater
            count += left_greater * right_less
            i += 1
        
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numTeams([1,2,3,4]))
    print(s.numTeams_([2,1,3]))