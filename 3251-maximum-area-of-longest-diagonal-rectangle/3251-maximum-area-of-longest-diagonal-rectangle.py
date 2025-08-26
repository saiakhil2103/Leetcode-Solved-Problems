class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        import math 
        answer=0
        area=0
        for dimension in dimensions:
            curr=math.sqrt((dimension[0]*dimension[0])+(dimension[1]*dimension[1]))
            if curr>answer:
                answer=curr
                area=dimension[0]*dimension[1]
            elif curr==answer:
                curr_area=dimension[0]*dimension[1]
                if curr_area>area:
                    area=curr_area
                    answer=curr 
        return area 