#include <stdio.h>
int main(void) {
	int name;
	printf("it works \n");
	scanf("%s",&name);
	printf("Hello %s",name);
	return 0;
}

//compile using command (gcc-o test test.c)
//gcc -o c_from_terminal c_from_terminal.c

// run using command(./test)
//./c_from_terminal

// together
// gcc -o c_from_terminal c_from_terminal.c | ./c_from_terminal

//input from a file (input.txt)
