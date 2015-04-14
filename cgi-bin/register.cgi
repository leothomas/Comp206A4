#!/usr/bin/perl
use CGI;
use strict;
use warnings;

#print "Content-type:text/html\r\n\r\n";
#variables assigned values base on user input
my $point = CGI->new;
my $name = $point->param('name');
my $username = $point->param('username');
my $password = $point->param('password');
my $confpassword = $point->param('confpassword');
my $filename = 'members.csv';

#to check for no spaces
my $includesSpace = 0;
my $empty = 0;
my $passMatch = 0;

if ($name =~ /\s/) {
	$includesSpace = 1;
}
elsif ($username =~ /\s/) {
	$includesSpace = 1;
}
elsif ($password =~/\s/) {
	$includesSpace = 1;
}
#check if input is empty
if ($name eq "") {
    $empty = 1;
}
elsif ($username eq "") {
    $empty = 1;
}
elsif ($password eq "") {
    $empty = 1;
}
if ($confpassword eq ""){
    $empty =1;
}
#check that passwords match
if($password ne $confpassword){
    $passMatch =1;
}
#error screen if input is empty
if($empty ==1){
    print "Content-type: text/html\r\n\r\n";
    print "<html>\n";
    print "<head><title>Error</title></head>\n";
    print "<body background = \"http://www.878bar.com.ar/img/fotos/09.jpg\">\n";       
    print "<p><b><font color=\"White\" size=20><center> Error: one or more fields was left empty <br></center></font></b></p>\n";
    print "<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Back to registration page</font></center></a>\n";
    print "</body>\n";
    print "</html>\n";
    exit 0;
}

# print error if a space is found in input
elsif($includesSpace == 1) {
	print "Content-type: text/html\r\n\r\n";
    print "<html>\n";
    print "<head><title>Error</title></head>\n";
    print "<body background = \"http://www.878bar.com.ar/img/fotos/09.jpg\">\n";       
    print "<p><b><font color=\"White\" size=20><center> Error: please avoid using spaces <br>in your registration info </center></font></b></p>\n";
    print "<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Back to registration page</font></center></a>\n";
    print "</body>\n";
    print "</html>\n";
	exit 0;
}
#print error if passwords down match
elsif ($passMatch ==1){
    print "Content-type: text/html\r\n\r\n";
    print "<html>\n";
    print "<head><title>Error</title></head>\n";
    print "<body background = \"http://www.878bar.com.ar/img/fotos/09.jpg\">\n";       
    print "<p><b><font color=\"White\" size=20><center> Error: entered passwords do not match <br></center></font></b></p>\n";
    print "<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Back to registration page</font></center></a>\n";
    print "</body>\n";
    print "</html>\n";
    exit 0;
}


#open members.csv file to check pre-existing users
open (my $fh, "<", $filename)
       or die "Can't open $filename: $!";

#intialize boolean used to break loop
my $boolean = 0;

#loops to find existing users
while (my $row = <$fh>) {

       #splits database info line by line, sparating different people
       my @dataBase = split("\n",$row);

       #for each line we separate each value (name, username, password, etc)
       foreach my $val (@dataBase) {
                my @parsedInfo = split(' ',$val);

                #compare username entered with all usernames
                #checks if username already exists
                if($parsedInfo[1] eq $username) {
                    print "Content-type: text/html\r\n\r\n";
                    print "<html>\n";
                    print "<head><title>Error</title></head>\n";
                    print "<body background = \"http://www.878bar.com.ar/img/fotos/09.jpg\">\n";       
                    print "<p><b><font color=\"White\" size=20><center> The username you requested <br>already exists </center></font></b></p>\n";
                    print "<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Back to registration page</font></center></a>\n";
                    print "</body>\n";
                    print "</html>\n";
                    $boolean = 1;
        			exit 0;
                }
        }
        #exits while loop if username already exists
        if($boolean == 1){
                last;
        }
}
close $fh;

#if username doesn't exist, append to members.csv file
if($boolean == 0){

    #append to file function
    open(my $fw, ">>", $filename) or die "Could not open the file $filename: $!";
    #adds basic info to user in members.csv including user as her/her own friend so they can see their
    # messages. 
    print $fw "\n$name $username $password $username";
    print "Content-type: text/html\r\n\r\n";
    print "<html>\n";
    print "<head><title>Error</title></head>\n";
    print "<body background = \"http://www.878bar.com.ar/img/fotos/09.jpg\">\n";       
    print "<p><b><font color=\"White\" size=20><center> Registration succesful! <br >Welcome to MontrealBarBook </center></font></b></p>\n";
    print "<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/welcome.html\"><center><font color=\"White\">Back to login </font></center></a>\n";
    print "</body>\n";
    print "</html>\n";
    exit 0;
        close $fw;
}
exit 0;
