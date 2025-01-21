from datetime import datetime
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass


class EstadoReporte(Enum):
    CLASIFICANDO = "clasificando"
    NO_ASIGNADO = "noAsignado"
    ASIGNADO = "asignado"
    POSTERGADO = "postergado"
    RESOLVIENDO = "resolviendo"
    SOLUCIONADO = "solucionado"


@dataclass
class Departamento:
    id: int
    nombre: str
    recursos_disponibles: bool = True
    palabras_clave: List[str] = None


@dataclass
class Evidencia:
    descripcion: str
    fotos: List[str]
    fecha_registro: datetime


@dataclass
class Reporte:
    id: int
    descripcion: str
    estado: EstadoReporte
    fecha_creacion: datetime
    ubicacion: str
    departamento: Optional[Departamento] = None
    nivel_confianza: float = 0.0
    evidencias: List[Evidencia] = None
    fecha_estimada: Optional[datetime] = None
    motivo_postergacion: Optional[str] = None
    historial_estados: List[dict] = None

    def cambiar_estado(self, nuevo_estado: EstadoReporte, motivo: str = None):
        if self.historial_estados is None:
            self.historial_estados = []

        self.historial_estados.append({
            "estado_anterior": self.estado,
            "estado_nuevo": nuevo_estado,
            "fecha": datetime.now(),
            "motivo": motivo
        })
        self.estado = nuevo_estado


@dataclass
class SolucionReporte:
    reporte_id: int
    accion_realizada: str
    evidencia: Evidencia
    tiempo_empleado: str
    fecha_solucion: datetime