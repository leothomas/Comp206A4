#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// interprets user name and password using Post method?
//invoke login script as "action" argument of CGI form. 
// displays error page if login info is incorrect + link back to welcome page
// links to topic update page is login is successful

// generate redirection pages using printf

/* chart string[100];
char c;
int a = 0;
int n = atoi(getenv("CONTENT_LENGTH")); */

//	TEST COMMENT CHECK FOR OVERRIDES

int main(void){
	char *data = getenv("QUERY_STRING");
	char ent_username[25], ent_password[25];
	sscanf(data, "%s %s", &ent_username, &ent_password);
	FILE *fp;
	fp = fopen("members.csv", "r+");

	printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
	printf("<html>");
	//printf("<head>");
	//printf("<title>Test post please ignore</title>");
	//printf("</head>");
	printf("<body> <h1><center> MontrealBarBook</h1></center></body>");
	while ()
	{
		if()
	}
	printf("</html>");
	return 0;
}