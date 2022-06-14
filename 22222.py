a = input()
a1 =a.lower().replace(' ',"").replace(".","").replace(',','').replace(';','').replace(':','').replace('...','').replace('!','').replace('?','').replace('-','').replace('(','').replace(')','').replace('\'','').replace('\"','').replace('–','')
b = a1[:]
c = a1[::-1]
if b == c :
    print(True)
else :
    print(False)
