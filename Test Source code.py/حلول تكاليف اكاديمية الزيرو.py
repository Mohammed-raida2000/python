
#print('"name: osama"\n"age : 38"\n"country: egypt"' )

#name = "osama"
#age = 38
#country ="egypt"
#print("hellow,""my name is %s and iam %i years old and i live is %s "%(name ,age,country))   #النوع 1
#print("hellow,""my name is {:s}and iam {:d}years old and i live is{:s}".format(name, age, country))#النوع 2
#print(f"hellow,my name is {name} and iam {age} years old and i live is {country}")#النوع 3

#print(type (name))
#print(type (age ))
#print(type (country))

name = "osama"
age = 38
country ="egypt"
print(f' "Hello "{name}" , How You Doing \  """ Your Age Is {age}"" + And Your Country Is: {country}')

#قم بعمل متغير name وبداخله القيمة “Elzero” ثم عن طريق ال Indexing + Slicing 
# قم بجلب الحرف الثاني في اول سطر والحرف الثالث
# في ثاني سطر والحرف الأخير في السطر الثالث, يجب عليك جلب الحرف بطريقة
# دايناميكية حيث أن الكلمة يمكن أن تتغير, شاهد المثال لترى المطلوب


name = 'mohammedjkfhwifhsifq'
print(len(name))

print("Second Letter Is %s ",(name[1]))                                          
print("Third Letter Is %s ",(name[2]))
print("last Letter Is %s ",(name[ len(name)-1 ]))

name = "#@#@Elzero#@#@"
print(name.strip("#@#@"))
print(name.lstrip("#@#@"))

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))
print(len (name_two))
print(name_two.center(20,"#"))
print("-"*50)
mai = "mohammed"
print(mai.center(14,"#"))        #نفس الهاشتاق الي في فيس بك رك يمعلم 
print(mai.center(9,"@"))
print(len(mai))

print("-"*50)

num1 = "19"
num2 = "9"
num3 = "15"
num4 = "130"
num5 = "950"
num6= "1500"
print(num2.rjust(4,"0"))


name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

print("-"*50)
msg = "I Love Python And Although Love Elzero Web School"
print(len(msg))
print(msg.count("Love"))

name = "Elzero"
print(name[2])

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","love"))
print(msg.replace("<3","love",1))

name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is{name}, And My Age Is {age}, And My Country Is country")


num =1+2j
print("Print Imaginary Part Here {} ".format(num.imag))
print("the real number is : {}".format(num.real))

no =2+5j
print("the imag number :{}".format(no.imag))
num = 10
print(float(num))
num = 159.650
print(int(num))


num1 =100
num2 =115
op = num1=-num2
print(op)


friends = ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]  #list

print( "the one method is "+friends[0]) #index
print("the one method is %s "% (friends[0]))
print("the one method is {:s}".format(friends[0]))
print(f"the one method is {friends[0]} ")

print("the one method is  "+friends[-1])
print("-"*50)
print("the one method is %s " % (friends[-1])  )
print("the one method is  {} ".format(friends))
print(friends[0:5:2]) # 0-5 range ,2= قديش يمشي ['Osama', 'Sayed', 'Mahmoud']
print(friends[1:5:2]) #1-5 rang ,2= قديش يمشي ['Ahmed', 'Ali']

print(friends[1:4])    #"Ahmed", "Sayed", "Ali",
print(friends[3:5])

#Ordered \\\\If you add new items to a list, the new items will be placed at the end of the list. 
# EX 
#append(1),clear(1),copy(1),count(),insert(1),extend(1),pop(1),remove(1),reverse(1),sort(1)
friend = ["Osama", "Ahmed", "Sayed","Ahmed"] #list 
friend.append("mai")
print(friend)  #['Osama', 'Ahmed', 'Sayed', 'mai']   الاضافة في الاخر 
friend.insert(0,"rana") #['rana', 'Osama', 'Ahmed', 'Sayed', 'mai']الاضافة في الاول او مكان انتا بدك اياه
print(friend)
shcool= friend.copy()
print(friend)
print(shcool)
friend.clear()
print(friend)
#shcool.count() 
#print(shcool)
a =[1,2,3,4]
a.extend(friend)
print(a)
a.pop(0)
print(a)
friend = ["Osama", "Ahmed", "Sayed","Ahmed"]
friend.remove("Sayed")
print(friend)
friend = ["Osama", "Ahmed", "Sayed","Ahmed"]
friend.reverse()
print(friend)
friend = ["Osama", "Ahmed", "Sayed","Ahmed"]
friend.sort()
print(friend)
x =[ 3,44,5,-1,2,17,33]
x.sort()
print(x)
print("-"*30)

print("-"*30)
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
print(friends)#['Ahmed', 'Sayed', 'Samah', 'Eman']
friends.extend(school)
print(friends)#['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']
print("-"*70)
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort(reverse=True)
print(friends)  
friends.sort(reverse=False)
print(friends)
print(type(friends))
print("-"*70)
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web","js","java"]]
print(type(technologies))
print(technologies[4][0])  
print(technologies[4][4])     
# الفرق بين ال str and tuple One item tuple, remember the comma:
a =("mohammed ")    
print(a[0])  # output:  m
print(type(a)) #<class 'str'>\
    
#<class 'tuple'>     الفرف بس ","
a =("mohammed ",)     
print(a[0])# output:  mohammed 
print(type(a)) #<class 'tuple'>

