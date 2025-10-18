from flask import Flask, render_template, request, jsonify
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()
DB = "inventory.db"

# ----------- CRUD -----------

@app.route("/crear_variable", methods=["POST"])
def crear_variable():
    data = request.json
    temp = data.get("temperatura")
    hum = data.get("humedad")
    ph = data.get("ph")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO variables (temperatura, humedad, ph) VALUES (?, ?, ?)",
        (temp, hum, ph)
    )
    conn.commit()
    conn.close()
    return jsonify({"result": "✅ Lectura guardada exitosamente."})

@app.route("/listar_variables", methods=["GET"])
def listar_variables():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM variables ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "temperatura": row[1],
            "humedad": row[2],
            "ph": row[3],
            "estado_temp": evaluar_temperatura(row[1]),
            "estado_hum": evaluar_humedad(row[2]),
            "estado_ph": evaluar_ph(row[3])
        })
    return jsonify(result)

@app.route("/eliminar_variable/<int:id>", methods=["DELETE"])
def eliminar_variable(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM variables WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"result": "🗑️ Variable eliminada exitosamente."})

@app.route("/actualizar_variable/<int:id>", methods=["PUT"])
def actualizar_variable(id):
    data = request.json
    temp = data.get("temperatura")
    hum = data.get("humedad")
    ph = data.get("ph")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE variables SET temperatura=?, humedad=?, ph=? WHERE id=?",
        (temp, hum, ph, id)
    )
    conn.commit()
    conn.close()
    return jsonify({"result": "♻️ Variable actualizada correctamente."})

# ----------- Evaluaciones -----------

def evaluar_temperatura(temp):
    if temp < 18:
        return "Baja 🌡️"
    elif temp > 30:
        return "Alta 🔥"
    else:
        return "Normal ✅"

def evaluar_humedad(hum):
    if hum < 40:
        return "Baja 💧"
    elif hum > 80:
        return "Alta 💦"
    else:
        return "Normal ✅"

def evaluar_ph(ph):
    if ph < 6.5:
        return "Ácido ⚗️"
    elif ph > 7.5:
        return "Básico 🧪"
    else:
        return "Normal ✅"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
