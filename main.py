from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    """
        Passando uma mensagem na tela.
        'Olá Mundo'
    """

    return {'message':'Olá Mundo'}