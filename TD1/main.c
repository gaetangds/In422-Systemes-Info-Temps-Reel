#include <stdio.h>
#include "header.h"

int main() {
	printHello();
   	int a = 10;
	int b = 15;
	compare2value(a, b);
	printforLoopValue(a, b);
	printwhileLoopValue(a, b);
	printf("Value : %d & memory address : %p \n", a, &a);
	assignValue(&a, b);
	printf("Value : %d & memory address : %p \n", a, &a);
   	return 0;
}
