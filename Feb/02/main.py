class Solution(object):
    def check(self, nums):
        x = 0
        length = len(nums)

        temp = []
        while x < length : 
            temp = self.rotate(nums,x,length)
            if self.is_sorted(temp,length) : return True
            x += 1

        return False


    def is_sorted(self,arr,length = -1):
        if length == -1 : length = len(arr)

        for i in range(length-1) : 
            if arr[i] > arr[i+1] : return False

        return True
        
    def rotate(self,arr,x,length = -1) : 
        if length == -1 : length = len(arr)

        result = []
        for i in range(length) :
            result.append(arr[(i+x) % length])
        return result

if __name__ == "__main__" : 
    nums = [2,1,3,4]
    s = Solution()
    print(s.check(nums))