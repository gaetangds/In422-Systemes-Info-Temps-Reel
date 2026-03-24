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
	sum(a, b);
	int arr[] = {1, 2, 3, 4, 5};
	int size = sizeof(arr) / sizeof(arr[0]);
	int search = 3;
	found(arr, size, search);
	
   	return 0;
}