a = tuple("mo")
print(type(a))
#1Python - Update Tuples
#uples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is databaseeated.

#Convert the tuple into a list to be able to change it:
friends = ("Osama", "Ahmed", "Sayed") #tuple ()
a =list(friends) #[] 
a[0]="elzero"
friends=tuple(a)
print(friends)

#التكليف   03  ///تكليفات الدروس من الدرس 024 إلى 025  
nums = (1, 2, 3)  #tuple ()
letters = ("A", "B", "C")  #tuple ()
list(nums) 
list(letters)
print("nums_and_letters_one ={} ".format(nums +letters)) #tuple ()
#التكليف   01  ///تكليفات الدروس من الدرس26\إلى 032
my_list = (1, 2, 3, 3, 4, 5, 1)
unique_list =[]
my_list
print(unique_list)
print(type(unique_list))
print(unique_list[0:4])

print("-"*40)

nums = {1, 2, 3}   #set
letters = {"A", "B", "C"}
a =list(nums)
b =list(letters)
print(set(a+b))  #1
a.extend(b)
letters = set(a)
print(letters)   #2


print("-"*40)
my_set = {1, 2, 3} #set()
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
a =list(my_set)
a.append("A")
a.append("B")
print(a)

print("-"*30)
set_one = {1, 2, 3,9,"mai"}
set_two = {1, 2, 3, 4, 5, 6,"rana"}
print(list( set_one.difference(set_two)))
print(set_one.difference_update(set_two))
print(set_one.symmetric_difference(set_two))
print(set_two.issuperset(set_one))

#*=========dictionary========

programming_lang ={
                      "lang1":"python",
                      "progress":"20%",
                      "lang2":"HTML",
                      "progress":"50%",
                      "lang3":"js",
                      "progress":"40%",
}
print(programming_lang)
print(programming_lang["progress"])
programming_lang.update({"lang4":"mohammed ",
                         "progress":"20%",
                         })
print(programming_lang)

#*2 two damentions 
prog ={
    
    "lang1":{
        "name":"python",
        "progrees":"40%",
        },
    "lang2":{
      "name":"html",
      "progrees":"50%",
        },
    "lang3":"js",
    "progrees":"30%",
}
print(prog["lang1"]["name"]+" ""Progress Is %s "% prog["lang1"]["progrees"])
print(prog["lang2"]["name"]+"Progress Is %s" %prog["lang2"]["progrees"])

prog.update({
    "lang4":{
        "name":"css",
        "progrees":"30%"
    }
} )
print(prog["lang4"]["name"]+"Progress Is %s" %prog["lang4"]["progrees"])
print(prog)




#* dict 3 variables 

semester1  ={
    
    "materail1":"circuts 1",
    "materail2":"electronics1"
    
}
semester2 ={
    
    "materail1":"circuts2",
    "materail2":"electronics2"
}
semester3 ={
    "materail1":"java1",
    "materail2":"pythons1"
}
allsemesters ={
    "level1":semester1,
    "level2":semester2,
    "level3":semester3,  
}
print(allsemesters)
print([semester2])
allsemesters.update({
    " memory":"2000-5-19",
    })
print(allsemesters)
print("-"*59)
allsemesters.popitem()
print(len( allsemesters))

semester1.get("materail1")
print(semester1)

allsemesters["semester5"] ="cswdwd"
print(allsemesters)
allsemesters["graduates"]= "semester5"
print(allsemesters)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "mode" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print('-'*40)
user ={
     "name":"mai"    
}
print(user)
print(user.setdefault("age","22years old")) 
user["years"]= 2023
print(user)
user.items()
print(user)
 
user.popitem()
print(user)

print('-'*40) 
user ={
     "name":"mai" ,
     "skills":" python" ,
     "progress":"55%",     
}
 
if "name" in user :
     print("the items are found,its:{:} ".format(name))
     

a ={1,2,3,4,5,"osama","meme",}
b ={1,2,3,"moh","osama"}

print(b.difference(a)) #*                a1الي موجود في<<
                          #*b2 و مش موجود 
a.difference_update(b)  #* الي موجود في التاني ومش موجود فالاول
print(a)
print(a.isdisjoint(b))



age =input('what\'s your age ?').strip()
mounth =age *12
weeks =mounth *4 
days =age *365 
hours =days *24
minutes =hours *60
seconds = minutes *60
print(f"you lived for :{mounth}mounths\n{weeks}weeks\n{days}days\n{hours}hours\n{minutes}minutes\n{seconds}seconds ")
#*  طريقة الطباعة تانية بنفس الاشي
age =int(input('what\'s your age ?'))
mounth =age *12
weeks =mounth *4 
days =age *365 
hours =days *24
minutes =hours *60
seconds = minutes *60
#*or
print("you lived for :")
print(f"{mounth}mounths .")
print(f"{weeks:,}weeks.")
print(f"{days:,}days.")
print(f"{hours:,}hours.")
print(f"{minutes:,}minutes.")
print(f"{seconds:,}seconds.")

#*تكليفات الدروس من الدرس 041 إلى 046

#* هدا السؤال بنحل بكزا طريقة انا هحل بالطريقة التقليدية والي الكل بعملها لكن 
num1 = int (input('enter the first numbers : ').strip())
operation=input('enter the operatos \""+" Or "-" Or "*" Or "/" Or "%"\" : ')
num2 = int (input('enter the secande numbers : ').strip())
database =[]
if   operation == "*":
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    print(num1*num2)
elif operation =='/':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    print(num1/num2)
elif operation == '-':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    print(num1-num2 )
elif operation =='+':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    print(num1+num2)

