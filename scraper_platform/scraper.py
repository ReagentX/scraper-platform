import sys
from multiprocessing.dummy import Pool as ThreadPool


class Scraper(object):
    def __init__(self, threads, cache):
        self.threads = threads
        self.cache = cache

    def __repr__(self):
        return f'<scraper object: max {self.threads} threads, {"cached" if self.cache else "uncached"}>'

    def scrape(self, lst: list, function, processes: int):
        """Handles multiprocessing using ThreadPool; sends items from a list to a function and gets the results as a list"""
        # Define the number of processes, use less than or equal to the defined value
        count_threads = min(processes, len(lst))
        if count_threads == 0:
                return []
        pool = ThreadPool(count_threads)

        # Tell the user what is happening
        print(f"Scraping {len(lst)} items using {function} in {count_threads} processes.")

        # Calls function() and adds the filesize returned each call to an lst
        result = (pool.imap_unordered(function, lst))
        pool.close()

        # Display progress as the scraper runs its processes
        while (len(lst) > 1):
            completed = result._index

            # Break out of the loop if all tasks are done or if there is only one task
            if (completed == len(lst)):
                sys.stdout.flush()
                sys.stdout.write('\r' + "")
                sys.stdout.flush()
                break

            # Avoid a ZeroDivisionError
            if completed > 0:
                sys.stdout.flush()
                sys.stdout.write('\r' + f"{completed/len(lst)*100:.0f}% done. {len(lst)-completed} left. ")
                sys.stdout.flush()
            sys.stdout.flush()

        pool.join()
        return list(result)