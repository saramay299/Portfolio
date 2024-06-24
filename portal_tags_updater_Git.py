#importing packages
import arcgis
from arcgis.gis import GIS
import getpass
import pandas as pd
from datetime import datetime
import csv


#create function that logs into portal
def gis_login():
    #getting username and password
    print('please enter your username.')
    username = input()
    print('please enter your password')
    password = getpass.getpass()

    #plugging in credentials
    gis = GIS('***ESRI link here***', username, password)
    return gis

#create a function that searches in portal
def content_search(gis):
    print("this program helps update portal tags. Please input a search term for the item you want to update tags for. Ex. 'title:Ports along US West Coast'")
    print("leaving this empty will mean the query searches for everything in portal")
    
    #ask user for input
    query_string = input()
    
    #search query string and get list
    content_list = gis.content.search(query_string)
    print("your search query returned " + str(len(content_list)) + " items.")
    
    #create empty dictionary to use for item review
    item_review = {}
    
    #create item num for dictionary assignment
    item_num = 1
    
    #for each item in the content list 
    for i in content_list:
        
        #add item to dictionary
        item_review[item_num] = i
        
        #plus one to the item counter
        item_num += 1
    
    for x in item_review:
        print(str(x) + ': ' + str(item_review[x]))

    return content_list

#content_list = content_search()

def remove_content_search(content_list):
     
    #create empty dictionary to use for item review
    item_review = {}
    
    #create item num for dictionary assignment
    item_num = 1
    
    #for each item in the content list 
    for i in content_list:
        
        #add item to dictionary
        item_review[item_num] = i
        
        #plus one to the item counter
        item_num += 1
    
    for x in item_review:
        print(str(x) + ': ' + str(item_review[x]))

    print('what items would you like to remove?')
    print('please input your answer as numbers seperated witha space and a comma')
    print('ex. 1, 2, 3')
    numbers = input()

    #split string by comma, makes the input a list
    numbers = numbers.replace(" ", "")
    numbers = numbers.split(',')
        
    for i in numbers:
        del item_review[int(i)]
        
    #return new dictionary and ask if there is anything else they'd like to remove
    print('this is what you have after removing items')
    for x in item_review:
        print(str(x) + ': ' + str(item_review[x]))
        
    content_list = []
    
    for x in item_review:
        content_list.append(item_review[x])
    return content_list
      

def add_tags():
    
    #create empty list to add tags to
    tags_to_add = []
    
    #ask them what tags they want to to add
    print('you have chosen to add tags')
    print('what tag would you like to add?')
    tag_to_add = input()
    tags_to_add.append(tag_to_add)
    
    print('do you still have tags you want to add? y or n')
    more_tags = input()
    more_tags = more_tags.lower()

    answers = ['y', 'n']
    
    while more_tags not in answers:
        print('what you entered was not an acceptable response')
        print('please try again. y or n.')
        more_tags = input()
    
    while more_tags == 'y':
        
        #ask what other tag they would like to add
        print('What tag would you like to add?')
        tag_to_add = input()
        tags_to_add.append(tag_to_add)

        #show them what tags they have so far and ask if there are more
        print('so far you want to add: ')
        print(tags_to_add)
        print('do you want to add more tags? y or n')
        more_tags = input()
        more_tags = more_tags.lower()

    return tags_to_add

def update_tags():
    
    print('You have chosen to update tags. This option will add all the same tags to all of the content you have listed')
    print('please know that any tags that currently exist on these items will be removed')
    print("do you have a tag you'd like to add? y or n")
    
    #ask reader if they want to add a tag and create variable for answer
    add_tag = input()
    add_tag = add_tag.lower()
    
    #create empty empty to add tags to 
    tags_list = []
    
    answers = ['y', 'n']
    
    while add_tag not in answers:
        print('what you entered was not an acceptable response')
        print('please try again. y or n.')
        add_tag = input()
    
    #while add tag answer is y get tags 
    while add_tag == 'y':
        print('what tag would you like to add?')
        tag_to_add = input()
        tag_to_add = str(tag_to_add)
        tags_list.append(tag_to_add)
        
        #have user review tags
        print('so far you have: ')
        print(tags_list)
        
        #ask user if they want to add more tags
        print('do you want to add another tag? y or n')
        print('if not the list you currently have will be added to the content you searched for earlier')
        
        add_tag = input()
        
        while add_tag not in answers:
            print('what you entered was not an acceptable response')
            print('please try again. y or n.')
            add_tag = input()

    
    return tags_list
	

def main():

    gis = gis_login()
    #gathering content from portal section===============================
    #call first content search
    content = content_search(gis)
    
    #create iterator for while loop
    print('you will have the chance to remove items later but for now...')
    print('do you want to add content to your initial search? y or n')
    continue_loop = input()
    continue_loop = continue_loop.lower()
    
    #if statements for content_add
    while continue_loop == 'y':
        
        additional_content = content_search()
        for item in additional_content:
            content.append(item)
        print(content)
        print('is there anything else you would like to add to this list? y or n')
        continue_loop = input()
        continue_loop = continue_loop.lower()
        
    remove_response = input()
    remove_response = remove_response.lower()
    
    while remove_response == 'y':
        content = remove_content_search(content)
        print('do you want to remove anything else? y or n')
        remove_response = input()
    
    print('your final list is of portal content to alter is: ')
    for i in content:
        print(i)
    #gathering content from portal section===============================
    #updating tags section===============================================
    print('do you want to add tags to the existing tags on your items or update all the tags with a fresh list? enter add or update')
    
    add_update_response = input()
    add_update_response = add_update_response.lower()
    
    if add_update_response == 'add':
        tags_list = add_tags()
        
        #grab loop for portal items and tags for each item
        for item in content:
            item_tags = item.tags

            #for each tag they want added add to item tags list
            for tag in tags_list:
                item_tags.append(tag)
            
            #print statement for user
            print('please be patient while we add your tags... *plays jeopardy music*')
            #update portal item with new tags list
            item.update(item_properties = {'tags':item_tags})

    elif add_update_response == 'update':
        new_tags = update_tags()
        
        #print statement for user
        print('please be patient while we add your tags... *plays jeopardy music*')
        
        #grab loop for portal items and tags for each item
        for item in content:
            item.update(item_properties = {'tags':new_tags})      
    
    print('here are your portal objects and their new tags.')
    for i in content:
        print(i)
        print(i.tags)
    return


main()
