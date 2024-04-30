from django.db import models
'''
# Create your models here.
class historique(models.Model):
    id_historique= models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #id_historique = models.ForeignKey(Historique, on_delete=models.CASCADE)
    delais= models.TextField()
    impact = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    resultat = models.TextField()
    class Meta:
        db_table = 'historique'
        '''