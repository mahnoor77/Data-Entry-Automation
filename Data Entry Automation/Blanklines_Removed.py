i = 0

while i < 11:

  
    with open('IPi%i.txt' %i,'r') as f, open('blanklinesremovedIPi%i.txt' %i,'a') as fs:
        for line in f:
            if not line.isspace():
                fs.write(line)
    i = i+1