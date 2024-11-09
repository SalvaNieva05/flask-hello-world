from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de alimentos
foods = [
    {"id": 1, "name": "Pizza"},
    {"id": 2, "name": "Empanada"},
    {"id": 3, "name": "Lomo"},
    {"id": 4, "name": "Hamburguesa"},
    {"id": 5, "name": "Pasta"}
]


# Endpoint /food para obtener la lista de aliment
@app.route('/food', methods=['GET'])
def get_food():


    return jsonify(foods)


# Endpoint /food para agregar un nuevo alimento
@app.route('/food', methods=['POST'])
def add_food():
    # Obtener los datos del cuerpo de la solicitud
    new_food = request.get_json()

    # Asegurarse de que el alimento tenga un nombre
    if not new_food.get('name'):
        return jsonify({"error": "El nombre del alimento es obligatorio"}), 400

    # Crear un nuevo id para el alimento
    new_id = max(food['id'] for food in foods) + 1 if foods else 1
    new_food['id'] = new_id

    # Agregar el alimento a la lista
    foods.append(new_food)

    return jsonify(new_food), 201


if __name__ == '__main__':
    app.run(debug=True)