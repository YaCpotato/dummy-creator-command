import argparse
import termcolor
import base
import random

# 警告(Warning)
warning = '*' * 30 + '\n'
warning += '*{:^28}*\n'.format('Warning')
warning += '*' * 30 + '\n'
colored_warning = termcolor.colored(warning, 'red')

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
    
    
    
    