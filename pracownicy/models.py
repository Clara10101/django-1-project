from django.db import models

class Etaty(models.Model):
    nazwa = models.CharField(max_length=50)
    placa_od = models.DecimalField(max_digits=6,decimal_places=2)
    placa_do = models.DecimalField(max_digits=6,decimal_places=2)

    def __unicode__(self):
        return "%s (pk=%d)" % (self.nazwa, self.pk)

class Zespoly(models.Model):
    nazwa = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s (pk=%d)" % (self.nazwa, self.pk)

class Pracownicy(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    ID_etatu = models.ForeignKey(Etaty)
    ID_szefa = models.ForeignKey("self",null=True,blank=True)
    zatrudniony = models.DateTimeField('data zatrudnienia')
    placa_pod = models.DecimalField(max_digits=6,decimal_places=2)
    placa_dod = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    ID_zespolu = models.ForeignKey(Zespoly,null=True,blank=True)

    def __unicode__(self):
        return "%s %s (pk=%d)" % (self.imie, self.nazwisko, self.pk)
