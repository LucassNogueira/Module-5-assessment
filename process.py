log_file = open("um-server-01.txt") #this imports the text file into our py file so we can use the data 


def sales_reports(log_file): #here we are defining a function that is taking in the file we brought in
    for line in log_file:   #here we are looping over every line in the file
        line = line.rstrip() #rstrip removes the trailing whitespace from the line 
        day = line[0:3] #this is slice notation starting from index 0 we want the information until we reach index 3
        if day == "Mon":   #here we are checking if the day is equal to the string "Tue"
            print(line) #we are printing out the line if all needs met


# sales_reports(log_file) #invoking the function we just defined above with the data we passed from the file


def over_ten(log_file):
    for line in log_file:
        line=line.split()
        if int(line[2]) > 10:
            print(line)


over_ten(log_file) 