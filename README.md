# Desafío Técnico: Login & Seguridad

## Objetivos de la Actividad
### Backend & Seguridad:
Implementar los endpoints necesarios para el flujo de OTP (One-Time Password) (impreso en consola no vamos a llegar a ver e-mails aún) y lógica de recuperación de cuenta.

### Frontend Pro:
Elevar la estética del login. Trabajar en el feedback visual (loaders, estados de error) y diseño responsivo.

### UX de Autenticación:
Añadir funciones críticas de experiencia de usuario: "Recordarme", "Olvidé mi contraseña" y validaciones en tiempo real.
________________________________________________________________________
# Ejecucion 
### Backend 

- Armar entorno virtual en python y luego instalar los requerimientos.
``` 
pip install -r requeriments.txt
```
- Configurar archivo "connection.py" ya que es el portador de las credenciales de PostgreSQL
```
LOGIN-X-BautiBustos/
├──backend
|       └──db/                  
│          └── connection.py 
```
### Ejecucion de FastAPI
Luego de haber activado el entorno virtual de python e instalar dependencias, dentro de la carpeta backend utilizar el comando:
```
fastapi dev main.py
```
### Frontend
- Con la terminal dentro de frontend ejecutar:
```
npm install package.json 
```
Luego de esta instalacion tendremos Astro y el servidor de ejecucion. **El servidor se ejecuta con el comando:**
```
npm run dev
```
Luego de eso tendremos el servidor de Astro corriendo con la pagina web. Cabe destacar que ambos servidores deben estar corriendo para su funcionamiento.

### Las credenciales de prueba son:
- **Usuario**: admin@test.com
- **Contraseña**: admin1234.

### Uso del OTP
Una vez dentro del olvide mi contraseña y colocado el mail, dentro de la consola del servidor de python se mostrara el codigo OTP junto al mail y un TempStamp ``` {'admin@test.com': {'code': ** 276561 **, 'time': 1775612183.2673972}} ``` 

**nota**: Como son servidores de prueba y desarrollo ambos son ejecutados en modo "dev". Ya que puede ser algo inestable para ejecutarlos en modo normal. (Ambos en ve de recibir el parametro dev, solamente recibirian el parametro run.)

# Teconologia utilizada
## Fast API
- Rendimiento: Basado en ASGI, permite el manejo de peticiones asincrónicas (async/await), optimizando la concurrencia y el tiempo de respuesta.

- Documentación Automática: Generación nativa de esquemas interactivos (Swagger/OpenAPI) que facilita el testing de los endpoints.

- Ligereza: Arquitectura minimalista y modular

- Modernización: Mientras Django es el estándar para sistemas "monolíticos" y administrativos, FastAPI es el estándar actual para Microservicios y arquitecturas de Nube.

- Auge de la IA: Es el framework preferido para integrar modelos de Machine Learning y IA Generativa, lo que hoy domina las búsquedas laborales de Python.

- Eficiencia de Costos: Al procesar más peticiones con menos recursos (CPU/RAM), las empresas reducen costos de infraestructura en la nube

- Actualmente es utilizadas por empresas como: Netflix, Uber, Microsoft.

## Seguridad implementada: HASH
Se opto por el guardado de las contraseñas dentro de la base de datos hasheadas como un plus de seguridad. Se utilizo como algoritmo de hasheo "BCrypt" (Este dato no deberia ser mostrado, pero esto es meramente educativo). Ya que asegura que dos contraseñas distintas no generen el mismo hash tambien se tuvieron en cuenta los siguientes puntos:

- **Irreversibilidad**: A diferencia del cifrado, el hash es una función de una sola vía. No se puede "des-hashear" para volver al texto plano.
- **Seguridad**: ante filtraciones: Si la base de datos es vulnerada, el atacante solamente vera cadenas de texto sin poder decifrarlas.
- **Integridad del Secreto**: El sistema nunca conoce la contraseña real.

## Astro

- Arquitectura de Islas: Permite enviar prácticamente cero JavaScript al navegador por defecto, cargando componentes interactivos solo cuando son necesarios.

- Agnoticismo de Frameworks: Permite usar componentes de React, Vue, Svelte o Angular dentro de un mismo proyecto, lo que da una flexibilidad total para escalar el frontend.

- Rendimiento Out-of-the-box: Al generar sitios estáticos (SSG) o con renderizado en el servidor (SSR) extremadamente ligeros, logra puntajes de Web Vitals casi perfectos sin esfuerzo extra.

- Experiencia de Desarrollo (DX): Incluye herramientas modernas como ruteo basado en archivos, manejo de Markdown/Content Collections y un servidor de desarrollo muy rápido.

- Optimización de Recursos: Maneja automáticamente la optimización de imágenes, fuentes y estilos, lo que reduce drásticamente el peso de la página y mejora la velocidad de carga.


## Logica del checkeo de la base de datos:
```
Usuario envía email + password en texto plano
        ↓
Busca el usuario en la BD por email
        ↓
Si existe → compara el hash de la contraseña enviada con el hash guardado
        ↓
 Coincide → login ok    No coincide → error
```
## Logica del OTP
```
Usuario ingresa email en recovery-pwd
        ↓
FastAPI verifica que el email existe y genera OTP
        ↓
Imprime OTP en consola
        ↓
Usuario ingresa el código OTP
        ↓
FastAPI verifica el código
        ↓
Usuario ingresa la nueva contraseña
        ↓
FastAPI actualiza la contraseña en la BDUsuario ingresa email

```

# Estructura de carpetas
```
log-in-x-bautibustos/
├── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── recovery.py
│   │   │   └── users.py
│   │   └── schemas/
│   │       └── user.py
│   ├── db/
│   │   └── connection.py
│   ├── web/
│   │   ├── html/
│   │   │   └── index.html
│   │   └── static/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── login.js
│   ├── bigbang.sql
│   ├── main.py
│   └── requeriments.txt
├── frontend/
│   ├── public/
│   │   └── favicon.svg
│   ├── src/
│   │   ├── assets/
│   │   │   ├── astro.svg
│   │   │   ├── background.svg
│   │   │   ├── maze-bank-completo.webp
│   │   │   ├── maze-bank-logo.png
│   │   │   └── maze-bank-logo.svg
│   │   ├── components/
│   │   │   ├── login/
│   │   │   │   ├── ChangePwd.astro
│   │   │   │   ├── LoginForm.astro
│   │   │   │   ├── OtpForm.astro
│   │   │   │   └── RecoveryPwd.astro
│   │   │   ├── ui/
│   │   │   │   ├── Alert/
│   │   │   │   │   ├── Alert.astro
│   │   │   │   │   └── Alert.ts
│   │   │   │   ├── Button.astro
│   │   │   │   └── InputMail.astro
│   │   │   ├── LoginContainer.astro
│   │   │   └── Welcome.astro
│   │   ├── layouts/
│   │   │   └── Layout.astro
│   │   └── pages/
│   │       ├── change-pwd.astro
│   │       ├── check-otp.astro
│   │       ├── index.astro
│   │       └── recovery-pwd.astro
│   ├── astro.config.mjs
│   ├── package.json
│   └── tsconfig.json
├── README.md
└── .gitignore