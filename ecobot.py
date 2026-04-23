OBJETOS = {
    "botella de plastico":{
        "reciclable": True,
        "tiempo_descomposicion": "450 años"
    },
    "bolsa de plastico":{
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },
    "caja de carton":{
        "reciclable": True,
        "tiempo_descomposicion": "2 meses"
    },
    "cepillo de dientes":{
        "reciclable": False,
        "tiempo_descomposicion": "500 años",
        "manualidad": "Puedes usarlo para limpiar esquinas o teclados dificiles"
    },
    "envase de yogur":{
        "reciclable": True,
        "tiempo_descomposicion": "30-50 años"
    },
    "vaso de papel con cubrimiento plastico":{
        "reciclable": False,
        "tiempo_descomposicion": "30 años",
        "manualidad": "Puedes usarlo como maceta para plantar semillas"
    },
    "vidrio":{
        "reciclable": True,
        "tiempo_descomposicion": "1 million de años"
    },
    "lata de aluminio":{
        "reciclable": True,
        "tiempo_descomposicion": "200 años"
    },
    "papel":{
        "reciclable": True,
        "tiempo_descomposicion": "2-6 semanas"
    },
    "pilas":{
        "reciclable": False,
        "tiempo_descomposicion": "500-1000 años",
        "manualidad": "Llevarlas a puntos de recolección especiales, no tirarlas a la basura"
    },
    "ropa de algodon":{
        "reciclable": True,
        "tiempo_descomposicion": "1-5 meses",
    },
    "madera":{
        "reciclable": True,
        "tiempo_descomposicion": "1-3 años"
    },
    "neumatico":{
        "reciclable": False,
        "tiempo_descomposicion": "600-800 años",
        "manualidad": "Se puede usar como maceta o columpio"
    },
    "esponja de cocina":{
        "reciclable": False,
        "tiempo_descomposicion": "200 años",
        "manualidad": "Puedes reutilizarla para limpiar superficies o zapatos"
}
}

def evaluar_objeto(nombre_objeto):  
    # Convierte el nombre del objeto a minúsculas para evitar errores con mayúsculas/minúsculas
    nombre_objeto = nombre_objeto.lower()  
    # Verifica si el objeto existe dentro del diccionario OBJETOS
    if nombre_objeto not in OBJETOS:
        # Si no existe, devuelve un mensaje indicando los objetos disponibles
        return f"No conozco ese objeto. Intenta con estos {list(OBJETOS.keys())}"
    # Obtiene los datos del objeto desde el diccionario OBJETOS
    datos = OBJETOS[nombre_objeto]
    # Verifica si el objeto es reciclable
    if datos["reciclable"] == True:
        accion = "RECICLAR"  # Si es reciclable, la acción será reciclar
    else:
        accion = "DALE UN NUEVO USO"  # Si no lo es, sugiere una manualidad
    # Construye el mensaje con la información básica del objeto
    resultado = f"🔍 OBJETO: {nombre_objeto}\n"
    resultado += f"♻️ ACCIÓN: {accion}\n"
    resultado += f"⏳ TIEMPO DE DESCOMPOSICIÓN: {datos['tiempo_descomposicion']}\n"
    # Si el objeto no es reciclable y además tiene una sugerencia de manualidad, la agrega al resultado
    if not datos["reciclable"] and "manualidad" in datos:
        resultado += f"🎨 SUGERENCIA: {datos['manualidad']}\n"
    # Retorna el mensaje final con toda la información procesada
    return resultado
# Ejemplo de uso: imprime la evaluación de "botella de plástico"
