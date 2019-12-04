import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

def nameAnalysis(data, name):
    is_name = data['name'] == name  #Iterates through every line of data frame to find which ones hold the name
    data_frame = data[is_name] #Saves all rows where name is to a new data frame
    data_frame = data_frame.sort_values(by=['year']) #Sorts the rows by year in ascending order
    data_frame = data_frame.set_index('year') #Sets year to index
    data_frame = pd.DataFrame(data_frame, columns=['count']) #Removes all columns except index (which is year) and count
    print(data_frame)

    dict1 = data_frame.to_dict() #Forces to dictionary, unfortunately first index is "count"
    dict2 = dict1['count'] #Removes "count" from dictionary, giving us dictionary where key is year and value is count

    #init_year = 1910
    #while init_year < 2018: #This while loop can be used to add values of 0 for years where name has no data
    #    if init_year in dict2:
    #        break
    #    else:
    #        dict2.update({init_year:0})
    #    init_year += 1

    lists_of_tuples = sorted(dict2.items()) #Creates list of tuples

    #x, y = zip(*lists)
    #plt.plot(x,y)
    #plt.show
    #print(dict2)


def yearAnalysis(data, year):
    is_year = data['year'] == year #Iterates through every line of Data frame to find which ones hold the same year
    data_frame = data[is_year] #Saves all rows where year matches to a new data frame
    data_frame = data_frame.sort_values(by=['count'], ascending=False) #Orders by occurences
    is_male = data_frame['gender'] == 'M' #Tests for M in gender
    m_data_frame = data_frame[is_male] #Makes new data frame of only males
    is_female = data_frame['gender'] == 'F' #Tests for F in gender
    f_data_frame = data_frame[is_female] #Data frame for females
    m_top5 = m_data_frame.head() #Creates value top 5 for men
    f_top5 = f_data_frame.head()
    list1 = f_top5["name"] #Is actually a data frame, but works for our purposes
    print(list1)
    string = '' #Creates empty string
    for i in list1:  #Adds each entry to string with comma and space in between
        string = str(string + i + ', ')
    string = string[0:-2] #Removes ', ' from final entry
    #print(m_data_frame.head(4))
    #print(f_data_frame.head(4))
    print("In " + str(year) + " the most popular female names in Maryland were " + string + ".\n")

data = pd.read_csv("MD.csv") #Loads CSV
#print(data.head()) #Check data layout
df = pd.DataFrame(data, columns=['year', 'gender', 'name', 'count']) #Removes "state" from set, not needed as it is always MD

choice = None #Sets empty value for choice

while choice != '3':
    choice = input("""This application will present statistics for name trends. Would you like to: 
    1. See data by year
    2. See data by name
    3. Exit program
    Please make an entry based on the number: """)
    if choice == '1':
        year = int(input("Enter a year: "))
        yearAnalysis(df, year)
    elif choice == '2':
        name = input("Enter a name: ")
        nameAnalysis(df, name)
    else:
        print("Invalid Input, please enter a valid choice of either 1, 2, or 3")

