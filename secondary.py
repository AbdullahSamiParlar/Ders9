from flask import Flask
import math
k = 10000
asallar = []

for a in range(2, k):
    is_asal = True
    for i in range(2, int(math.sqrt(a)) + 1): 
        if a % i == 0:
            is_asal = False
            break
    if is_asal:
        asallar.append(a)

def sep(asallar, separated="\n"):
    return(separated.join(map(str, asallar)))



asallar2=sep(asallar, sep="\n")
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<h1>{asallar2}</h1>'

@app.route("/test")
def bye():
    return f'<h1>---</h1>'

app.run(debug=True)