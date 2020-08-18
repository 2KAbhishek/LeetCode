class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0] * num_people
        i = 0
        loops = 0
        while candies > 0:
            if (i == num_people):
                loops += 1
                i = 0
            cur_candy = (loops * num_people) + (i + 1)
            if candies - cur_candy < 0:
                people[i] += candies
            else:
                people[i] += cur_candy
            candies -= cur_candy
            i += 1
        return people
        # people = num_people * [0]
        # give = 0
        # while candies > 0:
        #     people[give % num_people] += min(candies, give + 1)
        #     give += 1
        #     candies -= give
        # return people

