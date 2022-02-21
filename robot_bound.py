class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # cause facing the north 
        dirX , dirY = 0, 1
        x = y = 0
        for i in instructions:
            if i=="G":
                x , y = x+dirX , y+dirY
            elif i=="L":
                dirX, dirY = -1*dirY, dirX
            else:
                dirX, dirY = dirY, -1*dirX
        return (x,y)==(0,0) or (dirX,dirY)!=(0,1)