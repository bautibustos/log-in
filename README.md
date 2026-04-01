# Desafío Técnico: Login & Seguridad

## Objetivos de la Actividad
### Backend & Seguridad:
Implementar los endpoints necesarios para el flujo de OTP (One-Time Password) (impreso en consola no vamos a llegar a ver e-mails aún) y lógica de recuperación de cuenta.

### Frontend Pro:
Elevar la estética del login. Trabajar en el feedback visual (loaders, estados de error) y diseño responsivo.

### UX de Autenticación:
Añadir funciones críticas de experiencia de usuario: "Recordarme", "Olvidé mi contraseña" y validaciones en tiempo real.
________________________________________________________________________

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
- **Seguridad**: ante filtraciones: Si la base de datos es bulnerada, el atacante solamente vera cadenas de texto sin poder decifrarlas.
- **Integridad del Secreto**: El sistema nunca conoce la contraseña real.


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

# Estructura de carpetas
```
LOGIN-PGR/
├── api/
│   ├── routes/
│   │   └── users.py
│   └── schemas/
│       └── user.py
├── db/                  
│   └── connection.py 
├── web/
│   ├── html/
│   │   └── index.html
│   └── static/
│       └── style.css
│   └── js/
│       └── login.js
└── main.py
```