else:
    print('your choose is wrong')
#* انا هزود  اشي : انوا الناتج ينضاف في ليست 

num1 = int (input('enter the first numbers : ').strip())
operation=input('enter the operatos \""+" Or "-" Or "*" Or "/" Or "%"\" : ')
num2 = int (input('enter the secande numbers : ').strip())
database =[]
if   operation == "*":
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    resuelt =num1*num2
    database.append(resuelt)
    print(resuelt)
    print(database)
elif operation =='/':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    resuelt =num1/num2
    database.append(resuelt)
    print(resuelt)
    print(database)
elif operation == '-':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    resuelt =num1-num2
    database.append(resuelt)
    print(resuelt)
    print(database)
elif operation =='+':
    print(f' your operation is>> {num1 }\"{operation:.1s}\"{num1 } =')
    resuelt =num1+num2
    database.append(resuelt)
    print(resuelt)
    print(database)
else:
    print('your choose is wrong')

#*Ternary Operators
age = 17
print('App Is Suitable For You' if age > 16 else "App Is Not Suitable For You"  )


age =int (input('enter your age  :'))
mounth = age*12
weeks =  mounth*4
days =   age*365 
hours =  days*24
minuets = hours*60  
seconda = minuets*60

if age > 10 and age < 100 :
    print((f'Your Age In Months Is {mounth}'))
    print((f'Your Age In Months Is {weeks}'))
    print((f'Your Age In Months Is {days}'))
    print((f'Your Age In Months Is {minuets}'))
    print((f'Your Age In Months Is {seconda:,}'))
else:
    print('you are out of the stations')    
    
