from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensaje_de_prueba():
    return {"status": "viva", "mensaje": "Hola Laura, tu API en el VPS funciona!"}

@app.get("/calculo/{n1}/{n2}")
def sumar(n1: int, n2: int):
    resultado = n1 + n2
    return {"operacion": "suma", "resultado": resultado}
