from itertools import islice
import re
import csv
import pymongo as pym
from datetime import datetime
import dateutil.parser as dparser
global str
i = 1
client = pym.MongoClient('mongodb://localhost:27017/')
db = client["CBC22"]
table1 = db["CC22"]


name = " "
age = " "
phone = " "
date = " "
gender = " "
mappings = ['TEST NAME','REFERENCE RANGE','UNIT','RESULT']
lis = []
list1 = []
list2 = []
list3 = []
lis1 = []
list11 = []
list22 = []
dat = []
with open("Firsthalfipi%i.txt" %i,'r') as f:
     for d in f:
            if 'Patient Detail' in d:
                ln = ''.join(islice(f, 1))       
                l = list(ln.strip().split(' '))
                x = re.findall(r'\d{2}-\w{3}-\d{4}', ln)
                if (x):
                      
                      for strs in x:
                          print(strs)
                          date = date + strs
                print(l)

                g = 0 
                while g < len(l) and l[g].isdigit() != True:
                    str1 = " "
                    x = re.findall("[a-zA-Z]", l[g])
                    
                  
                    if x:
                     
                     for strs in x:
                     
                      str1 = str1 + strs
                    

                    name = name + " " + str1
                    g = g+1
                print(name)

                h = 0 
                while h < len(l):
                    if l[h].isdigit()==True:
                        age = age + " " + l[h] 

                    h = h+1
                print(age)

                k = 0 
                while k < len(l) and l[k].isalpha!=True:
                    if l[k] == '/' or l[k] == '(Y)/':
                        gender = gender + " " + l[k+1]
                           
                        #date = date + " " + l[k+2] + " " + l[k+3] 
               

                    k = k+1
                print(date)
                print(gender)
            if 'Mobile' in d or 'Mobile:' in d:
                ln = ''.join(islice(f, 1))       
      
                l = list(ln.strip().split(' '))

                g = 0 
                while g < len(l) and l[g].isalpha() != True and l[g] != 'Standard.':
                    phone = phone + " " + l[g]

                    g = g+1
                print(phone)
                phone1 = list(phone)
                print(phone1)
                f = 0
                phone2= " "
                while f < len(phone1):
                 if phone1[f].isdigit()==True:
                    

                    phone2 = phone2+phone1[f]
                 f = f+1
               
                print(phone2) 
            #if 'Registration Date' in d:
             #   ln = ''.join(islice(f, 1))       
              #  l = list(ln.strip().split(' '))

               # print(l)
                #j = 0 
                #while j < len(l) and l[j].isalpha() != True:
                 #   date = date + " " + l[j]
                  #  j = j+1
               # print(date)


    #i = i+1

    
    
