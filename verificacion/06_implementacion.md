# Proyecto Django 

# Estructura del codigo 
Para el desarrollo del proyecto en Django, se optó por una arquitectura modular basada en apps independientes. Cada app agrupa funcionalidades específicas y está asignada a un equipo de trabajo, facilitando la escalabilidad, el mantenimiento y la colaboración entre desarrolladores.

Directory structure:
└── juanfcarrillo-servicios-ciudadanos/
    ├── README.md
    ├── LICENSE
    ├── manage.py
    ├── requirements.txt
    ├── setup.sh
    ├── sonar-project.properties
    ├── .python-version
    ├── ciudadano_app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── backends.py
    │   ├── decorators.py
    │   ├── forms.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_reserva.py
    │   │   ├── 0003_tiporeporte_reporte.py
    │   │   ├── 0004_areacomunal_reserva_ciudadano.py
    │   │   ├── 0004_delete_reporte_delete_tiporeporte.py
    │   │   ├── 0005_remove_reserva_id_areacomunal_hora_de_apertura_and_more.py
    │   │   ├── 0006_alter_areacomunal_hora_de_apertura_and_more.py
    │   │   ├── 0007_areacomunal_espacio_publico_reserva_estado_reserva_and_more.py
    │   │   ├── 0008_merge_20250130_1245.py
    │   │   ├── 0009_remove_ciudadano_groups_and_more.py
    │   │   ├── 0010_ciudadano_sector_ciudadano_sectores_de_interes_and_more.py
    │   │   └── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── area_comunal.py
    │   │   ├── servicio_notificacion_correo.py
    │   │   ├── ciudadano/
    │   │   │   ├── ciudadano.py
    │   │   │   └── gestor_ciudadano.py
    │   │   └── reserva/
    │   │       ├── repositorio_reserva.py
    │   │       ├── reserva.py
    │   │       └── servicio_reserva.py
    │   ├── templates/
    │   │   ├── bienvenida.html
    │   │   ├── dashboard.html
    │   │   ├── login_ciudadano.html
    │   │   ├── registro_ciudadano.html
    │   │   ├── canales/
    │   │   │   ├── detalle_canal.html
    │   │   │   ├── lista_canales.html
    │   │   │   ├── muro.html
    │   │   │   ├── notificaciones.html
    │   │   │   └── partials/
    │   │   │       ├── comentario_form.html
    │   │   │       ├── noticia_detalle.html
    │   │   │       └── reaccionar_form.html
    │   │   ├── eventos/
    │   │   │   └── lista_eventos.html
    │   │   └── reporte/
    │   │       └── envio_reporte.html
    │   └── views/
    │       ├── __init__.py
    │       ├── bienvenida.py
    │       ├── dashboard.py
    │       ├── login.py
    │       ├── registro.py
    │       ├── canales/
    │       │   ├── canales.py
    │       │   ├── noticia.py
    │       │   ├── notificacion.py
    │       │   └── suscripcion.py
    │       ├── eventos/
    │       │   └── lista_eventos.py
    │       └── reporte/
    │           └── envio_reporte.py
    ├── entidad_municipal_app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── backends.py
    │   ├── decorators.py
    │   ├── forms.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_eventomunicipal_cupos_disponibles.py
    │   │   ├── 0003_remove_registroasistencia_fecha_actualizacion_and_more.py
    │   │   ├── 0004_entidadmunicipal.py
    │   │   ├── 0005_alter_entidadmunicipal_options_and_more.py
    │   │   ├── 0006_canalinformativo_noticia_comentario_reaccion_and_more.py
    │   │   ├── 0006_departamento.py
    │   │   ├── 0006_espaciopublico.py
    │   │   ├── 0007_alter_entidadmunicipal_correo_electronico_and_more.py
    │   │   ├── 0007_remove_departamento_fecha_creacion.py
    │   │   ├── 0008_alter_entidadmunicipal_correo_electronico_and_more.py
    │   │   ├── 0008_reportemunicipal.py
    │   │   ├── 0009_merge_20250129_2214.py
    │   │   ├── 0009_reportemunicipal_reporte_ciudadano.py
    │   │   ├── 0010_merge_20250129_2318.py
    │   │   ├── 0011_merge_20250130_1245.py
    │   │   ├── 0012_alter_comentario_ciudadano_and_more.py
    │   │   ├── 0013_alter_entidadmunicipal_options_and_more.py
    │   │   ├── 0014_alter_entidadmunicipal_password.py
    │   │   ├── 0014_canalinformativo_entidad_municipal.py
    │   │   ├── 0014_espaciopublico_direccion_and_more.py
    │   │   ├── 0015_entidadmunicipal_groups_and_more.py
    │   │   ├── 0016_merge_20250201_1345.py
    │   │   ├── 0016_merge_20250201_1739.py
    │   │   ├── 0017_alter_eventomunicipal_motivo_cancelacion.py
    │   │   ├── 0018_eventomunicipal_entidad_municipal.py
    │   │   ├── 0019_espaciopublico_descripcion_and_more.py
    │   │   ├── 0020_merge_20250203_1703.py
    │   │   └── __init__.py
    │   ├── models/
    │   │   ├── EntidadMunicipal.py
    │   │   ├── __init__.py
    │   │   ├── espacio_publico.py
    │   │   ├── canales/
    │   │   │   ├── __init__.py
    │   │   │   ├── canal_informativo.py
    │   │   │   ├── comentario.py
    │   │   │   ├── noticia.py
    │   │   │   └── reaccion.py
    │   │   ├── departamento/
    │   │   │   ├── departamento.py
    │   │   │   ├── repositorio_departamento.py
    │   │   │   ├── repositorio_departamento_django.py
    │   │   │   └── servicio_departamento.py
    │   │   ├── evento/
    │   │   │   ├── __init__.py
    │   │   │   ├── evento_municipal.py
    │   │   │   ├── registro_asistencia.py
    │   │   │   └── repositorio_eventos.py
    │   │   └── reporte/
    │   │       ├── reporte_municipal.py
    │   │       ├── repositorio_de_reporte_municipal.py
    │   │       ├── repositorio_de_reporte_municipal_django.py
    │   │       └── servicio_de_reporte_municipal.py
    │   ├── templates/
    │   │   ├── canales/
    │   │   │   ├── crear_canal.html
    │   │   │   ├── detalle_noticia.html
    │   │   │   ├── lista_canales_administrados.html
    │   │   │   ├── listado_noticias.html
    │   │   │   └── partials/
    │   │   │       ├── alerta_rapida_form.html
    │   │   │       └── crear_noticia_form.html
    │   │   └── entidad/
    │   │       ├── dashboard.html
    │   │       ├── login.html
    │   │       ├── login_entidad.html
    │   │       ├── eventos/
    │   │       │   ├── evento.html
    │   │       │   └── gestor_eventos.html
    │   │       └── reportes/
    │   │           ├── lista_reportes.html
    │   │           ├── resolver_reporte.html
    │   │           └── styles.css
    │   └── views/
    │       ├── __init__.py
    │       ├── bienvenida.py
    │       ├── dashboard.py
    │       ├── login.py
    │       ├── canales/
    │       │   ├── gestion_canal.py
    │       │   └── gestion_noticias.py
    │       ├── eventos/
    │       │   ├── evento.py
    │       │   └── gestor_eventos.py
    │       └── reportes/
    │           ├── agregar_evidencia.py
    │           ├── lista_reportes.py
    │           ├── postergar_reporte.py
    │           └── resolver_reporte.py
    ├── features/
    │   ├── canales_informativos_municipales.feature
    │   ├── control_asistencia.feature
    │   ├── enviar_reporte_por_parte_de_un_ciudadano.feature
    │   ├── environment.py
    │   ├── manejar_reportes.feature
    │   ├── notificar_reportes_y_estados_de_sectores_de_interes.feature
    │   ├── organizar_eventos_publicos_masivos.feature
    │   ├── realizar_actividades_grupales.feature
    │   └── steps/
    │       ├── canales_informativos_municipales_pasos.py
    │       ├── enviar_reporte_por_parte_de_un_ciudadano.py
    │       ├── manejar_reportes.py
    │       ├── notificar_reportes_y_estados_de_sectores_de_interes.py
    │       ├── organizar_eventos_publicos_masivos.py
    │       ├── realizar_actividades_grupales.py
    │       └── steps_control_asistencia.py
    ├── mocks/
    │   ├── repositorio_de_departamento_en_memoria.py
    │   ├── repositorio_de_reporte_en_memoria.py
    │   ├── repositorio_de_reporte_municipal_en_memoria.py
    │   ├── repositorio_eventos_memoria.py
    │   └── repositorio_reserva_en_memoria.py
    ├── servicios_ciudadanos/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── shared/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── decorators.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_alter_tiporeporte_departamento.py
    │   │   ├── 0003_alter_reporte_ciudadano.py
    │   │   ├── 0004_sector_alter_reporte_ciudadano_notificacion.py
    │   │   ├── 0005_notificacion_titulo.py
    │   │   ├── 0006_alter_notificacion_titulo.py
    │   │   └── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── ciudad/
    │   │   │   ├── ciudad.py
    │   │   │   ├── sector.py
    │   │   │   ├── servicio_de_estado_sector.py
    │   │   │   └── servicio_reporte_por_sector.py
    │   │   ├── notificacion/
    │   │   │   ├── notificacion.py
    │   │   │   └── servicio_de_notificacion.py
    │   │   └── reporte/
    │   │       ├── reporte.py
    │   │       ├── repositorio_de_reporte.py
    │   │       ├── repositorio_de_reporte_django.py
    │   │       ├── servicio_de_reporte.py
    │   │       └── tipo_reporte.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── error_session.html
    │   │   ├── landing_page.html
    │   │   └── includes/
    │   │       ├── footer.html
    │   │       └── header.html
    │   └── views/
    │       ├── __init__.py
    │       ├── error_session.py
    │       ├── landing_page.py
    │       └── logout.py
    ├── theme/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── package-lock.json
    │   ├── static_src/
    │   │   ├── package-lock.json
    │   │   ├── package.json
    │   │   ├── postcss.config.js
    │   │   ├── tailwind.config.js
    │   │   ├── .gitignore
    │   │   └── src/
    │   │       └── styles.css
    │   └── templates/
    │       └── base.html
    └── .github/
        └── workflows/
            └── ci.yml
