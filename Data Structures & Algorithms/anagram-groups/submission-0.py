class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap, where the keys will be in SORTED order, so we have a consistent way to 
        # determine if two strings are anagrams (nlogn) 

        # "act" --> sort it --> "act"
        # check if sorted version "act" exists as a KEY in our map
        # if not, then add the sorted version as a key, converted to a tuple, mapped to an array with just the unsorted version inside it, so length of the array will be 1
        # if it does, just add the unsorted version inside the value array
        # repeat for other elements
        # "cat" --> sort it --> "act"
            # add "cat" to same array that "act" is currently in 

        # return just the values of our map

        m = {}
        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string in m:
                m[sorted_string].append(string)

            else:
                m[sorted_string] = [string]
        return list(m.values())




