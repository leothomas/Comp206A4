#!/usr/bin/perl
use CGI;
use strict;
use warnings;

#print "Content-type:text/html\r\n\r\n";
#variables assigned values base on user input
my $point = CGI->new;
my $name = $point->param('name');
my $username = $point->param('username');
#removes carriage return from $username
chomp $username;
my $password = $point->param('password');
my $filename = 'members.csv';

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
			print "<body\n>";		
			print "<P>The username you entered already exists</P>\n";
            print '<a href="http://cs.mcgill.ca/~lthoma13/becomeMember.html"><center><font color="White">try again fool</font></center></a>\n';
			print "</body>\n";
			print "</html\n>";
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
        #adds basic info to user in members.csv
        print $fw "\n$name $username $password";
        print "Content-type: text/html\r\n\r\n";
                        print "<html>\n";
            print "<body>\n";       
            print "<P>Congrats bro-you didnt fuck it up</P>\n";
            print '<a href="http://cs.mcgill.ca/~lthoma13/becomeMember.html"><center><font color="White">try again fool</font></center></a>\n';
            print "</body>\n";
            print "</html>\n";
        close $fw;
}
exit 0;
