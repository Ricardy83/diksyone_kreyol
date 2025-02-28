from django.db import models




class Mot(models.Model):
    CATEGORIES = [
        ('non', 'Non'),
        ('vèb', 'Vèb'),
        ('adjektif', 'Adjektif'),
        ('advèb', 'Advèb'),
        ('ekspresyon', 'Ekspresyon'),
    ]
    mot = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    exemple = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.mot

class Synonyme(models.Model):
    mot = models.ForeignKey(Mot, related_name='sinonim', on_delete=models.CASCADE)
    synonyme = models.CharField(max_length=100)

class Antonyme(models.Model):
    mot = models.ForeignKey(Mot, related_name='antonim', on_delete=models.CASCADE)
    antonyme = models.CharField(max_length=100)

class Expression(models.Model):
    expression = models.CharField(max_length=200, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.expression
