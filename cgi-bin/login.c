#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#define MAXLEN 80
#define EXTRA 5
/* 4 for field name "user", 1 for "=" */
#define MAXINPUT MAXLEN+EXTRA+2
/* 1 for added line break, 1 for trailing NULL */
#define DATAFILE "./members.csv"

//1. SERVER SENDS USERNAME and PASS
//2. CHECK IF USERNAME IS IN MEMBERS.csv
//3. CHECK IF USERNAME and PASS is in memebers.csv
//FUNCTION CHECKIFNEW with memebers.csv
//FUNCTION CHECKUSERANDPASS
int question(int ru, int rp)
{
   if(ru != 0)
   {
      //printf("WRONG USERNAME\n");
      return 0;
      
   }
   else if(ru == 0  && rp != 0) 
   {
      //printf("Password doesn't match with username \n");
      return 0;
      
   }
   else
   {
      //we found the user
      return 1;
      
   }
}
void unencode(char *src, char *last, char *dest)
{
 for(; src != last; src++, dest++)
   if(*src == '+')
     *dest = ' ';
   else if(*src == '%') 
   {
     int code;
     if(sscanf(src+1, "%2x", &code) != 1) code = '?';
     *dest = code;
     src +=2; 
   }     
   else
     *dest = *src;
  *dest = '\n';
  *++dest = '\0';
}

void parse(char *username, char *password, char *data)
{
  char *temp;
  temp = strstr(data,"&password=");
  strncpy(temp,"          ",10); // we space out the password input
  temp = strtok(data," "); // gets username (before passtoken)
  strcpy(username,temp); // strcopy to username to username array
  while( temp != NULL ) // cycle through the dataarray and place it user and password array
    {
      // DEBUGIN PURP: printf("<p> %s\n",temp);
      strcpy(password,temp);
      temp = strtok(NULL," ");  
    }
  // the lets not forget this thing '\0'  
  username[strlen(username)] = '\0';
  password[strlen(password)-1] = '\0';
  // DEBUGGING PURPOSES
  /*
  printf("<P>Thank you! \n");
  printf("<p>Read password: |%s| \n ", password );
  printf("<p>Read username: |%s| \n ", username );
  */
}

int main(void)
{
char *token;
char *lenstr;
char input[MAXINPUT], data[MAXINPUT];// local vairbales
long len;

printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<HEAD><TITLE>Response</TITLE>\n");
lenstr = getenv("CONTENT_LENGTH");
if(lenstr == NULL || sscanf(lenstr,"%ld",&len)!=1 || len > MAXLEN)
  printf("<body bgcolor=\"#CCCCCC\"><P>Error in invocation - wrong FORM probably.</P></body>");
else 
{
  // HERE WE INITILIZE ALL THE FILES WE NEED IF FROM GOES SMOOTHLY
  char password[MAXLEN], username[MAXLEN];
  FILE *f;

  fgets(input, len+1, stdin);
  unencode(input+EXTRA, input+len, data);
  parse(username, password, data);
  f = fopen(DATAFILE, "r");
  if(f == NULL)
    printf("<body bgcolor=\"#CCCCCC\"><P>Sorry... DATABASE MISSING</P></body>");
  else
  {
    char tmppas[MAXLEN], tmpuser[MAXLEN], temp[200];
    int found,responseuser,responsepass;
    while(fgets(temp,200,f) != NULL)
    {
      // here we take the input of the shit and tokenize  
      //fgets(temp,512,fp);
      token = strtok(temp," ");// get first token
      token = strtok(NULL," ");// get second token--> what we want
      
      strcpy(tmpuser,token); // copy username to tmpuser
      tmpuser[strlen(tmpuser)] = '\0';
      // debugging purposes :printf("<p>tmpuser: |%s| \n",tmpuser);
      responseuser = strcmp(tmpuser,username); // compare tmpuser and username
      // debugging purposess :printf("reponsepass for tmpuser(%s): %d\n",tmpuser,responseuser);

      token = strtok(NULL," "); // get third token
      strcpy(tmppas,token); // copy token to tmppas
      tmppas[strlen(tmppas)] = '\0';
      // debuggin purposes printf("<p>tmppas: |%s| \n",tmppas);
      responsepass = strcmp(tmppas,password);
      // debuggin purposes printf("reponsepass for tmpas(%s): %d\n",tmppas,responsepass);
      found = question(responsepass,responseuser);
      if(found==1) // DID WE FIND IT IN THE FIRST LINE, IF SO BREAK... IF NOT KEEP LOOKIN
        break; // ends the while loop
      while (token != NULL) //nthe while loop that cycles through friends
      {
        token = strtok(NULL," ");
      }// end of while "friends"
    }//end of while for each line members.csv
    if(found==1)
    {
      printf("<meta http-equiv=\"refresh\" content=\"1; url=http://cs.mcgill.ca/~lthoma13/Comp206A4/welcome.html\">");
      printf("</HEAD>");
      printf("<body bgcolor=\"#CCCCCC\"><h2>Authenticated! WELCOME TO THE LONELY ASTRONOMER!<br> REDIRECTING IN 2secs... \n</h2></body>");
    }
    else
      printf("<meta http-equiv=\"refresh\" content=\"0; url=http://cs.mcgill.ca/~rsampa/ass4/welcome_relog.html\">");
  }
  fclose(f);
}
return 0;
}
/*
	printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
	printf("<html>");
	printf("<body> <h1><center> MontrealBarBook</h1></center></body>");

	if(checkSpace(ent_password)== 0){
		printf("<body><P><b><center>Incorrect login info</center></b></P></body>");
		printf(" <a href= \"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Please try again</font></center></a>");	
	}
	
	if (checkSpace(ent_username) == 0){
		printf("<body><P><b><center>Incorrect login info</center></b></P></body>");
		printf(" <a href= \"http://cs.mcgill.ca/~lthoma13/Comp206A4/becomeMember.html\"><center><font color=\"White\">Please try again</font></center></a>");
	}	
	
	//printf("<head>");
	//printf("<title>Test post please ignore</title>");
	//printf("</head>");
	
	//while ()
	{
		//if()
	}
	printf("</html>");
	return 0;
}*/

