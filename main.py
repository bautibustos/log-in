from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.routes.users import router as users_router

app = FastAPI()

# se definen las carpetas donde esta la pagina web
app.mount("/web/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/html")

# definicion de nueva ruta dentro de la api
app.include_router(users_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")