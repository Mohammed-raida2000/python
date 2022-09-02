#name = input("enter your name :")
#num =input ("enter your id number")
#print ("\n hello, your name is " + name.upper() + "\n your number is" +num )
#print("welcome " +name.upper() +   "your number is : " +num)
#--------------------------------------------------------------------------------------
#no1 =input(" ENTER  NUMBER 1: ")
#no2 =input (" ENTER NUMBER 2 :")
#Result = int(no1)+ float (no2)
#print(Result)
#--------------------------------------------------------------------------------------
#طريقة الادخال من الزبون من خلال التعريف
#def salma ():
    #name = input(" your name :")
    #pos  = input ("your pos :")
    #age  =input ("your age: ")
    #print("hello ,"+ name +",you are "+pos +",your age is "+ age )
#salma()
#salma() #استدعاء كمان شخص عادي بس مش طريقة رسمية
#--------------------------------------------------------------------------------------

#def cube(num):
    #return  num*num*num # هاي الدالة بتعطيك نتيجة مظروبة 3 مرات

#print(cube(3))
#--------------------------------------------------------------------------------------''
#def sequar(num):
   #  return num*num*num*num
#print(sequar(4))
     
#is_man = True
#is_engineer = True

#if is_man and is_engineer :
   # print ("your are an engineer man")
    #print("#-----------------------------")
#elif is_man and not (is_engineer):
     #print("you are man but not engineer")
     #print("#-----------------------------")
#elif not(is_man) and is_engineer :
     #print("you are women- an engineer ")
     #print("#-----------------------------")
#elif not (is_man) and not (is_engineer): #      مع او بدون قوس بزبط
         #print(" you are not an engineer man  ")
         #print("#-----------------------------")
#else:
     #print("you are not an engineer man ")
     #print("#-----------------------------")

#--------------------------------------------------------------------------------------''
#مقارنة بين اكبر رقم

#def max (num1,num2,num3):
  #if num1 >= num2 and num1 >= num2 >= num3:
   #  return num1
  #elif num2 >= num1 and num2 >= num3:
    # return num2
  #else:
      #return num3
#print(max (12,13,14))

#def max(no1 ,no2 ,no3):
    #if no1 >= no2 and no1>=no3:
        #return no1
    #elif no2>=no1 and no2>=no3:
       # return no2
   # else :
       # return no3
#print(min(23,32,44))    
#--------------------------------------------------

#title هان عشان تكبر اول حرف من كل كلمة 
#upper نفس الشغل بس هان كل الحروف الي فالكلمة 
#name =input("enter your name :")
#universty =input("enter your uni :")
#print(name.title()+" "+ universty.title() ) # هان يحول حروف الي بدخلها المستخدم لكبيرة
num1 =float(input(" enter first num :")) # يدخل رقم مش نص من ليوزر 
op   =input ("inter the operators :")# بنفع تحط سيمي كولون او قوس 
num2 =float (input(" enter secend num :"))  
# هندخل مجموع العمليات الحسابية 
#if op == "+":
     #print(num1 + num2 )
#elif op=="-" :
    # print(num1-num2)
#elif op=="*":
        # print(num1 * num2 )
#elif op=="/":
     #print(num1 / num2)
#else:
    #print(name.title() + " " +"please  syn errors ")# لو بدت تربط كلا مع بعض يعني نص +" "+ 

# عمل مودل بسييييط dictinary 
#--------------------------------------------------
#mounth = {1:"jan" ,2:"feb",3: "mar" ,4:"apr",5:"may" 
          
         # ,6:"jun",7:"jul",8:"aug",                           #بنقدر نحط برضوا بدل 1 نص 
         
        #   9:"sep",10:"oct",11:"nov",12:"dec" }
#print(mounth[8])
#print(mounth.get (13," erros")) #هان يمعلمي لو مش موجود بقلك خطا 

#--------------------------------------------------
##m=0
#while m <= 10:
     #print(m)
     #m += 1
     #if m > 9:
          #print ("finish")
          

#--------------------------------------------------
#password= "mai" 
#word ="" #  من المستخدم
#count =0 #  بداية العدداد "المحاولا"ت
#limit =3 # نهاية العداد م
#stop = False #  ايقاف الاحتمال او المحاولات لليوزر
#while word != password and not stop:
     #if count < limit :
           #word =input("enter password :")
           #count +=1
     #else: stop = True  #  عندما تنتهى من المحاولة 
                 
#if stop :  #stop=out
           #print("out of try")       
#else:
            #print ("corrects!")   
# سؤال اضافي //ممكن برضوا تخلي الادخال من اليوزر 
password= "rana" 
word ="" #  من المستخدم
count =0 #  بداية العدداد "المحاولا"ت
limit =3 # نهاية العداد م
stop = False #  ايقاف الاحتمال او المحاولات لليوزر
while word != password and not stop:   
     if count < limit :
           word =input("enter password :")
           count +=1
     else: 
          stop = True  #  عندما تنتهى من المحاولة 
print(f"your password is : {word }")     
print(f"the number of coun {limit-stop}") # يطبعلك اكمن محاولة حاول اليوزر                 
if stop :  #stop=out
           print("out of try")     # stop = true لان لما يسير الكاونت 3 هيقلك انتهنت المحاولات 
else:
            print ("corrects!")    # stop = false لان كول ما الكاونت ما وصل الايقاف هيقلك صح     
#*---------------------2--------------------------           
password ="rana"            
inword =""
startcount = 0 
stoplimit = 3
stopprog =False

while  inword !=password and not stopprog:
   
      if startcount < stoplimit:
            inword=input(("enter your password after try"))
      else: stoplimit =True     
print((f"your password is {inword}"))
if stoplimit :
      print("out")      
else:
      print("corrects") 
      
#** سؤال اضافي //ممكن برضوا تخلي الادخال من اليوزر 
password= "rana" 
word ="" #  من المستخدم
count =0 #  بداية العدداد "المحاولا"ت
limit =3 # نهاية العداد م
stop = False #  ايقاف الاحتمال او المحاولات لليوزر
while word != password and not stop: 
     if count < limit :
           word =input("enter password :")
           count +=1
     else: stop = True  #  عندما تنتهى من المحاولة 
print(f"your password is : {word }")     
print(f"the number of coun {limit-stop}") # يطبعلك اكمن محاولة حاول اليوزر                 
if stop :  #stop=out
           print("out of try")     # stop = False 
else:
            print ("corrects!")    # stop = true    
password ="rana"            
inword =""
startcount = 0 
stoplimit = 3
stopprog =False

while  inword !=password and not stopprog:
   
      if startcount < stoplimit:
            inword=input(("enter your password after try"))
      else: stoplimit =True     
print((f"your password is {inword}"))
if stoplimit :
      print("out")      
else:
      print("corrects")                     
#*--------------------------------------------------
# عمل فانكشن واستدعاءها من كلاس اخر او ملف اخر في مجموعة داتا
#modules والموضوع جدا جميل لان بتقدر تستدعي اكواد جاخزة كتبها آلاف الممبرمجين والمهندسين
#import Functions
#import textwrap
#print(Functions.mohammed)
#print(textwrap.)
#--------------------------------------------------
#هنعرف الكلاس جوات ملف الفنكشن الي هنستدعي منوا شو احنا عرفنا اشياء عن الاوبجيكت
import email
from email import iterators
from http.server import ThreadingHTTPServer
from multiprocessing.sharedctypes import Value
from xml.dom.minidom import Element
from Functions  import phone, socialmedia
appals = phone ("appals",True,120,"200$")#appals هو ابوجيكت من كلااس الفوون
redmi  =phone ("xiomai",False,2000,"2380$")
fb = socialmedia("all", 1200, "mohammed mai")
print(appals.size)
print(redmi.size)
print(appals.is_touchable())
#  تعليقsocial.madia
print(fb.home)
print(fb.is_touchable())
       
#--------------------------------------------------

#print(type(1000)) # <class 'int' > شكل الناتج 
#print(type({"one":1,"two":2,"three":3}))

#--------------------------------------------------   
#  عمل جمل  طباعة وتحت بعض  مع  ترتيب تحت بعص  
#moh =  ''' mohammed abu raida 
           #moh 
           #mai '''
    
#print(moh)
#----------------------------------------------------- المهم تحت
#*strip() دالة الستريب بتشيل يمعلم الفاراغات والمسافات من على اليمين واليساتر وغيرها
#moh =  '''           mohammed    abu  raida   '''
#print(moh.strip()) #*بتشي لالفراغ من كل الجوانب
#print(moh.rstrip())#*بتشيل الفراغ من اليمين r=rigth 
#print(moh.lstrip())#* l =left بتشيل الفراغ من اليسار
#-----------------------------------------------------
# مثلا لو بدي اشيل الهاتش من الكلام اول اي حرف بزبط زي هيك
#moh =  '''######mohammed    abu  raida#######'''
#print(moh.strip("#")) 
#print(moh.rstrip("#"))
#print(moh.lstrip("#"))

#-----------------------------------------------------
#*split بتتعامل مع المسافات وبتقسمهم من النص  
#mai = "am-mohammed-abu-raida-mech"
#print(mai.split())#هان بقسم الفراغ فقط 
#print(mai.split("-") )#هان بقسم الداش لان معطيه امر بين القوسين split("-")
#print(mai.split("-",2))# هان بقسم حسب الmaxsplit الي هيا عددهم مرتين  ببوقف
#--------------------------------------------
#*center()هان بتحط برموز قبل الاسم "و" بعد  الاسم الي انتا يدك اياه
#mai = "mohammed"
#print(mai.center(14,"#"))        #نفس الهاشتاق الي في فيس بك رك يمعلم 
#print(mai.center(9,"@"))
#print(len(mai))

#-----------------------------------------------------

#*count() هان بجيبلك يمعلم قديش عدد الكلامات المتشابهة او المتكررة  الي بدت تبحث عنهم
mai = "mohammed ,eng ,mohammed ,mai, mai,mai,mohammed "
print(mai.count("mai"))
rana ="mohammed ,eng ,mohammed ,rana, rana,rana,mohammed "
rana.count("rana")
print(rana)
#-----------------------------------------------------
#*swapcase(),  يعني ببدل الحرف لو كان كبير لصغير ومن صغير كبير dها بتبدل شغلة مكان شغلة بس 
mai = "mohammed"
moh = "MOHAmmad"
print(mai.swapcase())  # output: MOHAMMED
print(moh.swapcase())  #       :mohaMMAD
#-----------------------------------------------------
#*startswith() هان يمعلم بتشوفلك هل الكلمة او الاسم يبدا بحرف ال وبترجعلك صح او غلط 
mai = "mohammed"
print(mai.startswith("w",0,9))
#----------------------------------------------------
#*endswith() هان يمعلم بتشوفلك هل الكلمة او الاسم ينتهي  بحرف ال وبترجعلك صح او غلط 
#mai = "mohammed"
#print(mai.endswith("d",0,9))
#----------------------------------------------------
#mai = "aug mohammed mai "
#print(mai.title()) #بحط اول حرف كبير من اول كل كلمة 
#print(mai.endswith("e",0,12))
#print(mai.swapcase())
#print(mai.count("aug",0,40))
#print(mai.center(0,"@@"))
#print(len(mai))              #عشان نجيب الطول 
#print(mai.split(" ",2))
#print(mai.startswith("s",0,12))
#print(mai.endswith("g"))
#print(mai.center(29),"@@")
#print(mai.rjust(9),"@")
#print(mai.ljust(2),"@")
#----------------------------------------------------
#*rjust() نفسها نفس السينتر يمعلم =center()
 #*> rjust > ljust بتحط  رموز يمين او يسار الاسم الي انتا بدك اياه
#mai ="osama"
#print(len(mai))
#print(mai.rjust(9)) #بعد سبيس من اليمين 
#print(mai.ljust(9))# بعد سبيس من اليسار 
#print(mai.rjust(9),"#")#  بعد 9 فراغات  من اليمين وبحط داش ال9 فرغات اطول الكلي مع الفرغات
#print(mai.ljust(9),"#")# بعد 9 فراغات من اليسار وبحط داش
#print(mai.ljust(9 ,"#")) # بعد داش من اليسار
#print(mai.rjust(9 ,"#")) # بعد داش من اليمين
#print(mai.ljust(9),"#")# بعد 9 فراغات من اليسار وبحط داش
#----------------------------------------------------
#*expandtabs(tab size  @ \t  )   \t #هان بحط فراغات بين كل كلمة و انتا بتحددوا للفراغ 
mai ="l love\tyou\tpython\tlanguage"
print(mai.expandtabs(12))
#----------------------------------------------------
#*join()  #بترجع يمعلم هان مجموعة كلمات على شكل نص 
#m = ["moh","mohammed ","saeed","rami"] # type =list
#print(" ".join(m)) #بترجع يمعلم هان مجموعة كلمات على شكل نص 
#*replace( "odd","new", coun) هان بتبدل اشي مطرح اشي 
#mai =" one two three one five one one eigth nigth one"
#print(mai.replace("one","1"))
print(mai.replace("one","1",2))  # 2 الرقم يعني كل كلمتين استبدلهم

#*-------------------can only concatenate str (not "int") to str--------------------------------
#*------------------formating string -----------------------------------------------------------
#*------------------- هان حل مشكلة دمج لنص مع الارقام بطريقة بسيطة
# %d  is digit namber
# %f  is float  
# %s  its string
# %i  its integr num
# %.2f ملاحظة مرة حلوة وهيا تقدر تحدد اكم خانة الاصفار فالرقم المدخل
# %.5s برضوا بزبط كمان النص 
#name =" mohammed"
#age =22                     
#level = 4
#print( "my name is:%.5s and my age is :%d and study level at:%.2f" %(name,age,level))        1 
# truncate string بطريقة تانية بس اسهل وفيها مميازات اكتر
#print( "my name is: {:s} and my age is: {:d} and study level at: {:.2f} ".format(name,age,level))         2
#*-------------------------------------------------------------------------------------------------
name = "osama"
age = 38                                  #formating
country ="egypt"
print("hellow,""my name is %s and iam %i years old and i live is %s "%(name ,age,country))   #النوع 1
print("hellow,""my name is {:s}and iam {:d}years old and i live is{:s}".format(name, age, country))#النوع 2
print(f"hellow,my name is {name} and iam {age} years old and i live is {country}")#النوع 3
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#n= "mohammed"
#l="python"
#r= 3
#print("my name is %s iam %s developer and %d years exp" % (n,l,r))

# -------------------في مشكلة هان يمعلم لما نخلي اليوزر يدخل بياناتوا ما بزبط-------------------------
#name = input("enter your namr,please: ")
#age  = input("enter your age :")
#idnum= input("enter your id number :")
#msg  ="thank you!"
#print("your number is%sand your age is%dand %d your id number message %s " % (name.title(),age,idnum,msg.title()))
# ---------------------------------------------------------------------------------------------------------
#num = 123131412312
#print( "my name is: {:f}".format(num)) #بزبط مثلا اقسم الارقام لخانات زي هيك 
#print( "my name is: {:,.0f}".format(num)) #   تحدد عدد الاصفار اخر الارقام 
# --------------------------------------------
# -------------------------------------------------------------
#m,r,l =" mohammed ","mai ", 200
#print("welcome {1} {0} {2} ".format(m, r , l)) #1 0 2 هاي عبارة عن اندكس يمعلم للكلمات 
#print("welcome {1:s} {0:.3s} {2:.2f} ".format(m, r , l)) 
# --------------------------------------طريقة جديدة لطباعة -------------------------------------------------------------
#*----------------------formating---------------------------------------------
mai ="mohammed abu raida"
age =22
print("my name is {mai} and {age} is years ago ") # هان هيفكر انوا القوس من ظمن الاسم لكن شوف كيف هيتجاهلو
print(f"my name is {mai} and {age} is years ago ") #حطة حرف ال وزبط بكل بساطة "f" 

#================================= py formating شوف موقع ال عشان  تعرف كل اشي عن ال============================ 
#================================================================================================================ 
#*                      " Indexing + Slicing "
name = 'mohammedjkfhwifhsifq'
print(len(name))
print("Second Letter Is %s ",(name[1]))
print("Third Letter Is %s ",(name[2]))
print("last Letter Is %s ",(name[ len(name)-1 ]))

#*---------------------------------NUMBER TYPE---------------------------------------------------------------
num1 =  6+4j
print(type(num1))
print("the real number is %i :"%(num1.real)) 
print("the imeginary number is : {:} ".format(num1.imag))
print(f"the imeginary number is{num1.imag}")

#*===========================#تحويل الرقم من فلوت لانترجر  convert float num to the integer num
#num2 , num3, num4  = 3.22 , 3323, 2+7j
#print (int (num2))
#print(float(num3))
#print(int (num4)) #*TypeError: can't convert "complex to float" ما بقدر احول كمبليكس نمبر لفلوت او انتيجر
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#*Random variable generators.

#import random
#print(random.randrange(1, 10))

#@2@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#*====arithmetic operators====
# + addtion 
# -subtraction 
# *multiplication 
# \ division
# % modulus  باقي القسمة
# ** exponent الاوس
# //floor divison بتطلع عدد صحيح بس يمعلم يقبل القسمة  print("120// 20")
#==================
list1 =[" mohammed ","ahmed","true",223, "one" ]
#print(list1) #[' mohammed ', 'ahmed', 'true', 223, 'one'] بطبع كل عناصر المجموعة
#print(list1[0]) #mohammed بطبع اول عنصر بس يمعلم
print(list1[-1]) # اخر عنصر بطلعلك
#print(list1[1:3])
#print(list1[::3]) #هينط 3عناصر ويطلعللك
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]  #list
print(friends[0:5:2]) # 0-5 range ,2= قديش يمشي 
print(friends[1:5:2]) #1-5 rang ,2= قديش يمشي                   # slicing

#*================ #List Methods [] الدوال الي بتعامل معاها الليست
#*append(),clear(),copy(),count(),insert(),extend(1),pop(),remove(),reverse(),sort()
#*https://www.w3schools.com/python/python_lists_methods.asp    //the referanses
                                                            #*@@اهم اشي  