#*/////////////////////////////////////////////////////
country = input("Input Your Country : ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(f'your country in side the countries>> country .center(11,"#").strip().capitalize()')
     
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
    #* update OR added country 
    optins = input('can u \"added\" or\"update\" the same contry in database>>')
    if optins == 'added' or 'a'.strip().lower():
        # اضافة كل اشي بدخلو اليوزر جوات الليست
        same_word = input(" Input Your Country :").capitalize().strip()
        countries[countries.index(country)] =same_word
        print('country added'.center(20,"#"))
        print(countries)                          
else:
    print(f'Your Country Not Eligible For Discount And The Price Is ${price}') 
        #* added options
    options= input("can u added your Country choose \"yes or no\" ")
    if options == 'yes' .strip().capitalize(): 
            
        country = input("Input Your Country : ").capitalize().strip()
        countries.append(country)
        print('country added '.center(20,"#"))
        print(countries)       
    else:
    #* not added options
      print('country not  added'.center(20,"#"))
        
        
#*  الدروس من رقم 047 إلى رقم 050   

       #زبط خلص بعد ما نشف ريقي ...# مش راضي يزبط معايا 
          
#* تكليف 1        
#*****************************************
num =int(input('enter your number:'))

if num > 0 :
   while num:
      num -=1
      if num == 6 or num ==0  : #ادا وصل لرقمين هدول فط عنهم 
          continue 
      print(f'{num}') 
      if num == 1: # ولما يوصل لهان اطبع 
         print(f"{10-num}Numbers Printed Successfully.")    
else:
      print("Number 0 Is Not Larger Than 0") 

#***********************zfill)()*********************
# num =0
while num < 20 :
       #عند ال10 فط وكمل اللوب ما زبط الفط
      print(str(num+1).zfill(2))
      num+=1
print("All Numbers Printed")
#  هان العكس وبحط اصفار في خانة الاحاد
num = 20
if num > 0 :
   while num:
      num -=1
      if num == 6 or num ==8 or num ==12 : #ادا وصل لرقمين هدول فط عنهم 
          continue 
      print(str(num+1).zfill(2))       
#********************************************
#*التكليف  04
my_friends =[]
num =4
name  =input('>>>ENTER YOUR NAME if : ').strip()
while name == name.upper():
      print("Invalid Name".center(15,"#"))
      break
else:
     while len(my_friends) < num : 
           name == name.lower() 
           name  =input('>>>ENTER YOUR NAME !').strip()
           my_friends.append(name.capitalize())
           print(f"Friend {name} Added=> 1st Letter Become Capital")  
           print(my_friends)
           print(f"Names Left in List Is {4-len(my_friends)}")
           if num == len(my_friends):
                 
                 print('  list empty'.upper().center(15,"#"))

if num == len(my_friends): # عشان يطبعىالليست تحت بعض 
      print(f'the list frindes is >>>')
      my_friends.sort()
      index =0
      while index <len(my_friends):
            print(f'- {my_friends[index]}')
            index+=1
                   
                                      
#* الدروس من رقم 051 إلى رقم 055 من الدورة التعليمية      

#تكليف 1             
                   
my_nums = [15, 81, 5, 17, 20, 21, 13]   
index = 0
my_nums.sort(reverse=True) # هان بترتيب الليست تنازليا
for num in my_nums :
      
      if num % 5 == 0:
         index+=1
         print(f'{index}=> {num}')
print("All Numbers Printed")                        
                 
#تكليف 2                
                 
#***********************zfill)()*********************
# num =0
while num < 20 :
       #عند ال10 فط وكمل اللوب ما زبط الفط
      print(str(num+1).zfill(2))
      num+=1
print("All Numbers Printed")
#  هان العكس وبحط اصفار في خانة الاحاد
num = 20
if num > 0 :
   while num:
      num -=1
      if num == 6 or num ==8 or num ==12 : #ادا وصل لرقمين هدول فط عنهم 
          continue 
      print(str(num+1).zfill(2))       
#********************************************     

#* تكليف 3    مش زابط شقلب مخي             
# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
ranks=[100,80,40]
for rank ,value in my_ranks.items():
  if value =='A':
    print(f"My Rank in {rank} Is {value} And This Equal {ranks[0] }Points")
    
  elif value =='B':
    
    print(f"My Rank in {rank} Is {value} And This Equal {ranks[1] }Points")
  else:
    
    print(f"My Rank in {rank} Is {value} And This Equal {ranks[2] }Points")

print(f"Total Points Is {(ranks[0]+ranks[1]+ranks[2]+ranks[0])}")             
                 

#   تكليف 4                   
                 
#اول فرع                 

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
  #* هدا السؤال دوخني اكتر من 9 ساعات وانا بحل بمشكلة ال if-else     
A,B,C,D=100,80,40,20
#*or
#A=100
#B=80
#C=40
#D=20
for name in students :  
      print('-'*40)
      print(f"-- Student Name => {name}")
      print('-'*40)
      for material in students[name]:
        
        if students[name][material] =='A':
           print(f"- {material} => {A} Points") 
        elif students[name][material] =='B':
           print(f"- {material} => {B} Points")
           
        elif students[name][material] =='C':
           print(f"- {material} => {C} Points")
        else:
           print(f"- {material} => {D} Points")
      if name=='Ahmed':
         print(f"Total Points For Ahmed Is {A+B+C+D+A}")
        
      elif name== "Sayed":
         print(f"Total Points For Sayed Is {B+B+B+D+A}")
         
      else:
         print(f"Total Points For Mahmoud Is {D+A+A+B+B}")                 
                 
#*------------------------------------------------------------                 

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
  #* هدا السؤال دوخني اكتر من 9 ساعات وانا بحل بمشكلة ال if-else
A =[100,80,40,20]
for name,skills in students.items() :
  print('-'*40)
  print(f"-- Student Name => {name}")
  print('-'*40)
  
  for keys ,rank in skills.items():
    if rank =='A'  :
        print(f"- {keys} => {A[0]} Points")
         
    elif rank =='B':
           print(f"- {keys} => {A[1]} Points")
           
    elif rank =='C':
           print(f"- {keys} => {A[2]} Points")
    else:
           print(f"- {keys} => {A[3]} Points")       
  if name=='Ahmed':  #فكرة تانية عن طريق الاندكس #
         print(f"Total Points For Ahmed Is {A[0]+A[1]+A[3]+A[2]+A[0]}") 
  elif name== "Sayed": # يمكن الجمع زي هيك>>sum(A) orsum(A,40)mean>>+40
        print(f"Total Points For Sayed Is {A[1]+A[1]+A[1]+A[3]+A[0]}")  
  else:
        print(f"Total Points For Mahmoud Is {A[3]+A[0]+A[0]+A[1]+A[1]}")                 
                 
## output
##----------------------------------------
#-- Student Name => Ahmed
#----------------------------------------
#- Math => 100 Points
#- Science => 20 Points
#- Draw => 80 Points
#- Sports => 40 Points
#- Thinking => 100 Points
#Total Points For Ahmed Is 340
#----------------------------------------
#-- Student Name => Sayed
#----------------------------------------
#- Math => 80 Points
#- Science => 80 Points
#- Draw => 80 Points
#- Sports => 20 Points
#- Thinking => 100 Points
#Total Points For Sayed Is 360
#----------------------------------------
#-- Student Name => Mahmoud
#----------------------------------------
#- Math => 20 Points
#- Science => 100 Points
#- Draw => 100 Points
#- Sports => 80 Points
#- Thinking => 80 Points
#Total Points For Mahmoud Is 380##
                 
                 
#*الدروس من رقم 056 إلى رقم 059 من الدورة التعليمية                  
                 
                 #* مزبطش
#تكليف2                
def calculate(number1 ,number2 ,op):
                     #op=="" مكتبش العملية احمع لحالك
      if op == "+"or op=="" or op=='add'.lower().upper().capitalize().swapcase():
            r =number1+ number2 #يمكن للشخص أن يكتب العملية الحسابية بحروف كبيرة أو صغيرة او Mix بدون مشكلة. مثلا add, ADD, aDd
            print(r)
            
      elif op == "-" or op =='s'.lower().swapcase():
            r =number1- number2 # كتابة أول حرف فقط من العملية الحسابية
            print(r)
            
      elif op == "/":
            r =number1 / number2
            print(f'{r:0.3}') #   ا3ارقام عشرية بعد الفاصلة          
      else:
            print('<>syntax errors<>')
      
calculate(100, 900, input('enter the op \'(+),(-),(/)\' : ')) # 30
#calculate(10, 20,'')
#calculate(10, 20,) # 30++
            
calculate(input('ENTER NUM1: '),input('ENTER THE OPERATIONS :'),input('ENTER NUM2: '))
#-------------------------------------------------------------
#*تكليف3                        #*----output----
                                 #*Hello Osama Your Skills Is
                                   #*-HTML
                                   #*-CSS
                                   #*-JS
                                   #*-Python
                                   #*Hello Ahmed You Have No Skills To Show  
def show_skills(name ,*skills):                                                
     
     if  skills  : #إذا لم يكن لديه مهارات يجب عليك إظهار رسالة تفيد أنه ليس لديه مهارات حتى الآن
         print(f"Hello {name} Your Skills Is")
         for skill in skills:                          
            print(f'- {skill}') 
            continue 
     else:# تابع ادا مفش مهارات
         print()
         print(f"Hello {name} You Have No Skills To Show")         
show_skills("Osama", "HTML", "CSS", "JS", "Python")    
show_skills("Ahmed")
show_skills('mai') 
print('#*--------------------------------------')
                 
#التكليف 04         
def say_hello(name='Unknown' ,age='Unknown',country='Unknown'):
     
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")
    
say_hello(input('enter your name'), 38, "Egypt") 
say_hello('mai')        

#or مرة بال returen ومرة بدون

#التكليف 04         
def say_hello(name='Unknown' ,age='Unknown',country='Unknown'):
     
    return(f"Hello {name} Your Age Is {age} And You Live In {country}")
    
print(say_hello(input('enter your name'), 38, "Egypt") )

'''حل التكليفات
المطلوب حل تكليفات الدروس من 65 إلى 68'''

# *حل مشكلة ال ايروور هدا هوا "r"
# *SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
import os
num = 1
while num < 51:
    myfile = open(rf'C:\Users\jit\Desktop\Python1\txt{num}.txt', 'w')

    num += 1
    myfile.write(f'<> Elzero Web School<> => {num-1}\n')

    # في السطر الثالث قم بطباعة إسم الملف المفتوح حاليا
print(os.path.abspath(__file__))  # c:\Users\jit\Desktop\Python1\assign.py

# في السطر الثاني قم بطباعة المسار الموجود فيه الملف حاليا
# c:\Users\jit\Desktop\Python1#
print(os.path.dirname(os.path.abspath(__file__)))

# في السطر الأول قم بطباعة ال Current Working Directory
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt', 'a')  # *>>append()
myfile.write(f'Appended => Elzero Web School\n'*51)


myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt', 'r')  # *>>read
print(myfile.name)  # C:\Users\jit\Desktop\Python1\txt1.txt

# ---------------------
# في السطر الأول قم بطباعة عدد الأسطر الموجودة داخل الملف
print(f"Number Of Lines Is => {num} lines ")  # Number Of Lines Is => 51
# *OR*
myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt','r')  
# *>>read #نفتح الملف عشان نقراء منوا
myfile.seek(0)
r = myfile.readlines()
print(f"Number Of Lines Is* => {len(r)-1} lines ")
print('-'*20)
# ---------------------
# في السطر الثاني قم بحساب عدد الكلمات الموجودة في الملف
ind = 0
myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt', 'r')
for word in myfile.readlines():
    ind += 1
    print(f"Number Of Words  Is => {len(word)*31}")  # 28*31 =868 مش دقيق 
    break
# عدد الكلمات الموجودة في سطر واحد
ind = 0
myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt', 'r')
for word in myfile.readlines():
    ind += 1
    print(f"Number Of Words in one line Is => {len(word)}") #28
    break

# *----------------------------------------
# في الصف الثالث قم بطباعة عدد ال Characters الموجودة في الملف

myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt','r')  # *>>read #نفتح الملف عشان نقراء منوا
myfile.seek(0)  # بتحدد مكان الكورسر
r = myfile.read()  # >>> 1578Number Of Chars Is => 1578 characters!
print(f"Number Of Chars Is => {len(r)} characters!")

# *OR*
# myfile=open(r'C:\Users\jit\Desktop\Python1\txt1.txt','r')
#ind =0
# for word in myfile.read():
# ind+=1
# print(f"Number Of Words Is => {word}>>{ind}\n")#1578''
# عدد

#في السطر الرابع قم بطباعة كم عدد المرات التي وجد فيها الحرف “l”

lists =[]
myfile = open(r'C:\Users\jit\Desktop\Python1\txt1.txt','r')
for word in myfile.read():
    if word  == 'l':
       lists .append(word)  #Number Of l Char Is =>104
       print(f"Number Of {word } Char Is =>{(len(lists))}")
     
# *----------------------------------------
#التكليف 04
#بطريقة برمجية وبواسطة ال Loop قم بحذف آخر عشر ملفات txt
#*غلط الحل هان بس فكرة اللوب هيا 
from os import remove
import os

num =1
myfile = open(rf'C:\Users\jit\Desktop\Python1\txt{num}.txt', 'w')
if num == 40 :
    os.remove(fr'C:\Users\jit\Desktop\Python1\txt{num}.txt')

#*الدروس من رقم 069 إلى رقم 071 من 

'''التكليف 02
'''
v = 40
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v))  # 820


