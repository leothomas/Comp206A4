#!/usr/bin/python
import os
import stat 
import cgi
import cgitb
cgitb.enable()
from sys import stdin

print '''Content-Type: text/html\n\n
<html>
<head><title> Feed </title></head>
<body>
<body background = \"http://barraca.ca/wp-content/uploads/2011/12/Barraca-Bar-Plateau-Montreal-05.jpg\"> 
<font color=\"White\"><h1><center> MontrealBarBook</h1></center></font>
<table width=\"100%\" border=\"1\" cellspacing = \"6\">
<tr> <td valign = \"top\" align = \"middle\" width= \"25%\">'''
form = cgi.FieldStorage()
print "<font color= \"White\" size= \"6\">Logged in as: <b>", form["username"].value
print '''</b></font></td>
<td valign = \"bottom\" align = \"middle\" width= \"50%\" >
<form name= \"statusUpdate\" action = \"http://cgi.cs.mcgill.ca/~lthoma13/Comp206A4/cgi-bin/testpython.py\" method = \"POST\">
<textarea name = \"status\" cols= \"60\" rows = \"6\" placeholder=\"Whats on your mind? (max 300 characters)\" maxlength = "300"></textarea><br />
<center><input type= \"submit\" value = \"Submit\"></center></td>
<td valign = \"top\" width= \"50%\" ><a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/welcome.html\"><center><font color=\"White\" ><h2><b>Logout</b></h2></font></center></a>
</td></tr> </table><br>'''

read = open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r")
def ListMembers(read):
    try:
	#opens members.csv in read setting
	#read = open("http://cgi.cs.mcgill.ca/~lthoma13/Comp206A4/cgi-bin/members.csv", "r")
	#members contains a list of strings, each string is a line of members.csv
	members = read.readlines()
	#loops for each line in members.csv
	for current in range(len(members)):
	    #each line in members.csv is parsed by spaces and each entry is given an index
	    for idx, val in enumerate(members[current].split()):
		#the index 1 is always going to be the username
		if idx == 1:
		    #print the user name on the webpage
		    print "<font size = \"4\"><center>"
		    print val
		    print "<br></center></font>"
    #catches errors, most likely from opening the file
    except:
	print "Something fucked up"
    #close the rile reader
    read.close()

def AddFriend():
    try:
	#the user will be the hidden tag that contains the user that logged in
	#This code assumes the user name was passed correctly, and is valid
	user = form["username"].value
	#friend will contain what is entered into the searcf for friends button
	friend = form["friendToAdd"].value
	#trueUser is a boolean that tells in the entered friend name is a valid user
	trueUser = 1
	with open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r") as src:
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
	    with open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r") as src:
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
	    with open("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "wb") as src:
		src.writelines(newData)
	    #close file in override write setting
	    src.close()

	#if the friend name entered does not exist, this loop enters
	if trueUser == 1:
	    #html error code here
	    #print "you can't add that user as a friend
    except:
	    print "<b>Something fucked up</b>"

print '''<table width=\"100%\" border=\"1\" cellspacing = \"6\"><tr>
<td width = \"75%\"> <font color=\"White\" size = \"4\"><center><b>Messages from your friends:</b></center></font></td>
<td width = \"25%\"> <font color=\"White\"size = \"4\"> <center><b>Users:</b> (your friends appear in <font color = \"Red\"><b> red </b></font> )</center></font></td>
</tr>'''
print "<tr><td width = \"75%\"bgcolor = \"#D8D8D8\">"
print "</td>"
print"<td width = \"25%\" bgcolor = \"#D8D8D8\">"
ListMembers(read);
print ''' <br><form name = "addFriend" action = \"http://cgi.cs.mcgill.ca/~lthoma13/Comp206A4/cgi-bin/testpython.py\" method = "POST">
 <font color = \"Black\" size = \"5\"><center><b>Add a friend</b></center></font>
<center><input type = "text" name = "friendToAdd" placeholder = "Type in another user" autocomplete ="off" maxlength = \"15\"></center>'''
print "<input type = \"hidden\" name = \"username\" value = ", form["username"].value 
print "<center><input type = \"submit\" value = \"Submit\"></center></td>"
print "</tr>"
print "</table>"
print "</body>"
print "</html>"

