class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)

        arr1_count = defaultdict(int)

        end = []

        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            else:
                arr1_count[n] += 1
        end.sort()

        print(arr1_count)

        res = []
        for num in arr2:
            for count in range(arr1_count[num]):
                res.append(num)
        return res + end



        


            






