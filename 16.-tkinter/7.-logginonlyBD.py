import mariadb

conexionDatabase1 = mariadb.connect(
    user="root",
    password="root",
    host="localhost",
    port=3319,
    database="test"
)
cursor = conexionDatabase1.cursor()

# widget events
def mainLoggin(usuario, password):
    try:
        sentencia = f'SELECT id,username,NAME,email FROM users WHERE username="{usuario}" AND `password`="{password}"limit 1;'
        print(sentencia)
        cursor.execute(sentencia)
        registros = cursor.fetchone()
        if registros != 0:
            print(f'id {registros[0]} username {registros[1]} name {registros[2]} email {registros[3]}')
    except Exception as e:
        print(f'Ocurrio un error {e} ')



usuario = "mgallyonb"
password = "cL1pPFfW"

mainLoggin(usuario, password)
