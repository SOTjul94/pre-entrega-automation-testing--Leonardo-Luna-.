import test
import pytest
#lista de archivos a ejecutar
test_file = [
    "tests/test_login.py" ,
    "tests/test_inventory.py",
   "Tests/test_titulo.py"

]

# argumento para ejecutar las pruebas: archivos mas reporte html
pytest_args= test_file + ["-html=report.html","-self contained-html","-v"  ]


pytest.main(pytest_args)