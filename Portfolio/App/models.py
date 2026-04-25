from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)                # column: name (varchar(40))
    email = models.EmailField(max_length=40)              # column: email (validated as email)
    number = models.CharField(max_length=100)            # column: number (varchar(100))
    message = models.TextField(max_length=400)            # column: message (text up to 400 chars)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.number}"
