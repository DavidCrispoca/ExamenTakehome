from datetime import datetime
import jwt
from fastapi import Header, HTTPException
import config
import bcrypt

def hash_password(password: str) -> str:
    # Genera un salt automático y cifra la contraseña con Bcrypt
    pwd_bytes = password.encode('utf-8')
    return bcrypt.hashpw(pwd_bytes, bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, password_hash: str) -> bool:
    # Compara la contraseña ingresada con el hash guardado de forma segura
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def crear_token(usuario: dict) -> str:
    payload = {
        "sub": str(usuario["id"]),
        "username": usuario["username"],
        "rol": usuario["rol"],
        "iat": int(datetime.utcnow().timestamp()),
    }
    return jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

def usuario_actual(authorization: str = Header(default="")) -> dict:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token requerido")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(
            token,
            config.JWT_SECRET,
<<<<<<< HEAD
            algorithms=["HS256"]
        )
=======
            algorithms=["HS256"],
            )
>>>>>>> origin/main
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {
        "id": int(payload["sub"]),
        "username": payload.get("username"),
        "rol": payload.get("rol", "usuario"),
    }