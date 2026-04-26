#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

#define N_samples 100000

int main() {

    /* Structures to store the start and end time */
    struct timespec start;
    struct timespec end;

    /* Open file to put times datas in */
    FILE *file = fopen("times.csv", "w");
    if (file == NULL) {
        printf("Can not open times.csv \n");
        return 1;
    }
    fprintf(file, "iteration,time_ns\n");

    /* Use the current time as the seed so that the rand() function generates different numbers each time the program runs */
    srand(time(NULL));


    for (int i = 0; i < N_samples; i++) {

        /* Generate two large random 64-bit numbers */
        uint64_t a_left  = (uint64_t)rand();  /* first 32 bits  */
        uint64_t a_right = (uint64_t)rand();  /* last 32 bits */
        uint64_t a = (a_right << 32) | a_left; /* combine both */

        uint64_t b_left  = (uint64_t)rand();
        uint64_t b_right = (uint64_t)rand();
        uint64_t b = (b_right << 32) | b_left;
        
        /* Start measurement of time */
        clock_gettime(CLOCK_MONOTONIC, &start);

        volatile __uint128_t tau1 = (__uint128_t)a * (__uint128_t)b;

        /* End measurement of time */
        clock_gettime(CLOCK_MONOTONIC, &end);

        long seconds_diff    = end.tv_sec  - start.tv_sec;
        long nanosec_diff    = end.tv_nsec - start.tv_nsec;
        long elapsed_ns = (seconds_diff * 1000000000L) + nanosec_diff;     /* Store the elapsed time in nanoseconds */

        /* Write the result into the CSV file */
        fprintf(file, "%d,%ld\n", i + 1, elapsed_ns); /*%d = iteration number & %ld = elapsed time in nanosec*/
    }

    fclose(file);

    printf("%d measurements appended to times.csv\n", N_samples);
 
    return 0;
}