class Departamento:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__reportes = []
        self.__palabras_clave_priorizacion = {
            'impacto_seguridad': {
                'alto': [],
                'medio': []
            },
            'afectacion_publica': {
                'alto': [],
                'medio': []
            },
            'posibilidad_agravamiento': {
                'alto': [],
                'medio': []
            }
        }

    def obtener_nombre(self):
        """Retorna el nombre del departamento"""
        return self.__nombre

    def agregar_reporte(self, reporte):
        """Añade un reporte al departamento"""
        reporte.cambiar_estado("asignado")
        reporte.establecer_indice_prioridad(self.__palabras_clave_priorizacion)
        self.__reportes.append(reporte)

    def obtener_reportes(self):
        """Retorna la lista de reportes"""
        return self.__reportes

    def __ordenar_reportes_por_prioridad(self):
        """Ordena los reportes por prioridad de mayor a menor"""
        self.__reportes.sort(key=lambda x: x.obtener_prioridad(), reverse=True)

    def atender_reporte_mayor_prioridad(self):
        """Atiende el reporte de mayor prioridad"""
        self.__ordenar_reportes_por_prioridad()
        if not self.__reportes:
            return False

        reporte_top = self.__reportes[0]
        reporte_top.cambiar_estado("resuelto")

        # Cambiar estado de otros reportes a postergado
        for reporte in self.__reportes[1:]:
            reporte.cambiar_estado("postergado")

        return True

    def registrar_evidencia(self, reporte, evidencia):
        """Registra evidencia para un reporte específico"""
        if reporte in self.__reportes:
            reporte.registrar_evidencia(evidencia)

    def agregar_palabras_clave_priorizacion(self, criterio, categoria='medio', tipo='impacto_seguridad'):
        """
        Añade keywords al departamento

        :param criterio: Palabra clave a añadir
        :param categoria: 'alto' o 'medio'
        :param tipo: Tipo de keyword (impacto_seguridad, afectacion_publica, posibilidad_agravamiento)
        """
        if tipo in self.__palabras_clave_priorizacion and categoria in self.__palabras_clave_priorizacion[tipo]:
            if criterio not in self.__palabras_clave_priorizacion[tipo][categoria]:
                self.__palabras_clave_priorizacion[tipo][categoria].append(criterio)

    def obtener_criterios_palabras_clave_priorizacion(self):
        """Retorna todos los criterios de clasificación"""
        criterios = []
        for tipo in self.__palabras_clave_priorizacion:
            for categoria in self.__palabras_clave_priorizacion[tipo]:
                criterios.extend(self.__palabras_clave_priorizacion[tipo][categoria])
        return criterios