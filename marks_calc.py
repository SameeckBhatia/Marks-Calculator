#importing required libraries 
from statistics import *
import csv

#adding marks
append_or_not = input("Would you like to add marks?: ")

while append_or_not.lower() in "yes":
    
    inp_course = input("\nEnter your desired course: ")
    inp_cat = input("\nEnter your desired category: ")
    inp_weight = float(input("\nEnter %s weight: " %(inp_cat)))
    inp_mark = float(input("\nEnter %s mark: " %(inp_cat)))
    
    if not inp_course.isdigit() and inp_cat.isalpha() and \
       0 <= inp_weight <= 1.0 and 0 <= inp_mark <= 100.0:
        
        with open("marksheet.csv", "a", newline = "") as file:
            
            writer = csv.writer(file)
            writer.writerow([inp_course, inp_cat, \
                             inp_weight, inp_mark])
            file.close()
            
    else:
        
        print("Invalid input")
        
    append_or_not = input("\nAdd more?: ")
    
#opening csv file
f = open("marksheet.csv", "r")

line = f.readline().strip()

array = []

#adding csv values to dictionary
while line != "":
    
    array.append(line.split(','))
    
    line = f.readline().strip()
    
courses_dict = {}

#cleaning up dictionary
for i in range(1, len(array)):
    
    cat_dict = {}
        
    course = array[i][0]
    category = array[i][1]
    mark = array[i][3]
        
    if not course in courses_dict:
        
        marks_list = []
        
        for j in range(2, len(array[i])):
            
            marks_list.append(float(array[i][j]))
        
        cat_dict[category] = marks_list
        courses_dict[course] = cat_dict
        
    else:
        
        if category in courses_dict[course]:
            
            for j in range(2, len(array[i])):
            
                courses_dict[course][category].append(\
                    float(array[i][j]))
                
        else:
            
            marks_list = []
            
            for j in range(2, len(array[i])):
            
                marks_list.append(float(array[i][j]))
                
            courses_dict[course][category] = marks_list
    
#viewing marks
view_or_not = input("\nWould you like to view marks?: ")

if view_or_not.lower() in "yes":

    desired = input("\nEnter course: ")
    desired_dict = courses_dict[desired.lower()]
    
    #creating dictionary for weights
    
    weight_dict = {}
    
    for cat in courses_dict[desired]:
        
        weight_dict[cat] = courses_dict[desired][cat][0]
        
    #outputting weighted average for each category
    for i in desired_dict:
            
        list_1 = []
        
        if len(desired_dict[i]) > 2:
        
            for j in range(len(desired_dict[i]) // 2):
                
                list_1.append(desired_dict[i][j * 2 + 1])
                
        else:
            
            for j in range(len(desired_dict[i])//2):
                
                list_1.append(desired_dict[i][j + 1])
            
        desired_dict[i] = round(mean(list_1), 1)
    
    #creating a list for marks and accumulating weights    
    overall_list = []
    sum_weight = 0
    
    for k in desired_dict:
        
        overall_list.append(desired_dict[k] * weight_dict[k])
        sum_weight += weight_dict[k]
        
    total = round(sum(overall_list) / sum_weight, 1)
        
    print("\nYour mark for the course is", str(total) + "%")