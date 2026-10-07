import threading
import time
import sys

global_counter = 0


# Una funzione di lavoro intensivo per simulare un'operazione CPU-bound
def worker(thread_id, size):
    global global_counter
    count = 0
    for _ in range(size):
        count += 1
        global_counter += 1
        print(f"Thread {thread_id}:", count)
        print(f"Thread {thread_id} global counter:", global_counter)


size = int(sys.argv[1])
thread_size = int(sys.argv[2])

# Creazione di thread che eseguono la stessa funzione
threads = []
for thread_id in range(thread_size):
    threads.append(
        {
            "thread": threading.Thread(
                target=worker,
                args=(
                    thread_id,
                    round(10**size / 4),
                ),
            ),
            "thread_id": thread_id,
        }
    )

start_time = time.time()

# Avvio dei thread
for thread in threads:
    print(f"Starting thread {thread['thread_id']}")
    thread["thread"].start()
    print(f"Started thread {thread['thread_id']}")

# Attendo che i thread abbiano finito
for thread in threads:
    thread["thread"].join()
    print("Thread joined")

end_time = time.time()

print("Tempo impiegato:", end_time - start_time, "secondi")
