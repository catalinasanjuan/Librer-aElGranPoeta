#config.py
import os

db_config = {
    'user': os.getenv('DB_USER', '396794'),  # Usuario de AlwaysData
    'password': os.getenv('DB_PASSWORD', 'admin2025'),  # Contraseña de AlwaysData
    'host': os.getenv('DB_HOST', 'mysql-libreria-el-gran-poeta.alwaysdata.net'),  # Servidor de AlwaysData
    'database': os.getenv('DB_NAME', 'libreria-el-gran-poeta_bd')  # Base de datos de AlwaysData
}
