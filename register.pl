#!/zwarne/public_html/tests/perl
use CGI;
use strict;
use warnings;

#variables assigned values base on user input
my $name = 'Zac';
my $username = <>;
#removes carriage return from $username
chomp $username;
my $password = 'qwerty';
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
                        print "The username you entered already exists\n";
                        $boolean = 1;
                }
        }
        #exits while loop if username already exists
        if($boolean == 1){
                last;
        }
}

#if username doesn't exist, append to members.csv file
if($boolean == 0){

        #append to file function
        open(my $fw, ">>", $filename) or die "Could not open the file $filename: $!";
        #adds basic info to user in members.csv
        print $fw "\n$name $username $password";
        close $fw;
}
