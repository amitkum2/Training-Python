## Adding lall the elements of list
sum=0
list11=[1,2,3,45,55,5555]
for x in list11:
    sum +=x

print(sum)

## Multiplying lall the elements of list
mul=1
lista=[1,2,3,45,55,5555]
for x in lista:
    mul *=x

print(mul)

# largest  number
def maxfn(List):
    max= List[0]
    for x in List:
        if x>max:
            max=x
    return max

print(maxfn([1,2,3,45,55,5555]))


#smallest number

def minfn(List1):
    max=List1[0]
    for x in List1:
        if x<max:
            max=xt
    return max

print(minfn([2,3,4,22,33]))

#length of lest
print(len(lista))

# to find strings in list with mless than 4 char

def charfn(n,List):
    word=[]
    for x in List:
        if len(x)<= n:
            word.append(x)
    return word

print(charfn(4,['amit','anup','ami','himanshu','devansh']))


#cant add dupicate values to the list

b={1,2,3}

b.add(4)

print(b)

#how to remove duplicates from a list:








