from flask import Flask, jsonify, request  # Importamos Flask y funciones necesarias para la API

app = Flask(__name__)  # Inicializamos la aplicación Flask

# Definimos listas para almacenar perfiles, insumos y recetas (como diccionarios)
perfiles = [
    {
        "nombre": "Juan",
        "perfil_alimenticio": 1,
        "deficiencia": "Vitamina D"
    },
    {
        "nombre": "Ana",
        "perfil_alimenticio": 2,
        "deficiencia": "Hierro"
    },
    {
        "nombre": "Luis",
        "perfil_alimenticio": 3
    }
]  # Lista de perfiles

insumos = [
    {
        "nombre": "Tomates",
        "cantidad": 10
    },
    {
        "nombre": "Zanahorias",
        "cantidad": 5
    },
    {
        "nombre": "Acelga",
        "cantidad": 3
    },
    {
        "nombre": "Pechuga de pollo",
        "cantidad": 2
    },
    {
        "nombre": "Arroz",
        "cantidad": 1
    }
]   # Lista de insumos

recetas_favoritas = [
    {
        "titulo": "Milanesa de Pollo con Puré de Papa",
        "descripcion": "Ingredientes: Pollo, Papa, Pan rallado, Huevo "
                       "Instrucciones: "
                       "Preparar la milanesa de pollo empanizando las pechugas de pollo en pan rallado."
                       "Freír las milanesas hasta que estén doradas y crujientes."
                       "Preparar el puré de papa hirviendo las papas y luego aplastándolas con manteca y leche."
                       "Servir las milanesas con el puré de papa."
    },
    {
        "titulo": "Pollo al Horno con Ensalada de Tomate",
        "descripcion": "Ingredientes: Pollo, Tomates, Ajo, Aceite de oliva"
                       "Instrucciones: "
                       "Marinar el pollo con ajo picado, aceite de oliva y hierbas. "
                       "Hornear el pollo hasta que esté cocido y dorado. "
                       "Preparar una ensalada de tomate cortando los tomates en rodajas y aliñándolos con aceite de oliva, sal y pimienta. "
                       "Servir el pollo con la ensalada de tomate.",
    }
]   # Lista de recetas favoritas

# Endpoint para obtener la lista de perfiles
@app.route('/perfiles', methods=['GET'])
def obtener_perfiles():
    return jsonify(perfiles)  # Devolvemos la lista de perfiles

# Endpoint para agregar un nuevo perfil
@app.route('/perfiles', methods=['POST'])
def agregar_perfil():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    nuevo_perfil = {
        "nombre": data['nombre'],
        "perfil_alimenticio": data['perfil_alimenticio'],
        "deficiencia": data.get('deficiencia')
    }
    perfiles.append(nuevo_perfil)  # Agregamos el nuevo perfil a la lista
    return jsonify({"mensaje": "Perfil añadido"}), 201  # Devolvemos un mensaje de confirmación

# Endpoint para obtener la lista de insumos
@app.route('/insumos', methods=['GET'])
def obtener_insumos():
    return jsonify(insumos)  # Devolvemos la lista de insumos

# Endpoint para agregar un nuevo insumo
@app.route('/insumos', methods=['POST'])
def agregar_insumo():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    nuevo_insumo = {
        "nombre": data['nombre'],
        "cantidad": data['cantidad']
    }
    insumos.append(nuevo_insumo)  # Agregamos el nuevo insumo a la lista
    return jsonify({"mensaje": "Insumo añadido"}), 201  # Devolvemos un mensaje de confirmación

# Endpoint para obtener la lista de recetas favoritas
@app.route('/recetas', methods=['GET'])
def obtener_recetas():
    return jsonify(recetas_favoritas)  # Devolvemos la lista de recetas favoritas

# Endpoint para agregar una nueva receta
@app.route('/recetas', methods=['POST'])
def agregar_receta():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    receta = {
        "titulo": data['titulo'],
        "descripcion": data['descripcion']
    }

    # Verificar que no haya más de 5 recetas
    if len(recetas_favoritas) >= 5:
        return jsonify({"error": "No se pueden agregar más de 5 recetas"}), 400

    recetas_favoritas.append(receta)  # Agregamos la receta a la lista
    return jsonify({"mensaje": "Receta añadida"}), 201  # Devolvemos un mensaje de confirmación

# Función para iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutamos la aplicación en modo debug para desarrollo