#Python Collections (Arrays)
#*There are four collection data types in the Python programming language:
#*'List' is a collection which is ordered and changeable. Allows duplicate members. #*[]
#*'Tuple' is a collection which is ordered and unchangeable. Allows duplicate members.#*()
#*'Set' is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. but can be add and move()
#*'Dictionary' is a collection which is ordered** and changeable. No duplicate members.#* {keys:valus}

#list1[0]=2
#print(list1)  # لو بدك تعدل على الليست 

#*=================append(1)============ عشان تضيف عنصر جديد جوات القائمة 
#list1.append("maii")
#print(list1)
#*=================extend(2)============ هان بتدمدج ليست مع ليست يمعلم  
#a =[1,2,3,4]
#b= ["a","s","d"]
#a.extend(b)
#print(a)
#*==================remove(3)=========== هان بتحزف اشي من جوات اليست
#b.remove("s")
#print(b)
#*==================sort(4)============== بدك ترتب مثلا ممجوعة ارقام
#x =[ 3,44,5,-1,2,17,33]
#x.sort() 
#print(x)
#*x.sort(reverse=False) #[-1, 2, 3, 5, 17, 33, 44]  ترتيب يمعلم هان تصاعدي 
#*x.sort(reverse=True)  #[44, 33, 17, 5, 3, 2, -1]  ترتيب تنازلي 
#print(x) 
#*===================reverse()=========== عكس الليست
y= [" one", "two","th3","4th","5th"]
y.reverse() 
print(y)

#*=====================clear()===========
#* بلتزم هان يمعلم مثلا لو عندي تطبيق تسويق والزبون بيشتري وتراجع عن شغلة وبدوا يشيلها
#* او مثلا فالالة الحاسبة مثلا  

#prodects= ["tea", "milk"," meat","kokocoala" ] #anythings 
#prodects.clear()
#print(prodects)
#=========================================================
#prodects= ["tea", "milk"," meat","kokocoala" ]
#buys =prodects.copy()
#print(prodects)
#print(buys)
#================/
#prodects.append(" coco milk")  #هان ضاف عنصر جديد لليست بس بكون *اخر الليست 
#print(prodects)
#print(buys) # هان يمعلم 
#print(prodects.count(" string")) #بعد هان قديش العناصر الي جو الليست
#print(prodects.index("milk"))  #هان بجيبلك المنتج باي مكان فالليست

#*=================================insert()===================== >>==append() الفرق انوا اول الليست واخر الليست 
# *#هان يمعلم بدك تضيف عنصر جديد لليست باي مكان بدك اياه

#prodects.insert(0,"mai")      
#prodects.insert(-1 ,"mai")  
#print(prodects,"\n",prodects)
#*print(prodects.pop(0))=============pop()========================هان بتحزف من الليست عن طريق الاندكس
                                 #*The pop() method removes the specified index.
#*The del keyword also removes the specified index:
#Remove the first item:  del = delete
#thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#print(thislist)
#*                       str & tuple    الفرق بين ال 

                          #name = ("mohammed ")
                          #print(type(name))         <class 'str'>
#* comma only str and tuple___________________________________________
                          #name = ("mohammed " ,)
                          #print(type(name))          <class 'tuple'>
 
                          
                                 
#=============================================================================================================
#قم بحذف أول إسمين من القائمة ثم بعدها في سطر آخر قم بإزالة آخر إسم من القائمة
fr = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
fr.remove("Nasser")
fr.remove("Osama") 
#*or 
fr.pop(fr.index(1,0,2))
fr.pop(1)
print(fr )        #['Ahmed', 'Sayed', 'Salem']
fr.remove("Salem")
print(fr)         #['Ahmed', 'Sayed']
#*=============tuple concatenation============= هان بدمجلك اشياء مع بعض بمجموعة وحدة
#a=(1,2,3,4,5)
#b= ("moh","mai","dodo","mayar")
#c= a+b
#print(c)
#print("the postion of index is : {:d}".format(c.index(4)))
#or
#print(f"the postion of index is : {c.index(4)} ") # انا هان بنسى دايما حرف f 
#print(a)

#==============tuple destrut========
a =("mai","moh",3,"ali")
d , b,v, c = a                  # 
print(d,b,c)
print(c,b,v)
#================set============ هان يمعلم في كل مرة بتعطيك انكدس جديد مع العلم انوا ما بتقدر تختار اندكس بدك اياخ 
#mysetone= {"mai","two","th3","th4"}
#print(mysetone)
#print(mysetone[0]) #TypeError: 'set' object is not subsdatabaseiptable نوع الايررو هان ما بتقدر تحدد الاندس فيه

#* ==========union========  معناها اتحاد "يعني اشي اتحاد اشي " بس بطل كل مرة بشكل عشوائي 
b ={"mai", "mohammed","rana","yaqeen",}
#c ={1,2,3,4,5,6,7}
#d ={"f","r","5","t"}
#print(b.union(c))
#print(b.union(c,d))  
# نفسها برضوا زي هيك+
#print(b|c)

#===============add============ بدك تضيف اشي لمجموعة او ليست
#b ={"mai", "mohammed","rana","yaqeen"}
#b.add("meme")
#print(b)
#f= b.copy()
#print(b)
#print(f)
#remove()=========================================حزف عنصر مش موجود
#b =  {"mai", "mohammed","rana","yaqeen" }
#b.remove("rana")
##print(b)
#b.remove(1) #عنصر غير موجود ما بزبط
#print(b) #عنصر غير موجود ما بزبط

#* update()نفسها نفس الunion يمعلم 
#* =================update()==========هان يمعلم بعمل تحديث للاشي ولكن لو في اشي مكرر بين الي بدت تعملو ابديت بتجاهلو
#b =  {"mai", "mohammed","rana","yaqeen" }
#c ={1,2,"mai","rana"}
#b .update([ "css" ,  "html" ]) #ليست هان 
#b.update(c)
#print(b)
#____________________________________________________________________________
#update()             كيف تعمل ابديت (لتابل) مش[ ]ليست
#*1Python - Update Tuples
#*(tuples,) are unchangeable, meaning that you cannot change, add, or remove items once the tuple is databaseeated.

#Convert the tuple into a list to be able to change it:
friends = ("Osama", "Ahmed", "Sayed",) #tuple () <class 'tuple'>
a =list(friends) #[] 
a[0]="elzero"
friends=tuple(a)                    
print(friends)
#2
print("-"*30)
friends = ("Osama", "Ahmed", "Sayed") 
a =list(friends)
a.append("rana")  #ال3 طرق في اضافة العناصر 
fr.append("ertye")
fr.insert(2,"ranaaa")
friends= tuple(a)
print(friends)

#friends = {"Osama", "Ahmed", "Sayed",}
#name ={"elzero",}
#friends += name  # او extend بس لازم تكون ليست  
#[print(friends)
#*=================
#*----------------set methods()-----------------https://www.w3schools.com/python/python_ref_set.asp

#*difference() هان يعني الموجود في الاول مش موجود في التاني 
#a ={1,2,3,4,5,"osama","meme"}
#b ={1,2,3,"mai","moh"}
#print("-" *40 )         # جملة طباعة هان عادية 
#print(a.difference(b)) # هان يعني رجع الموجود في الاول ومش موجود في التاني على شكل سيت
#*a.difference_update(b) #هان يمعلم باخد الي مش موجود في القائمتين بحطهم في ليست لحال.
#print(b)The difference_update() #*method removes the items that exist in both sets.          
#                              #  يعني باخد الي  موجود في  اكس ومش موجود في واي وبرعهم سيت
#print(a.intersection(b))  #*هان معناها تقطاع "  يعني الي موجود في الاول و موجود فالتاني"\
#a.intersection_update(b)     
#print(b)
#print(a.symmetric_difference(b)) #هان يمعلم بشوف "الي مش موجود في الاتنين" وبحطهم في ليست.
#a.symmetric_difference_update(b) #هان يمعلم بشوف "الي      موجود في الاتنين"  وبحطهم في ليس
#print(b)
#=============================================================================================
#m={1,2,3,4,6}
#r={1,2,3,4}
#print(m.issuperset(r)) #True   " m "هل كل العناصر الموجودة في " # ار " موجودة في 
#print(r.issuperset(m)) #False هان العكس 
#< حاجة مختلفة عنهم>
#print(m.issubset(r))   #False      هل كل العناصر الي موجودة في "ام" موجودة في "r"
#print(r.issubset(m)) 
#print(m.isdisjoint(r)) # false 
#< حاجة مختلفة عنهم>
                         #*isdisjoint()
#a ={1,2,3,5}
#b ={"mai","moh" ,1 }

#print(b.isdisjoint(a)) #* true  "مفش عناصر هان موجودة هان" هل ولا عنصر من الاول موجود في التاني يبقى   

#*=========dictionary======== الشكل العام users =  "keys":"valuse",}
 
#  هان عندك "الكي" #ما بتاخد ليست اول شغلة زي هيك 

   # [1,2,3,4,] :"value"  <<list>>
#   (1,2,3,4,5)tuple لازم الكي يكون يا اما رقم او نص او 

#  الكي لازم يكون مميز وفريد بدون تكرر
# هان الندكبس ما بزط لازم لما بدنا اسم اشي من خلال "الكي"ي
#*=========Dictionary Methods      دوال الدكشنري

#* values() update() setdefault() popitem() pop() keys() items() get() fromkeys() copy() clear()

#* dic1 'one dimentions'  
user={
          "name"    : "mohammed",         #"key":"string"
          "age"     : 22 ,                #"key": "number"
          "country" : "palestine"  ,         
          "skills"  : ["python","html","css5",],            #"key": "list"
          "study"   : "web developer/app developer "
}
#print(user)
print("your age is: %i " % (user.get("age"))) #دمجنا ال "formating" ممتاز يمعلم
#print("your name is : %s" %(user.get("name")))
##print("your age is {:}".format(user.get("age")))         # بطريقة تانية ممتاز
print((f"your age is {user.get(22)}"))
#print(user["name"]) 
#print(user.keys())  #طباعة الكي dict_keys
#print(user.values())# dict_values
#*********************************&&*************************************
#* هان يا معلمي 'two dimensional dictionary '  

#languages ={
#"one" :               # يعني الفاليو هان بتكون ديكنشري تاني+-++
      #"name" :"js",
     #"progress": "90%",
     #},
#"two" :{
    #  "name":"html",
    #  "progress":"70%"     
    #  },
#"three":{
    # "name":"python",
    # "progress":"90%"
#}                 
#}
#print(languages)
#print(languages["two"])
#print(languages["three"]["name"])
# dictionary lenth
#print(len(languages))
#print(len(languages["two"]))

#* greate dictionary from variables : 'nested dic'

frameworkeone =  {         # بنخزن المحتوى في variable =frameworke
     "name":"js",
     "progress":"20%"
}
frameworketwo ={
     "name":"py",
     "progress":"70%"
}
frameworkeothree ={
     "name":"html",
     "progress":"40%"
} 
                    #خزن كل االفاريبال في قاريبال رئيسي
allframeworke ={
     "one":frameworkeone,  #"key":"value","key","value", ...
     "two":frameworketwo,
     "three":frameworkeothree
     
}
print(allframeworke )
allframeworke.clear()  
print(allframeworke)

#*clean()@@@@@@@@@@@@@@@@@@@@@@@@@
allframeworke.clear()
print(allframeworke)

#*update()@@@@@@@@@@@@@@@@@@@@@@@@@

#* بدنا نضيف على الفريم ورك عنصر جديد
#allframeworke.update( "name":"flutter", 
                     # "progress":"99%",})
#print(allframeworke)
#========================@==================================
mechactroins_engineer_one= {
     "spaical one":" mechanical enginnering" ,
     "progress":"60%"
     
}
mechactroins_engineer_two={
     "speical two ":" electrical enginnering" ,
     "progress":"80%"
     
}
mechactroins_engineer_three={
     "speical two ":" electronic enginnering" ,
     "progress":"50%"
     
}
mechactroins_engineer_fore={
     "speical two ":" software  enginnering" ,
     "progress":"80%"
     
}
mechactroins_engineer ={
     "one":mechactroins_engineer_one,
     "two":mechactroins_engineer_two,
     "three":mechactroins_engineer_three,
     "fore":mechactroins_engineer_fore
}
print(mechactroins_engineer)
#update()
mechactroins_engineer.update({
     "speical five ":" embedd  enginnering" ,
     "progress":"80%"
     })
print(mechactroins_engineer)
print(mechactroins_engineer.keys())
print(mechactroins_engineer.values())

#* setdefult() ا@نفس الكي بين الي بدك تضيفوا والي في الدشننري القديم اعطي القديم
          #    اختلف الكي بين الجديد والقديم ضيفوا لدكشنري 
user ={
     "name":"mai"    
}
print(user)
print(user.setdefault("name","mohammed"))
print(user.setdefault("age","22years old"))  
        #or
user.setdefault("age",22)
print(user)

#===================================================
#* popitem()            بحزف اخر اشي ضفتوا للدكشنري
#* update() 
#* name functions ["keys"]=values اضافة عنصر جديد user["keys"]=values
user ={
     "name":"mai" ,
     "skills":" python" ,
     "progress":"55%",     
} #* check on the items  using if condions
print(user)
if "name" in user :
     print(f"the items are found{name}") 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22
user.update({"age":22})                 #* @@@@@اضافة جديدة@@@@
print(user)# @or
user.update({"mohammed":20})
user.setdefault("id number","20182324")   #* ن"نفس الاشي " اضافة اشي جديد
print(user) # @or            
user["eng"] =2018                         #*ن"نفس الاشي " اضافة اشي جديدة
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22
#*popitem()
print(user.popitem())                #* \\ بحزف اخر اشي ضفتوا للدكشنر ي بس يمعلم
                                   
#* item()      # returns >> tuple  <<   # بترجع كل اشي ضفتوا جوا ليست مع كل الدكشننريت
#*The items() method will return each item in a dictionary, as tuples in a list.
alluser = user.items()
user.update({
    " memory":"2000-5-19"
})
print(alluser)
#output:dict_items([('name', 'mai'), ('skills', ' python'), ('progress', '55%'), (' memory', '2000\x019\x05')])    #


#*_______________________________________________________________ 
# ------[1,3,4,5,''mai] #*         هاي list
#_______________________________________________________________ 
# ------(1,2.3.4)       #*        هاي يمعلم tuple
#*_______________________________________________________________ 


#fromekeys()  انشاء ديكشنري  كجموهة تابل 
m= ("mohammed ","ahmed","rana","saja")  #keys     # نوعها عبارة عن tuple      () 
r= 2     # valus
print(dict.fromkeys(m,r))
print(type(m),type(r))  #<class 'tuple'> <class 'str'>   بترجعلك 
username=("mai",1,2,3,"rana","yaqeen")
password=(1200,1300,1400,1500)
dict.fromkeys(username,password)
print(dict.fromkeys(username,password))


#*=======================================================================================
                               #*####### Boolean()#######*#
#*========================================================================================
#boolean >>true or false
#*True values

print(bool(" ")) #space
print(bool("string"))
print(bool((0,1,))) #tuple
print(bool(100)) #int
print(bool({" ":" "})) #dict
print(bool(100.95)) #floating points
print(bool([1,2,3,4])) #list

#flase values
print(bool("")) #nonspace
print(bool(0))
#print(bool(NONE))
print(bool(False))
print(bool(()))
print(bool({}))


  
         
            #الشروط هان #*boolen operators
            #*and " * ", or "+"
            #*not !
#*and == لازم كل الشروط تتحقق            
#*or ==     شرط واحد يتحقق 
print( "=" *30)
age =22
country = "palestian" 

print(age >16 and country == "palestian")  
print(age >16 and country == "eygpt") 

print( "=" *30)

print(age >16 or country == "palestian")   
print(age >16 or country == "eygpt")  
print(not (age >16 or country == "eygpt"))    #شرط واحد  تحقق يبقى صح


#*-------------------------
# *---assignment operetor--- lect:35
#*-------------------------
#  =
# += جمع
# -=
# *=  طرح
# /=  قسمة
# **= الاوس exp
# %=  باقي القسمة
# //=
#=cdd----------------------------------

#*--------------------------------------
#*----comparison operators : lect :36 بتقارن بين العناصر زي  
#*--------------------------------------

#* [==] equal
#* [!=] not equal
#* [>]  greater than
#* [<]  less than 
#* [<=] equal or less than
#* [>=] equal or less than
#//=========================================================

#*-1  [==] equal
print("-"*50)
print(100 == 100)
print(100 == 200)
print(100 == 100.00)


#* [>]  greater than

print("-"*50)
print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40)

#* [<]  less than 
print("-"*50)
print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 40)

#*-2  [!=] not equal
print("-"*50)
print(100 != 100)
print(100 != 200)
print(100 != 100.00)

#* [>]  greater than or less than
print("-"*50)
print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
 
#* [<]  less than  or less than
print("-"*50)
print(100 <= 100)
print(100 <= 200)
print(100 >= 100.00)
print(100 <= 40)

#*--------------------------------------
#*----type conversion--- : lect :37 بنحول البيانات من نوع الي نوع 
#*--------------------------------------
#  من اهم المواضيع في لغة بايثون وفي باقي اللغات
 
 #* >>>>>>>>     set()  , tuple() , list() ,  dict() 
  
 
#* str()  نحول لسنرنق 
a =10.0
print(type(a))
print(type(str(a))) 

#* tuple()
c = "mohammed "        #*string
d =[1,2,3,4,5]         #*list
e ={"R","a","n","a"}   #*set
f ={"one":1, "two":2 } #*dictionry 
print((tuple(c))) 
print((tuple(d))) 
print((tuple(e))) 
print((tuple(f)))

#* list()
c = "mohammed "        #* string
d =(1,2,3,4,5)         #*tuple
e ={"R","a","n","a"}   #*set
f ={"one":1, "two":2 } #* dictionry
print((list(c))) 
print((list(d))) 
print((list(e))) 
print((list(f)))

