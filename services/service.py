import os
import platform
import random
from datetime import datetime
import fastapi
import psutil
import socket

async def funcion_elisa():
    mensajes = [
        "❤️ Hola, Elisa. ¡Que tengas un día estupendo!",
        "🌞 Elisa, recuerda sonreír. Hoy seguro que sale algo bueno.",
        "☕ Hora de un cafecito... o dos.",
        "🌸 Elisa, este servidor funciona mejor cuando tú estás de buen humor.",
        "🍰 Mensaje importante: te has ganado un trozo de tarta (virtual).",
        "🐱 Un gatito imaginario te manda un saludo.",
        "🎉 ¡Bienvenida, Elisa! Has encontrado el endpoint secreto."
    ]

    return {
        "ok": True,
        "mensaje": random.choice(mensajes)
    }

async def funcion_putos():
    mensajes = [
        "🚀 Todos los sistemas operativos.",
        "☕ Nivel de café: 97%.",
        "🐍 Python está de buen humor.",
        "🤖 La IA aprueba este servidor.",
        "✨ No hay bugs... de momento.",
        "🔥 Este endpoint funciona demasiado bien."
    ]

    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage("/")

    return {
        "status": "🟢 Online",
        "hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

        "host": platform.node(),
        "ip_local": socket.gethostbyname(socket.gethostname()),

        "usuario": os.getenv("USERNAME") or os.getenv("USER"),

        "sistema": platform.system(),
        "version_so": platform.release(),
        "arquitectura": platform.machine(),

        "python": platform.python_version(),
        "fastapi": fastapi.__version__,

        "cpu": {
            "nucleos": psutil.cpu_count(logical=True),
            "uso": f"{psutil.cpu_percent()} %"
        },

        "ram": {
            "total_gb": round(memoria.total / 1024**3, 2),
            "libre_gb": round(memoria.available / 1024**3, 2),
            "uso": f"{memoria.percent}%"
        },

        "disco": {
            "total_gb": round(disco.total / 1024**3, 2),
            "libre_gb": round(disco.free / 1024**3, 2),
            "uso": f"{disco.percent}%"
        },

        "uptime": datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%Y %H:%M:%S"),

        "pid": os.getpid(),

        "mensaje": random.choice(mensajes)
    }