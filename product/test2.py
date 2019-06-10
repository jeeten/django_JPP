input_str = input()
# while input_str:
e = input_str[0]
m = {}
for e in input_str:
    if  e in m.keys():
        # print('e in ',e)
        m[e] = m[e]+1
    else:
        m.update({e:1})

    
print(max(m)[0])
print(m)       
    