'''التكليف 03
'''
n = 20
l = list(range(n))
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")
# Output => Good

'''التكليف  04  
'''
# * @1
#  IF مرة الاف العادية
list = [1, 2, 3, []]  # True

if all(list):
    print('TRUE')
else:
    print('bad')

# -------- ومرة بالفانكشن العادية --------------
def my_all(list):  # name fun+para
    if all(list):  # condtions
        return(f'TRUE,list is>>{list}')
    else:
        return(f'false,list is>>{list}')

print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# --------ومرةlambda فانكشن--------------
lists = ([1, 2, 3, [0]])
lists = [1, 2, 3, []]
def my_all(list): return 'true'

if all(lists):  # condtions
    print(f'TRUE,list###>>{lists}')
else:
    print(f'false,list###>>{lists}')

# * @2

list = ([(), 0, False])
if any(list):
    print('true')
else:
    print('bad')

# ----------------------pre-definde func
def my_any(list3):
    if any(list3):
        return f'TRUE*>> {list3}'
    else:
        return f'FALSE* {list3}'
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False
# ------------------------ lampda functions
list4 = ([(), 0, False])
def my(my_any): return 'triu'
if any(list4):
    print(f'TRUE*>> {list4}')
else:
    print(f'FALSE* {list4}')

#* @ 3

