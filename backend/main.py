from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from api.routes.users import router as users_router
from api.routes.recovery import router as recovery_router


app = FastAPI()


# Configuración de CORS para permitir requests desde Astro
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4321"],  # puerto por defecto de Astro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# definicion de nueva ruta dentro de la api
app.include_router(users_router, prefix="/api")
app.include_router(recovery_router, prefix="/api")


"""
         Aca se deshabilitan la web que levanta el servidor de fast api.


# se definen las carpetas donde esta la pagina web
app.mount("/web/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/html")



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

"""