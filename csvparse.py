import csv

infile=open(file="person.csv",mode="r")
csvreader=csv.reader(infile,delimiter=",")
next(csvreader)
for x in csvreader:
    fname=x[0]
    lname=x[1]
    email=x[2]
    city=x[3]
    print("{}.{} is from {} and can be contact at {}\n".format(fname,lname,city,email))




