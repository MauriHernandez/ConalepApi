from django.db import models

class Docente(models.Model):
    claveDocente = models.CharField(max_length=10, primary_key=True)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13)
    curp = models.CharField(max_length=18)
    fechaNacimiento = models.DateField()
    domicilio = models.TextField()
    telefonoDomicilio = models.CharField(max_length=13, null=True, blank=True)
    telefonoCelular = models.CharField(max_length=13)
    correoElectronico = models.EmailField(max_length=250)
    ciudadNacimiento = models.CharField(max_length=100)
    nivelEstudios = models.CharField(max_length=30, choices=[
        ('PROFESIONAL TECNICO BACHILLER', 'Profesional Técnico Bachiller'),
        ('LICENCIATURA TITULADA', 'Licenciatura Titulada'),
        ('PASANTE DE LICENCIATURA', 'Pasante de Licenciatura'),
        ('MAESTRIA TITULADA', 'Maestría Titulada'),
        ('BACHILLERATO', 'Bachillerato')])
    genero = models.CharField(max_length=10, choices=[('HOMBRE', 'Hombre'), ('MUJER', 'Mujer')])
    areasFormacion = models.CharField(max_length=100)
    fechaIngresoConalep = models.DateField()
    nivelDocente = models.CharField(max_length=20, choices=[
        ('INSTRUCTO C', 'Instructo C'),
        ('TECNICO CB I', 'Técnico CB I'),
        ('TECNICO CB II', 'Técnico CB II'),
        ('TECNICO INSTRUCTOR A', 'Técnico Instructor A')])
    estatus = models.BooleanField()
    turno = models.CharField(max_length=10, choices=[('MATUTINO', 'Matutino'), ('VESPERTINO', 'Vespertino')])
    horasFrenteGrupo = models.IntegerField()
    edad = models.IntegerField()
    horasBasificadas = models.IntegerField()

class NivelDocente(models.Model):
    nivelDocente = models.CharField(max_length=20, primary_key=True)
    sueldoBase = models.FloatField()

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    claveDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    nivelDocente = models.ForeignKey(NivelDocente, on_delete=models.CASCADE)
    frecuenciaPago = models.CharField(max_length=10, choices=[('QUINCENAL', 'Quincenal'), ('SEMESTRAL', 'Semestral')])
    totalPago = models.IntegerField()

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.TextField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    hora = models.IntegerField()
    modalidad = models.CharField(max_length=10, choices=[('VIRTUAL', 'Virtual'), ('PRESENCIAL', 'Presencial'), ('HIBRIDA', 'Híbrida')])
    rol = models.CharField(max_length=10, choices=[('IMPARTIDO', 'Impartido'), ('RECIBIDO', 'Recibido')])
    observaciones = models.TextField(null=True, blank=True)

class CursoDocente(models.Model):
    id_curso_docente = models.AutoField(primary_key=True)
    claveDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Carrera(models.Model):
    id_carrera = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=100)

class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    semestre = models.IntegerField()
    abrCarrera = models.CharField(max_length=4, choices=[('CONA', 'Cona'), ('ENFE', 'Enfe'), ('CDIA', 'Cdia'), ('INFO', 'Info'), ('N/A', 'N/A')], default='N/A')
    carrera = models.CharField(max_length=100, choices=[('CONTABILIDAD', 'Contabilidad'), ('ENFERMERIA', 'Enfermería'), ('CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL', 'Ciencia de Datos e Inteligencia Artificial'), ('INFORMATICA', 'Informática'), ('N/A', 'N/A')], default='N/A')
    nucleoFormacion = models.CharField(max_length=20, choices=[('DISCIPLINAR BASICA', 'Disciplinar Básica'), ('PROFESIONAL', 'Profesional'), ('TRAYECTO TECNICO', 'Trayecto Técnico')])

class Administrativo(models.Model):
    claveAdministrativo = models.CharField(max_length=10, primary_key=True)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    telefonoCelular = models.CharField(max_length=13)
    correoElectronico = models.EmailField(max_length=250)
    titulo = models.CharField(max_length=20, choices=[('LICENCIADO/A', 'Licenciado/a'), ('INGENIERO/A', 'Ingeniero/a'), ('MAESTRO/A', 'Maestro/a')])
    genero = models.CharField(max_length=10, choices=[('HOMBRE', 'Hombre'), ('MUJER', 'Mujer')])
    estatus = models.BooleanField()

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    abrCarrera = models.CharField(max_length=4, choices=[('CONA', 'Cona'), ('ENFE', 'Enfe'), ('CDIA', 'Cdia'), ('INFO', 'Info')])
    claveAdministrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField('Alumno', through='GrupoAlumno')

class GrupoAlumno(models.Model):
    id_grupo_alumno = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    matricula = models.ForeignKey('Alumno', on_delete=models.CASCADE)

class HorasClase(models.Model):
    id_horasClase = models.AutoField(primary_key=True)
    horaInicio = models.CharField(max_length=25)
    horaFin = models.CharField(max_length=25)
    cantidadHoras = models.IntegerField()

class HorasClaseGrupoModulo(models.Model):
    id_horasClase_grupoModulo = models.AutoField(primary_key=True)
    id_horasClase = models.ForeignKey(HorasClase, on_delete=models.CASCADE)
    id_grupo_modulo = models.ForeignKey('GrupoModulo', on_delete=models.CASCADE)
    diaSemana = models.CharField(max_length=10, choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miércoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes')])

class Alumno(models.Model):
    matricula = models.CharField(max_length=12, primary_key=True)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    curp = models.CharField(max_length=18)
    fechaNacimiento = models.DateField()
    domicilio = models.TextField()
    telefonoDomicilio = models.CharField(max_length=13, null=True, blank=True)
    telefonoCelular = models.CharField(max_length=13)
    correoElectronico = models.EmailField(max_length=250)
    ciudadNacimiento = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=[('HOMBRE', 'Hombre'), ('MUJER', 'Mujer')])
    estatus = models.BooleanField()
    turno = models.CharField(max_length=10, choices=[('MATUTINO', 'Matutino'), ('VESPERTINO', 'Vespertino')])

class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    claveDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    duracion = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=[('PSICOLOGIA', 'Psicología'), ('MATERIA', 'Materia')])
    modalidad = models.CharField(max_length=10, choices=[('INDIVIDUAL', 'Individual'), ('GRUPAL', 'Grupal')])
    estado = models.CharField(max_length=10, choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADA', 'Completada'), ('CANCELADA', 'Cancelada')])

class Recurso(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    url = models.TextField()
    tipo = models.CharField(max_length=10, choices=[('VIDEO', 'Video'), ('PDF', 'PDF'), ('IMAGEN', 'Imagen')])
    fecha_subida = models.DateTimeField()
    claveDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)

class GrupoModulo(models.Model):
    id_grupo_modulo = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    id_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
