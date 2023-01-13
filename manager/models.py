from django.db import models

class skills(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to="nirajmedia/skills")
    def __str__(self):
        return self.name

class Planguage(models.Model):
    name = models.CharField(max_length=50)
    skill = models.ForeignKey(skills, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Dtool(models.Model):
    tool_name = models.CharField(max_length=50)
    skill = models.ForeignKey(skills, on_delete=models.CASCADE)
    def __str__(self):
        return self.tool_name
    
class Framework(models.Model):
    framework_name = models.CharField(max_length=50)
    skill = models.ForeignKey(skills, on_delete=models.CASCADE)
    def __str__(self):
        return self.framework_name

class DataBase(models.Model):
    database_name = models.CharField(max_length=50)
    skill = models.ForeignKey(skills, on_delete=models.CASCADE)
    def __str__(self):
        return self.database_name

class Project(models.Model):
    project_name = models.CharField(max_length=50) 
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="nirajmedia/projects")
    url = models.CharField(max_length=80)
    def __str__(self):
        return self.project_name

    class Meta:
        ordering = ['complete']

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'messege from ' + self.name
    
    class Meta:
        ordering = ['id',]