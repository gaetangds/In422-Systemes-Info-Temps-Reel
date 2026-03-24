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

void sum(int a, int b) { 
	printf("%d \n", a + b);
}

void found(int *arr, int size, int search){
	int found = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i] == search) {
			printf("Value %d found at index %d \n", search, i);
			found = 1;
			break;
		}
	}
	
	if (!found) {
		printf("Value not found \n");
	}


}