with open('secondHalfipi%i.txt' %i,'r') as fn:
     
     for d in fn:
        li = list(d.strip().split(' '))
        p = li[0]
        m = len(li)
        n=0

        if len(li) > 3:

           while n < 3 and li[n].isdigit() != True and li[n].replace('.', '', 1).isdigit() !=True and li[n] != "Less":
               strs = li[n]
               str1= " "
               b = 1

               while b < 2 and li[b].isalpha()==True:
                   #print(li[b])
                   if li[b].isalpha() == True:
                       strs = strs+" "+ li[b]
                       str1 = str1 + " "
                   #i = 2
                       #print(str)
                   b = b+1
               lis.append(strs)
               list11.append(str1)


               n = n + 1

               
               n = 1

               while n < m-1:
                  if li[n].isdigit() == True or li[n].replace('.','',1).isdigit() == True:
                     if li[n+1] == '-':
                        #print(li[i+1])
                        strs = li[n] + '' + li[n+1] + li[n+2]
                        #print(str)
                        list2.append(strs)
                     if li[n] == 0-0.2:
                         print("yesss")
                         strs = strs+li[n]
                         list2.append(strs)

                  if li[n]=="Less" or li[n] == "less":
                      strs = li[n] +" "+ li[n+1] + li[n+2]
                      list2.append(strs)
                  x = re.findall("^\d-\d.\d|^\d-\d*|^\d.\d\d-\d|<1|^\d-\d.\d|^\d\d-\d\d|^\d.\d-\d|^\d\d\d\d|^\d\d\d-\d\d\d|^\d.\d-\d.\d|^\d\d-\d|^\d-\d\d|^\d-\d.\d|^0-0.2", li[n])
                  #print(list2)

                  if (x):
                      str1 = " "
                      for strs in x:
                          print(strs)
                          str1 = str1 + strs
                      #print(str1)
                      list2.append(str1)
                  s = re.findall("^\s-\d.\d|^-\d.*|^-.\d",li[n])
                  if (s):
                    print("yesss")
                    strr = " "
                    strr1 = " "
                    for strs in s:
                      print(strs)
                      
                      strr1 = li[n-1] + strs
                    print(strr1)
                    list2.append(strr1) 

                  t = re.findall("^\d\d.\d-|^\d.\d-\s",li[n])
                  if (t):
                   print("yesss")
                   strr2 = " "
                   strr3 = " "

                   for strs in t:
                      print(strs)
                      strr2 = strr2 + strs
                      strr3 =  strr2+li[n+1] 
                   #print(strr3)
                   list2.append(strr3)
                   print(list2)



                  n = n+1
                  #print(len(list2))
                  #print(len(lis))

               if (len(lis)> len(list2)):
                   #print("yessss")
                   strn = " no range found"
                   list2.append(strn)
               n = 1
               while n < m:
                   if n != m-1:
                       if li[n].isdigit() == True or li[n].replace('.', '', 1).isdigit() == True:
                           if li[n + 1] != '-':
                               if li[n - 1] != '-' or li[n-1] != "Than":
                                 if len(li[n])<6:
                                   strs = li[n]
                                   list1.append(strs)
                                   break
                   else:
                       if li[n].isdigit() == True or li[n].replace('.', '', 1).isdigit() == True:
                           if n == m-1 and li[n-1] != '-':
                               strs = li[n]
                               list1.append(strs)
                   n = n + 1
               if (len(lis)> len(list1)):
                   strn = "value not found"
                   list1.append(strn)
               n = 1
               while n < m:
                   x = re.findall("%|fl|fL|pg|Pg|g/dl|g/dL|^g.*|^f.*",li[n])
                   b = re.findall("^x.*", li[n])

                   if (b):
                       if '12' in li[n] or '12' in li[n+1]:
                           str2 = "x10^12/I"
                           list3.append(str2)
                       elif '9' in li[n] or '9' in li[n+1]:

                           str2 = "x10^9/I"
                           list3.append(str2)
                       else:
                           str2 = "x10.e /ul"
                           list3.append(str2)
                   if (x):
                           strr = " "
                           for strs in x:
                               str1 = strr + strs
                               list3.append(str1)

                   n = n + 1
               #print(len(list2))
               #print(len(list3))
               if (len(lis)> len(list3)):
                   strn = "value not found"
                   list3.append(strn)
        j = 0
        k = 0
        list9 = []
        #list11= []
        #p = 0
        #while p < len(lis):
         #   list11.append("Test Name")
          #  p = p+1
       # while i < len(lis):
        # if "Hb" in lis[i]:
         #   lis[i] = "HGB"

         #if "Total RBC" in lis[i]:
          #  lis[i] = "RBC"


       #  if "WBC Count" in lis[i]:
        #    lis[i] = "WBC"

         #if "Neutrophils" in lis[i]:
          #  lis[i] = "%Neut"
         #if "Lymphocytes" in lis[i]:
          #  lis[i] = "%LYMP"

         #if "Monocytes" in lis[i]:
          #  lis[i] = "%MONO"

        #i = i + 1
        #dict2 = {}
        #dict2["Patient Name"] = name
        #dict2["Patient Address"] = address
        #dict2["Patient Age"] = age
        #dict2["Date"] = date
        #dict2["Patient Contact"] = phone2
        p = 0
        
        dict = {}
        while k < len(lis):

       

         #dict[mappings[j]] = lis[k]
         #dict[mappings[j + 1]] = list2[k]
         #dict[mappings[j + 2]] = list3[k]
         #dict[mappings[j + 3]] = list1[k]

         dict["Patient Name"] = name
         #dict["Patient Address"] = address
         dict["Patient Age"] = age
         dict["Date"] = date
         dict["Patient Contact"] = phone2
         
         
         b = k+1
         dict["Test Name" +" " +str(b)] = lis[k]


         dict[lis[k] +" "+"Range"] = list2[k]
         dict[lis[k] +" "+"Unit"] = list3[k]

         dict[lis[k] +" "+"Result"] = list1[k]
         list9.append(dict)
        
         k = k + 1
print(list9)

   
print(list1)
print(lis)

print(list2)
print(list3)
db.table.insert_one(dict)
    #print(dict) 

  