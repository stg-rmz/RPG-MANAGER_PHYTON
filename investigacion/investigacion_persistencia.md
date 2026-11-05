Tema 1: El patrón Repository

1. ¿Qué es el patrón Repository (o DAO) y qué problema resuelve?
R/: Separa la lógica de negocio del acceso a datos. Supongamos que queremos obtener personajes de nivel mayor o igual a 23, entonces como la lógica de negocio está separada aún se siguen coleccionando los objetos pero sin tener acceso a los datos, así que lo que hace no es saber cómo se obtienen los datos sino saber qué necesita para obtenerlos. Así que el repository administra los datos por completo.

2. ¿Qué diferencia hay entre la capa de negocio (Service) y la capa de datos (Repository)?
Service solo comprende la lógica de lo que necesita mas no de donde viene, cosa que sí logra hacer Repository. Por ejemplo, para una misión se requiere un nivel mayor o igual a 26, entonces Service comprende esa regla y no hace más, en cambio Repository va cargando, guardando y actualizando los datos.

3. ¿Por qué se dice que un Repository no debe validar reglas de negocio?
Porque no se puede probar la lógica de negocio sin la base de datos, también impide la separación de responsabilidades y se vuelve dependiente de las reglas cuando su trabajo es solo administrar los datos.

Tema 2: Contratos en Java y Python

1. ¿Qué es una interface en Java? ¿Qué pasa si una clase que la implementa olvida un método?
Una interface define qué métodos debe tener una clase y sí al implementar una clase se olvida un método no va a compilar, por así decirlo porque al definir una clase con interface es como un paquete en el cual se deben incluir todos sus métodos.

2. ¿Qué es una clase abstracta con ABC y @abstractmethod en Python? ¿Qué pasa si intentan crear un objeto de esa clase?
Una clase abstracta en python ayuda a abrir el camino para otras clases pero que no se puede implementar si hay métodos abstractos ya que se tienen que definir en otra clase, con @abstractmethod se marcan los métodos que las clases hijas deben implementar obligatoriamente.

3. ¿En qué se parecen y en qué se diferencian las dos formas?
Ninguna de las dos admite implementar directamente métodos abstractos sin implementar en otra clase, ambos permiten a un personaje tener sus métodos que las clases hijas deben implementar obligatoriamente.

Tema 3: Contratos en Java y Python Inyección de dependencias por constructor

1. ¿Qué significa "programar contra una interfaz y no contra una implementación"?
Significa que el código debe depender de las interfaces y no de clases fijas, por ejemplo se tiene que Mago y Arquero pueden atacar, entonces se crea a personaje con el método atacar y sus clases hijas Mago y Arquero heredan atacar, en vez de crear la clase Mago con el método atacar y Arquero con el mismo método atacar.

2. ¿Qué es la inyección de dependencias por constructor?
Lo que hace es darle a una clase sus dependencias a través del constructor en vez de que la clase cree las dependencias. Con el ejemplo, tenemos PersonajeService que recibe por el constructor a PersonajeRepository para guardar personajes.

3. ¿Qué ventaja tiene que el Service reciba el repositorio en vez de crearlo él mismo?
Facilita cambiar el repositorio, reutilizar el código y realizar pruebas sin afectar a la lógica de negocio.

Tema 4: Configuración y secretos

1. ¿Cómo se lee un archivo .properties en Java y un archivo .ini en Python?
Para Java es java.util.properties, para Python es import configparser.

2. ¿Para qué sirve .gitignore y qué pasa si un archivo ya se subió antes de ignorarlo?
.gitignore sirve para decirle a git qué archivos no debe rastrear, como los temp, config local o en general archivos basura. Si un archivo ya fue subido antes de ignorarlo se va con todos estos archivos y no solo con el programa.

