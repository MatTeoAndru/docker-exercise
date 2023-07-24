#Creare un sito in python con flask che ha due funzioni sole /cpu_XXX /ram_Y dove in un caso
#si esegue un processo che consuma uno sproposito di CPU per circa XXX secondi, e una che occupi la ram per un valore di Y GB

import os
import socket
import time

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(0.1)
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())

if __name__ == "__main__":
    app.run()
