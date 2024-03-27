import threading
import time
import sys


# Una funzione di lavoro intensivo per simulare un'operazione CPU-bound
def worker(size):
    count = 0
    for _ in range(size):
        count += 1


size = int(sys.argv[1])
thread_size = int(sys.argv[2])

# Creazione di thread che eseguono la stessa funzione
threads = []
for i in range(thread_size):
    threads.append(threading.Thread(target=worker, args=(round(10**size / 4),)))

start_time = time.time()

# Avvio dei thread
for thread in threads:
    thread.start()

# Attendo che i thread abbiano finito
for thread in threads:
    thread.join()

end_time = time.time()

print("Tempo impiegato:", end_time - start_time, "secondi")