#* set
c = "mohammed "        #* string
d =[1,2,3,4,5]         #*list
e ={"R","a","n","a"}   #*set
f ={"one":1, "two":2 } #* dictionry
print(( set  (c))) 
print(( set  (d))) 
print(( set  (e))) 
print(( set  (f)))

#* dict      هان ما بتعامل الا مع التبل والليست ولازم زي هيك   
         
d =(("a",1),("r",2),("m",3))          #*tuple
f =(["one",1],["two",2],["three",3])  #*list   
print(( dict (d))) 
print(( dict  (f)))   #*{'a': 1, 'r': 2, 'm': 3}
                      #*{'one': 1, 'two': 2, 'three': 3}

#*-------------------------
# *---usre input--- lect38
#*-------------------------

fname =input("what's your first name> ")
mname =input("what's your middel name> ")
lname =input("what's your last name> ")
fname =fname.strip().capitalize()#*>>
mname =mname.strip().capitalize()#*>>>> عشان نشيل الفراغات الي بين الكلام واول حرف كبير برضوا  upper =capitalize 
lname =lname.strip().capitalize()#*>>
print(f"welcome {fname}{mname:.1s}{mname} nice too meet you!")
# مثلا بدي فالاسم الوسطاني اطبع اول حرف زي هيكك
#* Mohammed "h" abu raid .>>> {:.1s}       1تعني الحرف الاول 


#*-------------------------
# *--- parctical slice email--- lect39
#*-------------------------
                                      #*[0:4] هدا هوا السلايس slice 
 
name = input('what\'s your Name ? ').strip().lower().capitalize() #mohammed 
Email=input('what\'s your Email ').strip()   #aburaida2017@gmail.com
print(f'hello {name},your email is {Email}')
thename =name[:Email.index("@")]
theemail= Email[Email.index("@")+1:]
print(f' your username is  thename &your website is{theemail}')

username =name[:] 
#*-------------------------
# *--- parctical your age full details --- lect40
#*-------------------------

# نحسب العمر بالاشهر والاسابيع والايام والاساعات والدقاق 

age =int(input('what\'s your  full age ?'))
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

#*-------------------------
# *--- control flow  --- lect41
# *--- if ,elif, else ---
# *--- make decisions ---
#*-------------------------

uname= "mohammed"
ucountry ="gaza"
ccours ="python course"
cprice =100

if ucountry =="palestian":   
  print(f'hello,{uname} because you are from {ucountry}')
  print(f'the course \"{ccours}\" price is: ${cprice-20}')
   
elif ucountry == "egypth":
      print(f'hello,{uname} because you are from {ucountry}')
      print(f'the course \"{ccours}\" price is: ${cprice-30}')
else:
     print(f'hello,{uname} because you are from {ucountry}')
     print(f'the course \"{ccours}\" price is: ${cprice-80}')
     
#*-------------------------The pass Statement-------------------     
# فرضا بدنا مثلا نعمل جملة اف وبدنا اياه بدون متحتوى يعني ما يعطيك ايروو لما تكون بجون محتوى زي هيك
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.    
a = 33
b = 200

if b > a:
  pass   

 
#*-------------------------
# *--- Nested ifالمتداخلة--- lect42
#*-------------------------
 # هان لو كان عندك عدد الدول محدود ,طيب لو كان عند ليست كامل من 20 دولة ... شوف محاظرة 45
uname= "mohammed"
ucountry ="jorden"    #conditons 2
ccours ="python course"
cprice =100
isstudent =True      #conditons 1

if ucountry =="palestian" or ucountry=="jorden": 
     if isstudent==True :
       print(f'hello,{uname} because you are from {ucountry} and student')
       print(f'the course \"{ccours}\" price is: ${cprice-30}')
     else:
          print(f'hello,{uname} because you are from {ucountry}')
          print(f'the course \"{ccours}\" price is: ${cprice-40}')      
elif ucountry == "egypth":
      print(f'hello,{uname} because you are from {ucountry}')
      print(f'the course \"{ccours}\" price is: ${cprice-50}')
else:
      print(f'hello,{uname} because you are from {ucountry}')
      print(f'the course \"{ccours}\" price is: ${cprice-80}')

#*-------------------------
# *--- teranry conditional operatorsالمختصرة 
#*-------------------------  Editor: Format On Save
 #*هاي الطريقة بتزبط لما تفعل الفورمات اون سيف 
 
country ='gaza'
if country== 'gaza':print(f'twerfeor country')
elif country== 'rafah':print(f'twerfeor country')
else:print(f'twerfeor country')

uname= "mohammed"
ucountry ="jorden"    #conditons 2
ccours ="python course"
cprice =100
isstudent =True      #conditons 1

if ucountry =="palestian" or ucountry=="jorden": 
     if isstudent==True :
       print(f'hello,{uname} because you are from {ucountry} and student')
       print(f'the course \"{ccours}\" price is: ${cprice-30}')
     else:
          print(f'hello,{uname} because you are from {ucountry}')
          print(f'the course \"{ccours}\" price is: ${cprice-40}')      
elif ucountry == "egypth":
      print(f'hello,{uname} because you are from {ucountry}')
      print(f'the course \"{ccours}\" price is: ${cprice-50}')
else:
      print(f'hello,{uname} because you are from {ucountry}')
      print(f'the course \"{ccours}\" price is: ${cprice-80}')
                           
                           
moverate = 18   #*   +18 vedio
age= input('enter your age ?')
if  age == 12:
     print(f'because your age less than  moverate')
     print(f' your age is :{age},can\'t be watch the vedio and')
else:
     print(f'u can watch the vedio and happy watching vedio')
# or 
#*This technique is known as Ternary Operators, or Conditional Expressions.
#* condtions if true | if condtions |else | condtions if false  "هده العوامل هي  "  
print('moverate not good 4u ' if age < moverate else' moverate good 4u and happy watching ') #جملة انجليزي 
print('yes') if 'm' in name else print('no')  # فسطر واحد بس 'المرونة' 
#*Ternary Operators///// lect43



#*-------------------------
#*--- calculate age advanced version & training --- lect44
#*-------------------------
#writ note 
print("-"*80)
print(' you can write the first letter or full name of the time unite '.center(80,'-')) 
print("-"*80)
age = int(input('pleas,enter your age ?'.title().strip()))
unit = input('please choose time unit :mounth, weeks ,days||'.strip().lower())
# get time unite 
mounths =int(age)*12
days =int(age)*365
weeks =int(mounths)*4
if unit== "mounth" or 'm':
     print(f'your choosed the unit mounths')
     print(f'you lived for {mounths:,} Mounths ')
        
elif unit== 'days' or 'd':
     print(f'your choosed the unit days')
     print(f'you lived for {days:,} Days ')  
     
elif unit== 'weeks' or 'w':
     print(f'your choosed the unit weeks')
     print(f'you lived for {weeks:,} Weeks ')
else:
     print('your choosed was false,please try again ! ')

#*-------------------------
# *--- membership operators  العضوية--- lect45
#*------------------------- هل العنصر هدا موجود عضو في المجموعة ؟؟؟
        #* in 
        #* not in                              تحسين: Nested ifالمتداخلة--- lect42
#*-------------------------

# string 
name = 'mohammed '
if 'm' in name :
     print("yes" )
else:
     print('no')
#or
#print('yes') if 'm' in name else print('no')
#print('a')if name =='mohammed' else name!='mohammed':print('b')
# فسطر واحد بس 'المرونة'  
#*Ternary Operators///// lect43
#*---------------------
name = 'mohammed '
print('m' in name ) 
print('s' in name ) #* موجود في 
print('m' not in name )     #* غير موجود فيه



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#*lists

africa_country =["egypt",'ksa','kuwait','bahrain']
price1  =70
yorob_country =['italy ','usa' ,'canada']
price2  =70

ucontry =input('enter your country :'.capitalize().strip())
if ucontry in africa_country :
     print(f'hello dear ,you have aprice ${price1}')
elif ucontry in yorob_country:
     print(f'hello dear ,you have aprice ${price2}')
else:
    print('you have\'t price  ') 

#*-------------------------
#*--- practical membership control  --- lect46
#*-------------------------


database_emply_admin =['mohammed','rana','yaqeen','mai','obeyda']
name =input("please ,enter your name admin!>>").strip().lower()
if name in database_emply_admin:
     print(f'hello {name},welcome back'.center(30,'@'))
     print(f'{name} you are admin !')
     options =input(f'{name} do you want to the\"delete or update\" your name??')
     #* remove options 
     if options == 'delete'.lower() or options == "d".lower():
          database_emply_admin.remove(name) #لتخزين كل اشي جوات الليست
          print('name deleted !'.center(15,'>>'))
          print(f'new admins !{database_emply_admin}')
     #* update options      
     elif options == 'update'.lower() or 'u'.lower():
          print(f'your old name is>>  name.capitalize()')
          new_name =input(f'inter your new name please!'.lower())
          database_emply_admin[database_emply_admin.index(name)] =new_name 
          print('name updated,thank you !!'.upper()) 
          print(f'new database {database_emply_admin}')           
     else:
          print("wrong options ,try again !!")
else :
     print(f'hello {name } you are\'t admin !')
       
     adname =input('choose \"yes or no\" to added  ')
     print('u  can choose yes or no or>>" \'y , n\' "<<') 
     if adname == 'y' or' yes' : 
                print('u have been added ') 
                database_emply_admin.append(adname) 
                print(database_emply_admin)
     else:
                print('u are\'t added , thank u')
                

#*-------------------------
#*--- loop >>-- while training lect49
#*--- simple bookmark manange---
#*-------------------------              
nameweb1 =[]      #database[list]
webpage  = 5  
while webpage  > 0:         
     
     web =input('website without https://')
     nameweb1.append(f' https://{web.lower().strip()} ')
     webpage -= 1
     print(f'<>  website added, \'{5-webpage}\' plases left  <>') #   العد بكون 1234
     print(f'\'{5-webpage}\' ')                                   # العد بكون 4321
     print(nameweb1)   
else: 
     print ('END ADDED WEBSITE'.center(30,"#"))
      
if len(nameweb1) > webpage :        #* check if list empty.
     #*---------------------------------------
     nameweb1.sort()                    
     print(f'the list is >>>')
     index =0 
     while index < len(nameweb1):    
      print(nameweb1[index]) # عشان يطبعلك اياها فوق بعض
      index+=1  
     #*------------------------------------------
#*========================appliction2     
listweb =[]
page = 5

while len(listweb) < page :
     
     web =input('website without https://')
     listweb.append(f'https://{web}')
     print(f'<>website added,\'{5-len(listweb)}\'plases left<>')
     print (listweb)
                
else:
     print ('END ADDED WEBSITE'.center(30,"#"))     

if len(listweb) == page:
     
     listweb.sort()
     print(f'the all list website is   >>>')
     index =0     
     while len(listweb) > index :   
      print(listweb[index]) 
      index+=1                                                  

#*------loop >>while ..training..50

# يوزر يدخل كلمات مرور مع عدد حاولات وتنبيه برضوا للمحاولة الاخيرة


try1 = 3
listpassword =[] #* ليست التخزين لكل كلمات المرور
password ='rana2001'
word =input('enter your password :').strip().lower()

while  word != password:
                          #*  tarnary operators تنبيه للفرصة والمحاولة الاخيرةs 
      print(f"wrong password and {'last'if try1 == 0 else try1} chance left")
      try1-=1 
      word =input('enter your password :').strip().lower()      
      listpassword.append(word) #*عشان يطبع كل كلمات المرور في ليست وحدة
      print(f'list-password is \'{listpassword }\'')
      print()
      if  try1 == 0 :
          print('all tries if finished'.center(30,"#"))
          listpassword.append(word) #*عشان يطبع كل كلمات المرور في ليست وحدة 
          print(f'list your tries-password is \'{listpassword }\'')
           #*--------------------------------
          listpassword.sort()              #*
          index =0                         #*
          while index < len(listpassword): #*[جزئية عرض الباسورد في اسطر]
           print(listpassword[index])      #*
           index+=1                        #*
           #*--------------------------------
          break          #* اي جملة بعدها مش هتنطبع

else:
      print(f'correct password //>> {word} <<'.center(30,"#"))  
    
#*----------------------------------                  
#*------loop >>for ..training..51    
#*----------------------------------     

name  ='mohammed '

for letters in name :          #*letters : اي اسم انتا بدك اياه
    
     print([ {letters.upper().strip() } ]*12)
     
else: 
     print('    <> done <>')
#***************************************     
number =[1,2,3,4,5,6,7,8,9,10]     

for num in number:
    
    #print(f'the number is {number[num]} ')
    if num %2 == 0 : # الارقام التي تقبل القسمة على 2
        print(f'the number is even {num}')
    else:
        print(f'the number is odd  {num}')
else :
        print(f'the loop is fineshed') #*هان مش شرط عشان هيتحقق هيا دايما هتتحقق     


#*----------------------------------                  
#*------loop >>for ..training..52---    
#*----------------------------------  

#* range 
myrange =range(1,51)

for range in myrange:
    print(f'my range is {range}')
    
for x in range(6):
  print(x)    

#Indatabaseement the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)  
  
  
#* -----dictionary in loop------ 


myskills ={
    'html':'90%',
    'css':'80%',
    'js':'70%',
    'python':'60%',
       
}    #* ''طريقة الحصول على الداتا من الدكشنري

print(myskills['css'])
#or
print(myskills.get('css'))
for skills in myskills:    #'1skills هي العناصر الي جوا الmyskills 2' 
    print(skills)
    
    print(f'my progress in lang {skills} is :{myskills.get(skills)}')
    #*or
    print(f'my progress in lang {skills} is :{myskills[skills]}')



#*------loop >>nested loop  training..53    
peoples =['mai','rana','yaqeen','rami','ali']

skills = ['html','css','python','js']

for name in peoples:       #outer loop
    print(f'{name.capitalize()} has skills : ')
    
    for myskills in skills:  #inner loop
        
        print(f'{myskills}>>{name}')
    
'''languages ={
"rana" :               # يعني الفاليو هان بتكون ديكنشري تاني+-++
      "html":"30%",
      "css" : "90%",
      "py"  :'70%'
},
"mai" :{
      "html":"50%",
      "css" : "70%",
      "py"  :'80%'     
      },

"ali":{

     "html":"30%",
      "css" : "70%",
      "py"  :'10%'
}                 
}'''
#print(languages["ali"])
#print(languages["ali"]['css'])

for name in languages:
    
    print(f'{name} skills and prog is ')
    
    for skills in languages[name] :
        
        print(f'{skills}=={languages [name][skills]}')
    
''' 
languages ={
"rana" :               # يعني الفاليو هان بتكون ديكنشري تاني+-++
      "html":"30%",
      "css" : "90%",
      "py"  :'70%'
      
     },
"mai" :{
      "html":"50%",
      "css" : "70%",
      "py"  :'80%'     
      },
"ali":{
     "html":"30%",
      "css" : "70%",
      "py"  :'10%'
}                 
}'''
for name in languages: 
      print(f' my name is : \'{name.capitalize()}\'')
      
      for skills in languages[name] :
          print(f' the skills is {skills} >> {languages[name][skills]}')
#print([languages['rana']])
#print(languages['rana']['html'])
#print('8'*30)

#*-----------------------------------------------------------------------------------
#*----loop advanced ----  54 #تابع لدكشنري
#*-----------------------------------------------------------------------------------
 
                          #* بطريقة تانية واسهل واسرع 
                          #* item() بتجيبلك عناصر الدكشنري


myskills ={
    'html':'90%',
    'css':'80%',
    'js':'70%',
    'python':'60%',
       
} 
#* item() بتجيبلك عناصر الدكشنري
print(myskills.items()) 
for skills in myskills:            #*1
      print(f'{skills}>> {myskills[skills]}')

print('*'*40)                 #*or
                                   #*2
for skills_key ,skills_value in myskills.items():
      print(f'{skills_key} >> {skills_value}')      
'''      
languages ={
"rana" :               # يعني الفاليو هان بتكون ديكنشري تاني+-++
      "html":"30%",
      "css" : "90%",
      "py"  :'70%'
      
     },
"mai" :{
      "html":"50%",
      "css" : "70%",
      "py"  :'80%'     
      },
"ali":{
     "html":"30%",
      "css" : "70%",
      "py"  :'10%'
}                 
}     
'''
#print(languages.items())
for name_key ,skills_value in languages.items()  :
      
      print(f'{name_key }>> ' )
      
      for prog,myprog in skills_value.items() :
            print(f'{prog} >>>{myprog}')
      
      
#*----------------------------------
#*----break ,pass ,continue ----54
#*----------------------------------


#*--break :وقف
mynamber =[1,2,3,4,10,12,5,7,8]

for namber in mynamber:
      
      if namber ==10:
            break 
      print(namber)

print('$'*20)
#*--pass : استمر
mynamber =[1,2,3,4,10,12,5,7,8]

for namber in mynamber:
      
      if namber ==10:
            pass             # مثلا الكود مش جاهز فبحطها عشان ما يعطي ايروو
      print(namber)
print('$'*20)      
#*-- contiuos
mynamber =[1,2,3,4,10,12,5,7,8]

for namber in mynamber:
      
      if namber ==10:
            continue     #عند ال10 فط وكمل اللوب 
      print(namber)    

#* طباعة الارقام+إذا كان الرقم أقل من 10 ضع قبله صفر     
num =0
while num < 20 :
         print(str(num+1).zfill(2))
         num+=1 
print("All Numbers Printed")


#*----------------------------------
#*---functions and return <def> ----55
#*----------------------------------
def functions_name(name):
      return f'YOUR NAME IS {name}' 
       
name =functions_name('rana')   
print(name)
#*----------------OR-----------
def age(age):
    return f'your age is {age} '
a =age(22)
print(a)
#*----------------and-----------

def age (age):
    print(f'your age is {age}')
age(22)    
# def >>keyword define
# age>>name functions
# (age)>>parameters
# print()>> task
# age(22) >>call fun & 22>>argumnts


#*----------------------------------
#*---functions parameters and arguments ----57
#*----------------------------------

#a,b,c ='rana','lana','soso'
#print(f'hello {a}')
#print(f'hello {b}')
#print(f'hello {c}')

