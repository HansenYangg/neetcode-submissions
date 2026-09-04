class TimeMap:
    ''' hashmap with key mapped to [[values array],
                                    [timestamps array]]
    set updates our map

    get performs binary search on the timestamps array associated with the key,
    and returns the value associated with timestamp if it exists, otherwise the value 
    that is associated with the largest timestamp_prev < timestamp

    '''
    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key][0].append(value)
            self.m[key][1].append(timestamp)
        else:
            self.m[key] = [[value], [timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.m:
            timestamps_arr = self.m[key][1]
            l, r = 0, len(timestamps_arr) - 1
            biggest = -1
            while l <=  r:
                m = (r + l) // 2
                if timestamps_arr[m] == timestamp:
                    return self.m[key][0][m]
                if timestamps_arr[m] > timestamp:
                    r = m - 1
                if timestamps_arr[m] < timestamp:
                    biggest = max(biggest, m)
                    l = m + 1
            if biggest != -1:
                return self.m[key][0][biggest]
            return ""



        else:
            return ""
        
