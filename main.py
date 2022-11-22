import csv
import random
from datetime import datetime
from connect import illegal, sendEmails
random.seed(datetime.now())
#dictionary of illegal matchups

#fill dictionary with name email pair from csv file. csv file is formatted as Name,Email
emails = {}
pairs = {}
#create 2 lists so that I can make pairs
l1 = []
l2 = []
complete = False

with open("emails.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        emails[row[0]] = {"email":row[1], "interests": ','.join(row[2:])}
        l1.append(row[0])
        l2.append(row[0])

#remove the header from each list
del(emails["Name"])
l1.remove("Name")
l2.remove("Name")

while(not complete):
    #assume it works
    complete = True
    #shuffle both lists
    random.shuffle(l1)
    random.shuffle(l2)
    for i in range(len(l1)):
        pairs[l1[i]] = l2[i]
    
    for key in pairs:
        #try again if anyone matched with themselves, their s/o, or each other
        if key == pairs[key] or (key in illegal and illegal[key] == pairs[key]) or key == pairs[pairs[key]] :
            complete = False
sendEmails(pairs, emails)