#* def      >>> function keyword [define]
#* pepols() >>> functions name
#* name     >>> Parameter
#* print(f'hello {name}')>>> task 
#* pepols('mai') >>>mai is arguments
#.
#.  التعريف 
#.
a,b,c ='mai','rana','moh'
def pepols(name):              #name = anythins parapmeters
    print(f'hello {name}')  
pepols(a)         
pepols(b)       
pepols(c) 
      
      
def addition (num1 ,num2): #parameter
      print(num1+num2)
      
addition(3,4)      #argument
addition(32,4)
#*********************************
def addition (num1 ,num2):
      
     if type(num1)!= int or type(num2)!= int:
            
            print('oniy interger allowed ')
     else:
             print(num1+num2)
          
addition(3,4)      
addition('oasama',41)


def full_name(first ,middell ,last):
      
 print(f' hello {first.strip().capitalize()} {middell:.1s} {last.capitalize()}')
      
full_name('mohammed', 'hazem ' ,'rabuaida')      

# لو كان ادخال من الشخض

def full_name(first ,middell ,last):
      
 print(f' hello {first.strip().capitalize()} {middell:.1s} {last.capitalize()}')
      
full_name(input('ENTER first name: '),input('ENTER sec name :'),input('ENTER last name: '))



#*----------------------------------
#*---functions  packing ,unpacking arguments (*arge)----58
#*----------------------------------


#* 1 argument is tuple
 
#* عدد لا محدود من          (*arge)

                        #outputs
num =[1,2,3,5]          #*  1 2 3 5
                        #*  [1, 2, 3, 5]     
                        #*  1 2 3 
print(num)                               
print(*num)   #* عدد لا محدود من الباراميتر(*parm)


def name(name1,name2,name3) : #Parameter
     name =[name1,name2,name3]  
     for name in name:
          print(f'hello {name}')
          print(type(name))        #*<class 'str'>    
name( 'mohammed','mai','lana' )   #arguments   

#* طيب لو بدي اضيف شخص تاني  على الاسماء الاشي التقليدي زي هيك

def name(name1,name2,name3,name4) :
       
      allname =[name1,name2,name3,name4]   #* بتخزن كل في ليست 
      for name in allname:
            print(f'hello {name}')
name( 'mohammed','mai','lana','rana' ) 
                                            #* = the solutions :
                                            
#* لكن الاشي صعب لما يكون عندك آلاف الاسماء من الموظفين
# الحل

def name(*name) : #Parameter
       
      for name in name:
            print(f'hello {name}')
            print(type(name))        #*<class 'str'>    
name( 'mohammed','mai','rana','lana','ranoosh' )

#* ادخال من المستخدم
def name(*name) : #Parameter
       
      for name in name:
            print(f'hello {name}')
            print(type(name))        #*<class 'str'>    
print( input('ENTER YOUR NAME :') )

print('-'*40) #سبريتور

def name(*all_employes):
     print(type(all_employes)) #*  <class 'tuple'>
     for name in all_employes:
            print(f'hello {name}')
name( 'mohammed','mai','lana','rana','ali' )            
def foo(a, b, c):
    print(a, b, c)
obj = {'b':10, 'c':'lee'}

foo(100,**obj) #'a' =100,'b'=10, 'c' =lee

def foo(param1, *param2):
    print(param1)
    print(param2)

def bar(param1, **param2):
    print(param1)
    print(param2)
                             #1
                             #(2, 3, 4, 5)
                             #1{'a': 2, 'c': 3}
foo(1,2,3,4,5)               
bar(1,a=2,c=3)
#-------------
def sum(*args): #pack the received positional args into data structure of tuple. after applying '*' - def sum((1,2,3,4))
    sum = 0
    for a in args:
        sum+=a
    print(sum)

sum(1,2,3,4)
#* or using items
def sum(**args): #pack keyword args into datastructure of dict after applying '**' - def sum({a:1,b:2,c:3,d:4})
    sum=0
    for k,v in args.items():
        sum+=v
    print(sum)

sum(a=1,b=2,c=3,d=4) #positional args sent to function sum
#*--------------------------------------------------تكليف
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
#calculate(10, 20,) # 30
#*----------------------------------
#*---functions default parameters ----59
#*----------------------------------

def say_hello(name,age,country):
 print(f'hello {name} your age is {age} and your country is {country}')
     
say_hello('mohammed',22,'gaza')
say_hello('rana',21,'gaza')
say_hello('mai',21,'gaza')
print('-'*30)
                     # فرضا المستخدم ما بدوا يدخل عمروا و بلدوا 
                     
#-----------------------------------------------------------------
def say_hello(name,age ='unknown',country='unknown'):
 print(f'hello {name} your age is {age} and your country is {country}')
     
say_hello('mohammed',22,'gaza')
say_hello('rana',21)
say_hello('mai') #TypeError: say_hello() missing 1 required positional argument: 'country'

print('-'*40)

def name(*all_employes):    #*     (*)>>>> tuple
     print(type(all_employes)) #* بتخزن كل في ليست  <class 'tuple'>
     for name in all_employes:
            print(f'hello {name}')
name( 'mohammed','mai','lana','rana','ali' )            
     # قد ما تزود ارجيمنت عادي

           #* 2 arg is (dictionry )
           
def name(**name) : #Parameter    
       #* بتخزن كل في ليست 
      for dell in name:
            print(f'hello {dell}')
            print(type(dell))        #*<class 'str'>    
name( mohammed ='30%',mai ='50%',rana='40%',lana='70%',ranoosh='10%' )


#*----------------------------------
#*---functions  packing ,unpacking arguments (**args)- ----60
#*----------------------------------
# 2 arg is dictionry 

def name(**all_employes):            #*     (**)>>> dictionary
     print(type(all_employes)) #* بتخزن كل في ليست  <class 'dict'>
     for name in all_employes.items():
            print(f'hello {name}')
name(html ='30%',css ='40%',js ='60%',py ='50%' )            
'''
#* لو دكشنري حقيقي طيب زي هيك 
languages =  {
"rana" :               # يعني الفاليو هان بتكون ديكنشري تاني+-++
      "html":"30%",
      "css" : "90%",
      "py"  :'70%'
      
},
"mai" :{
      "html":"50%",
      "css" : "70%",
      "py"  :'80%'     
      },

"ali":{
     "html":"30%",
      "css" : "70%",
      "py"  :'10%'
}}
'''
def name(**languages):            #*     (**)>>> dictionary
     print(type(languages)) #* بتخزن كل في ليست  <class 'dict'>
     for names ,keys in languages.items():
            print(f'hello {names}')
            for skills , value,rank in keys.items():
                  print(f'{skills}>>> {value}>>{rank}')            
name(**languages)

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

#*--------------------------------------
#*---functions packing,unpacking arguments trainings--61
#*--------------------------------------

myskills ={
    'Roby':'90%',
    'python':'60%',      
}
typle =('css','html','js')

def show_name(name ,*skillswithout ,**skillswithprogress ):
      print(f'hello {name} \n*skills without progress is : ')
      for skill in skillswithout:
            print(f'-{skill}') 
            
            print('*skills with progress is:')      
            for skillskeys ,skillsvalue in skillswithprogress.items():
                  
                  print(f'-{skillskeys}>> {skillsvalue}')
show_name('mohammed',myskills,typle )     
#*----------------------------------
#*---fun... scope - ----62
#*----------------------------------
 
x =1 # globle scope 
def one ():
      #global x
      x=7 #local scope
      print(f' functions globle scope is {x}')
def two ():
      x=10 #local scope
      print(f'<>functions globle scope is {x}')     

one()           # اول اشي بطبع هاي 
print(f'globle scope is {x}') # بعدين هاي 
two() # بعدين هاي يمعلم 
print(f'globle scope is <><>{x}') #بعدين هاي  من x=1

#*----------------------------------
#*---fun... Redatabasesion - ----63
#*----------------------------------
# مهم جدا جدا الدرس 
#يعني دور على نفسك جوا نفسك زززز
print('\U0001F600') # ايموجي 😀
print('\U0001F601') # ايموجي 😁
print('\U0001F603') # ايموجي 😁

#السؤال برجعلك الكلمة واضحة ونضيفة قد ما يكون فيها مكرر
def cleanword (word):
      if len(word)==1 : # تحقق من الطول
            return word
      print(f'print STATR condtions {word}')
      if word[0]==word[1]:
            print(f'print befor condtions {word}') # هل الحرف الاول بيساوي التاني 
            return  cleanword (word[1:])
      print(f'print befor<><>condtions {word}')      # بحزف الحرف الي الاندكس تاعوا صفر وبكمل للاخر
      return word[0] +cleanword (word[1:])
                                                      #   بعد ما حزف صار الي كان الاندس تاعوا  صفر هيساوي الجديد 1   
print(cleanword('mmmoohhhhhaammeeeddd \U0001F600'))


#*----------------------------------
#*---fun...lambda - ----63
#*----------------------------------
 #[1] فانكشن مجهولة يعني ملهاش اسم 
 #[2] استداعئها بدون نيم 
 #[3] يمكن استخدامها من ريترن فانكشن اخرى
 #[4] يمكن استخدامها في فانكشن بسيطة اما  فب المشاريع الكبيرة الفانكشن العادية
 #[5] بنكتبها في سطر واحد مش في بلوك فانكشن كبير 
 #[6] التايب بيكون فانكشن


#فانكشن العادية
def says(name):
      return f'hello {name}'
print(says('mohammed'))
print(says.__name__) # ااسم الفانكشن#says
#*--------------------------------
# الفانكشن لامبيد
hello =lambda fullname : f'hello {fullname}'
print(hello('ahmed ahmed ahmed'))
print(hello.__name__) #<lambda> ملهاش اسم
print(type(hello))#<class 'function'>
#------------------------------------
list4 = ([(), 0, False])
def my(my_any): return 'triu'
if any(list4):
    print(f'TRUE*>> {list4}')
else:
    print(f'FALSE* {list4}')
    
#* من تكاليق الزيرو
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
   

#*----------------------------------
#*---file handling - ----65 intro التعامل مع الملفات..
#*----------------------------------
#*- 'a'>>append--open file for appending values,databaseeat file if not exists
#*- 'r'>>read--[defaults value] open file for read &give error if file is not exist
#*- 'w'>>write--open file for writting & databaseeat file if not exists
#*- 'x'databaseeat--databaseeat file & give error if file is not exist 
#*- '+'	Activates read and write methods. '''من الرابط تعرفت عليها'''
#*------------------------------------
# لو بدك تسفيد اكتر شوف الصفحة هاي ممتازة 

'''https://phoenixnap.com/kb/file-handling-in-python
'''
#import os  #* operating sys
#file  =open('F:\moh.txt') #  F:\ >>  its locations. 
#* locations>>>C:\Users\jit (cwd)>> main current working directory
#print(os.getcwd())
#print(os.path.abspath(__file__))
#*c:\Users\jit\Desktop\python\TRY YOUR SRLF.py الفايال الي انتا فيه حاليا
#*abspath >> its abslaut path

#بتاخد عنوان الملف الي انتا فيه 
#*directory for the opened file
#print(os.path.dirname(os.path.abspath(__file__))) 
#print('*'*10) 
#print(os.getcwd())
#*change current working directory >>>>>>cwd() 
#os.chdir(os.path.dirname(os.path.abspath(__file__))) #*c:\Users\jit\Desktop\python
#print(os.getcwd())
#----------------------------------------------
#file  =open('F:\moh.txt') #F:\ >>its locations. 
#file  =open(r'F:\New folder\moh.txt') # لو كان الملف في  فوليدر  

#*----------------------------------
#*---file handling - ----66 Read Files
#*----------------------------------


myfile =open('F:\moh.txt','r')
#print(myfile)#file data obj>>المحتوى<_io.TextIOWrapper name='F:\\moh.txt' mode='r' encoding='cp1252'>
#print(myfile.name)
#print(myfile.mode)
#print(myfile.encoding)

#print(myfile.read()) #hello mohammed u are student in AUG and u are stupid men >>>dumn                      
#print(myfile.read(5)) #hello
'''method to print only the first line of the file:'''
#print(myfile.readline())  #hello mohammed 
#print(myfile.readline())  #u are student in AUG and u are stupid men >>>dumn
#print(myfile.readline(2)) # 2 is >>characters # ma

#print(type(myfile.readlines())) #*<class 'list'>
#print((myfile.readlines()))#['hello mohammed \n', 'u are student in AUG and u are stupid men >>>dumn\n', 'mai>>\n', 'moh>>\n', 'rana>>\n']
#print((myfile.readline(20)))   #[]
#print(type(myfile.readlines()))  #*<class 'str'>

for line in myfile:
      print(line)
      #print(len(line))
      if line.endswith('1'):
            break
#close the file
myfile.close()


#*----------------------------------
#*---file handling - ----66 write and appends Files
#*----------------------------------
#* write >>   بكتب في الملف , ولو فش ملف بنشأ ملف وبحزف محتوى الملف لقديم
#- 'w'>>write--open file for writting & databaseeat file if not exists
#يعني لما تيجي تعدل على المحنوى القديم بحزفوا لكنلو عملت كمان محتوى بحطوا عالقديم
myfile =open('F:\moh.txt','w')

'''myfile.write('welcome back mohammed \n ')
myfile.write('hello \n ')
myfile.write('therd line >')'''


# انشاء ملف جديد 
'''myfile =open(r'F:\maram.txt','w')
myfile.write('hello mohammed \n'*3)'''


'''mylist =['mohammed\n' ,'mai\n' ,'rana\n','maram\n']
myfile.writelines(mylist)
'''

#*- 'a'>>append--open file for appending values,databaseeat file if not exists
#*      بحزفش المحتوى القديم 
'''myfile =open('F:\maram.txt','w')
myfile.write('hello mohammed \n'*3)'''

myfile =open('F:\maram.txt','a')
myfile.write('hello ramii\n')
myfile.write('append from python>\n\n\n')  #غير النص بيضل محتفظ بالقديم 
                              #\n\n\n >>يعني بنزل تلات اسطر لو غيرت النص بعد ما نفدت ال\n


#*----------------------------------
#*---file handling import informations - ----67
#*----------------------------------
myfile =open('F:\moh.txt','a')
print(myfile.truncate(5)) #بقتطع جزء من النص داخل الملف 


myfile =open('F:\moh.txt','a')
print(myfile.tell())  #بقلك وين مكان المؤشر 

myfile =open('F:\moh.txt','r')  #   بتعدل مكان الكارسر وبطبع
myfile.seek(9)  #abu raida
print(myfile.read())


import os    # بتحزف ملف 
os.remove('F:\moh.txt')
#-----------------------------تكليفات الزيرو
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


#*----------------------------------
#*---build in functions- ----68
#*----------------------------------


# all ()
# any()
# id()
# bin()
#*-----------------------
import calendar
years =2020
month =5
print(calendar.month(years,month))
'''
     May 2020
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31 '''

#*-------------------------
#* all()
x =[1,2,3,4,5]  #true
if all(x):
     print('all elem is true')
else:
     print('at least one elem is false')     
     
x =[1,2,3,4,5,[]]  #false
if all(x):
     print('all elem is true')
else:
     print('at least one elem is false')     
     
x =[1,2,3,4,5,[]]   #true
if any(x):
     print('one elem is true')
else:
     print('no any true elme')     
     
x =[0,0,[]]  #fulse
if any(x):
     print('one elem is true')
else:
     print('no any true elme')
 
 #* bin 
print(bin(100))  #0b1100100 برجعلك باينيري     

#* id () 
a =1
b =2
print(id(1))   #2488966578416
                #2488966578448
print(id(2))

#*----------------------------------
#*---build in functions- ----69
#*----------------------------------
# sum()
# round()
# rang()
# print()
#*-----------------------

#*sum (iterable ,strars)

a = [2,3,6,9]
print(sum(a))     #>> iterable :[اجباري ]
print(sum(a, 30)) #>> 30 = strats :[اخياري ]

#*round (number ,number of digits) >>بتقرب من 

print(round(100.555))
print(round(100.449)) 
print(round(100.494,2)) #100.49 رقمين بعد الفاصلة العشرية
print(round(100.344,1)) #100.3>>1 =num of digits عدد الارقام بعد الفاصل

#*range (startsوendوstep)
 #starts>> مش اجباري 
 #stop>> اجباري عشان ما بروح للمالانهاية
 #step>> يفط قديه




print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]>>end
print(list(range(0,10,2)))#[0, 2, 4, 6, 8]>>st ,end ,step\
print(list(range(0,10,2)))   


#*print()
print('hello mohammed ,how are u ,how old are u ')
print('hello mohammd','how are u ','how old are u',sep=' $ ') #sep=sepearatros:

#*end()
print('hello mohammed',end='') #hello mohammedhow are u
print('how are u',end='\n')

print('hello mohammed',end='\n') #hello mohammed
                                 #how are u
print('how are u',end='\n')

print('hello mohammed',end=' what are u doings ') 
print('how are u',end='\n') #hello mohammed what are u doings how are u

#* abs ()

print(abs(-199))
print(abs(-199.123))

#*pow()#*(base: int, exp: int, mod: Literal[0]) -> NoReturn

print(pow(2, 5)) #2*2*2*2*
print(pow(2, 5,5)) #(2*2*2*2)%2
#min(items ,items,items)

print(min(12,33,55))
print(min('a','b','c')) # a
print(min('x','z','omer'))#omer
#max()
print(max(12,33,55)) #55
print(max('a','b','c')) # c
print(max('x','z','omer'))#z

#silice(stars ,end ,step)
a =['a','b','c','d','g']
print(a[:4])#['a', 'b', 'c', 'd']
#or <<نفس بعض>>
print(a[slice(4)])#['a', 'b', 'c', 'd']
print(a[slice(2 ,4 ,2)]) #['c', 'd']

#*----------------------------------
#*---Built in func - ----72  map(func, *iterables) --> map object)
#*----------------------------------
# map tacke afunc + iterator.
# map called map because it map the func on every elem.
# the func can be (pre-defined or lambda) func. >>#Syntax
                                                         #*lambda arguments : expression
