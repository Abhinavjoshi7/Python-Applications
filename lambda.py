x = lambda x : x+5
print(x(2))

x = [1,2,3,4,5,6,7,8,9,10,11,25,65,6,481,32,1,65,68]
#add two to each list element
mp = map(lambda i: i+2, x)
print(list(mp))
#only get the even items
mp = filter(lambda i: i%2==0, x)
print(list(mp))


