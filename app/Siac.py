from app.Departamento import Departamento

class Siac:
    def __init__(self):
        self.__reportes_no_asignados = []
        self.__departamentos = [Departamento('EPMMOP'), Departamento('AMT'), Departamento('EMASEO')]
        self.__departamentos_clasificacion = {
            'EPMMOP': [
                'hueco', 'calle', 'asfalto', 'paso cebra',
                'EPMMOP', 'bache', 'puente', 'vía', 'acera', 'semáforo',
                'infraestructura', 'drenaje', 'reparación vial',
                'construcción', 'mantenimiento'
            ],
            'AMT': [
                'choque', 'congestionamiento', 'vehículo', 'accidente',
                'señalización', 'parqueo', 'patrullaje', 'control vehicular',
                'revisión técnica', 'zona azul'
            ],
            'EMASEO': [
                'basura', 'residuos', 'reciclaje', 'limpieza',
                'acumulación de desechos', 'recolección', 'contenedores',
                'desechos sólidos', 'escombros', 'saneamiento'
            ]
        }

    def agregar_nuevo_reporte_no_asignado(self, reporte):
        self.__reportes_no_asignados.append(reporte)

    def obtener_reportes_no_asignados(self):
        return self.__reportes_no_asignados

    def __calcular_confianza(self, descripcion, keywords):
        """
        Calcula el nivel de confianza basado en las coincidencias de palabras clave
        :param descripcion: Descripción del reporte
        :param keywords: Lista de palabras clave del departamento
        :return: Nivel de confianza como porcentaje (0-100)
        """
        descripcion_palabras = descripcion.split()
        coincidencias = sum(1 for palabra in descripcion_palabras if palabra in keywords)
        if len(descripcion_palabras) == 0:
            return 0
        return (coincidencias / len(descripcion_palabras)) * 100

    def __encontrar_departamento_por_clasificacion(self, reporte):
        """
        Encuentra el departamento basado en el nivel de confianza con palabras clave
        :param reporte: Reporte a clasificar
        :return: Departamento con mayor nivel de confianza, si supera el umbral, o None
        """
        descripcion = reporte.obtener_descripcion().lower()
        max_confianza = 0
        departamento_seleccionado = None

        for departamento, keywords in self.__departamentos_clasificacion.items():
            confianza = self.__calcular_confianza(descripcion, keywords)
            if confianza > max_confianza:
                max_confianza = confianza
                departamento_seleccionado = departamento

        # Definir un umbral mínimo de confianza (por ejemplo, 50%)
        if max_confianza >= 10:
            return departamento_seleccionado
        return None

    def asignar_automaticamente_reporte_a_departamento(self):
        for reporte in self.__reportes_no_asignados[:]:
            nombre_departamento = self.__encontrar_departamento_por_clasificacion(reporte)

            if nombre_departamento:
                departamento = next(
                    (dep for dep in self.__departamentos if dep.obtener_nombre() == nombre_departamento), None)

                if not departamento:
                    departamento = Departamento(nombre_departamento)
                    self.__departamentos.append(departamento)

                departamento.agregar_reporte(reporte)
                self.__reportes_no_asignados.remove(reporte)

    def asignar_manualmente_reporte_a_departamento(self, reporte, departamento):

        if departamento not in self.__departamentos:
            self.__departamentos.append(departamento)

        if reporte in self.__reportes_no_asignados:
            self.__reportes_no_asignados.remove(reporte)

        departamento.agregar_reporte(reporte)

    def agregar_criterios_clasificacion_por_departamento(self, departamento, criterios):
        """
        Añade criterios de clasificación a un departamento
        :param departamento: Departamento al que se añadirán los criterios
        :param criterios: Lista de criterios a añadir
        """
        if departamento not in self.__departamentos:
            raise ValueError(f"El departamento '{departamento}' no existe.")

        # Filtrar criterios duplicados
        criterios_existentes = set(self.__departamentos_clasificacion[departamento.obtener_nombre()])
        nuevos_criterios = [criterio for criterio in criterios if criterio not in criterios_existentes]

        # Añadir los nuevos criterios
        self.__departamentos_clasificacion[departamento.obtener_nombre()].extend(nuevos_criterios)

    def obtener_criterios_clasificacion_por_departamento(self, departamento):
        """
        Obtiene los criterios de clasificación de un departamento
        :param departamento: Departamento del que se obtendrán los criterios
        :return: Lista de criterios de clasificación
        """
        if departamento not in self.__departamentos:
            raise ValueError(f"El departamento '{departamento}' no existe.")

        return self.__departamentos_clasificacion[departamento.obtener_nombre()]