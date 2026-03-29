#include <stdio.h>
#include <time.h>
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
	int arr2[] = {1, 6, 18, 54, 68, 77};
	int size2 = sizeof(arr2) / sizeof(arr2[0]);
	int search2 = 68;
	binary_search(arr2, size2, search2);
	int arr3[] = {7, 1, 8, 2, 3, 9, 70, 55, 12, 69, 43, 105, 199, 2024, 25};
	int size3 = sizeof(arr3) / sizeof(arr3[0]);
	int type = 0; 
	clock_t start = clock();
	ordererList(arr3, size3, type);
	clock_t end = clock();
	double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time taken: %f seconds\n", time_taken);
	printf("Memory used: %lu bytes\n", sizeof(arr));
	printArray(arr3, size3);
   	return 0;
}
