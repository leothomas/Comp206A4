#!/usr/bin/python
import sys
import os
import stat
#to use stdin, uncomment below
#from sys import sdtin 

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
