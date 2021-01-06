#include <chrono>
#include <iostream>
#include <pthread.h>
#include "config.hpp"


int main() {
    long long sum;
    std::chrono::high_resolution_clock::time_point start_time;
    std::chrono::high_resolution_clock::time_point end_time;
    int64_t exec_time;
    start_time = std::chrono::high_resolution_clock::now();
    for (long long i = 0; i < NUMS_TO_ADD; ++i) {
        sum += i;
    }
    end_time = std::chrono::high_resolution_clock::now();
    exec_time = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time-start_time).count();
    std::chrono::duration<double> exec_time_dur = std::chrono::duration_cast<std::chrono::duration<double>>(end_time-start_time);
    
    std::cout << "One thread took " << exec_time << " to add " << NUMS_TO_ADD << " numbers answer=" << sum << std::endl;
    std::cout << "One thread took " << exec_time_dur.count() << "s to add " << NUMS_TO_ADD << " numbers answer=" << sum << std::endl; 

}
