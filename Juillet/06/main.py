class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1=len(nums1)
        self.arr1=nums1
        self.n2=len(nums2)
        self.arr2=nums2
        self.freq=Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old=self.arr2[index]
        self.freq[old]-=1
        if self.freq[old]==0:
            del self.freq[old]
        self.arr2[index]+=val
        nval=self.arr2[index]
        self.freq[nval]+=1

    def count(self, tot: int) -> int:
        count=0
        for a in self.arr1:
            if tot -a in self.freq:
                count+=self.freq[tot-a]
        return count
