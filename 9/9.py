class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # converting to string:
        # x = str(x)
        
        # for i in range(len(x)//2):
        #     if x[i] != x[(len(x)-1)-i]:
        #         return False
        # return True

        # without converting to string:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        divider = 1
        while x >= 10 * divider:
            divider *= 10

        print(f'divider={divider}')
        while x:
            print(f'x={x}')
            left = x // divider
            right = x % 10

            if left != right:
                return False
            
            x = (x % divider) // 10
            divider /= 10
        return True