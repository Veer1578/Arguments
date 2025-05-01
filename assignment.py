def close(s):
    if s == 'yes':
        return 'shutdown'
    elif s == 'no':
        return  'shutdown aborted' 
    else:
        return 'Sorry'
    

choice = input('Do you want to shutdown?')
print(close(choice))