#*بستخدمها لما مثلا بدي انفد فانكشن وارجعلها من مكان معين

##* use map wiht predefined functions
#*-----------------------------
#*-----predefind  func --------لامابدا فانكشن بدل الفاكشن الحقيقة 
#*-------------------------------

def formattexet(text):
    return f'-{text}-'

mytext =['mohammed','rana','mai']
myformatedata =map(formattexet,mytext)  #*func, *iterables =variables
#  خزن الاسماء في فاريبال واقدر استدعيها من مكان تاني
print(myformatedata)# <map object at 0x0000014FD925ADD0>
# loop :
for name in myformatedata:
    print(name)

#*لو بديش اخزنها في فاريبال----------

def formattexet(text):
    return f'-{text.strip().capitalize()}-'

mytext =['mohammed','rana','mai']
print(myformatedata)# <map object at 0x0000014FD925ADD0>
# loop :
for name in map(formattexet,mytext):#/ ما بخزن في ليست /نوع البيانات ماب
    print(name)
    #*--------------------/----------------

'''    with counter
'''    
def formattexet(text):
    return f'-{text}-'
mytext =['mohammed','rana','mai']
myformatedata =map(formattexet,mytext)
count =enumerate(mytext,1)
for counts,name in count: 
    print(f'{counts}-{name}')
    
    
    
#* ممكن نعمل لوب على الاسماء كليست-------------

def formattexet(text):
    return f'-{text}-'
mytext =['mohammed','rana','mai']
print(myformatedata)# <map object at 0x0000014FD925ADD0>
# loop :
for name in list(map(formattexet,mytext)): #نوع البيانات ليست مش ماب 
    print(name)
print('-'*20)
#*-----------------------------
#*-----lambda func --------لامابدا فانكشن بدل الفاكشن الحقيقة 
#*-------------------------------
# يعني ممكن احتاج فانكشن بس لاستخدام واحد ومش محتاجها لكل السيستم فهان عملنا هيك
# formattexet بدل هنحط ///lambda 
mytext =['mohammed','rana','mai']
                        #*text
for name in (map(lambda text :f'-{text.strip().capitalize()}-',mytext)): #نوع البيانات ليست مش ماب 
    print(name) 
print('-'*20)
#*or 
mytext =['mohammed','rana','mai']

for name in tuple(map(lambda text :f'-{text.strip().capitalize()}-',mytext)): #نوع البيانات ليست مش ماب 
    print(name)

print('*'*20)
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
for name in (map(lambda text :f'{text}',friends_map)): #نوع البيانات ليست مش ماب 
    print(name[1:len(name)-1])


#*-----------------------------------
#*---Built in func - ----72  filter (func, *iterables) --> map object)
#*----------------------------------
'''فلترة البايانات'''
'''
1- filters tack afun +iterators>>                      نفس الماب
2- filter run afun on every Element>>                  نفس الماب 
3- the fun can be pre defined fun or lambda function>>  نفس الماب 
3- filter out all Element for which the fun return True @
5- the function need to return boolen Value @
'''

def checknum( num):
    if  num >10 :     #*>>>>>>>>>> note<<<<<<<<<
        return num
mynum =[1,13,9,44,5,67]

result= filter(checknum ,mynum)# خزنها في ليست
for numb in result:
    print(numb) 
    
    #*or 
print('*'*30)
def checknum( num):
        return num >10   #تكتب الترجيع في الشرط #*>>>>>>>>>> note<<<<<<<<<
mynum =[1,13,9,44,5,67]

result= filter(checknum ,mynum)# خزنها في ليست
for numb in result:
    print(numb)     
   
# طيب لو عايز اطلع الصفر
print('@'*20)
def checknum( num):
    if  num == 0 :
        return True
mynum =[0,1,13,9,44,5,67,0,0,0]

result= filter(checknum ,mynum)# خزنها في ليست
for numb in result:
    print(numb)    
    
 #*    
print('@'*20)
def checkname( name):
        return name.startswith('m')
myname =['mai' ,'rana', 'mohammed' ,'mary' ,'maram' ,'lana']

result= filter(checkname ,myname)# خزنها في ليست
for namee in result:
    print(namee)    
      
#*-------lambda func

print('@'*20)     
myname =['mai' ,'rana', 'mohammed' ,'mary' ,'maram' ,'lana']

result= filter(lambda name :name.startswith('l') ,myname)# خزنها في ليست
for namee in result:
    print(namee)    
    
    


#*----------------------------------
#*---Built in func - ----74  Reduce (func, *iterables) -->  object)
#*----------------------------------
'''بتطبق الفانكشن على اول عنصرين والناتج تبعهم مع الي بعدوا
'''
#* >> بتجمع او بتظرب مجموعة اراقام مع بعض 

#For example,
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)

#* real functions # 

from functools import reduce

def sumall(num1,num2):
    return num1 +num2
allnum =[1,2,77,9,3]      #itertions
result =reduce(sumall,allnum)# بتاخد اسم الفانكشن والعناصر 
print(result)  #((((1+2)+77)+9)+3) =92
#---------------------------------
nums = [2, 4, 6, 2]   
def multiply(num1,num2):
    return num1 * num2
result =reduce(multiply,nums) 
print(result)   #96<<output
#* <<same the option>> using lambda func 
nums = [2, 4, 6, 2]   
result =reduce(lambda num1 ,num2 :num1*num2,nums) #paramerts :retuern
print(result)

#*-----------lambda func

def sumall(num1,num2):
    return num1 +num2
allnum =[1,2,77,9,3]
result =reduce(lambda num1 ,num2 : num1+num2,allnum)# بتاخد اسم الفانكشن والعناصر 
print(result)


#*----------------------------------
#*---Built in func - ----75  enumerate(Iterable, start: int)
#*----------------------------------
# هان باختصار شغل كاونتر 
# يعني بخليك تعمل كاومنر للوب مثلا من اي نقطة بدك ايايها
'''enumerate() '''    #*Return an enumerate object.
                #*iterable
                #*an object supporting iteration


listname = ['maohammed ','rami ', 'rana' ,'ramdan','mai', 'lana']

namecounter=enumerate(listname,0)

for counter,name in namecounter :
    print(f'{counter}-{name}' )
    
    #-----------------
def formattexet(text):
    return f'-{text}-'

mytext =['mohammed','rana','mai']
myformatedata =map(formattexet,mytext)  #*func, *iterables =variables
#  خزن الاسماء في فاريبال واقدر استدعيها من مكان تاني
'''print(myformatedata)# <map object at 0x0000014FD925ADD0>
'''# loop :
count =enumerate(mytext,1)
for counts,name in count:
    
    print(f'{counts}-{name}')  
    
      
#* help ()    

#*print(help(print())) # functions 

#*reversed(iterable)  # بتعكس الاتيربل
# >>Return a reverse iterator over the values of the given sequence

str ='mohammed '
print(reversed(str))
for charcaters in reversed(str):
    print(charcaters)




def welcome_jawwal(namepage):
    print(f'welcome back in web site page {namepage}')
    
def quation(name):
    print(f'how are u {name}')    



#*----------------------------------
#*---Modules >> built in modules 76
#*----------------------------------
''' modules >>في فانكشن بتعمل الفكرة  حسب الموديولز  الي انتا عايزه
'''
# 1-modules is afile contain aset of func
# 2-u can import module in your app to help u-
# 3-u can import multiple modules 
# 4-u can databaseeat your own modules
# 5-modules saves your time 

'''import main modules '''
          
import random # call  alls moduels
#print(random)                #(variable) random: () -> float
print(f'print random float number {random.random()}')#print random float number 0.33540147491433514     
      
'''show all functions into modules '''      
      
#import random
#print(dir(random)) #dir >> بترجعلك كل اشي ,داتا وعناصر جوات  الموديولز    
 
''' import one or two functions intos modules 
''' # يعني يديش ارجع فانكشن واحد ولا تنين من جوات الموديول مش كلو
import random
from random import randint , randrange#Return random integer in range [a, b], including both end points.

print(f'print random integers number {random.randint(100,200)}')
print(f'print random float number {random.random()}') #random: () -> float


#*----------------------------------
#*---Modules >> databaseeat your modules 77 
#*----------------------------------
      
import sys 
print( sys.path)   # ببحث عن المسارات الي بدك تستدعي منها الموديلوز

''' طيب لو بدك تضيف مسار جديد من المسارات يبحث عنوا   
'''      
import sys 
sys.path.append(r'f:\ranoosh')
print( sys.path) #'f:\\ranoosh'

#-------------
'''عشان يزبط الاستدعاء لازم '#اعمل ملف جديد#' واعمل فيه الاشياء الي بدي استدعيها مثلا
'''
'''
def welcome_jawwal(namepage):
    print(f'welcome back in web site page {namepage}')   
def welcome_paltel(name):
    print(f'how are u {name}') 
'''
    # استدعاء كل الفانكشن 
import aburaida   # aburaida >> >>اسم الملف الي فيه الفانكشن الي بنستدعيها
print(dir(aburaida)) # طلع كل محتوي هادا المديلوز
 # اسم الملف .اسم الفانكشن
aburaida.welcome_jawwal('mohammed')#mohammed welcome back in web site  jawwal page
aburaida.welcome_paltel ('rana') #how are u rana

# طيب لو بنا نعمل اسم مستعار لابوريده
'''alias >> الاسم المستعار'''
import aburaida as aljoker   #>>aljoker اسم مستعار هدا للاسم الاصلي 
print(dir(aljoker))
aljoker.welcome_jawwal('mohammed')
aljoker.welcome_paltel ('rana')

# استدعاء فانكشن وحدة بس من الفانكشن الريسية

from aburaida import welcome_paltel
welcome_paltel('rana*') #how are u rana

'''alias >> الاسم المستعار'''

from aburaida import welcome_jawwal as modern
modern('rana*') #how are u rana



#*----------------------------------
#*---Modules >>install external packages 78
#*----------------------------------

'''packages >> فيها مجموعة موديولز  والفايلات الخاصة بالباكج هدا 
'''
# 1- Modules & packages >مجموعة موديولز جوا فايال
# 2- external install  package with python package managers pip
# 3-pip install the pakage and its dependencies
# 4- moudles list 'https://docs.python.org/3/py-modindex.html' >>#*internal pakages
# 5- pakage and moudules directory 'https://pypi.org/'
# >>5>>>Find, install and publish Python packages with the Python Package Index
# 6- pip manual 'https://pip.pypa.io/en/stable/installation/'
# 
#* تعرف نوع الباكج عالجاهز ..pip --version
# pip --version..pip 21.1.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2800.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.8)
#* تحديت ال
'''pip install --upgrade pip
'''

'''Installing collected packages: termcolor
'''
 #*use >>>pip install termcolor & pyfiglet

'''import termcolor   # لو ايروور >>reload windos>>ctral 
import pyfiglet

#print(dir(termcolor)) 

print(pyfiglet.figlet_format("mohammed"))
print(termcolor.colored('mohammad',color='green'))
# مع بعض 
print(termcolor.colored(pyfiglet.figlet_format("mohammed"),color='green'))

'''

#*----------------------------------
#*---date and time intro--- 79
#*---------------------------------
#* https://docs.python.org/3/library/datetime.html

''''
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 'date', #*'datetime',
'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''
#print(dir(datetime.datetime))
# # محتوى الديت تايم
import datetime 
print(dir(datetime.datetime.now().day))
import datetime

print(datetime.datetime.now()) #2022-07-25 23:41:01.802170

#*print cirrent years 
print(datetime.datetime.now().year)# 2022
#*print cirrent month
print(datetime.datetime.now().month)# 7
#*print cirrent day
print(datetime.datetime.now().day)# 25
#*print start and end of date 
print(datetime.datetime.min)# 0001-01-01 00:00:00
print(datetime.datetime.max)# 9999-12-31 23:59:59.999999
#*print specfic date
print(datetime.datetime(2000,5,19))#2000-05-19 00:00:00
print(datetime.datetime(2000,5,19,10,30,2))#2000-05-19 10:30:02
#-------- تاريخ اليوم وميلادي
mybirthday =datetime.datetime(2000,5,19,11,30,2)
date_day =datetime.datetime.now()
print(f'mybirthday is {mybirthday}') #mybirthday is 2000-05-19 11:30:02
print(f'date now is {date_day}')     #date now is 2022-07-26 08:28:23.160292
print(f'days between mybirthday and date_day is {(date_day-mybirthday).days} days')#time between mybirthday and date_day is 8102 days, 21:01:07.699722
# الطباعة على سطر واحد ..>>

mybirthday =datetime.datetime(2001,12,3,11,30,2)
date_day =datetime.datetime.now()
#name =input(f'inter your name \U0001F600 :')
#print(f'{name} yourbirthday is {mybirthday}',end=' @ ') #mybirthday is 2000-05-19 11:30:02
#print(f'date now is {date_day}') 


#*----------------------------------
#*---date and time format time--- 80
#*---------------------------------
#*>>>>>>https://strftime.org/
#https://docs.python.org/3/library/datetime.html
#>https://strftime.org/

mybirthday =datetime.datetime(2000,5,19,11,30,2) 
print(mybirthday)
print(mybirthday.strftime('%a'))
print(mybirthday.strftime('%A'))
print(mybirthday.strftime('%B'))
print(mybirthday.strftime('%b'))
print(mybirthday.strftime('%y %b %a'))#00 May Fri

print('*'*20)
dd =datetime.datetime.now().date()
print(f'Today Is "{datetime.datetime.now().date()}"') #Today Is "2022-07-28"
print(f'Today Is "{datetime.datetime(2021,7,28).date()}"')#Today Is "2021-07-28"
print(f'Today Is* ',dd.strftime('%b %w, %Y')) #Today Is "2021-07-28"
print(f'Today Is/ ',dd.strftime('%w - %b - %Y')) #Today Is/  4 - Jul - 2022
print(f'Today Is+ ',dd.strftime('%w / %B / %y')) #Today Is+  4 / July / 22
print(f'Today Is- ',dd.strftime('%w / %B / %Y')) #Today Is-  4 / July / 2022
print(f'Today Is- ',dd.strftime('%a,  %w %B %Y')) #Today Is-  Thu,  4 July 2022

#*----------------------------------
#*---Iterable and Iterator--- 81
#*---------------------------------
'''https://book.pythontips.com/en/latest/generators.html
'''
#*----Iterable
# 1- يحتوي الكائن على بيانات يمكن التكرار عليها
# 1- object contains data that can be iterated upon
# 2- ex- str , list ,set ,tuple ,dict =>data type in python
#*----Iterator 
# 1-obiect used to iterat over iterabl using #*next()method return 1 elements  at Atime
# 2-you can generator Iterator from Iterable when using #*iter()methods
# 3-for loop already call iter() method on the iterable behind the scene لوب خلف الكواليس
# 4-gives 'stopiteration' if thers no next elements


string = 'MOHAMMAD' #iterabl =>str 
for letter in string:
    print(letter,end=" ") #M O H A M M A D

num1 =True #iterator =>bool
for number in iter( num1 ):
    print(num1)  #TypeError: 'bool' object is not iterable
        
   
#*----Iterator
   
string = 'MOHAMMAD'    
#print(iter(string)) #M O H A M M A D <str_iterator object at 0x00000225A198AE00>   
itertor =  iter(string)
print(itertor)  



for name in 'ABURAIDA' : #=> str
    print(name ,end=" ") #A B U R A I D A

#*----------------------------------
#*---Generators =>'yield'--- 82
#*---------------------------------      
    #*'yield'=='return'
# زيها زي الفانكشن العادية زلكن باستخدم يلد     
#generator is afunctions with 'yield' keyname instead of 'return'    
#its support iteration and rutern gen iterator by calling 'yield' 
#ممكن  يكون في واحد  او اكتر من يلد   
#generators function can have one or more yield    
#بنستخدم نكست عشان نتسدعي اليلد وبرضوا ما بكملش من البداية
#by using next() it resume from where it called 'yield' not from begining
#لما بنستدعيها بتبداش اتوماتيكلي هيا بتعطيك التحكم 
# when called ,its not start automatically ,its only give you the control. 


def mygen ():
    return 1
print(mygen()) #1
#*-------فانكشن عادية       

def mygen ():
    yield 1
    yield 2
    yield 3
    yield 4      
print(mygen()) #<generator object mygen at 0x000001B0E26D21F0>
gen =mygen() 
''' ,بتقدر تحكم فيها وقت ما بدك وتطبع تطبع الي بدك اياه قبل ولا بعد ...زي هيك
'''
print(next(gen)) # 1>> next(iterator[, default])
print('mohammad abu raida')
print(next(gen)) # 2>>  
print('mohammad abu raida') 
print(next(gen)) # 3>>  
print('mohammad abu raida')    
print(next(gen)) # 4>>   

for number in gen: # بطبع ارقام ونص
    print(number)
    
'''بطبع رقم بس الي في ال yield'''  
for number in mygen():            
    print(number)   
    
'''output اكمل من مطرح ما وقفت
1
mohammad abu raida
2
mohammad abu raida
3
mohammad abu raida
4'''

#* >>بدنا نتعمق حبة جوا هدا الدرس<<
'''
#*Generators are iterators, 
but you can only iterate over them once.
It’s because they do not store all the values in memory,
they generate the values on the fly. 
You use them by iterating over them,
either with a ‘for’ loop or 
by passing them to any function or construct that iterates. 
Most of the time generators are implemented as functions.
However, they do not return a value, they yield it.
Here is a simple example of a generator function:
'''

def reverse_string(my_string):
  # Your Code Here
  for name in reversed(my_string): 
   yield name  

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
  
  
  
def generator_function():
    for i in reversed(range(10)):
        yield i

for item in generator_function():
    print(item)
print(next(item))   


my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter)) # Y
print(next(my_iter)) #a...
    
#*----------------------------------
#*--decoreator--- 83
#*---------------------------------    
    
# some time meta programming
# every thing in python  is object even  functions
# decorator take  afunctions and add somefunctialty and return it
# decerator warp other functions and enherans their behaviors .
# decerator is higher order functions(fun accept fun as aparamerte) 
 
def mydecorators (func) : #decorator 
    
    def nestedfunc():  # any name its just for decoration
        
        print('befor') #message from dedatabaseeoter
        
        func() #execut func
        
        print('after')#message from dedatabaseeoter
        
    return nestedfunc() #return all data   

@mydecorators   # شوكر سنتاكس
def newstr():
    print('hello in new string ')
  
print('*'*20)
@mydecorators
def oldstr():
    print('hello in old string ')

#--------output--------
'''
befor
hello in new string after
********************
befor
hello in old string
after
'''
#-----------------------

#*--------function with parameter --------
# ممكن اعمل شرط يتحقق من كزا شغلة لو كان عندك اكتر ممن رقم اقل  من كزا ويتحقق من كل اشي يدخل على الفانكشن
# يعني الديكوريتر هيا الي بتشيك على اي فانكشن بدون ما اضل اعيد الشرط باي فانكشن بدي اعملوا
# بنقدر بنعمل اكتر من ديكوريتور من نفس فانكشن ر
print('*'*20)
def mydecorators_one (func) : #decorator 
    
    def nestedfunc(num1,num2):  # any name fun 
        #print('befor') #massge from dedatabaseeoter
        if num1 ==0 or num2 ==0 :
            print('warnning:the number is less than zero')
        print('mydecorators one***')    
        func(num1,num2) #execut func
        
        #print('after')#massge from dedatabaseeoter   
    return nestedfunc #return all data

def mydecorators_two(func) : #decorator 
    
    def nestedfunc(num1,num2):  # any name fun 
        #print('befor') #massge from dedatabaseeoter
        #if num1 ==0 or num2 ==0 :
            #print('warnning:the number is less than zero')
        print('mydecorators two***')     
        func(num1,num2) #execut func
        
        #print('after')#massge from dedatabaseeoter   
    return nestedfunc #return all data

@mydecorators_one
def sumall (num1,num2):
    print (num1+num2 )  #30  
sumall(0,20)

@mydecorators_two  #الترتيب مهم //مين يبدا الاول من الديكوريتور
 
def sumall (num2,num3): #'warnning:the number is less than zero
    print (num2+num3 )  #30  
sumall(0,20)


#--------- 

print('*'*20)
def mydecorators (func) : #decorator 
    
    def nestedfunc(*number):  # any name fun 
        #print('befor') #massge from dedatabaseeoter
        for num in number: #عشان يشيك على اي رقم بتحطوا جديد
         if num == 0:
            print('warnning:the number is less than zero')
            
        func(*number) #execut func
        
        #print('after')#massge from dedatabaseeoter   
    return nestedfunc #return all data

@mydecorators
def summation (num1,num2,num3,num4): #'warnning:the number is less than zero
    print (num1+num2+num3+num4)
summation(0,20,30,3)  #output
'''warnning:the number is less than zero
50
'''  
#-----------speed test-------
# بدنا نعمل فانكشن تحسب بداية ونهاية الفانكشن والفرق بيهم 
from time import time
print('*'*20)
def speedtest (func) : #decorator 
    def warrbing():  # any name fun 
        
        start =time()  # وقت تشغيل الفانكشن
        func() #تنفيدد الفانكشن
        end =time()    # وقت نهاية الفانكشن
        print(f'function running time is {end -start:0.4}')
    return warrbing #return all data

@speedtest
def bigloop (): #'warnning:the number is less than zero
    for num in range(1,20000):
        print(num)
bigloop ()

'''https://www.freecodecamp.org/news/python-decorators-explained-with-examples/'''
from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   
daily_backup()



   
'''Note: @wraps takes a function to be decorated and 
adds the functionality of copying over the function name,
docstring, arguments list,
etc. This allows us to access 
the pre-decorated function’s properties
in the decorator.
#*https://book.pythontips.com/en/latest/decorators.html
'''

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

