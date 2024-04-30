"""from django.db import models
#from user.models import User
#from historique.models import Historique

class Incident(models.Model):
    id_incident = models.AutoField(primary_key=True)
    #id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #id_historique = models.ForeignKey(Historique, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    impact = models.CharField(max_length=100)
    vidmage = models.FileField(upload_to='incident_vidmages/', blank=True, null=True)

    def __str__(self):
        return f"Incident {self.id_incident}"
   """ 
from django.db import models
from user.models import User
#from historique.models import Historique

class Incident(models.Model):
    id_incident = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #id_historique = models.ForeignKey(Historique, on_delete=models.CASCADE)
    description = models.TextField()
    impact = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    vidmage = models.FileField(upload_to='incident_vidmages/', blank=True, null=True)
    class Meta:
        db_table = 'incident'  # Ensure that the table name matches the actual table name in your database