3. Busquen un caso real de contraseñas o llaves filtradas en GitHub: qué pasó y qué consecuencias tuvo.
Un contratista de CISA subió por error credenciales de administrador y llaves de acceso a una cuenta personal de Github, esto expuso archivos de configuración con llaves de acceso a AWS GovCloud, la CISA revocó el acceso del contratista, dio de baja el repositorio expuesto y auditó los registros de actividad. Afortunadamente nadie usó las llaves de acceso.
Fuente: CISA revela cómo un error en Github expuso llaves de AWS - Humberto Toledo 11 de julio de 2026

Tema 5: MariaDB desde el código

1. ¿Qué es JDBC y qué hace un driver? ¿Qué librería cumple ese papel en Python para MariaDB?
JDBC (Java DataBase Connectivity) es una API de Java que permite conectarse y trabajar con bases de datos, un driver es el componente que traduce las instrucciones de JDBC al lenguaje de la base de datos, en Python para trabajar con MariaDB se usa la librería mariadb.

2. ¿Qué es la inyección SQL? Muestren un ejemplo con el nombre de un personaje y expliquen por qué PreparedStatement (Java) o los parámetros %s (Python) la evitan.
Es una vulnerabilidad que permite a un atacante manipula consultas en una base de datos, entonces esto puede llegar a que los datos sean robados o que borren los datos. Tanto PreparedStatement (Java) o parámetros %s (Python) lo evitan porque separa el código SQL de los datos ingresados por el usuario. Digamos que un usuario ingresa un nombre que sea Guerrero, nivel = 999 entonces se crea un personaje el cual su nombre sea exactamente ese sin que el juego se altere y el personaje sigue empezando con nivel 1.

3. ¿Qué es una transacción y qué hace commit()? ¿Qué pasa en PyMySQL si no se llama?
En una transacción lo que se busca es cumplir ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad), entonces se crea un paquete de operaciones que garantizan que se cumplan todas o ninguna. Un commit sirve para guardar o documentar un progreso o cambio para que se suba y no quede solo en la sesión local. Si no se llama el commit en PyMySQL quedarían los cambios como borrados y se perderían luego por no guardar esos cambios con commit.

4. ¿Por qué hay que cerrar las conexiones? ¿Qué es try-with-resources en Java y with en Python?
Porque las bases de datos tienen un límite entonces puede llegar el momento en que no deje entrar a nadie más, me parece bien usar métodos guiándose por si un usuario o jugador está mucho tiempo AFK o sin registrar acciones lo mejor sería desconectarlo para darle paso a uno que sí vaya a jugar y no se sature el servidor con jugadores AFK.

Tema 6: MongoDB desde el código

1. ¿Qué es un ObjectId y qué información guarda por dentro?
Un objectid lo que hace es crear un identificador único por defecto a cada documento con un valor de 12 bytes.

2. ¿En qué se parece un documento de MongoDB a un HashMap de Java o a un dict de Python?
Se parecen en el modo en el que se accede a los datos, se accede por su nombre en vez de por su posición en el arreglo, se pueden meter documentos de otras y de diferentes tipos de datos. Lo diferente es que dict y HashMap están en la memoria RAM y MongoDB lo guarda en formato BSON en el disco.

3. ¿Qué diferencia hay entre MongoDB local, MongoDB Atlas y mongoplayground.net? ¿Cuál de los tres puede usar un programa en Java o Python?
Para MongoDB local el servidor queda dentro del computador en el disco duro con una conexión localhost: 27017, en MongoDB Atlas el servidor que se usa es la nube oficial de MongoDB en AWS, Google Cloud o Azure y para mongoplayground.net es una página web para practicar en el navegador, entonces playground es el único que no se puede conectar a Java o Python.

Tema 7: ORM

1. ¿Qué es un ORM?
Significa Object-Relational Mapping (Mapeo Objeto-Relacional). Lo que hace es trabajar con la base de datos como si fueran objetos sin escribir SQL a mano.

2. Nombren uno de Java y uno de Python.
Java: Hibernate.
Python: SQLAlchemy

3. Den una ventaja y una desventaja de usar un ORM en lugar de escribir el SQL a mano.
Ventaja: Puede trabajar con objetos y no repite SQL.
Desventaja: En consultas con muchos JOIN, es más confuso y lento que SQL a mano.