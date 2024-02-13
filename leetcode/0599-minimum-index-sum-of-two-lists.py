class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = []
        min_value = float('Inf')
        for i, string1 in enumerate(list1):
            for j, string2 in enumerate(list2):
                if string1 == string2:
                    common_strings.append((string1, i+j))
                    if i+j < min_value:
                        min_value = i+j
                    break
        answer = [s[0] for s in common_strings if s[1] == min_value]
        return answer

        
