class RangeEncoding():
    def minRanges(self, arr):
        if(len(arr) == 0): return 0
        count = 1
        for i in range(1, len(arr), 1):
            if arr[i-1] != arr[i]-1:
                count += 1
        return count
