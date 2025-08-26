from django.db import models

class LeadershipMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='leadership_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} — {self.position}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} — {self.role}"

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "Контакты Федерации"