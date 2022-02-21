# Fresh Promotion - amazon oa 
'''
Input: 
codeList = [[apple, apple], [banana, anything, banana]] 
shoppingCart = [orange, apple, apple, banana, orange, banana]

Output: True
'''
class solution:
    def freshPromo(self, codeList, shoppingCart):
        # solving using two pointers
        # first pointer for group and second one for codeList
        cartPtr = 0
        codePtr = 0
        while cartPtr <len(shoppingCart) and codePtr<len(codeList):
            # taking groups such as [apple, apple]
            group = codeList[codePtr]
            gPtr = 0
            # going through all the shoppingCart items 
            while gPtr<len(group) and cartPtr<len(shoppingCart):
                # if matches
                if group[gPtr]==shoppingCart[cartPtr] or group[gPtr]=="anything":
                    gPtr+=1
                else:
                    gPtr = 0
                cartPtr+=1
            if gPtr!=len(group):
                return False
            codePtr+=1
        if codePtr<len(codeList):
            return False
        return True
                
if __name__=="__main__":
    codeList = [["apple", "apple"], ["banana", "anything", "banana"]] 
    shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]
    ob = solution()
    print(ob.freshPromo(codeList, shoppingCart))
    