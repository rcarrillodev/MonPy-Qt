MonPy-Qt
========

Este proyecto ha sido descontinuado dado que la url que se usaba ya no existe.
==============================================================================


MonPy es una pequeña aplicacion realizada en Python con ayuda de PyQt que permite consultar el tipo de cambio en
distintas monedas del mundo.

Las monedas que soporta son:

+ Dolar Australiano – AUD
+ Dolar Canadiense – CAD
+ Euro -EUR
+ Libra – GBP
+ Rupia Hindú – INR
+ Yen Japonés -JPY
+ Peso Mexicano – MXN
+ Yuán Chino – RMB
+ Dolar Singapurense – SGD
+ Bath Thailandés – THB
+ Dolar Americano – USD 

Su funcion tiene como base la Google Calculator, por lo tanto esta sujeto a la actualidad de los datos en el servicio.

Requisitos del Sistema:
=======================

+ Python 2.6 +
+ QT4
+ PyQt4

En la seccion de descargas de éste repositorio esta un paquete para Linux que incluye MonPy listo para ser ejecutado sin
necesidad de instalar algun paquete adicional.

La version para WINDOWS ya incluye las librerias y básta solo con ejecutar el .exe para arrancar el programa.


Como Usar?
----------
+ Al abrir el programa introduzca en el primer cuadro de texto la cantidad a ser convertida
+ Seleccione de la primer lista la moneda local (desde donde esta haciendo la conversion) y en la siguiente lista la moneda a la cual desea convertir la cantidad especificada.
+ En el cuadro de abajo aparecera la cantidad convertida.

Guardando Moneda Preferida
--------------------------
+ Especifique en las listas las monedas que desea que se guarden como moneda preferida y dé clic en el boton del engrane

La moneda preferida se mantendrá guardada en un archivo del programa, en caso de que no tenga internet se cargara la moneda preferida con la ultima actualizacion de conversion para poder usar el programa sin conexion.

Actualizando Moneda
-------------------
En caso de desconexion mientras usa el programa o si desea actualizar la conversion dé clic en el boton de actualizar para volver a obtener la conversion sde el servicio de internet


--------------------------------------------------------------------------------------------


Licencia
========

Éste programa esta bajo licencia GPL/GNU para uso y modificacion publica, cualquier obra deribada de ésta misma deberá
conceder acceso al codigo fuente como está especificado en el documento : http://www.gnu.org/licenses/gpl.txt

Preguntas, Sugerencias y / o reportes de problemas por éste medio en el apartado "Issues" o bien en la pagina de la 
aplicacion:
http://rafuru.github.com/MonPy-Qt


Release Log:
============

+ (1.0) 16-Jul-2012 : Version Inicial
+ (1.5)	11-Ago-2012 : 
	+ [Nuevo] Opcion para guaradar moneda preferida
	+ [Nuevo] Opcion para actualizar la moneda actual
	+ [BugFix]	Optimizado el uso de conexion y modo off-line para moneda preferida
	+ [BugFix]	Mejoras en el codigo (muchas)
