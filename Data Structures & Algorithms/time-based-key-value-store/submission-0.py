class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        l=self.store[key]
        left=0
        right=len(l)-1
        res=-1
        while left<=right:
            mid=left+(right-left)//2
            if l[mid][0] <=timestamp:
                    res=mid
                    left=mid+1
            else:
                right=mid-1
        return l[res][1] if res!=-1 else ""