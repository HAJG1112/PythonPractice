
import multiprocessing
import time
import concurrent.futures
from time import perf_counter

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

def main():
    # this is known as a context manager
    with concurrent.futures.ProcessPoolExecutor() as executor:
        #f1 = executor.submit(do_something, 1) #submit function to thread
        #f2 = executor.submit(do_something, 1) #submit function to thread
        #print(f1.result())
        #print(f2.result())

        '''
        Here we pass in a list as an iterable to our results queue
        '''
        secs = [5,4,3,2,1]
        #results = [executor.submit(do_something, sec) for sec in secs]
        #for f in concurrent.futures.as_completed(results):
        #    print(f.result())

        '''
        Now we map some iterable to a function
        '''
        results = executor.map(do_something, secs)  #map only returns the results, and stores them
        for result in results:
            print(result)  #now we loop through the results that we have collated! We can also handle exceptions in the result iterator

if __name__ == '__main__':
    
    tic = perf_counter()
    main()
    toc = perf_counter()
    print(f"Elapsed Time: {toc-tic}")