class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = [0, 0] #[5 bill, 10 bill]
        for i in bills:
            if i == 5:
                pocket[0] += 1
                continue
            if i == 10:
                if pocket[0] == 0:
                    return False
                pocket[0] -= 1
                pocket[1] += 1
                continue
            if i == 20:
                if pocket[0] >= 1 and pocket[1] >= 1:
                    pocket[0] -= 1
                    pocket[1] -= 1 
                    continue
                elif pocket[0] >= 3:
                    pocket[0] -= 3
                    continue
                return False
            return False
        return True
        