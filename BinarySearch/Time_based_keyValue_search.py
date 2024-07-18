class TimeMap:

    def __init__(self):
        self.time_map= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key,[])
        l,r = 0,len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][0] <=timestamp:
                l = mid+1
                res= values[mid][1]
            else:
                r = mid-1
        return res
        
