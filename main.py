# main.py

# Importacion de Vistas
from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto

# Importacion de Controllers
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import Proyectocontroller

# Importacion de Models
from models.empleado import Empleado
from models.departamento import Departamento
from models.proyecto import Proyecto    

empleado_controller = EmpleadoController()
departamento_controller = DepartamentoController()
proyecto_controller = Proyectocontroller()

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        # Empleado
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1.1":
                    # Código para crear empleado
                    rut = input("Ingrese el RUT del empleado: ")
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la dirección del empleado: ")
                    telefono = input("Ingrese el teléfono del empleado: ")
                    email = input("Ingrese el email del empleado: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    salario = float(input("Ingrese el salario del empleado: "))
                    departamento_id = int(input("Ingrese el ID del departamento: "))

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

                elif sub_opcion == "1.2":
                    # Código para listar empleados
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                        print(emp)

                elif sub_opcion == "1.3":
                    # Código para buscar empleado por RUT
                    rut = input("Ingrese el RUT del empleado a buscar: ")
                    empleado = empleado_controller.buscar_empleado_por_rut(rut)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")

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
                        salario = float(input("Ingrese el nuevo salario del empleado: "))
                        departamento_id = int(input("Ingrese el nuevo ID del departamento: "))

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

                elif sub_opcion == "1.5":
                    # Código para eliminar empleado
                    rut = input("Ingrese el RUT del empleado a eliminar: ")
                    empleado_controller.eliminar_empleado(rut)
                    print("Empleado eliminado exitosamente.")

                elif sub_opcion == "1.6":
                    break

        # Departamento
        elif opcion == "2":
            while True:
                menu_departamento()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "2.1":
                    nombre = input("Ingrese el nombre del departamento: ")
                    gerente_id = input("Ingrese el ID del gerente (opcional): ")
                    gerente_id = int(gerente_id) if gerente_id else None

                    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
                    departamento_controller.crear_departamento(nuevo_departamento)
                    print("Departamento creado exitosamente.")

                elif sub_opcion == "2.2":
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(dep)

                elif sub_opcion == "2.3":
                    id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        print(departamento)
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.4":
                    id_dep = int(input("Ingrese el ID del departamento a modificar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        nombre = input("Ingrese el nuevo nombre del departamento: ")
                        gerente_id = input("Ingrese el nuevo ID del gerente (opcional): ")
                        gerente_id = int(gerente_id) if gerente_id else None

                        departamento_modificado = Departamento(id=id_dep, nombre=nombre, gerente_id=gerente_id)
                        departamento_controller.modificar_departamento(departamento_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.5":
                    id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                    departamento_controller.eliminar_departamento(id_dep)
                    print("Departamento eliminado exitosamente.")

                elif sub_opcion == "2.6":
                    break

            while True:
                menu_proyecto()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "3.1":
                    nombre = input("Ingrese el nombre del proyecto: ")
                    id = input("Ingrese el ID del gerente (opcional): ")
                    id = int(id) if id else None

                    nuevo_proyecto = Proyecto(nombre=nombre, id=id)
                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                    print("Proyecto creado exitosamente.")

                elif sub_opcion == "3.2":
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(dep)

                elif sub_opcion == "3.3":
                    id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        print(departamento)
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "3.4":
                    id_dep = int(input("Ingrese el ID del departamento a modificar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        nombre = input("Ingrese el nuevo nombre del departamento: ")
                        gerente_id = input("Ingrese el nuevo ID del gerente (opcional): ")
                        gerente_id = int(gerente_id) if gerente_id else None

                        departamento_modificado = Departamento(id=id_dep, nombre=nombre, gerente_id=gerente_id)
                        departamento_controller.modificar_departamento(departamento_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "3.5":
                    id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                    departamento_controller.eliminar_departamento(id_dep)
                    print("Departamento eliminado exitosamente.")

                elif sub_opcion == "3.6":
                    break

        # Proyecto
        elif opcion == "3":
            while True:
                menu_proyecto()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "3.1":
                    nombre = input("Ingrese el nombre del proyecto: ")
                    descripcion = input("Ingrese la descripcion del proyecto: ")
                    fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
                    

                    nuevo_proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                    print("Proyecto creado exitosamente.")

                elif sub_opcion == "3.2":
                    proyectos = proyecto_controller.listar_proyecto()
                    for pro in proyectos:
                        print(pro)

                elif sub_opcion == "3.3":
                    id_pro = int(input("Ingrese el ID del proyecto a buscar: "))
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        print(proyecto)
                    else:
                        print("Proyecto no encontrado.")

                elif sub_opcion == "3.4":
                    id_pro = int(input("Ingrese el ID del departamento a modificar: "))
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        nombre = input("Ingrese el nuevo nombre del proyecto: ")
                        descripcion = input("Ingrese la nueva descripcion del proyecto: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio del proyecto (YYYY-MM-DD): ")

                        proyecto_modificado = Proyecto(id=id_pro, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio)
                        proyecto_controller.modificar_proyecto(proyecto_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "3.5":
                    id_pro = int(input("Ingrese el ID del proyecto a eliminar: "))
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        proyecto_controller.eliminar_proyecto(id_pro)
                        print("Proyecto eliminado exitosamente.")
                    else:
                        print("Proyecto no encontrado.")

                elif sub_opcion == "3.6":
                    break

        # Salir
        elif opcion == "4":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()



