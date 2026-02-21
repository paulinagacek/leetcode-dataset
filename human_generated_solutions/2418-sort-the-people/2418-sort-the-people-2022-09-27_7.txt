class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            tall_index = heights.index(max(heights[i:]))
            names[i], names[tall_index] = names[tall_index], names[i]
            heights[i], heights[tall_index] = heights[tall_index], heights[i]
        return names