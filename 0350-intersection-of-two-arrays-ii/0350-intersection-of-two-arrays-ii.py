class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1,s2 = len(nums1), len(nums2)
        l,r=0,0
        nums1.sort()
        nums2.sort()
        result = []
        while(l<s1 and r<s2):
            if(nums1[l] == nums2[r]):
                result.append(nums1[l])
                l+=1
                r+=1
            elif(nums1[l]>nums2[r]):
                r+=1
            else:
                l+=1
        return result
        