#ascii values are in reverse order
s = input("Enter a string: ") #01 31 15 05 94 101 411 101 401 611 111 801 801 101 401
#reverse the string  
s = s[::-1] # 104 101 108 108 111 116 104 101 114 101 49 50 51 13 10
print(s)
i = 0
result = ""
while(i<len(s)-1):
    x = s[i] + s[i+1] #combine the first and second values like 1 and 0 as string "10"
    if x=="32": #32 in ascii is a space
        result = result + " " #add as a result
    elif int(x) in range (65,91) or int(x) in range(97,100):
        res = res + chr(int(x)) #chr converts the numeric value into its representing ascii value 
        
        