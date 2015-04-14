#!/usr/bin/python
import sys
import os
import stat
#to use stdin, uncomment below
#from sys import sdtin 

def ListMembers():
    try:
	#opens members.csv in read setting
	read = open("members.csv", "r")
	#members contains a list of strings, each string is a line of members.csv
	members = read.readlines()
	#loops for each line in members.csv
	for current in range(len(members)):
	    #each line in members.csv is parsed by spaces and each entry is given an index
	    for idx, val in enumerate(members[current].split()):
		#the index 1 is always going to be the username
		if idx == 1:
		    #print the user name on the webpage
		    print val
    #catches errors, most likely from opening the file
    except:
	print "Something fucked up"
    #close the rile reader
    read.close()
#run the method
ListMembers()

def AddFriend():
    try:
	#the user will be the hidden tag that contains the user that logged in
	#This code assumes the user name was passed correctly, and is valid
	user = "leo1"
	#friend will contain what is entered into the searcf for friends button
	friend = "zac1"
	#trueUser is a boolean that tells in the entered friend name is a valid user
	trueUser = 1
	with open("members.csv", "r") as src:
	    #members is a list, each string contains one line of the file
	    members = src.readlines()
	    #this loop will run, the same number of times as there are lines in the file
	    for current in range(len(members)):
		#this loop is to break each line up by spaces and index each string
		for idx,val in enumerate(members[current].split()):
		    #if the username index (which is always 1) matches the entered friend name
		    if idx ==1 and val == friend:
			#print "you can add this user"
			#set trueUser to true ie. the friend name entered is valid
			trueUser = 0
	#close the file in the read setting
	src.close()

	#this if loop adds the new friend to the user's data
	if trueUser == 0:
	    with open("members.csv", "r") as src:
		data = src.readlines()
		#this series of loops is the same as above
		#but returns the line index corresponding to the user who made the request
		for current in range(len(data)):
		    for idx, val in enumerate(data[current].split()):
			if idx == 1 and val == user:
			    infoLine = current
		#this will create a new string for the index which the user is found
		data[infoLine] = data[infoLine].rstrip()+" "+friend+"\n"
		#new data contains all the member.csv information plus the user's new friend
		newData = data
	    #close the file in read setting
	    src.close()
	    #this overwrites the entire member.csv file to include the new friend
	    with open("members.csv", "wb") as src:
		src.writelines(newData)
	    #close file in override write setting
	    src.close()

	#if the friend name entered does not exist, this loop enters
	if trueUser == 1:
	    #html error code here
	    #print "you can't add that user as a friend
    except:
	#print "Something fucked up"
#runs the function
AddFriend()

def DisplayMessages(userName):
    try:
	#boolean to chekc for the valid user's line of information in members.csv
	usersInfo = 1
	friendsList = ""
	#open members.csv in read mode
	with open("members.csv","r") as src:
	    #members is a list with each line from members.csv at an index
	    members = src.readlines()
	    #count holds the number the user's info is found at
	    count = 0
	    #first for loop iterates through the number of lines in the file
	    for current in range(len(members)):
		#This breaks up each line into strings and indexes each one
		for idx, val in enumerate(members[current].split()):
		    #if the username matches the given one, return the line
		    if idx == 1 and val == user:
			userInfo = 0
			count = current
	    src.close()
	#if valid user information is found
	if usersInfo == 0:
	    #breaks up the user's information by spaces and indexes each entry
	    for index, value in enumerate(members[count].split()):
		#friends have indexes>2, these friend names are added to friendsList
		if index > 2:
		    friendsList=friendsList+value+" "
	#if no valid user information is found
	elif usersInfo == 1:
	    print "username is not in members.csv"
	#open the topics.csv which contains all the posts, in read 
	with open("topics.csv", "r") as src:
	    #messages contains each line of topics.csv in a list
	    messages = src.readlines()
	    #counter is used so that only 10 messages are printed
	    counter = 0
	    #pointer is used so that messages can include usernames
	    pointer = 0
	    #while not at the end of topics.csv file
	    while pointer<len(messages):
		#separate each friend in the users friends list
		for idx,val in enumerate(friendsList.split()):
		    #if the user who posted is on your friends list print their name and message
		    if val.strip() == messages[pointer].strip() and counter<10:
			print messages[pointer]
			print messages[pointer+1]
			counter = counter+1
		pointer=pointer+2
	    src.close()
    except:
	print "fuck"
DisplayMessages(username)

def WritePost():
    try:
	#userName and message are what the user enters into the textbox
	userName = "zac1"
	message = "new message text"
	packet = userName+"\n"+message+"\n"
	#open the file in read mode 
	with open("topics.csv", "r") as original:
	    #copy all the lines into a list
	    messageFile = original.read()
	    #add new messages to start of file
	    updatedMessages = packet + messageFile
	    original.close()
	#open file is override write mode
	with open("topics.csv", "w") as modified:
	    #rewrite file with new messages
	    modified.write(updatedMessages)
	    modified.close()
    except:
	print "You fucked up!"
WritePost()

