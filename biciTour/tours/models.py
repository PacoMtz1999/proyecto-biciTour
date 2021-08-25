from django.db import models

# Create your models here.

class recorridos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID")
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.TextField()
    ciudad = models.TextField()
    kmReco = models.TextField()
    tieEsti = models.TextField()
    pInicio = models.TextField()
    costo = models.FloatField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen recorrido")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["-created"]

    def __str__(self):
        return self.ciudad


class mensajeContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField(verbose_name="Usuario")
    email = models.EmailField(verbose_name="Correo Electronico")
    asunto = models.TextField(verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre


class registrameRecorrido(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID")
    nombre = models.TextField(verbose_name="Usuario(s)")
    email = models.EmailField(verbose_name="Correo electrónico")
    recorrido = models.TextField(verbose_name="Nombre del recorrido")
    telefono = models.TextField(verbose_name="Número de teléfono")
    nPersonas = models.TextField(verbose_name="Participantes del recorrido")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ["-created"]

    def __str__(self):
        return self.recorrido