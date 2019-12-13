import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import sys

class Kid:
    def __init__(self, name=None):
        self.name = name  # Name, duh
        self.energy = 20  # Default energy level
        self.compound = None  # No combinations yet

    def __add__(self, another_robot):
        '''
        Override method for addition of two objects
        :param another_robot: Robot object being added on
        :return: Returns results of CompoundRobot SuperClass, which
            adds both Robot Objects together and mingles attributes.
        '''
        return CompoundRobot(self, another_robot)

    def attack(self, another_robot, energy_gain):
        '''
        Battle class - Provides for algorithmic challenges to occur.
        :param another_robot: String: Robot object challenger
        :param energy_gain: Integer: Energy up for grabs
        :return: None, actually. This is a setter class.
        '''
        # If main Robot object is stronger than challenger, decide winner
        if self.energy > another_robot.energy:
            winner = self
            loser = another_robot
        # If main Robot object is weaker than challenger, decide winner
        elif self.energy < another_robot.energy:
            winner = another_robot
            loser = self
        # Energy distribution decision chain
        else:
            # If energy gain is larger than or equal to energy available
            if energy_gain >= self.energy:
                self.energy = 1
            # Otherwise remove energy gain
            else:
                self.energy = self.energy - energy_gain
            # No further operations required
            return
        # If energy gain is larger than or equal to energy available
        if loser.energy <= energy_gain:
            winner.energy = winner.energy + (loser.energy - 1)
            loser.energy = 1
        # Otherwise trade energy gain
        else:
            winner.energy = winner.energy + energy_gain
            loser.energy = loser.energy - energy_gain

class Children(Kid):
    '''
    Super class of Robot for super-robots!

    Attributes:
        Energy: Integer: Energy of Robot Object
        Compound: List: List of Robot Objects combined to
            create super-robot competitor
    '''
    def __init__(self, robot1, robot2):
        super().__init__(self)
        self.components = [robot1, robot2]
        self.energy = robot1.energy + robot2.energy
        robot1.compound = self
        robot2.compound = self

    def __iadd__(self, robot):
        '''
        Override method for addition of two objects via += operator
        :param robot: Object: Robot being added to initial robot
        :return: self: Object: Robot receiving additional robot
        '''
        # Combine energy units, attributes
        self.energy = self.energy + robot.energy
        self.components.append(robot)
        robot.compound = self
        return self

def nameAnalysis(data, name):
    """
    So far occurences of that name by year.
    """
    is_name = data['name'] == name  # Iterates through every line of data frame to find which ones hold the name
    data_frame = data[is_name]  # Saves all rows where name is to a new data frame
    data_frame = data_frame.sort_values(by=['year'])  # Sorts the rows by year in ascending order
    data_frame = data_frame.set_index('year')  # Sets year to index
    data_frame = pd.DataFrame(data_frame,
                              columns=['count'])  # Removes all columns except index (which is year) and count
    # print(data_frame)

    dict1 = data_frame.to_dict()  # Forces to dictionary, unfortunately first index is "count"
    dict2 = dict1['count']  # Removes "count" from dictionary, giving us dictionary where key is year and value is count
    # print(dict2) #Working on percentage per year

    init_year = next(iter(dict2))  # This sets the initializing year to first key in dictionary of occurences
    pctDict = dict()  # Empty dictionary for holding year/percentage
    while init_year < 2019:  # This creates dictionary where key = year and value = percentage
        year_total = (data.loc[df['year'] == init_year, 'count'].sum())
        year_pctg = dict2[init_year] / year_total
        year_pctg = year_pctg * 100
        pctDict[init_year] = year_pctg
        init_year += 1

    # init_year = 1910
    # while init_year < 2018: #This while loop can be used to add values of 0 for years where name has no data if we need it
    #    if init_year in dict2:
    #        break
    #    else:
    #        dict2.update({init_year:0})
    #    init_year += 1

    # lists_of_tuples = sorted(dict2.items()) #Creates list of tuples


def yearAnalysis(data, year):
    """
    So far this will print the five most popular male and female names in a given year
    """
    is_year = data['year'] == year  # Iterates through every line of Data frame to find which ones hold the same year
    data_frame = data[is_year]  # Saves all rows where year matches to a new data frame
    data_frame = data_frame.sort_values(by=['count'], ascending=False)  # Orders by occurences

    is_female = data_frame['gender'] == 'F'  # Tests for F in gender
    f_data_frame = data_frame[is_female]  # Data frame for females
    f_top5 = f_data_frame.head()
    list1 = f_top5["name"]  # Is actually a data frame, but works for our purposes
    listFNames = list()  # AMARIIIIIIII!!!!! FOR PIE CHART!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in list1:  # Turns top 5 female names into ist for piechart
        listFNames.append(i)
    countf = f_top5["count"]
    listFCount = list()  # AMARIIIIIIII!!!!!!FOR PIE CHART!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in countf:  # Turns counts for those 5 female names into list for piechart
        listFCount.append(i)
    string = ''  # Creates empty string
    for i in list1:  # Adds each entry to string with comma and space in between
        string = str(string + i + ', ')
    string = string[0:-2]  # Removes ', ' from final entry

    is_male = data_frame['gender'] == 'M'  # Tests for M in gender
    m_data_frame = data_frame[is_male]  # Makes new data frame of only males
    m_top5 = m_data_frame.head()  # Creates value top 5 for men
    listm = m_top5["name"]
    listMNames = list()  # AMARI PIE CHART!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in listm:
        listMNames.append(i)
    countm = m_top5["count"]
    listMCount = list()  # AMARI PIE CHART!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in countm:
        listMCount.append(i)
    stringm = ''
    for i in listm:
        stringm = str(stringm + i + ', ')
    stringm = stringm[0:-2]

    print("\nIn " + str(year) + " the most popular female names in Maryland were " + string + ".")
    print("The most popuar male names in Maryland were " + stringm + ".\n")


print("This program will provide an overview and analysis on baby names between the years 1910 and 2018.")
choiceState = 'HELP'
while choiceState == 'HELP':
    choiceState = input("""Please enter the abbreviation of the state you would like to investigate (ie. MD for Maryland.)
        To see a list of abbreviations type 'Help': """)
    choiceState = choiceState.upper()
    if choiceState == 'HELP':
        abb = pd.read_csv('https://raw.githubusercontent.com/SatanicTadpole/final/master/abbreviations.csv')
        abbDF = pd.DataFrame(abb)  # The following two were attempting to remove the index
        abbDF = abb.set_index('State')
        print(abbDF)
    else:
        url = 'https://raw.githubusercontent.com/SatanicTadpole/final/master/' + choiceState + '.csv'

# abbreviations = pd.read_csv('https://raw.githubusercontent.com/SatanicTadpole/final/master/abbreviations.csv')
# abbreviations = abbreviations.set_index('year')
# adict = abbreviations.to_dict()
# print(adict)
data = pd.read_csv(url)  # Loads CSV
# print(data.head()) #Check data layout
df = pd.DataFrame(data, columns=['year', 'gender', 'name',
                                 'count'])  # Removes "state" from set, not needed as it is always MD

print('You have chosen ' + choiceState + '.')

choice = None  # Sets empty value for choice

while choice != '3':
    choice = input("""Would you like to: 
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
    elif choice == '3':
        print("\nProgram Terminated")
        exit()
    else:
        print("Invalid Input, please enter a valid choice of either 1, 2, or 3")

