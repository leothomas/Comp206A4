#!/usr/bin/python
import os
import stat 
import cgi
import cgitb
import sys
cgitb.enable()
from sys import stdin

print "Content-Type: text/html\n\n"
print "<html>"

form = cgi.FieldStorage()
user = form["username"].value 

def ListMembers():
    try:
		#opens members.csv in read setting
		#members contains a list of strings, each string is a line of members.csv
		read = open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r")
		members = read.readlines()
		#define an array of friends, to temporarily save friends
		user_friends = []
		#loops for each line in members.csv
		for current in range(len(members)):
		#this loop is to break each line up by spaces and index each string
			for idx,val in enumerate(members[current].split()):
				#if statement finds the line of data containting the current logged in user
				if idx == 1 and val == user:
					#loop iterates of elements of logged in user to append friends to user_friends
					for ind, value in enumerate (members[current].split(), start = 4):
						user_friends.append(value)
		
		for current in range(len(members)):
		    #each line in members.csv is parsed by spaces and each entry is given an index
			for idx, val in enumerate(members[current].split()):
			#the index 1 is always going to be the username
			#checks if the current user is in the temporary user_friends array	
				if idx == 1 and val in user_friends:
				    #print the user name on the webpage in red if it is a friend
					print "<font size = \"4\" color = \"Red\"><center><b>"
					print val
					print "</br></b></center></font>"
				elif idx == 1:
				    #print the user name on the webpage in black if it isn't a webpage.
					print "<font size = \"4\" ><center>"
					print val
					print "<br></center></font>"
	    #catches errors, most likely from opening the file
    except:
		print "Something fucked up"
    #close the file reader
    read.close()

def AddFriend(user, friend):
	try:
		#the user will be the hidden tag that contains the user that logged in
		#friend will contain what is entered into the searcf for friends button
		#trueUser is a boolean that tells in the entered friend name is a valid user
		trueUser = 1
		#already friend is a boolean tells is the enters friend name is already friends with the user
		alreadyFriend = 0
		#members is a list, each string contains one line of the file
		src = open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r") 
		members = src.readlines()
		#this loop will run, the same number of times as there are lines in the file
		for current in range(len(members)):
		#this loop is to break each line up by spaces and index each string
			for idx,val in enumerate(members[current].split()):
			    #if the username index (which is always 1) matches the entered friend name
			       if idx == 1 and val == friend:
					#set trueUser to true ie. the friend name entered is valid
					trueUser = 0
		#close the file in the read setting
		src.close()
		#this if loop adds the new friend to the user's data
		if trueUser == 0:
			src2 = open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r")
			data = src2.readlines()
			#this series of loops is the same as above
			#but returns the line index corresponding to the user who made the request
			for current in range(len(data)):
				for idx, val in enumerate(data[current].split()):
					if idx == 1 and val == user:
						infoLine = current
			#this will create a new string for the index which the user is found
			for idx, val in enumerate(data[infoLine].split()):
				# prevents from adding same friend twice. 
				if idx >3 and val==friend:
					alreadyFriend = 1
					print '''
					<head><title> Feed </title></head>
					<body>
		 			<font color = \"White\" size = \"5\"><center><b>You are already friends with <font color = \"Red\">'''
		 			print friend
		 			print "</b></center></font>"
					break
			# adds friend if the friend is not already a friend
 			if alreadyFriend == 0:
				data[infoLine] = data[infoLine].rstrip()+" "+friend+"\n"
				#new data contains all the member.csv information plus the user's new friend
				newData = data
		    	#close the file in read setting
				src2.close()
		    	#this overwrites the entire member.csv file to include the new friend
				src3 = open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "wb")
				src3.writelines(newData)
		    	#close file in override write setting
				src3.close()
				#if the friend name entered does not exist, this loop enters
				print "<font color=\"Red\" size = \"5\"><center> <b>"
				print friend 
				print " </font><font color = \"White\"size = \"5\">was added as a friend</b></center></font>"
		#catch if user doesn't exist
		elif trueUser == 1:
			print '''
			<head><title> Feed </title></head>
			<body>
 			<font color = \"Red\" size = \"5\"><center><b>User does not exist</b></center></font>'''
	except:
		print "<br><center><font color = \"Red\"><b>Something is wrong. We're working on it</font></b></center>"

#html scripting
print ''' 
	<head><title> Feed </title></head>
	<body background = \"http://barraca.ca/wp-content/uploads/2011/12/Barraca-Bar-Plateau-Montreal-05.jpg\"> 
	<font color=\"White\"><h1><center> MontrealBarBook</h1></center></font>'''

#creates friend variable if one was entered and passes it to the addfriend method
if "friendToAdd" in form:
	friend = cgi.escape(form["friendToAdd"].value)
	AddFriend(user, friend)
#creates table 
print '''<table width=\"100%\" border=\"1\" cellspacing = \"6\">
	<tr> <td valign = \"top\" align = \"middle\" width= \"25%\">
	<font color= \"White\" size= \"6\">Logged in as: <b>'''
#user greeting
print form["username"].value
#status update form
print '''</b></font></td>
	<td valign = \"bottom\" align = \"middle\" width= \"50%\" >
	<form name= \"statusUpdate\" action = \"http://cgi.cs.mcgill.ca/~lthoma13/Comp206A4/cgi-bin/testpython.py\" method = \"POST\">
	<textarea name = \"status\" cols= \"60\" rows = \"6\" placeholder=\"where are you going out tonight? (max 300 characters)\" maxlength = "300"></textarea><br />
	<center><input type= \"submit\" value = \"Submit\"></center></td>
	<td valign = \"top\" width= \"50%\" ><a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/welcome.html\"><center><font color=\"White\" ><h2><b>Logout</b></h2></font></center></a>
	</td></tr> </table><br>'''

print '''<table width=\"100%\" border=\"1\" cellspacing = \"6\"><tr>
	<td width = \"75%\"> <font color=\"White\" size = \"4\"><center><b>Messages from your friends:</br>'''

#if "statusUpdate" in form
#	message = cgi.escape(form["statusUpdate"].value)
#	PostMessage(user, message)

print '''</b></center></font></td>
	<td width = \"25%\"> <font color=\"White\"size = \"4\"> <center><b>Users:</b> (your friends appear in <font color = \"Red\"><b> red </b></font> )</center></font></td>	
	</tr>'''
print "<tr><td width = \"75%\"bgcolor = \"#D8D8D8\">"
print "</td>"
print"<td width = \"25%\" bgcolor = \"#D8D8D8\">"
ListMembers();
print ''' <br><center><form name = "addFriend" action = \"http://cgi.cs.mcgill.ca/~lthoma13/Comp206A4/cgi-bin/testpython.py\" method = "POST">
 <font color = \"Black\" size = \"5\"><center><b>Add a friend</b></center></font>
<center><input type = "text" name = "friendToAdd" placeholder = "Type in another user" autocomplete ="off" maxlength = \"15\"></center>'''
print "<input type = \"hidden\" name = \"username\" value = "
print form["username"].value 
print "><center><input type = \"submit\" value = \"Submit\"></center></td>"
print "</tr>"
print "</table>"
print "</body>"
print "</html>"

