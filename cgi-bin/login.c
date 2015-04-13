#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void){

  //Initializig strings for existing user/password combinations
  char exuser[20], expass[20];
  //Initializing pointers to the entered user/password
  char *user, *pass;
  //Initializing strings to store stdin and file input
  char temp[45], input[50];
  //Initializing and opening members.csv file
  FILE *members = fopen("/home/2015/lthoma13/public_html/Comp206A4/cgi-bin/members.csv", "r");
  //Initializing the pointer used to determine when EOF is reached
  char *check;

  //Scanning the std and assigning the second part to a string
  fscanf(stdin, "username=%s", input);

  //Splitting the rest of stdin to obtain separated strings for user/pass
  user = strtok(input, "&");
  strtok(NULL, "=");
  pass = strtok(NULL, "=");
  

  //Output to browser
  printf("Content-Type:text/html\n\n");
  printf("<html>");




  //Scanning he first line of the file member.csv
  fgets(temp,44,members);
  //Discarding the first string and assigning the two others to existing user/password
  sscanf(temp, "%*s %s %s", exuser, expass);
  
  //loops the member list to find a match
  while(check!=NULL){
  
    //Correct combination found
    if ((strcmp(user, exuser)|| strcmp(pass,expass)) ==0){

      //Prints Success message to webpage and gives link to access main content
      printf("<head><title>Successful login!</title></head>");
      printf("<body background=\"http://barraca.ca/wp-content/uploads/2011/12/Barraca-Bar-Plateau-Montreal-05.jpg\">");
      printf("<br><br><p><b><font color=\"White\" size=20><center>Successful login! </center></font></b></p>");
      printf("<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/feedpage.html\"><center><font color=\"White\">Click here to go to your feed page</font></center></a>");
      printf("</body>");
      printf("</html>");
      return 0;
      break;
    }
  
  //Reads the following line of the members.csv file and assigns to corresponding strings
  check = fgets(temp,44,members);
        sscanf(temp, "%*s %s %s", exuser, expass);
  
  }

  //Closing the file that was opened
  fclose(members);
  

  //Printing error message and displaying link to homepage
  printf("<head><title>Error</title></head>");
        printf("<body background=\"http://barraca.ca/wp-content/uploads/2011/12/Barraca-Bar-Plateau-Montreal-05.jpg\">");
        printf("<br><br><p><b><font color=\"White\" size=20><center>Incorrect username/password combination </center></font></b></p>");
        printf("<a href=\"http://cs.mcgill.ca/~lthoma13/Comp206A4/welcome.html\"><center><font color=\"White\">Return to Homepage</font></center></a>");
        printf("</body>");
        printf("</html>");

  return 0;
}