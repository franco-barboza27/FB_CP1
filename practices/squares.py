# 1st FB Squares
rts=[3,7,12,25,30,45,50,65,70,85,90,105,110,125,130,145,150,165,170,185,190,205,210,225,230,245,250,265,270,285]
# ^ list  of roots
sqrs=list(map(lambda sqr: sqr*sqr, rts))
# ^ list of perfect squares
i=0
# ^ keeps track of index of squares
for rt in rts:
 # prints each thingy
 print(f"Root:{rt}--->Square:{sqrs[i]}")
 i+=1