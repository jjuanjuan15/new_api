import random

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

