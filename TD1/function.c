#include <stdio.h>
#include "header.h"

void printHello(){
	printf("Hello World \n");
}

void compare2value(int a, int b) {
	if (a > b) {
		printf("%d \n", a);
	} else if (a < b) {
		printf("%d \n", b);
	} else {
		printf("Equal");
	}
}

void printforLoopValue(int start, int end) {
	for (int i = start; i <= end; i++) { 
		printf("%d ", i);
	}
	printf("\n");
}

void printwhileLoopValue(int start, int end) {
	int cpt = start;
	while (cpt <= end) { 
		printf("%d ", cpt);
		cpt++;
	}
	printf("\n");
}

void assignValue(int* a, int b) {
	*a = b;
}

