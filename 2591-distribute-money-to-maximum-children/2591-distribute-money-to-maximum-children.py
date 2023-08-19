class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
       
        if money < children:
            return -1
        
        # Assign 1$ to every child
        money -= children 
        
        # getting count of 7 i.e(7+1) for each student
        count = money // 7

        # amount remaining after giving 7 i.e(7+1) to every child
        remaining = money - (count * 7)

        if count > children:
            #We have to give one child more than 8$
            return children - 1
        elif count < children:
            if remaining == 3 and children - count == 1:
                # Because we cannot give 4 to any child 
                return count - 1
            else:
                return count
        elif count == children and remaining != 0:
            # Again we have to give extra amount to one child
            return count - 1
        else:
            return count