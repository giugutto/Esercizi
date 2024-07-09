# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solutions:
    def reverse(self, x: int) -> int:
        lista_numeri= [1,2,3,4,5,6,7,8,9]
        stringa_rovescio = ''
        iniziale = ''
        for num in str(x):
            if num in lista_numeri:
                stringa_rovescio += num
            else:
                iniziale += num
        if iniziale:
            self.x = sorted(stringa_rovescio, reverse= True)
        elif iniziale == '':
            self.x = sorted(stringa_rovescio, reverse= True)    
        sorted(str(x), reverse=True)


class Solutions:
    def reverse(self, x: int) -> int:
        lista_numeri = ['1','2','3','4','5','6','7','8','9']
        stringa_rovescio = ''
        iniziale = ''
        for num in str(x):
            if num in lista_numeri:
                stringa_rovescio += num
            else:
                iniziale += num
        
        # Reverse the numeric part
        reversed_string = ''.join(sorted(stringa_rovescio, reverse=True))
        
        # Combine with initial part if it exists
        result_string = iniziale + reversed_string
        
        # Convert back to integer
        return int(result_string)
    

x = Solutions()
print(x.reverse(-456))
###########################
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n 


potenza = Solution()
print(potenza.myPow(2.00000,10))