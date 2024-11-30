# Gestor de Laboratorios

 ![1732829091608](static/docs/image/readme/1732829091608.png)

## Descripción General

El Gestor de Laboratorios, GESLAB FS 1.0, es una aplicación web desarrollada usando el Framework Django y diseñada para llevar un  registro y control de instalaciones farmacéuticas, los productos que fabrica o produce, y de su representante o Director, posibilitando hacer gestión sobre los mismos.

## Características Principales

1. **Gestión de laboratorios:** Permite listar, crear, editar y eliminar laboratorios, pudiendo agregarse nuevos campos de ser necesario. Se captura el nombre del laboratorio, un alias, ciudad, país
  
   * Vista "Información de Laboratorios"

      ![info_labs.png](static/docs/image/readme/info_labs.PNG

   * Vista "Agregar Laboratorio"

      ![add_lab.png](static/docs/image/readme/form_labs.png)

   * Vista "Editar Laboratorio"

      ![edit_labs.png](static/docs/image/readme/edit_labs.png)

   * Vista "Eliminar Laboratorio"

      ![del_lab.png](static/docs/image/readme/del_lab.png)

2. **Gestión de Productos Farmacéuticos:** Permite listar, crear, editar y eliminar productos. Cada producto sólo puede pertenecer a un Laboratorio. Se puede asignar un año de vencimiento para control de stock. Se captura el nombre, laboratorio, año fabricación, año expiración, precio de costo y precio de venta.
  
   * Vista "Información de Productos"

      ![info_prods.png](static/docs/image/readme/info_prods.png)

   * Vista "Agregar Producto"

      ![add_prod.png](static/docs/image/readme/add_prod.png)

   * Vista "Editar Producto"

      ![edit_prod.png](static/docs/image/readme/edit_prod.png)

   * Vista "Eliminar Producto"

      ![del_prod.png](static/docs/image/readme/del_prod.png)

3. **Gestión de Directores:** Permite listar, crear, editar y eliminar Directores, pudiendo agregarse nuevos campos de ser necesario. cada Director, sólo puede pertenecer a un Laboratorio.
  
   * Vista "Información de Directores"

      ![info_dires.png](static/docs/image/readme/info_dires.png)

   * Vista "Agregar Director"

      ![add_dire.png](static/docs/image/readme/add_dire.png)

   * Vista "Editar Director"

      ![edit_dire.png](static/docs/image/readme/edit_dire.png)

   * Vista "Eliminar Director"

      ![del_dire.png](static/docs/image/readme/del_dire.png)

4. **Gestión del Sistema (ADMIN):** El sistema permite crear perfiles de usuario, grupos, asignar permisos,  etc.
  
   * Vista "Sitio Administrativo"

      ![sitio_admin.png](static/docs/image/readme/sitio_admin.png)

   * Vista "Gestión Laboratorios"

      ![sitio_admin_labs.png](static/docs/image/readme/sitio_admin_labs.png)

   * Vista "Gestión Productos"

      ![sitio_admin_prods.png](static/docs/image/readme/sitio_admin_prods.png)

   * Vista "Gestión Directores"

      ![sitio_admin_dires.png](static/docs/image/readme/sitio_admin_dires.png)

5. **Reportes:** Se pueden generar los siguientes informes: Información por Laboratorio, Producto y Director.

6. **Otras características:** El sistema incluye distintos métodos de búsqueda dinámicas y a través de filtros con selectores.

7. **Autenticación y Registro de Usuarios:** El sistema dispone de un módulo para el registro y autenticación de usuarios, otorgando varios niveles de seguridad y segregación de la información.
  
   * Vista "Login"

      ![login.png](static/docs/image/readme/login.png)

   * Vista "Registro"

      ![registro.png](static/docs/image/readme/registro.png)

## Consultas (queries) utilizando la shell de Django

1) Desde el ambiente virtual:

   ```bash

   python manage.py shell
   
   ```

2) Importar los modelos

   ```bash

   from laboratorio.models import Laboratorio, DirectorGeneral, Producto
   
   ```

3) Generar las consultas:

   3.1) Obtener todos los objetos: Laboratorio, DirectorGeneral y Productos.

   3.1.1) Obtiene y guarda todos los registros de la tabla Laboratorio. Genera un bucle para mostrar los elementos de la variable de uno en uno, son dos líneas de código

   ```bash

   labs = Laboratorio.objects.all() 
      for lab in labs: 
         print(lab)
   
   ```

   3.1.2) Los registros de la tabla DirectorGeneral

   ```bash

   dires = DirectorGeneral.objects.all()
     for dire in dires:
        print(dire)
   
   ```

   3.1.3) Los registros de la tabla Productos
  
   ```bash

   pds = Producto.objects.all()
     for pd in pds:
      print(pd)
   
   ```