'''How to Add Arguments to Decorators in Python'''

def decorator_name(f):
   
    def decorated(*args, **kwargs):
        if   can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = False
print(func())


print('#'*20)

from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x,y):
   """Do some math."""
   return x + y
result = addition_func(4,3)
# Output: addition_func was called
 

from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    pass
print(my_func.__name__)
print(my_func.__doc__)


    

from functools import wraps

def logit(logfile): # main decorator
    def logging_decorator(func): #func decorators.
        @wraps(func)
        def wrapped_function(*args, **kwargs): # nested decorators
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit('out.log')
def myfunc1():
    pass
myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string
@logit(logfile='func2.log')
def myfunc2():
    pass
myfunc2()


#*-------------------------------
#*https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
#*-------------------------------
# مثال جدا ممتاز وفي كتير افكار لو بدك تتعمق فالديكوربتور


from functools import wraps
import tracemalloc
from time import perf_counter 


def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


print(make_list1())
print(make_list2())
print(make_list3())
print(make_list4())
#-------------------output
'''
Function: make_list1
Method: Range
Memory usage:            0.000056 MB    
Peak memory usage:       3.592968 MB    
Time elapsed is seconds: 0.119595       
----------------------------------------None
Function: make_list2
Method: List comprehension
Memory usage:            0.000416 MB    
Peak memory usage:       3.594324 MB    
Time elapsed is seconds: 0.120739       
----------------------------------------None
Function: make_list3
Method: Append
Memory usage:            0.000424 MB    
Peak memory usage:       3.594188 MB    
Time elapsed is seconds: 0.144785       
----------------------------------------None
Function: make_list4
Method: Concatenation
Memory usage:            0.000416 MB    
Peak memory usage:       4.393252 MB    
Time elapsed is seconds: 54.760649      
---------------------------------------'''

#*----------------------------------
#*--practical >> loop on many iterators with zip()--- 86
#*--------------------------------- 

# تسمح لك بدمج اكتر من ليست او تابل مع بعض  وبتعطيك اياهم في ناتج واحد
'''zip() return azip object contains all object
   zip() length is the length of lowest object'''
# يعني الاقل طول هان بتحكم في فياقي الاوبجكتت

list1 =[1,2,3,5,6,7]
list2 =['a','b','c'] # هاي بتتحكم في الليست الاولى
alllist =zip(list1,list2)
for item in alllist:
    print(item)
#*or
for item1,item2 in zip(list1,list2):
    print('list one item=>',item1)
    print('list one item=>',item2)
    
print('*'*30)
#-output    
    
'''
(1, 'a')
(2, 'b')
(3, 'c')
'''
#  الي هيتحكم فيهم كلخم هوا الي بكون اقل طول وبخليهم نفس طولوا
list1 =[1,2,3,5,6,7]
list2 =['A','B','C','f'] # 
tuple1 =('mohammed','rana','mouhmoud','mai')
dic1 ={'lang1':'python','lang2':'html','lang3':'css','lang4':'node.js'}
for item1,item2,item3,item4 in zip(list1,list2,tuple1,dic1): 
    print('list one item1=>', item1)
    print('list one item2=>', item2)
    print('tuple1 one item3=>',tuple1)
    print('dict one keys=>',item4, 'values=>', dic1[item4])#>>keys  # dic  =keys :values
    

print('*'*30)

listname  =('meme','rana','jana','moh')
listnum =[1,2,3,4,5,6]
dictio =dic1 ={'lang1':'python','lang2':'html','lang3':'css','lang4':'node.js'}

for list1,list2,list3 in zip(listname,listnum,dictio):
    print('list one item1=>', list1)
    print('list one item2=>', list2)
    print('dict one keys=>',list3, 'values=>', dictio[list3])#>>keys  # dic  =keys :values

#* مثال لو عندك مثلا مجموعة اسماء كاملة في الداتا بيس وبدي اجمعهم مع بعض 

first_name =['mohammed','rami', 'mohmoud','sami']
lastname =['aburaida','aburami','abu mai','abumeme']
age = [23, 65, 11, 36, 83]
for first_name,lastname,age in zip(first_name,lastname,age):
    print(f'{first_name} {lastname} is {age} Years Old')
   




# *----------------------------------
# *--practical >>  image manipulation with ''pillow''--- 87
# *---------------------------------
# دكيومنت فيه كل اشي تعلق الصور وتعديلها...
# Common modes are “L” (luminance) for greyscale images الصور ابيض اسود
# , “RGB” for true color images,  الصور الملونة 
# and “CMYK” for pre-press images. للصور التي يتم ضغطها مسبقًا.

# Pillow (PIL Fork) 9.2.0 documentation
#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
#           التعديل على الصور ...

#*Cutting, pasting, and merging images

from PIL import Image
# Open The Image
myImage = Image.open(r"C:\Users\jit\Desktop\Python1")

# Show The Image
myImage.show()

# بدنا نعمل قص لصورة تو جزء منها 
box_databaseop =(0,0,400,400)
mynewImage =myImage.databaseop(box_databaseop)
mynewImage.show()



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




# *----------------------------------
# *--DOC STRING &commenting vs documenting--- 88
# *---------------------------------
  
    #*الفرق بين 
'''DOC STRING and any string ''' #>>>documenting
#* its comments   #>>>commenting   
    
#print(__doc__) #or 

#help(__doc__)  #DOC STRING  طبعلك هدا ملاحظ 

print(dir(__doc__))


def say_hello_to(name):
    '''parameter(someone) => Person Name
    Function To Say Hello To Anyone'''

    return f'hello {name}'
print(say_hello_to("Osama")) # "Hello Osama"

# Write Doc String Line For The Function Here

print(say_hello_to.__doc__)
# Function Doc String Output

    
# *----------------------------------
# *--installing and use pylint foe better code --- 89
# *---------------------------------
# مهم جدا جدا عزيزي بساعدك لما ترفع الكود على الgithup

#تنصيب ال PyLint لفحص ال Code وكتابة Code سليم
## بعملك تقيم من خلال 
# #*pylint.exe C:\Users\jit\Desktop\python\TRY YOUR SRLF.py
# وبقلك هل الكود سليم 100% من ناحية الترتيب والتنسيق.


# هيزبط لما تسخدم 3.8.10 64bit  win stor 
 
# #*----------مش زايط يمعلم

'''
this is my module to databaseeat fullname functions
'''
def fullname (name):
    '''this fun only printting fullname to some one'''
    print(f'hello {name}')    
fullname('mohammed abu raida')


# *----------------------------------
# *--errors and exceptions rasining--- 90
# *---------------------------------

# exceptions is aruntime errors reporting mechanism
# exceptions gives u the msg to understand the problem
# traceback gives u the line to look for the code in this line #تتبع اثر الكود عشان يقلك وين الخطا باي سطر 
# exceptions have types {syntaxerror,indexerror,keyerror,etc...} انواعها
# exceptions list #*https://docs.python.org/3/library/exceptions.html
# raise kayword used to raise your own exceptions

X =-10
if X < 0 :
    print(f'the number {X} is lise than zero')
    raise Exception(f'the number {X} is lise than zero')#اعتراض*#* #ما بطبع اي اشي يعدها لان ايروور 
    #print('grtysr')
else:
    print(f' is good nummber and okay ')

print('this msg after condtions') # هدا بنطبع سؤال في خطا ام لا



y ='mohammad'

if type(y) != int :
     #print('only needd number')
     raise ValueError('only number allowed')#* ما بكبع اي اشي بعدها#ValueError: only number allowed

print('contiuos code')     

y =10

if type(y) != int :
     #print('only needd number')
     raise ValueError('only number allowed')
print('contiuos code')     # بطبع هاي contiuos code



#*----------------------------------
#*--    exceptions handling ---
#*--  Try |except |else| finally ---
# *----------------------------------
# *--except >>handel the errors
# *--try  >>test the code for errors
# *---------------------------------
# *--else =>>if no errors
# *--finally =>>run the code --- 91
# *---------------------------------


import numbers


try : # try the code 
    
    number =int(input('write your age>>'))
except: # في حال مسك ايرروhandel the errors
    
    print(f'this\'s  not integers,its{type(number)}')
    

else: # if no errors < ادا ما في ايررو 
    print(f'good ,your age is {number}')
 
finally: # بتنفد باي حال من الاحوال 
    
    print('the code that allowed to inter your age ')         

# بقدر اطلع نوع الايروو لشخص برضوا 
try  : #بجربلك الكود 
   print(10/0)
   print(x)
   print(int('hello'))
   
except ZeroDivisionError: # ادا نوع الايرور اطبع هاي 
    print('can\'t divide')
     
except NameError:
       print('identifier not fount') 
       
except ValueError :
       print('ValueError') 
       
except  : # لو ما في نوع محدد  من الايروو
       print('the error notfound')               
           


#*----------------------------------
#*--    exceptions handling ---
#*--  Try |except |else| finally ---
#* ---   advanced examplrs ---
# *----------------------------------

the_file =None
tries =5

while tries > 0 :
    
    try :
        print('-'*50)
        print(f'{"-"*3}enter the file name with abs path to open',"-"*3)
        print(r'eg: C:\Users\jit\Desktop\Python1\txt1.txt',"-"*3)
        print(f'{"-"*3}your tries is\'{tries}\' left',"-"*3)
        print('-'*50)
        filename_path =input('file name =>>: ').strip()
        openfile =open(fr'{filename_path}','r')
        print(openfile.read())
        break
    
    except FileNotFoundError: #  لو في ايروو ومعروف
     print(f'{"-"*3}the file not found,pleas be sure the name is valid')
     tries-=1
     
    except : #اي نوع ايررور
        print(f'{"-"*3}error happend') 
        
    finally: # تتنفد في كل الحالات 
        # طيب ما دام بتتنفد في كل الحالات فبالتالي ممكن يغلق الملف اول ما تعمل رن 
        # طيب الحل ??
        # الحل\\ اتحقق من حالة الملف 
        if the_file == None:
           openfile.close()
           print('file closed')  
else: #>> loop  end لما تنتهي الوايل لوب
    
    print(f' {"-"*3}all tries is done')    

# *----------------------------------
#* ---Debugging code ----0943
# *----------------------------------

# يستخدم في المشاريع الضخمة عشان يكتشف الخطا وهوا بمشي سطر بسطر 

# *----------------------------------
#* ---Type Hinting ----094 يعني تلميح 
# *----------------------------------

# يعني مثلا كنت يتتشغل في تيم واسلمت مشروع الهم فلازم تحط تلميح حسب الاوبجمت الي قدامك

def fullname (*name) ->str:  #*  هان Type Hinting
    return f'the full name is :{(name)}'
fullname(print('mohammad','hazem','abu raida'))  

def fullname (num1,num2) ->int:  #*  هان Type Hinting
    print (num1 + num2)
fullname(10,10,'+')    



#* ----------------------------------
#* -- Regular Expressions => Intro 95--
#* ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [databaseedit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
'''يسخدم مثلا في انوا اشيك على موقع او اي بي او ايميل هل مكتوب بشكل صحيح هل ناسي الهاتش او الدوت ... زي هيك
 خصوصا في الداتا بيس تاع الموقع الشخص ...
'''
#* ----------------------------------------
#* -- Regular Expressions => Quantifiers 96--
#* ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# ------------- https://regex101.com/r/m6hdatabaseA/1 مهم جدا جدا ...


#* -----------------------------------------------------------------------
#* -- Regular Expressions => Characters Classes Training's -- 97
#* -----------------------------------------------------------------------
# [0-9]
# [^0-9] كل اشي ماعدا المن صفر لتسعة
# [A-Z] كل الحروف كابتل
# [^A-Z] ماعدا الكابتل
# [a-z] كل الحروف سمول
# [^a-z] ماعدا لسمول
# -------------


#* ---------------------------------------------------------
#* -- Regular Expressions => Re Module Search And FindAll --
#* ---------------------------------------------------------
#* search()  => Search A String For A Match And Return A First Match Only
#* findall() => Returns A List Of All Matches and Empty List if No Match
#* ---------------------------------------------------------------------
#* Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info) () is groub
#* ----------------------------------------------------------

import re 

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search) # <re.Match object; span=(0, 2), match='OO'>
print(my_search.span())  #(0, 2) 
print(my_search.string)  #OOsamaEElzero
print(my_search.group()) #OO


is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

  print("This is A Valid Email")

  print(is_email.span())
  print(is_email.string)
  print(is_email.group())

else:

  print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []: #ادا البحث ليس فارغ او اليست

  empty_list.append(search)

  print("Email Added")

else:

  print("Invalid Email")

for email in empty_list:

  print(email)
 
 
#*----------------------------------------------------
#* -- Regular Expressions => Re Module Split And Sub --101
#* ----------------------------------------------------
#* split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
#* sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
#* ---------------------------------------------------------------------

import re

string_one = "I Love Python Programming Language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)

print("#" * 50)

string_two = "How-To_Write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)

print("#" * 50)

# Get Words From URL

for counter, word in enumerate(search_two, 1):

  if len(word) == 1:

    continue

  print(f"Word Number: {counter} => {word.lower()}")

#*-------------sub(pattern,repl,count)

print("#" * 50)
my_string = "I Love Python"
print(re.sub(r"\s", "-", my_string, 1)) 
 


#* ------------------------------------------------------
#* -- Regular Expressions => Group Trainings And Flags --
#* ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group())
print(search.groups())

for group in search.groups():

  print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}") 
 
 

# * ------------------------------------------
# * -- Object Oriented Programming => Intro --1
# * ------------------------------------------


# https://www.geeksforgeeks.org/inheritance-in-python/
# https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/
#*  &&& learn   solid principle 



# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
# *     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
# *     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# * [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# * [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#     - Methods[Behaviors] => Walking, Stopping
# * [9] Class Is The Template For databaseeating Objects [Object Constructor | Blueprint]
#     - Class Car Can databaseeate Many Cars Object
# ---------------------------------------------

# * ----------------------------------------------------------
# * -- Object Oriented Programming => Class Syntax and Info --2
# * ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate #*Means databaseeate Instance of A Class 
# [03] #Instance => Object databaseeated From Class And Have Their Methods and Attributes #
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
#*[06] Class May Contains Methods and Attributes
# [07] When databaseeating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You databaseeate Object From Class
# [09] __init__ Method Is= Initialize The Data For The Object بتهيأ الداتا بتبعتك  
# [10] Any Method With Two Underscore in The Start and End #*Called Dunder or Magic Method
#* [11] self Refer To The Current Instance databaseeated From The Class And Must Be First Param
# [12] self Can Be Named Anything  #* اي اسم مش مشكلة
# [13] In Python You Dont Need To Call new() Keyword To databaseeate Object
# -------------------------------------------------------------------

