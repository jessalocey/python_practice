#a very C way to do it:
#f = open("example_data.csv")
#print(f.read(10)) #first 10 bytes
#f.close()

col=0

with open("example_data.csv") as f: #like English: with "file.txt" as "name I give it" do the following:
#    print(f.read()) #this reads in the file, saves it in memory and then prints it out. Not great.
    
#a better way
#    while True:
#        data = f.readline()
#        print(data)

#        if not data:
#            break

#best
    for line in f:
        row=line.split(",")
        print(row[col])