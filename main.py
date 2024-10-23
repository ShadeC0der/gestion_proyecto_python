# main.py

# Importacion de Vista
from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto, menu_registrodetiempo, menu_informes

# Importacion de Controllers
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import Proyectocontroller
from controllers.registro_tiempo_controller import RegistroDeTiempoController
from controllers.informes_controller import InformesController

# Importacion de Models
from models.empleado import Empleado
from models.departamento import Departamento
from models.proyecto import Proyecto
from models.registro_tiempo import RegistroDeTiempo

#añadir controllers
empleado_controller = EmpleadoController()
departamento_controller = DepartamentoController()
proyecto_controller = Proyectocontroller()
registro_de_tiempo_controller = RegistroDeTiempoController()
informes_controller = InformesController()

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        # Empleado
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                # Opcion 1
                if sub_opcion == "1.1":
                    # Código para crear empleado
                    rut = input("Ingrese el RUT del empleado: ")
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la dirección del empleado: ")
                    telefono = input("Ingrese el teléfono del empleado: ")
                    email = input("Ingrese el email del empleado: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    try:
                        salario = float(input("Ingrese el salario del empleado: "))
                    except ValueError:
                        print("Error: El salario debe ser un número.")
                        continue  # Volver al inicio del bucle para reintentar
                    try:
                        departamento_id = int(input("Ingrese el ID del departamento: "))
                    except ValueError:
                        print("Error: El ID del departamento debe ser un número entero.")
                        continue  # Volver al inicio del bucle para reintentar

                    nuevo_empleado = Empleado(
                        rut=rut, 
                        nombre=nombre, 
                        direccion=direccion, 
                        telefono=telefono, 
                        email=email, 
                        fecha_inicio=fecha_inicio, 
                        salario=salario, 
                        departamento_id=departamento_id
                    )
                    
                    empleado_controller.crear_empleado(nuevo_empleado)
                    print("Empleado creado exitosamente.")

                # Opcion 2
                elif sub_opcion == "1.2":
                    # Código para listar empleados
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                        print(emp)

                # Opcion 3
                elif sub_opcion == "1.3":
                    # Código para buscar empleado por RUT
                    rut = input("Ingrese el RUT del empleado a buscar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")

                # Opcion 4
                elif sub_opcion == "1.4":
                    # Código para modificar empleado
                    rut = input("Ingrese el RUT del empleado a modificar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        nombre = input("Ingrese el nuevo nombre del empleado: ")
                        direccion = input("Ingrese la nueva dirección del empleado: ")
                        telefono = input("Ingrese el nuevo teléfono del empleado: ")
                        email = input("Ingrese el nuevo email del empleado: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
                        try:
                            salario = float(input("Ingrese el nuevo salario del empleado: "))
                        except ValueError:
                            print("Error: El salario debe ser un número.")
                            continue  # Volver al inicio del bucle para reintentar
                        try:
                            departamento_id = int(input("Ingrese el nuevo ID del departamento: "))
                        except ValueError:
                            print("Error: El ID del departamento debe ser un número entero.")
                            continue  # Volver al inicio del bucle para reintentar

                        empleado_modificado = Empleado(
                            id=empleado[0],
                            rut=rut,
                            nombre=nombre,
                            direccion=direccion,
                            telefono=telefono,
                            email=email,
                            fecha_inicio=fecha_inicio,
                            salario=salario,
                            departamento_id=departamento_id
                        )
                        
                        empleado_controller.modificar_empleado(empleado_modificado)
                        print("Empleado modificado exitosamente.")
                    else:
                        print("Empleado no encontrado.")

                # Opcion 5
                elif sub_opcion == "1.5":
                    # Código para eliminar empleado
                    rut = input("Ingrese el RUT del empleado a eliminar: ")
                    empleado_controller.eliminar_empleado(rut)
                    print("Empleado eliminado exitosamente.")

                # Opcion 6
                elif sub_opcion == "1.6":
                    break
                
                # Opcion no Valida
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

        # Departamento
        elif opcion == "2":
            while True:
                menu_departamento()
                sub_opcion = input("Seleccione una opción: ")
                
                # Opcion 1
                if sub_opcion == "2.1":
                    # Crear departamento
                    nombre = input("Ingrese el nombre del departamento: ")
                    gerente_id_input = input("Ingrese el ID del gerente (opcional): ")
                    try:
                        gerente_id = int(gerente_id_input) if gerente_id_input else None
                    except ValueError:
                        print("Error: El ID del gerente debe ser un número entero.")
                        continue  # Volver al inicio del bucle para reintentar

                    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
                    departamento_controller.crear_departamento(nuevo_departamento)
                    print("Departamento creado exitosamente.")

                # Opcion 2
                elif sub_opcion == "2.2":
                    # Listar departamentos
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(dep)

                # Opcion 3
                elif sub_opcion == "2.3":
                    # Buscar departamento por ID
                    try:
                        id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                    except ValueError:
                        print("Error: El ID del departamento debe ser un número entero.")
                        continue
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        print(departamento)
                    else:
                        print("Departamento no encontrado.")

                # Opcion 4
                elif sub_opcion == "2.4":
                    # Modificar departamento
                    try:
                        id_dep = int(input("Ingrese el ID del departamento a modificar: "))
                    except ValueError:
                        print("Error: El ID del departamento debe ser un número entero.")
                        continue
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        nombre = input("Ingrese el nuevo nombre del departamento: ")
                        gerente_id_input = input("Ingrese el nuevo ID del gerente (opcional): ")
                        try:
                            gerente_id = int(gerente_id_input) if gerente_id_input else None
                        except ValueError:
                            print("Error: El ID del gerente debe ser un número entero.")
                            continue

                        departamento_modificado = Departamento(id=id_dep, nombre=nombre, gerente_id=gerente_id)
                        departamento_controller.modificar_departamento(departamento_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                # Opcion 5
                elif sub_opcion == "2.5":
                    # Eliminar departamento
                    try:
                        id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                    except ValueError:
                        print("Error: El ID del departamento debe ser un número entero.")
                        continue
                    confirmacion = input(f"¿Está seguro que desea eliminar el departamento con ID {id_dep}? (s/n): ")
                    if confirmacion.lower() == 's':
                        resultado = departamento_controller.eliminar_departamento(id_dep)
                        if resultado:
                            print("Departamento eliminado exitosamente.")
                        else:
                            print("Departamento no encontrado o no se pudo eliminar.")
                    else:
                        print("Operación cancelada.")

                # Opcion 6
                elif sub_opcion == "2.6":
                    break
                
                # Opcion no Valida
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

        # Proyecto
        elif opcion == "3":
            while True:
                menu_proyecto()
                sub_opcion = input("Seleccione una opción: ")
                
                # Opcion 1
                if sub_opcion == "3.1":
                    # Crear proyecto
                    nombre = input("Ingrese el nombre del proyecto: ")
                    descripcion = input("Ingrese la descripción del proyecto: ")
                    fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")

                    nuevo_proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                    print("Proyecto creado exitosamente.")

                # Opcion 2
                elif sub_opcion == "3.2":
                    # Listar proyectos
                    proyectos = proyecto_controller.listar_proyecto()
                    for pro in proyectos:
                        print(pro)

                # Opcion 3
                elif sub_opcion == "3.3":
                    # Buscar proyecto por ID
                    try:
                        id_pro = int(input("Ingrese el ID del proyecto a buscar: "))
                    except ValueError:
                        print("Error: El ID del proyecto debe ser un número entero.")
                        continue
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        print(proyecto)
                    else:
                        print("Proyecto no encontrado.")

                # Opcion 4
                elif sub_opcion == "3.4":
                    # Modificar proyecto
                    try:
                        id_pro = int(input("Ingrese el ID del proyecto a modificar: "))
                    except ValueError:
                        print("Error: El ID del proyecto debe ser un número entero.")
                        continue
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        nombre = input("Ingrese el nuevo nombre del proyecto: ")
                        descripcion = input("Ingrese la nueva descripción del proyecto: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD): ")

                        proyecto_modificado = Proyecto(id=id_pro, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
                        proyecto_controller.modificar_proyecto(proyecto_modificado)
                        print("Proyecto modificado exitosamente.")
                    else:
                        print("Proyecto no encontrado.")

                # Opcion 5
                elif sub_opcion == "3.5":
                    # Eliminar proyecto
                    try:
                        id_pro = int(input("Ingrese el ID del proyecto a eliminar: "))
                    except ValueError:
                        print("Error: El ID del proyecto debe ser un número entero.")
                        continue
                    confirmacion = input(f"¿Está seguro que desea eliminar el proyecto con ID {id_pro}? (s/n): ")
                    if confirmacion.lower() == 's':
                        resultado = proyecto_controller.eliminar_proyecto(id_pro)
                        if resultado:
                            print("Proyecto eliminado exitosamente.")
                        else:
                            print("Proyecto no encontrado o no se pudo eliminar.")
                    else:
                        print("Operación cancelada.")

                # Opcion 6
                elif sub_opcion == "3.6":
                    break
                
                # Opcion no Valida
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

        # Registro de tiempo
        elif opcion == "4":
            while True:
                menu_registrodetiempo()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "4.1":
                    fecha = input("Ingrese la fecha del registro de tiempo (YYYY-MM-DD): ")
                    horasTrabajadas = float(input("Ingrese las Horas trabajadas: "))
                    descripcion = input("Ingrese la descripcion del proyecto: ")
                    empleado_id = input("Ingrese el id del empleado: ")
                    
                    nuevo_registro = RegistroDeTiempo(fecha=fecha, horasTrabajadas=horasTrabajadas, descripcion=descripcion, empleado_id=empleado_id)
                    registro_de_tiempo_controller.crear_registro(nuevo_registro)
                    print("Registro creado exitosamente.")

                elif sub_opcion == "4.2":
                    registro = registro_de_tiempo_controller.listar_registro()
                    for reg in registro:
                        print(reg)

                elif sub_opcion == "4.3":
                    id_reg = int(input("Ingrese el ID del registro a buscar: "))
                    registro = registro_de_tiempo_controller.buscar_registro_por_id(id_reg)
                    if registro:
                        print(registro)
                    else:
                        print("Registro no encontrado.")

                elif sub_opcion == "4.4":
                    id_reg = int(input("Ingrese el ID del departamento a modificar: "))
                    registro = registro_de_tiempo_controller.buscar_registro_por_id(id_reg)
                    if registro:
                        fecha = input("Ingrese la nueva fecha del registro de tiempo (YYYY-MM-DD): ")
                        horasTrabajadas = float(input("Ingrese las nuevas Horas trabajadas: "))
                        descripcion = input("Ingrese la nueva descripcion del proyecto: ")
                        empleado_id = input("Ingrese el nuevo id del empleado: ")
                    
                        nuevo_registro = RegistroDeTiempo(fecha=fecha, horasTrabajadas=horasTrabajadas, descripcion=descripcion, empleado_id=empleado_id, id=id_reg)
                        registro_de_tiempo_controller.modificar_registro(nuevo_registro)
                        print("Registro modificado exitosamente.")
                    else:
                        print("Registro no encontrado.") 

                elif sub_opcion == "4.5":
                    id_reg = int(input("Ingrese el ID del registro a eliminar: "))
                    registro = registro_de_tiempo_controller.buscar_registro_por_id(id_reg)
                    if registro:
                        registro_de_tiempo_controller.eliminar_registro(id_reg)
                        print("Registro eliminado exitosamente.")
                    else:
                        print("Registro no encontrado.")

                elif sub_opcion == "4.6":
                    break

        # Generación de Informes
        elif opcion == "5":
            while True:
                menu_informes()
                sub_opcion = input("Seleccione una opción: ")

                # Permitir que el usuario ingrese "5.1" o "1"
                if sub_opcion == "5.1":
                    informes_controller.generar_informe_empleados()
                elif sub_opcion == "5.2":
                    informes_controller.generar_informe_departamentos()
                elif sub_opcion == "5.3":
                    informes_controller.generar_informe_proyectos()
                elif sub_opcion == "5.4":
                    informes_controller.generar_informe_registros_tiempo()
                elif sub_opcion == "5.5":
                    informes_controller.generar_informe_empleados_pdf()
                elif sub_opcion == "5.6":
                    break  # Volver al menú principal
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

        # Salir
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()



