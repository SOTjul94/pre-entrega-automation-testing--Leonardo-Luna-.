
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

Iniciar sesión con credenciales válidas e inválidas
Verificación del catálogo de productos
Interacción con el carrito de compras (añadir productos y verificar su contenido)
Verificación de existencia del menú y otros elementos del sitio
🛠️ Tecnologías Utilizadas
Python : lenguaje de programación principal
Pytest : Framework de pruebas para estructurar y ejecutar pruebas
Selenium WebDriver : Para la automatización de la interfaz web
Git/GitHub : Para controlar versiones y compartir el código
📁 Estructura del Proyecto
preentrega_G.oliverio/

Copy to BlackBox
    ├── images/     # Carpeta con capturas de pantalla
    ├── tests/      # Carpeta contenedora de los diferentes tests y funciones
        ├── Objects # Carpeta contenedora del archivo Register con datos necesarios para realizar los test.
        └── baseActions  # Carpeta contenderod de distintas funciones reutilizables      
    ├── conftest.py # Configuraciones adicionales para pytest 
    ├── run_test.py # Aplicacion para la ejecucion de todos los tests
    ├── pytest.ini  # Archvivo configuracion pytest
    ├── Requirements.txt # Requerimientos para ejecutar los tests
    └── READNE.md   # Este archivo
⚙️ Instalación de Dependencias
Asegúrese de tener Python 3.7 o superior instalado.
Instale las dependencias necesarias:
pip instalar selenio pytest pytest-html

Descargue el WebDriver correspondiente a su navegador:

Controlador de Chrome

GeckoDriver (Firefox)

Asegúrese de que el WebDriver esté en su PATH o especifique su ubicación en el código.

▶️Ejecución de las Pruebas
Para ejecutar todas las pruebas: python3 -m pytest runtest.py

Para generar un informe HTML: El informe se genera automáticamente. Se puede cancelar esta opción desde pytest.ini

✅ Funcionalidades Implementadas
Automatización de inicio de sesión Caso de éxito con credenciales válidas

Verificación del Catálogo Comprobación del título de la página Verificación de presencia de productos Validación de elementos de la interfaz (menú, filtros, etc.)

Interacción con el Carrito Añadir producto al carrito Verificar que el contador se incrementa

Navegar al carrito

Comprobar que el producto añadido aparece correctamente en el carrito de compras

✨ Características adicionales
Funciones auxiliares reutilizables: En los archivos:
Copy to BlackBox
└── tests/      
    └── baseActions
        ├── acciones_base.py
        └── usuario_acciones.py
Datos modificables para reutilizar la aplicación en caso de una nueva versión: En el archivo:
Copy to BlackBox
└── tests/      
    └── Objects
        └── Register.py

