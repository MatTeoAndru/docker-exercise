#Creare un sito in python con flask che ha due funzioni sole /cpu_XXX /ram_Y dove in un caso
#si esegue un processo che consuma uno sproposito di CPU per circa XXX secondi, e una che occupi la ram per un valore di Y GB

from flask import Flask
import time
import psutil
import socket


app = Flask(__name__)

@app.route('/')
def instruction():

    container_id = socket.gethostname()
    return f"Container ID: {container_id}\nendpoint disponibili: 1) /cpu_ che accetta int:seconds 2) /ram_ che accetta int:gb_int:seconds"



@app.route('/cpu_<int:seconds>')
def consume_cpu(seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        pass
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"CPU consumed for {seconds} seconds. CPU Usage: {cpu_usage}%."

@app.route('/ram_<int:gb>_<int:seconds>')
def consume_ram(gb, seconds):
    data = [0] * (gb * 1024 * 1024)
    time.sleep(seconds)
    ram_usage = psutil.virtual_memory().percent
    del data
    return f"RAM occupied for {gb} GB and kept for {seconds} seconds. RAM Usage: {ram_usage}%."

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
