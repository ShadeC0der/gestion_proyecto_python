# controllers/informes_controller.py

import pandas as pd
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import Proyectocontroller
from controllers.registro_tiempo_controller import RegistroDeTiempoController

class InformesController:
    def __init__(self):
        self.empleado_controller = EmpleadoController()
        self.departamento_controller = DepartamentoController()
        self.proyecto_controller = Proyectocontroller()
        self.registro_tiempo_controller = RegistroDeTiempoController()

    def generar_informe_empleados(self):
        empleados = self.empleado_controller.listar_empleados()
        df = pd.DataFrame(empleados, columns=[
            'ID', 'RUT', 'Nombre', 'Dirección', 'Teléfono', 'Email', 'Fecha Inicio', 'Salario', 'Departamento ID'
        ])
        df.to_excel('informe_empleados.xlsx', index=False)
        print("Informe de empleados generado exitosamente en 'informe_empleados.xlsx'.")

    def generar_informe_departamentos(self):
        departamentos = self.departamento_controller.listar_departamentos()
        df = pd.DataFrame(departamentos, columns=[
            'ID', 'Nombre', 'Gerente ID'
        ])
        df.to_excel('informe_departamentos.xlsx', index=False)
        print("Informe de departamentos generado exitosamente en 'informe_departamentos.xlsx'.")

    def generar_informe_proyectos(self):
        proyectos = self.proyecto_controller.listar_proyecto()
        df = pd.DataFrame(proyectos, columns=[
            'ID', 'Nombre', 'Descripción', 'Fecha Inicio'
        ])
        df.to_excel('informe_proyectos.xlsx', index=False)
        print("Informe de proyectos generado exitosamente en 'informe_proyectos.xlsx'.")

    def generar_informe_registros_tiempo(self):
        registros = self.registro_tiempo_controller.listar_registro()
        df = pd.DataFrame(registros, columns=[
            'ID', 'Fecha', 'Horas Trabajadas', 'Descripción', 'Empleado ID'
        ])
        df.to_excel('informe_registros_tiempo.xlsx', index=False)
        print("Informe de registros de tiempo generado exitosamente en 'informe_registros_tiempo.xlsx'.")
