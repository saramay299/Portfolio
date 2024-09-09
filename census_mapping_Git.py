'''
Sara Maholland
CS 5001
Final Project
'''
# Import modules
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import mapclassify
from census import Census
import T_F_Functions 
import numpy as np


#asking user what state they would like
print("This program will print a choropleth map of a chosen state and variable from the US Census.\n")

#listing US states as a choice
US_states = ["AK", "AL", "AR", "AS", "AZ", 
             "CA", "CO", "CT", "DE", "FL", 
             "GA", "HI", "IA", "ID", "IL", 
             "IN", "KS", "KY", "LA", "MA", 
             "MD", "ME", "MI", "MN", "MO",
             "MS","MT", "NC", "ND", "NE", 
             "NH", "NJ", "NM","NV", "NY", 
             "OH", "OK", "OR", "PA","RI", 
             "SC", "SD", "TN", "TX", "UT", 
             "VA", "VT", "WA", "WI", "WV", "WY"] 

print("States to pick from: ", US_states)

#dictiionary for the US sstates and their shapefiles. 
tracts = {"AL": "tl_2019_01_tract.zip",
"AK": "tl_2019_02_tract.zip",
"AR": "tl_2019_05_tract.zip",
"AZ": "tl_2019_04_tract.zip",
"CA": "tl_2019_06_tract.zip",
"CO": "tl_2019_08_tract.zip",
"CT": "tl_2019_09_tract.zip",
"DE": "tl_2019_10_tract.zip",
"FL": "tl_2019_12_tract.zip",
"GA": "tl_2019_13_tract.zip",
"HI": "tl_2019_15_tract.zip",
"IA": "tl_2019_19_tract.zip",
"ID": "tl_2019_16_tract.zip",
"IL": "tl_2019_17_tract.zip",
"IN": "tl_2019_18_tract.zip",
"KS": "tl_2019_20_tract.zip",
"KY": "tl_2019_21_tract.zip",
"LA": "tl_2019_22_tract.zip",
"MA": "tl_2019_25_tract.zip",
"MD": "tl_2019_24_tract.zip",
"ME": "tl_2019_23_tract.zip",
"MI": "tl_2019_26_tract.zip",
"MN": "tl_2019_27_tract.zip",
"MO": "tl_2019_29_tract.zip",
"MS": "tl_2019_28_tract.zip",
"MT": "tl_2019_30_tract.zip",
"NC": "tl_2019_37_tract.zip",
"ND": "tl_2019_38_tract.zip",
"NE": "tl_2019_31_tract.zip",
"NH": "tl_2019_33_tract.zip",
"NJ": "tl_2019_34_tract.zip",
"NM": "tl_2019_35_tract.zip",
"NV": "tl_2019_32_tract.zip",
"NY": "tl_2019_36_tract.zip",
"OH": "tl_2019_39_tract.zip",
"OK": "tl_2019_40_tract.zip",
"OR": "tl_2019_41_tract.zip",
"PA": "tl_2019_42_tract.zip",
"RI": "tl_2019_44_tract.zip",
"SC": "tl_2019_45_tract.zip",
"SD": "tl_2019_46_tract.zip",
"TN": "tl_2019_47_tract.zip",
"TX": "tl_2019_48_tract.zip",
"UT": "tl_2019_49_tract.zip",
"VA": "tl_2019_51_tract.zip",
"VT": "tl_2019_50_tract.zip",
"WA": "tl_2019_53_tract.zip",
"WI": "tl_2019_55_tract.zip",
"WV": "tl_2019_54_tract.zip",
"WY": "tl_2019_56_tract.zip"}

#dictiionary state level fips codes 
fips = {"AL": "01",
"AK": "02",
"AR": "05",
"AZ": "04",
"CA": "06",
"CO": "08",
"CT": "09",
"DE": 10,
"FL": 12,
"GA": 13,
"HI": 15,
"IA": 19,
"ID": 16,
"IL": 17,
"IN": 18,
"KS": 20,
"KY": 21,
"LA": 22,
"MA": 25,
"MD": 24,
"ME": 23,
"MI": 26,
"MN": 27,
"MO": 29,
"MS": 28,
"MT": 30,
"NC": 37,
"ND": 38,
"NE": 31,
"NH": 33,
"NJ": 34,
"NM": 35,
"NV": 32,
"NY": 36,
"OH": 39,
"OK": 40,
"OR": 41,
"PA": 42,
"RI": 44,
"SC": 45,
"SD": 46,
"TN": 47,
"TX": 48,
"UT": 49,
"VA": 51,
"VT": 50,
"WA": 53,
"WI": 55,
"WV": 54,
"WY": 56}

state = input("What state would you like to map?\n")

#adding check to make sure the user puts in a string
while type(state) != str:
    state = input("What state would you like to map?\n")

#converting user state choice to all uppercase
state = state.upper()

#checking that the state they entered was a state that can be mapped
list_check_state = T_F_Functions.index_check(US_states, state)

#if the list_check_state comes back false, prompt user to enter another state
while list_check_state == False:
    print("The state you selected is not able to be mapped. Please select another")
    state = input("What state would you like to map?\n")
    state = state.upper()
    list_check_state = T_F_Functions.index_check(US_states, state)

#variables that can be mapped
variables = ["poverty rate", "people with bachelors degrees", "percent black/african American", 
             "income", "women", "men", "median income", "speaks spanish at home", "percent hispanic or latino",
             "percent covered by health insurance"]



#printing available variables for the user
print("You can pick any of these variables \n")

print(variables)

print("and this program will print a map of your chosen state at the county level.\n"
      + "Please enter the variable exactly as written.")

