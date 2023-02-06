# Exercise Dir and Help
# string methods
# changing case of each char using lower and upper methods
def changeCase(str):
    str=list(str)
    caseStr=list(map(lambda char: char.upper() if char.islower() else char.lower(),str))
    return ''.join(caseStr) 
string="taha Hussain"
# print(changeCase(string))


# Exercise Python input/output
# (i)
def swap(num1,num2,num3,num4):
    num1,num2,num3,num4=num4,num3,num2,num1
    return num1,num2,num3,num4
a,b,c,d=2,56,78,9
# print(f'Before Swaping\na:{a}, b:{b}, c:{c}, d:{d}')
a,b,c,d=swap(a,b,c,d)
# print(f'After Swaping\na:{a}, b:{b}, c:{c}, d:{d}')

# (ii)
# print("To Convert Celcius to Farhenheit Press 1")
# print("To Convert Farhenheit to Celcius Press 2")

# will check if proper convertor is selected
def tempChecker():
    checkValue=int(input())
    if(checkValue==1 or checkValue==2):
        return checkValue
    print("Press 1 or 2")
    return tempChecker()

# temp=tempChecker()

# will check if proper value is selected
def valueChecker(degree):
    if(degree==1):
        value=float(input("Enter Degrees in Celcius: "))
        if(value>=0 and value <=100):
            return value
        else:
            print("Between 0 to 100")
            return valueChecker(degree)
    else:
        value=float(input("Enter Degrees in Farhenheit: "))
        if(value>=32 and value<=212):
            return value
        else:
            print("Between 32 to 212")
            return valueChecker(degree)

# tempValue=valueChecker(temp)

# convertor function
def tempConvertor(temperature,value):
    if(temperature==1):
        calculated="{:.2f}".format((value*9/5)+32)
        newTemp=f'{calculated} F'
    else:
        calculated="{:.2f}".format((value-32)*5/9)
        newTemp=f'{calculated} C'
    return newTemp

# print(tempConvertor(temp,tempValue))


# Exercise Lists
# (i) using reverse array method
def isPalindrome(str):
    str=list(str.lower())
    onlyAlpha=list(filter(lambda char:char.isalpha(),str))
    alphaString=''.join(onlyAlpha)
    onlyAlpha.reverse()
    return alphaString==''.join(onlyAlpha)
    
# print(isPalindrome("Was it a car or a cat I saw?"))
# (ii)
def firstLast(arr):
    count=0
    for value in arr:
        if(len(value)>=2 and value[0]==value[len(value)-1]):
            count+=1
        else:
            continue        
    return count
exampleCase=['abc', 'xyz', 'aba', '1221']
# print(list(exampleCase[0]))
# print(firstLast(exampleCase))
# Dictionary
# (i) get users according to age using get method
def getUser(useDictionary,age):
    user=[]
    for i in useDictionary:
        if(i.get("age")>=age):
            user.append(i);
    return user if len(user)>1 else "No user"

usersData=[{"name":"Taha","age":19},{"name":"Haris","age":14},
           {"name":"Fouz","age":18},{"name":"Hussain","age":9}]
userAge=int(input("Users above age? "))
print(getUser(usersData,userAge))

# (ii)
def concatDictionary(*arguments):
    concatObj=arguments[0]
    for obj in arguments:
        concatObj.update(obj)
    return concatObj

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(concatDictionary(dic1,dic2,dic3))

# Exercise List Comprehensions

# (i)
def lowerCase(arr):
    newarr=[]
    for string in arr:
        if(len(string)>5):
            newarr.append(string.lower())
        else:
            newarr.append(string)
    return newarr;

exampleString=["TAHA","HUSSAIN","Saleem","ALI","HASAN","FAROOQ"]
# print(lowerCase(exampleString))

# (ii)
def removeElements(arr):
    del arr[0]
    del arr[3]
    del arr[3:]
    return arr
    # return arr[1:4]

# print(removeElements(['Red', 'Green', 'White', 'Black',
#                       'Pink', 'Yellow','Teapink']))

# caesarcipher is an algorithm which moves each
# alphabet in a string to jump times forward
# "a" with jump=1 will become "b"
# e.g 
# input: str=asbcz jump=2
# output: str=cudeb 
def caesarCipher(str,jump):
    lower="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str=list(str)
    answer=""
    for i in range(len(str)):
        if(str[i] in lower):
            if((lower.index(str[i])+jump)>len(lower)):
                temp=lower.index(str[i])+jump
                while(temp>len(lower)):
                    temp-=len(lower)
                answer+=lower[temp]
            else:
                answer+=lower[lower.index(str[i])+jump]
        elif(str[i] in upper):
            if((upper.index(str[i])+jump)>len(upper)):
                temp=upper.index(str[i])+jump
                while(temp>len(upper)):
                    temp-=len(upper)
                answer+=upper[temp]
            else:
                answer+=upper[upper.index(str[i])+jump]
        else:
            answer+=str[i]
    return answer

caesar=str(input("Enter String "))
jumpChar=int(input("Enter Number of characters to jump: "))
print(caesarCipher(caesar,jumpChar))


