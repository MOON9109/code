

height = [0,1,0,2,1,0,1,3,2,1,2,1]


left=0
right=len(height)-1

maxleft=0
maxright=0
vol =0
while(left<right):
    maxleft = max(maxleft, height[left])
    maxright = max(maxright, height[right])
    if maxleft <= maxright:
        vol = vol + maxleft -height[left]
        left =left+1
    else:
        vol = vol + maxright -height[right]
        right =right-1
print(vol)
        
