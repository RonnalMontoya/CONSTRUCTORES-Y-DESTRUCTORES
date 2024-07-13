class ConexiónBasedeDatos:
    """
    Clase que representa una conexión a una base de datos.
    """

    def __init__(self, db_name):
        """
        Constructor que inicializa la conexión a la base de datos.
        :param db_name: Nombre de la base de datos a la que se conectará.
        """
        self.db_name = db_name
        self.connection = None
        self.connect()

    def connect(self):
        """
        Método que simula la conexión a la base de datos.
        """
        self.connection = f"Conexión establecida a {self.db_name}"
        print(self.connection)

    def close(self):
        """
        Método que simula el cierre de la conexión a la base de datos.
        """
        if self.connection:
            print(f"Cerrando la conexión a {self.db_name}")
            self.connection = None
        else:
            print("No hay conexión para cerrar")

    def __del__(self):
        """
        Destructor que se llama cuando el objeto es destruido.
        Realiza la limpieza y cierre de la conexión si está abierta.
        """
        self.close()
        print(f"Objeto de conexión a {self.db_name} destruido")

# Demostración del uso de constructores y destructores

# Crear una instancia de ConexiónBasedeDatos
db_conn = ConexiónBasedeDatos("mi_base_de_datos")

# Realizar algunas operaciones con la conexión (simuladas)
print("Realizando operaciones con la base de datos...")

# Cerrar la conexión explícitamente
db_conn.close()

# El objeto db_conn será destruido al finalizar el programa, invocando el destructor (__del__)
