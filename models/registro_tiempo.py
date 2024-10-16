  
class RegistroDeTiempo:
    def __init__(self, id=None, fecha="", horasTrabajadas="", descripcion="", empleado_id=""):
        self._id = id
        self._fecha = fecha
        self._horasTrabajadas = horasTrabajadas
        self._descripcion = descripcion
        self._empleado_id = empleado_id

    # Getters
    def get_id(self):
        return self._id

    def get_fecha(self):
        return self._fecha

    def get_horasTrabajadas(self):
        return self._horasTrabajadas

    def get_descripcion(self):
        return self._descripcion
    
    def get_empleado_id(self):
        return self._empleado_id
    
    # Setters
    def set_id(self, id):
        self._id = id

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_horasTrabajadas(self, horasTrabajadas):
        self._horasTrabajadas = horasTrabajadas

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_empleado_id(self, empleado_id):
        self._empleado_id = empleado_id