#asking user for
variable = input("What variable would you like mapped?\n")

#checking to make sure the input the user gave was a string
while type(variable) != str:
    variable = input("What variable would you like mapped?\n")

variable = variable.lower()

#checking the variable they put in was in the lsit
list_check_variable = T_F_Functions.index_check(variables, variable)

#if the variable they entered was not in the list prompt for another entry
while list_check_variable == False:
    print("The variable you selected is not available to be mapped. Please type in your choice again.")
    user_input = input("Do you need to see the choices again? Y for yes, N for no.")
    if user_input == "Y" or user_input == "y":
        print(variables)
    variable = input("What variable would you like mapped?\n")
    variable = variable.lower()
    list_check_variable = T_F_Functions.index_check(variables, variable)

#pulling shapefiles for state chosen and creating the string that will read it in
tract_string = tracts[state]
state_fips = fips[state]

api_ky = Census("") #<<<< this is where your census API key would go


state_census = api_ky.acs5.state_county_tract(fields = ('NAME','B06010_006E','B06010_005E', 'C17002_001E', 'B02001_003E',
                                                        'C17002_002E', 'C17002_003E', 'C15010_001E', 'B01003_001E', 'B06010_001E',
                                                        'B06010_004E', 'B06010_007E', 'B06010_008E', 'B06010_009E', 'B06010_010E', 
                                                        'B06010_002E', 'B06010_003E', 'B01001_026E', 'B01001_002E', 'B19013_001E',
                                                        'B19019_001E', 'B19025_001E', 'C16001_003E', 'B01001I_001E', 'B27001_001E'),
                                       state_fips = state_fips,
                                       county_fips = "*",
                                       tract = "*",
                                       year = 2017)

#create data frame from state census and create string for shapefile
state_df = pd.DataFrame(state_census)

shapefile = ("https://www2.census.gov/geo/tiger/TIGER2019/TRACT/" + tract_string)

#read in shapefile
user_state = gpd.read_file(shapefile)

#create variable to join shapefile and dataframe
state_df["GEOID"] = state_df["state"] + state_df["county"] + state_df["tract"]

#merging the data
state_merge = user_state.merge(state_df, on = "GEOID")

#create a new dataframe to select from columns and show dataframe
state_variable_tract = state_merge[["STATEFP", "COUNTYFP", "TRACTCE", "GEOID", "geometry", 
                                   "B06010_006E","B06010_005E", "B02001_003E", "C17002_001E", 
                                   "C17002_002E", "C17002_003E", "C15010_001E", "B01003_001E",
                                   "B06010_001E", "B06010_004E", "B06010_007E", "B06010_008E",
                                    "B06010_009E", "B06010_010E", "B06010_002E", "B06010_003E", 
                                    "B01001_026E", "B01001_002E", "B19013_001E", "B19019_001E",
                                    "B19025_001E", "C16001_003E", "B01001I_001E", "B27001_001E"]]

#dissolving the tracts within each county and adding the values together
state_county = state_variable_tract.dissolve(by = 'COUNTYFP', aggfunc = 'sum')

#getting poverty rate by dividing income raios and total population 
state_county["poverty rate"] = (state_county["C17002_002E"] + state_county["C17002_003E"] / state_county["B01003_001E"] * 100)
state_county["people with bachelors degrees"] = (state_county["C15010_001E"] / state_county["B01003_001E"] * 100)
state_county["percent black/african American"] = (state_county["B02001_003E"] / state_county["B01003_001E"] * 100)
state_county["income"] = (state_county["B06010_004E"] + state_county["B06010_005E"] + state_county["B06010_006E"] + state_county["B06010_007E"] + 
                          state_county["B06010_008E"] + state_county["B06010_009E"] + state_county["B06010_010E"] + state_county["B06010_010E"] +
                          state_county["B06010_002E"] / state_county["B01003_001E"] * 100)# state_county["B06010_003E"])
state_county["women"] = (state_county["B01001_026E"] / state_county["B01003_001E"] * 100)
state_county["men"] = (state_county["B01001_002E"] / state_county["B01003_001E"] * 100)
state_county["median income"] = (state_county["B19025_001E"] / state_county["B01003_001E"])
state_county["speaks spanish at home"] = (state_county["C16001_003E"] / state_county["B01003_001E"] * 100)
state_county["percent hispanic or latino"] = (state_county["B01001I_001E"] / state_county["B01003_001E"] * 100)
state_county["percent covered by health insurance"] = (state_county["B27001_001E"] / state_county["B01003_001E"] * 100)


#creating dictionary out of the values for the chosen variable
variable_dict = dict(state_county[variable])

#getting the min and max values for the variable and turning it into a string to use later
min_variable_value = min(variable_dict, key = variable_dict.get)
max_variable_value = max(variable_dict, key = variable_dict.get)
min_string = "the fips code for the county with the lowest value of the variable you've chosen is: " + str(fips[state]) + str(min_variable_value)
max_string = "the fips code for the county with the highest value of the variable you've chosen is: " + str(fips[state]) + str(max_variable_value)


#create subplots
fig, ax = plt.subplots(1, 1, figsize = (20, 10))

#plot data

state_county.plot(column = variable, 
                    ax = ax,
                    cmap = "YlGn",
                    legend = True,
                    scheme = 'NaturalBreaks')



#stylize plots
plt.style.use('bmh')

#title
ax.set_title(variable + " in " + state, fontdict = {'fontsize': '25', 'fontweight' : '3'})

#create string to add to the plot to show best and worst areas
txt = min_string + ", and " + max_string + "."
plt.figtext(0.5, 0.001, txt, wrap = True, horizontalalignment = 'center', fontsize = 12)

plt.show()