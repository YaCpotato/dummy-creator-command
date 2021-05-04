import base
import random

# command line value
import argparse

# cli color
import termcolor

# cli selector and select definition
import enquiries
ua_create_categorical = termcolor.colored('Add categorical column: ', 'green')
ua_create_numeric = termcolor.colored('Add numeric column: ', 'green')
ua_publish = 'Complete creation and publish data.'
ua_exit = 'Stop creating data and EXIT'
actions = [ua_create_categorical, ua_create_numeric, ua_publish, ua_exit]

guide_1 = termcolor.colored('Enter length of dataframe: ', 'green')
guide_2 = termcolor.colored('Enter the column name: ', 'green')
guide_3 = termcolor.colored('Enter the list of value separated by spaces: ', 'green')
guide_4 = termcolor.colored('Enter the percentages of the values you entered in the same order separated by spaces: ', 'green')

retry = termcolor.colored('must be a number. please retry.', 'red')

if __name__ == '__main__':
    
    df = base.DummyFrame()
    
    parser = argparse.ArgumentParser()
    #parser.add_argument("pass", help = "the yaml file you use here", type = str)
    parser.add_argument("-i","--index", help = "dataframe's index", type = str, default='cs')
    args = parser.parse_args()
    
    if args.index == 'ts':
        print('Create time series data.')
    elif args.index == 'cs':
        print('Create cross section data.')
    else:
        pass 
    
    try:
        length = int(input(guide_1))
    except:
        print(retry)
        length = int(input(guide_1))
    
    col_name = input(guide_2)
    values = input(guide_3).split(' ')
    values_percentage = [int(n) for n in input(guide_4).split(' ')]
    
    a = random.choices(population = values, weights = values_percentage, k = length)
    
    user_action = enquiries.choose('Choose Action: ', actions)
    
    if user_action == ua_create_categorical:
        print(ua_create_categorical)
    elif user_action == ua_create_numeric:
        print(ua_create_numeric)
    elif user_action == ua_publish:
        print(ua_publish)
    elif user_action == ua_exit:
        print(ua_exit)
    else:
        print('OOOOOO')
    
    
    
    