import enquiries

options = ['Do Something 1', 'Do Something 2', 'Do Something 3']
choice = enquiries.choose('Choose one of these options: ', options)

print(choice)


# 警告(Warning)
warning = '*' * 30 + '\n'
warning += '*{:^28}*\n'.format('Warning')
warning += '*' * 30 + '\n'
colored_warning = termcolor.colored(warning, 'red')