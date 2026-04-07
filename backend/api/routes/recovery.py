from fastapi import APIRouter, HTTPException, Response
import bcrypt
import db.connection
from api.schemas.user import OTPrequest,OTPVerify, UpdatePassword
import random, time

router = APIRouter()

otp = {}

def gen_otp(email):
    # genero el codigo otp de 6 digito
    code = random.randint(100000, 999999)
    global otp # llamo a la variable globl 
    # utilizo el mail como indice de busqueda
    otp[email] = {
        "code":code,
        "time": time.time()
        }
    print(otp)
    #añadir logica para que si existe un autentication code, no se renueve a menos que se vensa 


# aca se verifica que el mail este en la base de datos
@router.post("/recovery")
def get_user(data: OTPrequest):
    with db.connection.get_connection() as conn:
        with conn.cursor() as cursor:
            # busca correo en la base de datos
            cursor.execute(
                'SELECT id_user, name, email FROM "USERS" WHERE email = %s',
                (data.email,)
            )
            #recupera resultados
            user = cursor.fetchone()
    # si el usuario no existe o esta mal escrito devuelvo un 404
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else: # si el usario existe genero el OTP
        """
        PARA LA APLICAION DENTRO DE UN PROGRAMA ENCERIO
        se haria un campo OTP, donde guardaria los datos que estan en el diccionario OTP
        luego se haria un request y compararia datos
        """
        gen_otp(data.email)
    return Response(status_code=200)

@router.post("/otp")
def check_otp(data: OTPVerify):
    if data.email in otp:
        # comparo que el codigo sea el correcto y que el tiempo de generacion y el tiempo actual no supere los 300 segundos (5minutos)
        if otp[data.email]["code"] == data.code and otp[data.email]["time"]+300>time.time():
            del otp[data.email]
            return Response(status_code=200, content="OTP correcto")
        else:
            return Response(status_code=401, content="OTP incorrecto")
    else:# si esto no es correcto es pq no se genero el otp
        return Response(status_code=401, content="OTP otro error")
    

@router.post("/updt-pwd")
def update_password(data: UpdatePassword):
    # una vez que se verifica que el OTP es correcto, se pasa a la nueva pestaña
    # donde se debe poner la nueva contraseña
    # luego se envia, aca se encripta
    new_pwd = bcrypt.hashpw(data.pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    # aca se actualiza en la base de datos
    with db.connection.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'UPDATE "USERS" SET pwd = %s WHERE email = %s',
                (new_pwd, data.email)
            )
    # se retorna 200 si fue correcto el proceso.
    return Response(status_code=200)