import os
from urllib.parse import urlparse

# Obtén la URL de la base de datos desde las variables de entorno
database_url = os.getenv('MYSQL_URL')

# Analiza la URL
if database_url:
    parsed_url = urlparse(database_url)
    db_config = {
        'user': parsed_url.username,
        'password': parsed_url.password,
        'host': parsed_url.hostname,
        'port': parsed_url.port,
        'database': parsed_url.path.lstrip('/'),
    }
else:
    raise ValueError("MYSQL_URL no está definida en las variables de entorno.")