# * Syntax
# class Name:
#     Constructor => Do Instantiation [ databaseeate Instance From A Class ]
#     Each Instance Is Separate Object # instance 3
#     def __init__(self, other_data)
#         Body Of Function

# doucumentions >>https://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html


class Member:
        
        # Constructor 
    def __init__(self):  
        
        # Body Of Function .....# Each Instance Is Separate Object
        print("A New Member Has Been Added")

member_one = Member() 
member_two = Member()
member_three = Member()

# <class '__main__.Member'> # لو بدي اعرف الباينات في اي كلاس  زي هيك
print(member_one.__class__)

print(dir(Member))
my_dictionary = {
    'name': "Osama",
    'age': 36,
    'monthly_salary': 5000,
    'yearly_salary': ''  # Something
}


class phane:

    def __init__(self) -> None:

        print('welcome back  here ')
first = phane()


# * ------------------------------------------
# * -- Object Oriented Programming => Intro --3
# * ------------------------------------------

# Self: Point To Instance databaseeated From Class/تشير الى متيل تم إنشاءه من الكلاس الاصلي 
# Instance Attributes تمتيل الصفات : Instance Attributes Defined into The Constructor
# -----------------------------------------------------------------------
# Instance Methods تمتيل الدوال : Take Self Parameter Which Point To Instance databaseeated From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

#* -----------------------------------------------------
#* -- Object Oriented Programming => Class Attributes --6
#* -----------------------------------------------------

#*>> Class Attributes: Attributes Defined Outside The Constructor
#*>> Instance Attributes Defined into The Constructor
#* -----------------------------------------------------------


#* قائمة اسماء ممنوع تكون من ظمن اسم اليوزر 
#*  عدد الاسماءاليوزر المظافة  قبل الحدف 
#*  عدد الاسماءاليوزر المظافة بعد  الحدف 
#* class method > الها علاقة بالديكوريتور ومربوطة مع لكلاس نفسوا مش بالانستنس

class Member:  
     
   #*---Attributes class & constracators
   
    not_allow_name =['rannosh','meme' ,'moha'] # قائمة الاسماء الممنوعة 
    users_count =0                             # counter 
   
    #* using class method into constracators
    # decoratorsطباعة عدد اليوزرز باستخدام الكلاس  والديكوتريتور 
   
    @classmethod             # decorators class method 
    def show_users_count(Cls):  # class method >> Cls
       
       print (f'we have {Cls.users_count} Users in our system')
    
    @staticmethod   # بس الوضيفة انها تطبع وخلص   بدون ما اصل للكلاس ولا للاوبجكت 
    def sey_hello (): # ونحط جوات لكلاس لان الها علاقة جوات الكلاس 
      
      return f'welcom back'  

    def __init__(self, first_name, middel_name, last_name, gender) -> None: # constractors 4 parameters
         
   #*--- instance Attributes (data)
   
        # f.name ,mname ,lname ,gender >> Attributes  # الصفات 
        self.fname = first_name    # instance Attributes 1
        self.mname = middel_name   # instance Attributes 2
        self.lname = last_name
        self.gender = gender
          
        Member.users_count += 1  # users_count = users_count + 1
        
   #--- instance method (functions)  # نفسها نفس الاشي الي فوق بترجع الاسم كامل     
    
    def fullname(self):
        
        #بدنا نشيك على اول اسم هل من ظمن القائمة ام لا 
      if self.fname in Member.not_allow_name :
        
         raise ValueError("Name Not Allowed")
      
      else:
         
                # self =تعود=>  name Instance = self  .Attributes
         return f'{self.fname} {self.mname} {self.lname}' #rana naji abu raida

#check name and put Mr , Ms or non 

    def name_with_title (self):  # mr ,ms or non 

        if self.gender == 'male':

            return f'hello Mr {self.fname} ' #Instance name.Attributes

        elif self.gender == 'fmale':

            return f'hello Ms {self.fname} '
        else:
            
            return f'hello  {self.fname} '
    
    def get_all_info (self):
      
      return f'{self.name_with_title()},your full name is {self.fullname()}' 
    
    def deleted_users (self) :
      
        Member.users_count -= 1
        
        return (f' User \'{self.fname}\' Is Deleted')
       
'''معرفة عدد اليوزر قبل الاضافة '''     
print(f'Number of users is \'{Member.users_count}\' ')
 
nameone   = Member('rana', 'na', 'abu raida', 'fmale')  #inastanc --  arge*
nametwo   = Member('mai', 'awa', 'abu raida', 'fmale')    
namethree = Member('mohammed', 'ha', 'abu raida', 'male')
namefour  = Member('meme', 'ka', 'abu raida', 'male')

''' 
using inastans method outside constracators(outside class)
'''

'''
معرفة عدد اليوزر بعد الاضافة 
'''  
print(f'Number of users become \'{Member.users_count}\' ')
#User meme Is Deleted
print(namefour.deleted_users()) 
#Number of users after deleted '3'
print(f'Number of users after deleted \'{Member.users_count}\' ')

print(nameone.fname, nameone.mname, nameone.lname,) # fullname طريقة هبلة 
print(nametwo .fname)  # Instance.Attributes variable fname: str
print(namethree.fname)
print('*'*20)
print(nametwo.fullname())  # fullname>>mohammed hazem abu raida بترجع الاسم الي فوق
print(nametwo.name_with_title())  # hello Mr mohammed


# Instance Methods Can Freely Access #Attributes And Methods On The Same Object
print(nameone.get_all_info().upper()) # hello Ms rana ,your full name is rana naji abu raida

print(nameone.fullname()) # هاي 
print(Member.fullname(nameone))  # نفس هاي 

Member.show_users_count() #decoratorsطباعة عدد اليوزرز باستخدام الكلاس  والديكوتريتور 

Member.sey_hello()



#*-------------------------------------------------------------------
#* -- Object Oriented Programming => Class Methods & Static Methods --
#* -------------------------------------------------------------------
#*--- Class Methods: ايجباري ال param= cls
# - Marked With *@classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require databaseeation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
#*--- Static Methods: ما بتاخد  param
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
#*--- inastanc method : بتاخد  param = self
# -----------------------------------------------------------
print('*'*20)



class main_dashboard :

  number_counters =0 
  @classmethod 
  
  def show_name_counters(Cls):
    
    return f'we have {Cls.number_counters} User// in the system'
  
  
  def __init__(self , fullname ) -> None:
      
     main_dashboard.number_counters+=1

     self.fname =fullname 
     
     
  def fullname (self):
    
    return f' Your name is  {main_dashboard.fullname()}'


print(f'Number of users is \'{main_dashboard.number_counters}\' *') # inastans point 

name = main_dashboard('mohammed hazem abu raida***') 

print(f'Number of users is \'{main_dashboard.number_counters}\' *')  

print(name.fname)  
    
print(main_dashboard.show_name_counters())   

 
#* --------------------------------------------------
#* -- Object Oriented Programming => Magic Methods --7
#* --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class skills :
  
  def __init__(self) -> None:
    
    self.skill =['python' ,'css' ,'js']
  
  def __str__(self) -> str:  # str  = human readable msg

    return f'your skills is  {self.skill}'
  def __len__(self) :
   
   return len (self.skill)
        
profile = skills()  #inastances class

print(len(profile)) #3
profile.skill.append('php')
profile.skill.append('jQuary')   
print(profile) # بتعطيك موقع الكلاس في المومري 
print(len(profile))#* 5

#TypeError: object of type 'skills' has no len()
#magic method ليه ما زبط : لان لازم استخدم معها الماجي ميتوت 

#*--------توضيح---------

#print(profile.__class__) #بتعطيك الكلاس الرئيسي الي اجت منوا ال inastances   
#mystr ='mohammed'  
#print(type(mystr))#<class 'str'>
#print(mystr.__class__) #<class 'str'>
#*--------------------------------------
#print(dir(float )) # int , str , ... # محتوى الفلوت 
#print(float.__class__) 
#*--------------------------------------

#print(dir(type))
#print(dir(mystr))
#print(str.upper(mystr))  # نفسها نفس ال  print(Memeber_one.full_name())

#*-----مشروع كامل عن الكلاس 


class users:
                                   # *... طريقة 1 بتتعامل مع كوسنتركاتور constracators
    counter_users = 0              # *>>   #* عشان نجيب عدد المستخدمين داخل السيستم
    
    @classmethod                   # *>>
    def show_name_counters(Cls):  # *>>''' ادا وصل عدد المستخدمين جوات السيستم5 اطبعلو انوا اليسستم فل'''

        while Cls.counter_users == 5:
               
          return f'sys is full and number of users in side sys is :{Cls.counter_users}'
           
        return f'we have {Cls.counter_users} User in the system'  # *>>
 
      
    def __init__(self, firstname, ids, gender) -> None:
        '''instant attriabuts'''
        users.counter_users += 1
        self.fname = firstname
        self.id_num = ids
        self.gender = gender
        #self.birthday =birthday
        
    ''' gender male = Mr ,gnder fmale = Ms >>>'''

    def titelgender(self):

        if self.gender == 'male':

            return f'Mr {self.fname}'

        elif self.gender == 'fmale':

            return f'Ms {self.fname}'
        else:
            return f'{self.fname}'
          
    '''*show Users name & id '''
    
    def firstname(self):  

        return f'welcome back {self.titelgender()} in your eleven up ,ID number is {self.id_num} '
    
    ''' add users  '''
    def added_users(self):
      
      users.counter_users+=1
      print(f'User {self.fname} Is Added')
    
    ''' deleted users  '''  
    def deleted_users(self):
      users.counter_users-=1
      print(f'User {self.fname} Is deleted') 
   
print(f'Number of users is \'{users.counter_users}\'')  #  = Number of users is 0 
name_one = users('mohammed ', 22, 'male')  # user1
name_two = users('mai', 21, 'fmale')  # users 2
name_three = users('rana', 21, 'fmale')    # users 3
name_four = users('ibrahim', 22, 'male')
name_five = users('hamdy', 22, 'male')
name_six = users('hamd', 23, 'male')
print(f'Number of users is \'{users.counter_users}\'') #Number of users is '5'

print(name_one.firstname())
print(name_two.firstname())
print(name_three.firstname())
print(name_four.firstname())
print(name_five .firstname())
print(name_six .firstname())

print('-'*20)

print(f'Number of users  on sys \'{users.counter_users}\'')#Number of users  on sys '6'
#print(name_six .added_users())  #>>User hamdy Is Added
print(f'Number of users  on sys \'{users.counter_users}\'') #Number of users  on sys '7'

print('-'*20)

print(print(name_six .deleted_users())) #>>User hamd Is deleted
print(f'Number of users in the sys \'{users.counter_users}\'')

'''show all users in systems '''
print(users.show_name_counters())   #  from constractors decorators 
     
        
# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --8 الوراثة
# ------------------------------------------------


class Food:  # Base Class

  def __init__(self, name, price):  #--constractor

    self.name = name

    self.price = price

    print(f"{self.name} Is databaseeated From Base Class")

  def eat(self):

    print("Eat Method From Base Class")

class Apple(Food):  # Derived Class

  def __init__(self, name, price, amount):

    # Food.__init__(self, name)  # databaseeate Instance From Base Class

    super().__init__(name, price)

    self.amount = amount

    print(f"{self.name} Is databaseeated From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

  def get_from_tree(self):

      print("Get From Tree From Derived Class")

# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()

#*------------------------method 2
class pmw_car:

    def __init__(self, name, model, newmodel) -> None:

        self.name = name
        self.model = model
        #self.color =color
        self.newmodel = newmodel
        # *pmw is made in Germany and model car is 2012
        print(f'{self.name} is made in Germany and model car is {self.model}/')

    def add_new_model(self):  # add new model at same pmw car

        print(f'{self.name} {self.newmodel} is  New model Added ->> Old module is {self.model}')
         #print(f'{self.name} is made in Germany and model car is {self.newmodel}')
         #print(f'Old module is {self.model}  and new modle is {self.newmodel}')
        
class skoda(pmw_car):

    # *def meth(self, arg):
    def __init__(self, name, model, price, newmodel) -> None:

        # pmw_car.__init__(self, name, model)  # databaseeate Instance From pmw class
        super().__init__(name, model,newmodel)  #* ورثناهم من الكلاس الرئيسي 

        self.price = price  # السعر خاص بسيارة سكودا
       # self.newmodel = newmodel ملهاش اي ستنين لازمة لان اصلا موروثة من الكلاسي الاصلي 
        
       #4 print(f'Old module is {self.model}  and new modle is {self.newmodel}')
        
        print(f'{self.name} is made in AMIRCAN and model car is {self.model} and price ${self.price}//')
        

print('-'*20)
car1 = pmw_car('pmw', 2012, 2013)  # pmw_car(name, model, newmodel)
car1.add_new_model()

print('-'*20)
car1 = pmw_car('cady', 2018, 2017) # # cady 2017 is  New model Added #
car1.add_new_model()
print('-'*20)

# skoda(name, model, price) #skoda remsh is made in AMIRCAN and model car is 2014 and price $22K//
car2 = skoda('skoda remsh', 2014, '22K',2016)
car2.add_new_model()

print('-'*20)                                                        
car2 = skoda('panda', 2012, '15K',2010)
car2.add_new_model()  #panda 2010 is  New model Added # تورث ميثوت الاضافة من الكلاس الاول لتاني
print('-'*20)        
        
        
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --9
# ---------------------------------------------------------

class BaseOne:         # class one 

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")


class BaseTwo:       # class two

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo): # class derived (class one + class two)

  def __init__(self, name):
      
    self.name = name

    print(f"{self.name}")

my_var = Derived('inherant  class')

#print(Derived.mro())    # method resoluthon order #(method) mro: () -> list[type]
                        # Return a type's method resolution order.
print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base): #  ورثان من كلاس الاول 

  pass

class DerivedTwo(DerivedOne): # ورثان من الكلاس التاني وبالتالي هيكون ورثان من الاول لان اصلا التاني ورثان من الاول 

  pass        
        
        

# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --10 >>متعدد الاوجه>>
# -------------------------------------------------

#* بتعمل اكتر من شغلة وحاجات مختلفة من  نفس الميثتوت في كزا كلاس 

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"Key_One": 1, "Key_Two": 2}))


 # بشكل عام 
 
 # نفس الميثوت بعمل كزا وضيفة في كزا كلاس  وايضا بتقدر تورث شغلات بينهم 
  
class A :  
    
    def do_something (self):  # نفس الميثوت
        
        print( 'From Class A*****')  #   ازا هدا الميثتوت مش موجود في باقي لكلاسات طلع ايروري زي هيك !!هدا فحالة استدعيت نفس لكلاس الي ماخد  ومتثورت من الي هتستدعيه
        
        raise NotImplementedError("Derived Class Must Implement This Method")
    
class B(A) :
        
        def do_something (self): # نفس الميثوت
        
         print('From Class B*****')

class C(B) :
        
       pass   
         
     
var =C()   
var.do_something()          
        
        
#--------------------------------------------------
# -- Object Oriented Programming => Encapsulation --9 
# --------------------------------------------------
# ( يعني أنواع البيانات الي بتعامل معاها هيا ( عامة - محمية - خاصة
#* Encapsulation التغليف 
# - Restrict Access To The Data Stored in Attirbutes and Methods

#* Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - into Our Outside The Class
#* Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
#* Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

class Member:

  def __init__(self, name):

    self.name = name  # Public

one = Member("Ahmed")
print(one.name)

one.name = "Sayed"   # ببتقدر توصلوا من اي مكان وبتعدل عليه
print(one.name)
#*------------
class Member:

  def __init__(self, name):

    self._name = name  # Protected

one = Member("Ahmed")
print(one._name)        # .one underscore(._)= protected 
one._name = "Sayed"
print(one._name)

#*------------
class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self): # method

    return f"Hello {self.__name}"

one = Member("Ahmed")
# print(one.__name)    # error ,because private cant be acasse to the  method
print(one.say_hello())
   
 
 
 
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --12
# ------------------------------------------------------
#* بنستخدمهم لما يكون برايفت وبدنا نوصل لشغلة جواتهم

# get >> بتجيب الاسم وبتطبعلك اياه 

# set >> بتجيب الاسم اول الاوبجت وبتعدل عليه 

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name # ركز هان بدون  return

one = Member("Ahmed")

print(one.say_hello()) # Hello Ahmed

print(one.get_name())  #Ahmed

one.set_name('mhamoud') #(new_name: Any) -> None
print(one.get_name())   # mhamoud
#----
one._Member__name ='rami'   # privat name >> رغم انوا برايفت قدرنا نوصل للاسم ونعدل  عليه كمان
print(one._Member__name)  #rami
#----
 
 
#* --------------------------------------------------------
# *-- Object Oriented Programming => @ Property Decorator --13
# *-------------------------------------------------------
 
 # بنستخدمها لما يكون عندك ميثوت بس الها وضيفة وحدة بدون باراميتر ,,بس  فيها 'self' 

class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property                     #<<< بس شغلتها تطلع  age *365 
  def age_in_days(self): # هان ميثوت ما بتقبل بارميرتر  ولا اشي بس وضيفتها ترجع رقم 

    return f" {self.age * 365:0.1f} "  #float no

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hello())
#print(one.age_in_days())

print(one.age_in_days)
 

# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod  

class Programming(metaclass=ABCMeta):  # كلاس مجرد بس وضيفتوا انوا ينظم الريل كلاس real class
 
 #  لازم عدد  الميثون هان يكون نفسوا في باقي لكلاسات والسبب انهم برثوا من الكلاس المجرد ونفس اسم الميثوت والباث والنمط د
 # هان في 2 ابستراكات ميثوت 
  @abstractmethod   
  def has_oop(self): #method 1 ما بترجع اشي 

    pass

  @abstractmethod 
  def has_name(self): #method 2

    pass

