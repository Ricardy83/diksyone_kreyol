from django.db import models

class DictionaryEntry(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    
    
    def __str__(self):
        return f" {self.word} - {self.definition}"

