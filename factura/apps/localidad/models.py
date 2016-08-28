from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
    	return "%s" % (self.nombre) 

class Estados(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
    	return "%s" % (self.nombre)

    def natural_key(self):
        return(self.nombre)

class Municipios(models.Model):
    nombre = models.CharField(max_length=100)
    estados = models.ForeignKey(Estados)
    
    def __unicode__(self):
    	return "%s" % (self.nombre)

    def natural_key(self):
        return(self.nombre)