class Python(Programming):  # كلاس 1 << وضيفتوا يتورث خصائص الكلاس المجرد programming 

  def has_oop(self): 

    return "Yes"
  def has_name(self):  #  نفس الباث تاع ال abstractmethode                 # الي فوق من الكلاس المجرد
    return "python"

class Pascal(Programming):# يتورث من الكلاس الرئيسي المجرد خاصئصه ويطلعلك NO

  def has_oop(self):

    return "No"

  def has_name(self):  #  نفس الباث تاع ال abstractmethode 
                       # الي فوق من الكلاس المجرد

    return "Pascal"

one = Pascal()
two = python()
print(one.has_oop())
print(one.has_name())



# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# بنقول عنها ابساراكت  كلاس ادا في اكتر من ابستراكت ميثوت
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):  # كلاس مجرد بس وضيفتوا انوا ينظم الريل كلاس real class

  @abstractmethod
  def has_oop(self): # 1 abstract method

    pass

  @abstractmethod
  def has_name(self): # 2 abstract method

    pass

class Python(Programming):  # كلاس 1 << وضيفتوا يتورث خصائص الكلاس المجرد programming 

  def has_oop(self):   # 1 real class

    return "Yes"
  def has_name(self): # 2 real class

    return "python"

class Pascal(Programming):   # يتورث من الكلاس الرئيسي المجرد خاصئصه ويطلعلك NO

  def has_oop(self):   # 1 real class

    return "No"

  def has_name(self):  # 2 real class

    return "Pascal"

one = Pascal()
two = Python()

print(one.has_oop())#No
print(one.has_name())#Pascal

print(two.has_oop())#Pascal
print(two.has_name())#python



#*-----------------------------------------------------
#*----------example for OPP (CLASS )
#*-----------------------------------------------------

def name(name1,name2,name3,name4) :
       
      allname =[name1,name2,name3,name4]   #* بتخزن كل في ليست 
      
      for name in allname:
            print(f'hello {name}')
name( 'mohammed','mai','lana','rana' ) 
#//-------------------------

class users :

 def __init__(self ,username,email,age):
  self.username =username
  self.email =email
  self.age= age

#exceptions
class  user_name_error(Exception) :  
   pass
class invalid_email_error(Exception):
  pass
class invalid_age_error(Exception):
  pass
class under_age_error(Exception):
  pass

# data_base خزنا البراميتر جوات ليست>> username,email,age
data_list =[
  ('mohammed','abureada2017@gmail.com',22),
  ('Rana ','rana2001@gmail.com',13) ,
  ('mai ','mai2000@gmail.com' ,21),
  ("jane", "jane@example.com", 21),
  ("bob", "bob@example", 19),
  ("jane", "jane2@example.com", 25),
  ("steve", "steve@somewhere", 15),
  ("joe", "joe", 23),
  ("anna", "anna@example.com", -3),
]

# بدنا نرجع الليست على  ديكشنري عشان نقدر نتعامل معاها من الفور وناخد ونرجعمنها داتا 

addition_list= {}  # dictionary عشان نرجع الاسماء فيها لما نطبق عليها الif cond

for username,email,age in data_list :

  try :
# وضح نوع الايرور 
    if username in addition_list:
       raise user_name_error()

    email =email.split('@')
    if len(email) != 2 :
      raise invalid_email_error()
    if age < (-2) :
      raise under_age_error()
    if age < 15:
       raise invalid_age_error()   
# باستثناء هدول 
#  
  except user_name_error:
        print(f"Username \'{username} is in use.")
  except invalid_age_error:
        print(f"{age} years old is Invalid age")
  except under_age_error:
        print(f"User {username} is under Age.")
  except invalid_email_error:
        print(f" {email} is not a valid email address.")
  else:      
       
      addition_list[username] =users(username, email, age)


# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)


# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close

# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>

# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# 

# SQlite >> database

import sqlite3

# great db 
database =sqlite3.connect("database.db")

#*execute > بتنفد شغلة وحدة 

#*  add table and fields via "(execute directe)" :

#*  OR--add table and fields via "cursor.execute"

cursor =database.cursor()
'''
cursor.execute('create table if not exists users (idusers integer, username text )')
cursor.execute('create table if not exists skills (name text, user_id integer, progres integer )')
'''
# Insert data 1


'''
cursor.execute('insert  into users(username  ,idusers ) values(20181615, "Mahmoud")')
cursor.execute('insert  into users(username  ,idusers ) values(20181659, "Mohammed")')
cursor.execute('insert  into users(username  ,idusers ) values(20193244, "rana")')
cursor.execute('insert  into users(username  ,idusers ) values(20181376, "mai")')
'''

# Insert data 2 # for loop 

'''
input_user =["mohammed", 'rami' ,'rana' ,'mai' ,'sameer' ,'jamal']

for key , user in enumerate(input_user) :
    
    cursor.execute(f'insert  into users(username  ,idusers ) values("{user}" ,{key +1}) ')
'''
#--- fetch data # ==pop data >> استخراج الداتا  


#database.execute("select idusers from users")
#database.execute("select username  , idusers from users")
database.execute("select * from users") # --(*) all data from users


#print(cursor.fetchone())    #fetchone())
print((cursor.fetchall()))    #fetchall()
#print(cursor.fetchmany(2))  #fetchmany(2)

# save all change inside  db
database.commit()
#  close db
database.close() 


# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------
import sqlite3
database =sqlite3.connect('database.db')

cursor =database.cursor()

#cursor.execute(f'insert into skills (iddnum ,skillsname  ,progress) values("3","Go","55%")')

#cursor.execute(f'insert into skills  values("3","Go","55%")')

typle =("3","gen","65%")
#cursor.execute(f'insert into skills  values(?,?,?)',typle)

#cursor.execute(f'select * from skills')

#cursor.execute("select * from skills order by iddnum") الترتيب حسب الاي دي
#cursor.execute("select * from skills order by skillsname") الترتيب حسب اسم المهارات
#cursor.execute("select * from skills order by iddnum asc") # ترتيب تصاعدي
#cursor.execute("select * from skills order by iddnum dasc") # ترتيب تنازلي ي
#cursor.execute("select * from skills order by iddnum >2")
#cursor.execute("select * from skills order by skillsname limit 3 offset 2") #على الاقل تلات3 عناصر وتجاوز اول تنين2 منهم
cr.execute("select * from skills where user_id not in(1, 2, 3)") # من الرينج  كزا الي كزا 
cr.execute("select * from skills where user_id in(1, 2, 3)")
results = cursor.fetchall()

# Loop On Results
for row in results:

  print(f"Skill Name => {row[0]},", end=" ")
  print(f"Skill Progress => {row[1]},", end=" ")
  print(f"User ID => {row[2]}")

# Save (Commit) Changes
database.commit()

# Close Database
database.close()





#*--------------------------------------
# delete Data >>
# update date >> advanced qutations
#*--------------------------------------
# create table on db
# enter from users
# printing all data on db 
# update date
# deleting date
# show all gb

import sqlite3

database =sqlite3.connect('database.db')
cursor =database.cursor()
#1------------------------------------------
cursor.execute('create table if not exists users(idnum integer ,username text)')
cursor.execute('create table if not exists skills (numskill integer , skills text )')
#2-------------------------------------------

enter =input('can i ENTER data (y or n):?')

if enter == 'y' or enter =='Y' :

    counter =0
    while counter != 3 : 
            
         Enter_user =input('Enter your name :')
         user     =[Enter_user]
         counter+=1
    #for loop  users 
         for keys , username in enumerate(user):   

            cursor.execute(f'insert into users (idnum ,username ) values("{keys +1}" , "{user}")')
    print('---data added----')

elif enter =='n' or enter == 'N':
     print('\ndata in side database\n') 

     cursor.execute('select * from users ')

     results =cursor.fetchall()
 
     for data in enumerate(results)  :

       print(f'Users Id: {data[0]}',end =' ')
    
       print(f'usersname is :{data[1]}')
print('---thank u---')

database.commit() # AUTO SAVE DATA WHEN Users added بحفظ تلقائي 

print('-'*30)

#3-----------------------------------------------
#  >> update data >>#لازم يكون فيهاا بيانات الداتا بيس عشان تقدر تعدل فيها # ما زبط تعدل 
                                                                          
update = input('can i updtate data (y or n):/')

if update == 'y' :

    update_user =input('Enter your update_name :')

    userid =input('Enter your id :')

    #user=[update_user]  

    cursor.execute(f"update users set username ='{update_user}' where idnum ='{userid}' ")
    database.commit()

#elif update== 'n':
#----------------------------------------------------------
#* delete data &show data after deleted .
# خلينا المستخدم يختار الاندكس المناسب ويحزفوا من الداتا بي
    
delete = input('can i delete data (y or n):/')
if delete== 'y' :

   idnumber =input('Enter your \'idusersname\' can be deleted :')

   cursor.execute(f'delete from users where idnum = {idnumber} ')
   

#4---------------------------------------------------------------
print('-'*30)

#*fetch data & show all data in db  
cursor.execute('select * from users ') # بنختار الداتا 
results_after_deleted =cursor.fetchall() # خونها في فمتغير عشان تقدر تتعامل معاها 

for data in results_after_deleted:

    print(f'Users Id: {data[0]}',end =' ')
    
    print(f'usersname is :{data[1]}')
#print(f'you deleted {data[0]} in users name ')

database.commit()
database.close()


#*------------------------
#*-- انشاء قاعدة بيانات والادخال من اليوزر
#*------------------------
# طريقة 1

import sqlite3
#create data base 
database = sqlite3.connect('database.db')

#sucsses msg 
print('--Connecting data base is Successfully--')

# done all operations inisde db
cursor =database.cursor()

#create table inside db
cursor.execute('create table if not exists users(idnum integer ,username text)')
cursor.execute('create table if not exists skills (numskill integer , skills text )')

#enter from users (3 trys)
counter =0
while counter != 3 : 
            
    Enter_user =input('Enter your name :')

    Enter_skills =input('Enter your skills :')

    # sorte data inside list
    user     =[Enter_user]
    idnumber =[Enter_skills]
    counter+=1
    
    #for loop  users 
    for keys,username in enumerate(user):   

        cursor.execute(f'insert into users (idnum ,username ) values("{keys }" , "{username}")')

    #for loop  skills     

    for numskill,skills in enumerate(idnumber):   

        cursor.execute(f'insert into skills (numskill , skills) values("{numskill }" , "{skills}")')    

    # fetch data  
       
    cursor.execute('select * from users')
    #cursor.execute('selet username from users')

    resulte =cursor.fetchall()  # resulte>> وبالتالي بنوصل للبيانات من خلال الاندكس(mohammed ,1) >> (index 0,index 1)
    print('-'*20)

    for items in resulte:

        print(f'Users ID  is :{items[0]} ,', end=' ')  
        print(f'User name is :{items[1]}.')
 

# close database
print("Connection To Database Is Closed")

#sucssefully msg added 
print('added sucssefully !!')

database.commit()
database.close()

#*------------------------
#*-- انشاء قاعدة بيانات والادخال من اليوزر
#*------------------------
#   Try  and except طريقة 2


import sqlite3

def getall_data():

    try :

        #create data base 
        data = sqlite3.connect('database.db')
        #sucsses msg 
        print('--Connecting data base is Successfully--')
        # done all operations inisde db
        cursor =data.cursor()

        #create table inside db
        cursor.execute('create table if not exists users(idnum integer ,username text)')
        cursor.execute('create table if not exists skills (numskill integer , skills text )')

         #enter from users (3 trys)
        counter =0
        while counter != 3 : 
            
            Enter_user =input('Enter your name :')

            Enter_skills =input('Enter your skills :')

            # sorte data inside list
            user     =[Enter_user]
            idnumber =[Enter_skills]
            counter+=1
        print(f'{user}>>{idnumber}')
    
    #for loop  users 
        for keys,username in enumerate(user):   

            cursor.execute(f'insert into users (idnum ,username ) values("{keys}" , "{username}")')

    #for loop  skills     

        for numskill,skills in enumerate(idnumber):   

            cursor.execute(f'insert into skills (numskill , skills) values("{numskill }" , "{skills}")')

    #added sucssefully msg  
        print('added sucssefully !!')        

    except sqlite3.Error as error:  # contints all errors

        print(f'TYPE ERROR :{error}')    

    finally: # بتتنفد دايما باي وقت 
        
        if (data):

            data.commit()
            # close database
            print("Connection To Database Is Closed")
            data.close()

getall_data()


#*------------------------
#*-- انشاء قاعدة بيانات والادخال من ليست جاهزة ر
#*------------------------
#   طريقة  3

import sqlite3

databse = sqlite3.connect('database.db')

cursor =databse.cursor()

cursor.execute('create table if not exists users(idnum integer ,username text)')

cursor.execute('create table if not exists skills(skillsname text, progres integer)')

input_user =["mohammed", 'rami' ,'rana' ,'mai' ,'sameer' ,'jamal']

degrees    =['30%','50%','70%' ,'10%', '66%','33%']
skills     =['php' ,'js' ,'html', 'python' ,'css' ,'dart']

for keys , items, in enumerate(input_user) :

  cursor.execute(f'insert into users(idnum ,username ) values("{keys +1}" , "{items}")')
     
for skill in  skills:

  for deg in degrees :

    if len(degrees) == 0:

       cursor.execute(f'insert into skills (skillsname , progres) values("{skill}","{deg}")')

# fetch data 
databse.execute('select * from users')
resulte =cursor.fetchall()

print(f"Database Has {len(resulte)} Rows.")

for row in resulte:

    print(f"UserID => {row[0]},", end=" ")

    print(f"Username => {row[1]}")

print("Connection To Database Is Closed")


databse.commit()
databse.close()





#*----------------------------
#same idea but diff ways -------
#*----------------------------

import sqlite3

database =sqlite3.connect('database.db')

cursor =database.cursor()

def close_commit ():
    
    database.commit()
    database.close()

# تجربة ادخال الid من اليوزر ما بزبط
'''def id_users():

   ids = input(f'<< Enter Id >>:'.strip())

id_users()'''

input_msg ="""
-(a) >>add skills
-(d) >>delete skills
-(u) >>update skills
-(s) >>showe all skills
-input your options: ['a','d','u','s'] : """   
list =['a','b','u','s']

msg =input(input_msg)

cursor.execute('create table if not exists users(idnumber integer ,username text)')
cursor.execute('create table if not exists skills (iddnum integer , skillsname text  , progress integer)')

def add_skills():
    #num=input('Enter num of trying to added( 3 Tries):> ')
    #while int(num) <= 3 :
        print('-welcome backe in add skills-')

        skills =input('enter  skills >>'.capitalize().strip())
        cursor.execute(f'select skillsname from skills where skillsname ="{skills}" and iddnum ="{ids}" ')
        resulte =cursor.fetchall()

        if resulte != None: # Theres No Skill With This Name In Database

            prog =  input('enter progress>>'.strip())
            cursor.execute(f'insert into skills (iddnum ,skillsname  ,progress) values("{ids}" , "{skills}","{prog}%")')
        
        else:# Theres A Skill With This Name in Database
             print("You Cannot Add It")

        print(f'--{skills} skill still added --')
        close_commit()  
    #else:
       # print('try agin')
       # close_commit()
    


def delete_skills():  

    dell =input('Enter your delete skill :'.capitalize().strip()) 

    cursor.execute(f'delete from skills where skillsname  ="{dell}" and iddnum  = "{id}" ')
    print(f'--{dell} skills deleted --')
    close_commit()
     

def update_skills():    

    update =input('write  skills to update: '.capitalize().strip())

    prog =  input('enter  new progress>>: '.strip())
                                                           #ب >>بدون بعمل تحديث لكل اليوزر المتشابهiddnum = '{idd}'
    cursor.execute(f"update skills set progress = '{prog}' where skillsname = '{update}' and iddnum = '{id}'")

    close_commit()
    #print(f'--{update} skills update --')
 
def showe_all_skills():
    
    cursor.execute(f'select * from skills where iddnum = "{id}"')
    resulte =cursor.fetchall()

    for row in resulte:

      print(f"Skill => {row[0]},", end=" ")

      print(f"Progress => {row[1]}%")
    close_commit()


if msg == 'a' :

    add_skills()

elif msg== 'd':

    delete_skills()

elif msg =='u' :
     update_skills()

elif msg == 's':

    showe_all_skills()

else:

    print("App Is Closed.")

# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------

print(__name__)

# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

import timeit

print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000"))

name = "Elzero"

print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000"))  # اطبعهم على نفس السطر

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4)) #تكرار لعملبة التنفيد اربع مرات يعني اربع مليون عملية وع كل عملية وقت تنفيد خاص

# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------
#اختبار وقت تنفيد الكود   باستخدام methode timeit


import timeit

print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000"))

name = "Elzero"

print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000")) # كرر الاسم ألف مرة جنب بعض 

# print(random.randint(0, 50)) # رقم عشوائي انتجر فالرينج هدا 

#timeit(stmt, setup, timer(repeat: int), number ,globals>>Optional[Dict[str, Any]])

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))

#*------------------------------------------من التكاليف 

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



# -------------------------
# -- Outro and Resources --
# -------------------------
# Documentations => https://docs.python.org/3/
# --------------------------------------------
# Useful Websites:
# - Real Python     => https://realpython.com/
# - Programiz       => https://www.programiz.com/python-programming
# - GeeksforGeeks   => https://www.geeksforgeeks.org/python-programming-language/
# - W3Schools       => https://www.w3schools.com/python/default.asp
# - LearnPython     => https://www.learnpython.org/
# - TutorialsPoint  => https://www.tutorialspoint.com/python/index.htm
# -----------------------------------------------------------------
# Collection
# - https://wiki.python.org/moin/BeginnersGuide/Programmers
# ---------------------------------------------------------
# Resources
# - https://awesome-python.com/
# ---------------------------------------------------------
# The Next Level ?
# - GUI With Tkinter & PyQt
# - Parsing Html With BeautifulSoup
# - Manage HTTP Requests With Requests Module
# - Web Development With Django & Flask & Web.py
# - The Binary Number System
# ---------------------------------------------------------
















