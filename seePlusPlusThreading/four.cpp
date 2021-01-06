#include <chrono>
#include <iostream>
#include <vector>
#include <thread>
#include "config.hpp"

void add_numbers(long long start, long long end) {
    long long sum;
    for (long long i = start; i < end; ++i) {
        sum += i;
    }
    std::cout << sum << std::endl;
}


int main() {
    int NUM_THREADS = 4;
    
    std::chrono::high_resolution_clock::time_point start_time;
    std::chrono::high_resolution_clock::time_point end_time;
    int64_t exec_time;
    std::vector<long long> starts;
    std::vector<long long> ends;
    for (int i = 0; i < NUM_THREADS; ++i) {
        if (i == 0) {
            starts.push_back(0);
            ends.push_back(NUMS_TO_ADD / NUM_THREADS);
        } else {
            starts.push_back(ends[i-1] + 1);
            ends.push_back(ends[i-1] + 1 + (NUMS_TO_ADD / NUM_THREADS));
        }
    }

    std::vector<std::thread> threads;
    for (int i = 0; i < NUM_THREADS; ++i) {
        if (i == 0) {
            threads.push_back(std::thread(add_numbers, 0, NUMS_TO_ADD / NUM_THREADS));
        } else {
            threads.push_back(std::thread(add_numbers, starts[i], ends[i]));
        }
    }

    start_time = std::chrono::high_resolution_clock::now();

    for (auto &curr_thread : threads) {
        curr_thread.join();
    }

    end_time = std::chrono::high_resolution_clock::now();
    exec_time = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time-start_time).count();
    std::chrono::duration<double> exec_time_dur = std::chrono::duration_cast<std::chrono::duration<double>>(end_time-start_time);
    
    std::cout << "Two threads took " << exec_time << " to add " << NUMS_TO_ADD << " numbers answer=" << std::endl;
    std::cout << "Two threads took " << exec_time_dur.count() << "s to add " << NUMS_TO_ADD << " numbers answer=" << std::endl; 

}

