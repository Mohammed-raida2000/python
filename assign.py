
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
