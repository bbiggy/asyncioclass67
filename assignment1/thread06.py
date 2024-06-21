# Working With Many Threads
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level= logging.INFO,
                         datefmt= "%H:%M:%S")
    
    thread = list()
    for index in range(3):
        if index == 1:
            time.sleep(2)
        logging.info("Main      : before creating thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        thread.append(x)
        x.start()
    
    for index, thread in enumerate(thread):
        logging.info("Main      : before joining thread %d.", index)
        thread.join()
        logging.info("Main      : thread %d done.", index)