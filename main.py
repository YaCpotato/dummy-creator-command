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

categorical_df = termcolor.colored('Categorical', 'green')
timeseries_df = termcolor.colored('TimeSeries', 'green')
tscs_selection = [categorical_df, timeseries_df]

# cli navigation beginning
guide_1 = termcolor.colored('Enter length of dataframe: ', 'green')
guide_b1 = termcolor.colored('Enter index name of dataframe: ', 'green')
# cli navigation add column
guide_2 = termcolor.colored('Enter the column name: ', 'green')
guide_3 = termcolor.colored('Enter the list of value separated by spaces: ', 'green')
guide_4 = termcolor.colored('Enter the percentages of the values you entered in the same order separated by spaces: ', 'green')

# message case of unexpected
retry = termcolor.colored('must be a number. please retry.', 'red')

df = pd.DataFrame(index=[], columns=[])

def define_index():
    global df
    name = input(guide_b1)
    cs_or_ts = enquiries.choose('Choose Index Type (Categorical or Time) : ', tscs_selection)
    
    if cs_or_ts == timeseries_df:
        # not supported
        return
        range_q = input('Please Enter begin and end date separated by spaces :').split(' ')
        range_index = pd.date_range(range_q[0], range_q[1])
    elif cs_or_ts == categorical_df:
        df[name] = range(0,length)
        df = df.set_index(name)

def do_action():
    global df
    # choose action
    user_action = enquiries.choose('Choose Action: ', actions)
    
    # if publish or exit
    if user_action == ua_publish:
        name = input('Save as.. :')
        if name[-4:] != '.csv':
            name = name + '.csv'
        df.to_csv(name)
        exit()
    elif user_action == ua_exit:
        exit()
    elif user_action == ua_preview:
        print(df.head())
        do_action()
    # if create column...

    # define column name
    col_name = input(guide_2)
        
    if user_action == ua_create_categorical:
        make_relation = input('Do you want to make relationships with other columns? yes or no (no)')
        if make_relation == 'yes':
            create_relation()
        else:
            values = input(guide_3).split(' ')
            values_percentage = [int(n) for n in input(guide_4).split(' ')]
            df[col_name] = random.choices(population = values, weights = values_percentage, k = length)
    elif user_action == ua_create_numeric:
        print('this selection not supported yet.')
    
    do_action()

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
    
    define_index()
    do_action()
    
    
    
    