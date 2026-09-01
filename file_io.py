## FILE IO:
##Reading a file
#f = open('myfile.txt', 'r')
#print(f)
#text = f.read()
#print(text)
#f.close

#Writing a file
#f = open('myfile.txt', 'a')
#f.write('Hello, World!')
#f.close()

#with open('myfile.txt', 'a') as f:
    #f.write("Hey i am inside with")
#f = open('myfile.txt', 'r')
#i = 0
#while True:
    #i = i +1
    #line = f.readline()
    #m1 = int(line.split(",")[0])
    #m2 =int(line.split(",")[1])
    #m3 =int(line.split(",")[2])
    #print(f"Marks of student {i} in Maths is: {m1*2}")
    #print(f"Marks of student {i} in Sst is: {m2*2}")
    #print(f"Marks of student {i} in English is: {m3*2}")
    
    
    #print(line)
    #if not line:
        #print(line, type(line))
        #break
#f = open('myfile2.txt', 'w')
#lines = ['line 1\n', 'line2\n', 'line3\n']
#f.writelines(lines)
#f.close

## seek() fun:
with open ('myfile.txt', 'r') as f:
    print(type(f))
    f.seek(10) ## move to the 10th byte in the file

    data = f.read(5) ## read the next 5 bytes
    print(data)

## tell() fun:
with open ('myfile.txt', 'r') as f:
    dara = f.read(10)
    current_position = f.tell() ## saves the current position

## Truncate() fun:
with open('sample.txt', 'w') as f:
    f.write('Hello World !')
    f.truncate(5)
with open('sample.txt', 'r') as f:
    print(f.read())
    
    
    













    

