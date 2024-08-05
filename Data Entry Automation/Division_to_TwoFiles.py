from itertools import islice

i = 0

while i < 11:
    brek = False
    brk = False
    with open('blanklinesremovedIPi%i.txt' %i,'r') as f, open('Firsthalfipi%i.txt' %i,'a') as fs:
        for d in f:
           fs.write(d)
           if 'TEST(s)' in d or 'Test' in d or "Reference Value" in d or "Unit" in d:
             break
    
    #i = i+1

    
    with open('blanklinesremovedIPi%i.txt' %i,'r') as f, open('secondHalfipi%i.txt' %i,'a') as fs:
        for d in f:
         if "TEST(s)" in d or "Test" in d or "est" in d:
           brek = True
         if brek==True:
                if "TEST" in d or 'Test' in d  or "Reference Value" in d or "Unit" in d:
                 continue
                elif "Note" in d or 'NOTE' in d or 'Peripheral' in d or 'Dr.' in d:
                  break
                else:
                 fs.write(d)
                 if '#BASO' in d or '#'+'BASO' in d:
                     break 
                 if "Eosinophils" in d:
                  ln = ''.join(islice(f, 1))
                  if "Metamyelocytes" not in ln:
                    break 
                  else:
                    fs.write(ln)


         elif "WBC" in d or 'Hb' in d:
            brek = True
         if brk == True:
            fs.write(d) 
        
       
       
    i = i+1