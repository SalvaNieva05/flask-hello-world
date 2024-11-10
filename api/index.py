from flask import Flask, jsonify, request  # Importamos Flask y funciones necesarias para la API

app = Flask(__name__)  # Inicializamos la aplicación Flask

# Definimos listas para almacenar perfiles y insumos
perfiles = []  # Lista de objetos de tipo Usuario
insumos = []   # Lista de objetos de tipo Insumo

# Clase Usuario
class Usuario:
    def __init__(self, nombre, perfil_alimenticio, deficiencia=None):
        self.nombre = nombre
        self.perfil_alimenticio = perfil_alimenticio
        self.deficiencia = deficiencia

    def __str__(self):
        perfiles = {
            1: "Flexible",
            2: "Vegetariano",
            3: "Vegano",
            4: "Inflexible por salud"
        }
        perfil = perfiles.get(self.perfil_alimenticio, "Desconocido")
        if self.perfil_alimenticio == 4 and self.deficiencia:
            return f"{self.nombre}, {perfil} ({self.deficiencia})"
        else:
            return f"{self.nombre}, {perfil}"

    def to_dict(self):
        # Método para convertir el objeto en un diccionario
        return {
            "nombre": self.nombre,
            "perfil_alimenticio": self.perfil_alimenticio,
            "deficiencia": self.deficiencia
        }

# Clase Insumo
class Insumo:
    def __init__(self, nom, cant):
        self.nom = nom
        self.cant = cant

    def __str__(self):
        cad = "Insumo: {:<10}| Cantidad: {:<10}"
        return cad.format(self.nom, self.cant)

    def to_dict(self):
        # Método para convertir el objeto en un diccionario
        return {
            "nombre": self.nom,
            "cantidad": self.cant
        }

# Endpoint para obtener la lista de perfiles
@app.route('/perfiles', methods=['GET'])
def obtener_perfiles():
    return jsonify([p.to_dict() for p in perfiles])  # Convertimos cada objeto en diccionario para enviar como JSON

# Endpoint para agregar un nuevo perfil
@app.route('/perfiles', methods=['POST'])
def agregar_perfil():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    nuevo_perfil = Usuario(
        nombre=data['nombre'],
        perfil_alimenticio=data['perfil_alimenticio'],
        deficiencia=data.get('deficiencia')
    )
    perfiles.append(nuevo_perfil)  # Agregamos el nuevo perfil a la lista
    return jsonify({"mensaje": "Perfil añadido"}), 201  # Devolvemos un mensaje de confirmación y código 201

# Endpoint para obtener la lista de insumos
@app.route('/insumos', methods=['GET'])
def obtener_insumos():
    return jsonify([i.to_dict() for i in insumos])  # Convertimos cada objeto en diccionario para enviar como JSON

# Endpoint para agregar un nuevo insumo
@app.route('/insumos', methods=['POST'])
def agregar_insumo():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud
    nuevo_insumo = Insumo(
        nom=data['nombre'],
        cant=data['cantidad']
    )
    insumos.append(nuevo_insumo)  # Agregamos el nuevo insumo a la lista
    return jsonify({"mensaje": "Insumo añadido"}), 201  # Devolvemos un mensaje de confirmación y código 201

# Función para iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutamos la aplicación en modo debug para desarrollo