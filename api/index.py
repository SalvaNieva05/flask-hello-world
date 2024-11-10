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

recetas = [
    {
        "titulo": "Ensalada Mediterránea",
        "descripcion": "Una ensalada fresca con tomates, pepinos, aceitunas, queso feta y un toque de aceite de oliva."
    },
    {
        "titulo": "Sopa de Zanahorias",
        "descripcion": "Sopa suave y cremosa de zanahorias, cebolla y jengibre, ideal para los días fríos."
    },
    {
        "titulo": "Pechuga de Pollo al Horno",
        "descripcion": "Pechuga de pollo marinada con hierbas, limón y aceite de oliva, cocida al horno para un plato saludable."
    },
    {
        "titulo": "Arroz Integral con Verduras",
        "descripcion": "Un plato saludable con arroz integral, zanahorias, guisantes y pimientos."
    },
    {
        "titulo": "Tortilla de Acelga",
        "descripcion": "Tortilla vegetariana con acelga, cebolla y huevo."
    }
]   # Lista de recetas

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

# Endpoint para obtener la lista de recetas
@app.route('/recetas', methods=['GET'])
def obtener_recetas():
    return jsonify(recetas)  # Devolvemos la lista de recetas

# Endpoint para agregar una nueva receta
@app.route('/recetas', methods=['POST'])
def agregar_receta():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    receta = {
        "titulo": data['titulo'],
        "descripcion": data['descripcion']
    }

    # Verificar que no haya más de 5 recetas
    if len(recetas) >= 5:
        return jsonify({"error": "No se pueden agregar más de 5 recetas"}), 400

    recetas.append(receta)  # Agregamos la receta a la lista
    return jsonify({"mensaje": "Receta añadida"}), 201  # Devolvemos un mensaje de confirmación

# Función para iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutamos la aplicación en modo debug para desarrollo
