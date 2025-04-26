from fastapi import FastAPI
from app.routes import converter_route

app = FastAPI()

# Incluir as rotas
app.include_router(converter_route.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
