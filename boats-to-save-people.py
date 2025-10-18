class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        light,heavy = 0,len(people) - 1
        while light <= heavy:
            boats += 1
            weight_heavy = people[heavy]
            weight_light = people[light]
            if weight_heavy + weight_light <= limit:
                light += 1
            heavy -= 1  
        return boats
