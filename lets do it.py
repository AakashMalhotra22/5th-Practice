l = [-1,0,1,2,-1,-2]

ans = []
for i in range(len(l)-2):

    for x in l[(i+2):len(l)]:
         if l[i]+l[i+1]+x ==0:
             ans.append([l[i],l[i+1],x])
         else:
             pass
    l.reverse()
    for y in l[(i + 2):len(l)]:
        if l[i] + l[i + 1] + y == 0:
            ans.append([l[i], l[i + 1], y])
        else:
            pass

print(ans)