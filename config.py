

db_config = {
    'user': parsed_url.username,
    'password': parsed_url.password,
    'host': parsed_url.hostname,
    'database': parsed_url.path[1:],  # Elimina el primer "/"
    'port': parsed_url.port
}