3.2) Obtener el laboratorio del Producto cuyo nombre es ‘Producto 1’.

   ```bash

   pd_1 = Producto.objects.get(nom_prod='Producto1') # Primero, obtener el nombre del Producto 1 (debe ser el mismo)        
   lab_pd_1 = pd_1.lab_prod    # Encontrar el laboratorio por el producto asociado
   print(lab_pd_1)      # Imprimir el resultado
   
   ```

3.3) Listar y ordenar todos los productos por nombre, y muestre los valores de nombre y laboratorio.

   ```bash

   lista_productos_ordenados = Producto.objects.order_by('nom_prod')    # Primero, obtener todos los productos ordenados por nombre
    for producto in lista_productos_ordenados:        # Bucle para mostrar los resultados uno a uno
     print(producto.nom_prod, producto.lab_prod)        # se imprimen los elementos con sus atributos nombre y laboratorio
   
   ```

3.4) Imprimir por pantalla los laboratorios de todos los productos.

   ```bash

   for producto in Producto.objects.all():
      print(producto.lab_prod)
   
   ```

## Migraciones

Se procedió a actualizar el modelo inicial de datos agregando campos personalizados con el nombre "actualizado_campo".

* Se generan las migraciones luego de modificar los modelos, usando el comando "makemigrations"

  ```bash
  
  python python manage.py makemigrations laboratorio --name actualizado_campo
  
  ```

* Se aplican las migraciones usando el comando "migrate"

  ```bash
  
  python python manage.py makemigrations laboratorio --name actualizado_campo
  
  ```

  ```bash
  
  Migrations for 'laboratorio':
  laboratorio\migrations\0004_actualizado_campo.py
     + Add field alias_lab to laboratorio
     + Add field f_expiracion to producto
  laboratorio\migrations\0004_actualizado_campo.py
     + Add field alias_lab to laboratorio
     + Add field f_expiracion to producto
     + Add field alias_lab to laboratorio
     + Add field f_expiracion to producto
     + Add field f_expiracion to producto
  
  ```

## Tecnologías Utilizadas

* **Framework de Desarrollo:** Django 5.1.3.
* **Frontend:** HTML, CSS, JavaScript, Bootstrap.
* **Backend:** Python, Django.
* **Base de datos:** PostgreSQL v16.
* **Otras tecnologías:** Git, Github.

## Instalación y Configuración

1. **Clonar el repositorio:**

   ```bash

   https://github.com/jcordovaj/EvalM7.git
   
   ```

2. **Crear un entorno virtual:**

   * En Linux/macOS

   ```bash
   
   python -m venv venv_lab
   
   source venv_lab/bin/activate  
   
   ```

   * En Windows

   ```bash
   
   python -m venv venv_lab
   
   venv_lab\Scripts\activate 
   
   ```

3. **Instalar las dependencias:**

   ```bash
   
   pip install -r requirements.txt
   
   ```

4. **Configurar la base de datos:**

   * Crear usuario : userdjango
   * Password      : userdjango

   ```sql
   
   CREATE ROLE userdjango WITH LOGIN
      SUPERUSER
      CREATEDB
      CREATEROLE
      INHERIT
      NOREPLICATION
      BYPASSRLS
    CONNECTION LIMIT -1
    PASSWORD 'userdjango';
   
   ```

   * Crear BBDD

   Nombre: db_final_orm
   Usuario: userdjango (superuser)
   pass: userdjango
   collation: Spanish_spain.1252

5. **Ejecutar la aplicación:**

   ```bash
   
   python manage.py runserver
   
   ```

6. **Administrador del Sistema**

   * Administrador = Admin
   * Password      = 123456

7. **Generación de usuarios de prueba**

   Se ha empleado la siguiente nomenclatura para crear los usuarios de prueba.
   * user: usuarioX (X=Un número entero positivo correlativo)
   * correo: [usuarioX@usuarioX.com](mailto:usuarioX@usuarioX.com)
   * pass: clavefacil1234

## Contribución (Things-To-Do)

Se puede contribuir con los problemas o nuevas ideas, por favor respetar el estilo de programación y no subir código basura. Puede utilizar: forking del repositorio, crear pull requests, etc. Toda contribución es bienvenida.

## Licencia

Proyecto con fines educativos, Licencia MIT

## Autor

Jota Córdova - Fun Manager

* **Otros colaboradores**
  * Nelson Ramirez - Tutor
