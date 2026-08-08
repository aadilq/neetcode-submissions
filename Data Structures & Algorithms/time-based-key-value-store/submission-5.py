class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        valueList = self.dictionary.get(key, "")
        
        res = ""

        L, R = 0, len(valueList) - 1

        while L <= R:
            mid = (L + R) // 2
            if valueList[mid][1] <= timestamp:
                res = valueList[mid][0]
                L = mid + 1
            else:
                R = mid - 1
        return res

        
