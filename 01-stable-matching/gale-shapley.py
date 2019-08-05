# My implementation of the Gale-Shapley Algorithm
# for the "Dating Problem"

import numpy as np
import pandas as pd

# initalise each person
men = ['Xavier', 'Yancey', 'Zeus']
women = ['Amy', 'Bertha', 'Clare']

# initialise favrouite dataframes
data = {
    '1st':['Amy', 'Bertha', 'Amy'],
    '2nd':['Bertha', 'Amy', 'Bertha'],
    '3rd':['Clare', 'Clare', 'Clare']
}
men_pref_df = pd.DataFrame(data, index=men)

data = {
    '1st':['Yancey', 'Xavier', 'Xavier'],
    '2nd':['Xavier', 'Yancey', 'Yancey'],
    '3rd':['Xavier', 'Yancey', 'Zeus']
}
women_pref_df = pd.DataFrame(data, index=women)


# Gale-Shapley algorithm begins here!

# Thinking for workflow: 
    # move over to a Jupyter notebook,
    # put gale-shapley file in this file,
    # import the file into the jupyter notebook
    # make code as reusable as possible!!

# initalise everyone to be single
match_df = pd.DataFrame(data=None, columns = ['Partner'], index=men)



# print the data frames
print('Men\'s preferences:', men_pref_df, '\nWomen\'s preferences:', women_pref_df, sep='\n')


print(match_df)