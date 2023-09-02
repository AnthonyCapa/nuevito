from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a la base de datos Access
conexion_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\PC 1\Documents\bdpruebaa.accdb;'  # Reemplaza con la ruta de tu archivo .accdb
)

# Crea una función para establecer la conexión a la base de datos
def conectar_bd():
    return pyodbc.connect(conexion_str)

@app.route('/')
def mostrar_reporte():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Consulta SQL para obtener los datos de la tabla "Cursos"
    cursor.execute('SELECT Id, Nombre_Curso, Id_Estudiante FROM Cursos')
    cursos = cursor.fetchall()

    # Consulta SQL para obtener los datos de la tabla "Estudiantes"
    cursor.execute('SELECT Id_Estudiante, Nombre, Apellido, Edad FROM Estudiantes')
    estudiantes = cursor.fetchall()

    conexion.close()

    return render_template('cursos_y_estudiantes.html', cursos=cursos, estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)
