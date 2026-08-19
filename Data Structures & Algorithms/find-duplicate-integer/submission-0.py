class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        [1,3,4,2,2]
                  s
                  f
        1 -> 3 -> 2 -> 4
                  ^    |
                   - - -   
        '''

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow
                 