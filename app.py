#==== 4 String features ====

string = "sabbah eltaj"

#Coverting case to upper
#print(string.upper())

#Coverting case to lower
#print("SABBAH".lower())

#String slicing
#print(string[2:8])


#==== 6 Lists and String justifying ====
food = ['Bananas', 'Apple']

#Inserting items to beginning and end in lists
#Adding to end
food.append('Onions')

#Adding to beginning
food.insert(-len(food), '$$$') # reverse counting & starts from 0
food.insert(0, '$$$')
#print(food)

#Inserting items to beginning and end in string
#In strings called justifying or padding

#left justify
print(string.ljust(20, '%'))

#right justify
print(string.rjust(20, '#'))

#center justify
print(string.center(20, '@'))


#==== 9 Data type conversion ====
studentID = 98432463
students = ['Sabbah', 'Ahmed']

#get type of a var
print(type(studentID)) # is int class

#convert it to string
newID = str(studentID)
print(type(newID)) # will return str class

#convert to hex
print(hex(studentID))

#convert to set
print(set(students))

#convert from real number to complex one
print(complex(studentID))


#==== 10 Code for indentation ====

#creating a list from items
def createArray(*items) :
   return list(items)


result = createArray('sa', 'saaa', 23)
print(result)

#another example
for i in range(10):
   if(i % 2 == 0) :
      print(i)