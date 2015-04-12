#include <stdio.h>
#include <stdlib.h>

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
	char username[25], password[25];

	sscanf(data, "%s %s", &username, &password);
	printf("Content-Type:text/html\n\n");
	printf("<html>");
	
	//printf("<head>");
	//printf("<title>Test post please ignore</title>");
	//printf("</head>");
	printf("<body> <h1><center> MontrealBarBook</h1></center></body>");
	// printf("username: %s, password: %s", username, password);
	printf("</html>");
	exit(0);
}