mylist =([10, 100, -20, -100, 50])
''''print(min(mylist)) # -100'''
#or

def my_min(mylist):
    return min(mylist)
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, 100, 50))) # -20

#* @ 4
mylist =([10, 100, -20, -100, 50])
print(max(mylist)) # 100
#or

def my_max(mylist):
    return max(mylist)
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700


'''تكليفات الدروس من الدرس 072 إلى 075
'''

#*قم بعمل Function بإسم remove_chars تزيل أول وآخر حرف من اي String

'''هان الاشي عادي لكن لو بدنا اياه بالفناكشن مع الماب 
'''
# * functions +for()
from functools import reduce


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(list):
    for name in friends_map :
        print(name[1:len(name)-1])
remove_chars(friends_map)

#* functions +map ()
print('*'*20)
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
def remove_chars(list):
    return list
cleaned_list =map(remove_chars,friends_map)

for name in cleaned_list:
    print(name[1:len(name)-1])

 #*ولكن بإستخدام Lambda Function   

print('*'*20)
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
for name in (map(lambda text :f'{text}',friends_map)): #نوع البيانات ليست مش ماب 
    print(name[1:len(name)-1])
    

print('-'*30)            
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
      
def get_names(texts):
     
     for name in friends_filter:
         if name.endswith('m'):
            print(name)
         
get_names(friends_filter)        
 
#* << same the option>>باستخدام الفلتر 
      
print('-'*30) 
           
def get_names(texts):
    return texts.endswith('m')
   
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]     
names =filter(get_names ,friends_filter)
for name in names:
    print(name)    
    
#* <<same the option>> using lambda func 

print('-'*30)    
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]     
names =filter(lambda text :text.endswith('m') ,friends_filter)
for name in names:
    print(name) 

#-----------------------------------------      

#*------التكليف 03

nums = [2, 4, 6, 2]   
def multiply(num1,num2):
    return num1 * num2
result =reduce(multiply,nums) 
print(result)   #96<<output
#* <<same the option>> using lambda func 
nums = [2, 4, 6, 2]   
result =reduce(lambda num1 ,num2 :num1*num2,nums) #paramerts :retuern
print(result) 
#-----------------الطريقة الاولى 1     
print('-'*30)        
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaSdatabaseipt")
counter =enumerate(reversed(skills),50) 
for counter,myskills in counter:
    if type( myskills) ==  int :
        continue
    print((f'{counter} - {str(myskills)}'))   
       
#--------------- طريقة تانية2   
print('-'*20)    
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaSdatabaseipt")

def oper(myskills):
    return counter
counter =enumerate(reversed(skills),50) 
for counter,myskills in counter:
    if type( myskills) == int :
        continue
    print((f'{counter} - {str(myskills)}'))   
              


#*الدروس من رقم 076 إلى رقم 078

# نكليف 1
import random  # its modules
from random import randrange, randint

print("Random Number Between 10 And 50 =>",random.randrange(10,50)) #any num between 10-50 and int 
print("Random Even Number Between 2 And 10=>",random.randrange(2,10,2)) #only num is even and between 2-10
print("Random Even Number Between 2 And 10=>**",random.randint(2,10))  #any num even and int
print("Random Odd Number Between 1 And 9 =>",random.randrange(1,10,2))  #any num odd and int
print(f'# Module Methods Content Here {dir(random)}')

# نكليف 2   

''' on folder my_mod.py'''
def say_welcome(name):
     print(f'welcome {name}')
say_welcome('mohammad/')     
 
def say_hello(name):
     print(f'hello {name}')
say_hello('mohammad+')

'''on folder main.py'''
#import my_mod
# اتستدعاء
#my_mod.say_hello('mohammad*') 
#my_mod.say_welcome('mai*')

#print(dir(my_mod))

#import my_mod

# اتستدعاء
#my_mod.say_hello('mohammad*') 
#my_mod.say_welcome('mai*')

#print(dir(my_mod))

#تكليف 3

#from my_mod import say_welcome

#say_welcome('osama')

#تكليف 4

#from my_mod import say_welcome as new_welcome

#new_welcome('osama')

#
#* الدروس من رقم 079 إلى رقم 080
#التكليف 01

 # الحلين نفس بعض لكن واحد فيه الوقت والتاني مفش فيع عن طريق  method date

# Message Will Be
#* حدفنا الوقت عطريق method date 
"Days From 2021-06-25 To 2021-08-10 Is => 46"
import datetime
date =datetime.datetime(2021 ,6,25).date()
today =datetime.datetime.now().date()
print(f'The Date Is {date}',end= " to ")
print(f'{today} Is =>{(today-date).days}')
#* without method date 00:00:00 to 16:33:10.239649
'''The Date Is 2021-06-25 00:00:00 to 2022-07-28 16:33:10.239649 Is =>398'''
import datetime
date =datetime.datetime(2021 ,6,25)
today =datetime.datetime.now()
print(f'The Date Is {date}',end= " to ")
print(f'{today} Is =>{(today-date).days}')

