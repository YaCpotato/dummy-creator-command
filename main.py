import random
import os
import pandas as pd

# command line value
import argparse

# cli color
import termcolor

# cli selector and select definition
import enquiries
ua_create_categorical = termcolor.colored('Add categorical column: ', 'green')
ua_create_numeric = termcolor.colored('Add numeric column: ', 'green')
ua_preview = termcolor.colored('Preview dataframe head: ', 'green')
ua_publish = 'Complete creation and publish data.'
ua_exit = termcolor.colored('Stop creating data and EXIT', 'yellow')
actions = [ua_create_categorical, ua_create_numeric, ua_preview, ua_publish, ua_exit]

# cli navigation beginning
guide_1 = termcolor.colored('Enter length of dataframe: ', 'green')

# cli navigation add column
guide_2 = termcolor.colored('Enter the column name: ', 'green')
guide_3 = termcolor.colored('Enter the list of value separated by spaces: ', 'green')
guide_4 = termcolor.colored('Enter the percentages of the values you entered in the same order separated by spaces: ', 'green')

retry = termcolor.colored('must be a number. please retry.', 'red')

df = pd.DataFrame(index=[], columns=[])

def do_action():
    global df
    # choose action
    user_action = enquiries.choose('Choose Action: ', actions)
    
    # if publish or exit
    if user_action == ua_publish:
        df.to_csv('')
        exit()
    elif user_action == ua_exit:
        exit()
    elif user_action == ua_preview:
        print(df.transpose().head())
        do_action()
    # if create column...

    # define column name
    col_name = input(guide_2)
        
    if user_action == ua_create_categorical:
        values = input(guide_3).split(' ')
        values_percentage = [int(n) for n in input(guide_4).split(' ')]
        series = create_categorical(col_name, values, values_percentage)
        print(type(series))
        print(series)
        df = df.append(series, ignore_index = True)
        print('column added.')
    elif user_action == ua_create_numeric:
        print('this selection not supported yet.')
    
    do_action()


def create_categorical(col_name, values, values_percentage):
    # if first columns, normal create
    series_value = random.choices(population = values, weights = values_percentage, k = length)
    column = pd.Series(series_value, name = col_name, dtype='str')
    return column

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # #parser.add_argument("pass", help = "the yaml file you use here", type = str)
    # parser.add_argument("-i","--index", help = "dataframe's index", type = str, default='cs')
    # args = parser.parse_args()
    
    # if args.index == 'ts':
    #     print('Create time series data.')
    # elif args.index == 'cs':
    #     print('Create cross section data.')
    # else:
    #     pass 
    
    # define dataframe length
    try:
        length = int(input(guide_1))
    except:
        print(retry)
        length = int(input(guide_1))
    
    do_action()
    
    
    
    