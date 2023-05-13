# RodrigoQ
prodructor-consumidor memoria compartida
import multiprocessing

def productor(cola):
    for i in range(10):
        cola.put(i)
        print(f"El productor agregó {i} a la cola")

def consumidor(cola):
    while True:
        item = cola.get()
        print(f"El consumidor eliminó {item} de la cola")

if __name__ == "__main__":
    cola = multiprocessing.Queue()
    productor_process = multiprocessing.Process(target=productor, args=(cola,))
    consumidor_process = multiprocessing.Process(target=consumidor, args=(cola,))
    productor_process.start()
    consumidor_process.start()
    productor_process.join()