# التكليف 02
#قم بطباعة التاريخ والوقت الخاص باليوم الحالي بأكثر من طريقة
print('*'*20)
dd =datetime.datetime.now().date()
print(f'Today Is "{datetime.datetime.now().date()}"') #Today Is "2022-07-28"
print(f'Today Is "{datetime.datetime(2021,7,28).date()}"')#Today Is "2021-07-28"
print(f'Today Is* ',dd.strftime('%b %w, %Y')) #Today Is "2021-07-28"
print(f'Today Is/ ',dd.strftime('%w - %b - %Y')) #Today Is/  4 - Jul - 2022
print(f'Today Is+ ',dd.strftime('%w / %B / %y')) #Today Is+  4 / July / 22
print(f'Today Is- ',dd.strftime('%w / %B / %Y')) #Today Is-  4 / July / 2022
print(f'Today Is- ',dd.strftime('%a,  %w %B %Y')) #Today Is-  Thu,  4 July 2022



# تكليف 1
def reverse_string(my_string):
  # Your Code Here
  for name in reversed( my_string):
      yield name

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
  
# تكليف 2
from functools import wraps
def mydecorators (funcly): # decorator
    @wraps(funcly)
    def Function():        #=>pre-defined fun
        
        print("Sugar Added From Decorators") #=> befor func
        
        funcly()
        
        print('#'*20)
        print("Sugar Added From Decorators")
    
    return Function  
 
@mydecorators
def make_tea():
    
    print("Tea databaseeated")   
def make_Coffe():
    
    print("Coffe databaseeated")
    print('#'*20)

make_tea() 
make_Coffe()    

# Needed Output

"Sugar Added From Decorators"
"Tea databaseeated"
"####################"
"Sugar Added From Decorators"
"Coffe databaseeated"
"####################"


def hi(name="yasoob"):
    return "hi " + name

print(hi())

def hi(name='unknown'):
    return "hi " + name

print(hi("yasoob"))        
        


def hi(name):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi("yasoob")
print(a()) 
print('#'*20)





#الدروس من رقم 086 إلى رقم 089 

'''https://pillow.readthedocs.io/en/stable/handbook/tutorial
.html#rolling-an-image'''
# تكليف رقم 3
from PIL import Image
import PIL
import os, sys

'''open image'''

myimage =Image.open(r'C:\Users\jit\Desktop\elzero-pillow.png')
'''show image'''

myimage.show()

'''cut image-print(im.format, im.size, im.mode( -العمق-البعد%))'''
dimentions =(0,0,400,400)
newimage =myimage.databaseop(dimentions)
'''convert image to black'''

newimage=newimage.convert('L')
newimage.show()

'''save the pic'''
newimage.save(r'C:\Users\jit\Desktop\black.jpg') #or png

newdimentions =(0,0,1200,400)
nimage =myimage.databaseop(newdimentions)

'''Color transforms converts'''
nimage=nimage.convert('L') 

'''Merging imagesنسخ الصورة على الصورة الاصلية '''
mynewimage =Image.open(r'C:\Users\jit\Desktop\rana.png')

Image.Image.paste(myimage ,mynewimage,(400, 280))
myimage.show() # الاصلية myimage


'''rotating a image 90 deg counter clockwise'''
#(resample)PIL.Image.Resampling.BICUBIC or PIL.Image.NEAREST

nimage=nimage.rotate(180, PIL.Image.NEAREST, expand = 1)
nimage.show()


#  تكليف رقم 5  

# Function Doc String Output 

# Write Function With Help To Get The Output


def say_hello_to(name):
    '''parameter(someone) => Person Name
    Function To Say Hello To Anyone'''

    return f'hello {name}'
print(say_hello_to("Osama")) # "Hello Osama"

# Write Doc String Line For The Function Here

print(say_hello_to.__doc__)
# Function Doc String Output


# تكليف 2
import numbers
import re

regular = re.search(
    r'L(E\w{5})', 'EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111')

print(regular.group())  # <re.Match object; span=(10, 17), match='LElzero'>

# تكليف 1

reg1 = re.search(r'(\w\s)', 'eeeeE llllLl lllzzZzzzz eroe operationr pollo')

print(reg1.group())

# تكليف3
number = ("من السؤال")
reg2 = re.search(r'(.?\(\d+\)\s\d{1,4}?-\d{4})', number)
print(reg1.group())
# تكليف4
string = (" من السؤال")
reg3 = re.search(
    r'(http)(s)?://(www)?.(\w+).?(\w+|\d+)(:?|/?)(\d+|\w+)(\/?|\w+)/\w+.(php|py', string)
print(reg1.group())



#* object ---oop 


class Game:

   # Write Class Content

    def __init__(self, name, developer, year, price) -> None:

        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    @property
    def price_in_pounds(self):

        return f'{self.price *15.6:0.1f}'


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(
f"Price In Egypt Is {game_one.price_in_pounds} Egyptian Pounds", end="\n")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
#  Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 50 Egyptian Pounds

# تكليف 2


