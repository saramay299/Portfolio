'''
Sara Maholland
CS5001
True/False functions for final project
'''

def index_check(my_list, value):
    '''
    function that tests if a value is in a list
    parameters: list to check and value to check for
    '''
    #if type my_list is not a list raise type error
    if type(my_list) != list:
        raise TypeError("my_list must be type list")
    #go into T or F statements
    if value in my_list:
        return True
    else:
        return False

def dict_check(my_dict, key):
    '''
    function that tests if a key exists in a dictionary
    parametersL the dictionary and the key to test for
    '''
    #if the my_dict variable is not a dictionary, raise an error
    if type(my_dict) != dict:
        raise TypeError("my_dict must be type dictionary")
    #go into T or F statements
    if my_dict.get(key) == None:
        return False
    else:
        return True


def main():
    pass

main()