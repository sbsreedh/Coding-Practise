class Solution:
    def frequencySort(self, s: str) -> str:
        """ Returns string with characters sorted by their frequency
        in decreasing order.
        Time complexity: O(N+Klog(K)) # Where N is the length of original string, K is the number of unique characters in the string.
        Space complexity: O(n), where
        n is len(string).

        """
        freq = collections.Counter(s)  # character frequency hash map
        # for char in string:
        #     if char in freq:
        #         freq[char] += 1
        #     else:
        #         freq[char] = 1
        # convert hash map to list of tuples: (character, fraequency)
        # and sort it by frequency in decreasing order
        # sort in this case is O(1) since max number of characters = 52
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # compose resulting string
        result = []
        for element in freq:
            result.append(element[0] * element[1])
        return "".join(result)
    