class User:

    def __init__(self, first_name, midell_name, age, gender) -> None:

        # inastance attributes
        self.fname = first_name
        self.mname = midell_name
        self.age = age
        self.gender = gender

    def full_details(self):

        if self.gender == 'Male':

            return f'Hello Mr {self.fname} {self.mname:.1s}. [{str(40-self.age).zfill(2)}] Years To Reach 40 '
        elif self.gender == 'Female':
            return f'Hello Mrs {self.fname} {self.mname:.1s}. [{40-self.age}] Years To Reach 40 '


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

#التكليف 03

class Message:
  
  def print_message (self):
      
      return 'Hello From Class Message'

Message =Message()

print(Message.print_message())

# Output
# Hello From Class Message



# تكليف 04


class Games:

    # Write Class Content
    def __init__(self, game1) -> None:

        self.game1 = game1

    def show_games1(self):  # method 1

        print(f'I Have One Game Called \"{self.game1}\" ')

    # * ---الفكرة هان

    def show_games2(self):  # method 2
        print('I Have Many Games: ')
        for self.game in self.game1:

            print(f'-- {self.game}')

    def show_games3(self):  # method 3

        print(f'I Have {self.game1} Game.')


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games1()
my_games_names.show_games2()
my_games_count.show_games3()
# Ouput
'''
I Have One Game Called "Shadow Of Mordor" 
I Have Many Games:
-- Ys II
-- Ys Oath In Felghana
-- YS Origin
I Have 80 Game.
'''


#تكليف  05

# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# databaseeate Admin Class Here
class  Admins(Members):
    
    pass
 
 # databaseeate Moderators Class Here     
class Moderators(Admins):
    
    pass


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator




# تكليف 05

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

# Write The Class Called "Text" Here
class Text ( A ,B , C):
    
    def __init__(self, one ,two, three ):
        
      super().__init__( one ,two ,three )
    #@property             
    def show_name (self ):  # خلل هان 
        
        print (f'The Name Is {self.show_name()} ')
           

the_name = Text("El" ,"ze" , "ro")

the_name.show_name()

# Ouput
# The Name Is Elzero 









class Student: #* الاسم ورقم الطالب 
    def __init__(self, name, student_number):
      #inastances attribute (data)
        self.name = name
        self.student_number = student_number
        self.classes = []
      # inastances method (func) 
    def enrol(self, course_running):  #   السماح بالتسجيل فاكتر من كورس 
        self.classes.append(course_running)
        course_running.add_student(self)

class Department: # القسم
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {} 

    def add_course(self, desdatabaseiption, course_code, databaseedits):

        self.courses[course_code] = Course(self)

        return self.courses[course_code]
        


class Course:
    def __init__(self, desdatabaseiption, course_code, databaseedits, department):
        self.desdatabaseiption = desdatabaseiption
        self.course_code = course_code
        self.databaseedits = databaseedits
        self.department = department
        self.department.add_course(self)

        self.runnings = []

    def add_running(self, year):  # سنة التسجيل فالكورس 
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning: # يمكن تسجيل اكتر من طالب فالكورس في نفس العام
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)


maths_dept = Department("Mathematics and Applied Mathematics", "R121312") #(self, name, department_code):
mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1) #(self, desdatabaseiption, course_code, databaseedits):
mam1000w_2013 = mam1000w.add_running(2013) #(self, year): 

bob = Student("Bob", "Smith") #(self, name, student_number):
bob.enrol(mam1000w_2013)

#*---------------------الوراثة inheratnt------------------------

class Person:
    def __init__(self, name, latsname, number):
        self.name = name
        self.latsname= latsname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        super(self , Student).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


jane = Student(Student.POSTGRADUATE, "mohammed", "aburaida", "SMTJNX045")#(self, name, surname, number):
jane.enrol(a_postgrad_course)

bob = Lecturer(StaffMember.PERMANENT, "Rana", "aburaida", "123456789")
bob.assign_teaching(an_undergrad_course)



import sqlite3

database =sqlite3.connect(r'C:\Users\hp\Desktop\dirctory\elzeroo.db')

cursor =database.cursor()
cursor.execute('create table if not exists users (idd integer , name text ,birthday integer, email text)')

def Users ():

    ids =input('Enter your id numbers: ')
    name =input('Enter your name: ')
    BD =input('enter your birthday: ')
    email =input('enter your email: ')

    # fetch data
    cursor.execute(f'select idd from users where idd= {ids}')
    results =cursor.fetchone()

    while results != None: # Theres A Skill With This Name in Database ادا 

      print("You Cannot Add It")
      cursor.execute(f'delete from users where idd ={ids}')
      print("User Deleted.")

      # show last  items deleted 
      for items in  results :
        
        print(f'\nID => {ids}, Name => "{name}", Date Of Birth => {BD}, Email =>"{email}"',end=' ')

      break
      
    else:  # ما بضيف اي شخص مكرر
      print("User Not Found.")
      cursor.execute(f'insert into users values({ids},"{name}",{BD},"{email}")')

    #last row in db  
    i=0
    while i ==0:
      cursor.execute(f'select * from users')
      results =cursor.fetchall()
      i+=4
      print(f"\n last row in db :", end= ' ')
      print(f'>>>{ results[i] }') 

    # fetch data
    cursor.execute(f'select * from users')
    result =cursor.fetchall()

    for data in result :

      print(f'{data}')
      #print(f'ID => {ids}, Name => "{name}", Date Of Birth => {BD}, Email =>"{email}"',end='')

    
Users()
database.commit()
database.close()
































