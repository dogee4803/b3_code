from django.db import models

class Client(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    id_creator = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='created_courses')
    make_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class CurrentCourse(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrolled_courses')
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='current_courses')
    connect_date = models.DateField(auto_now_add=True)
    progress = models.FloatField(default=0)

    def __str__(self):
        return f"{self.id_client} - {self.id_course}"

class Module(models.Model):
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    number_of_days = models.IntegerField()

    def __str__(self):
        return f"Module for {self.id_course}"

class Block(models.Model):
    id_module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='blocks')
    text_information = models.TextField()
    images = models.CharField(max_length=200)
    video = models.CharField(max_length=200)

    def __str__(self):
        return f"Block in {self.id_module}"

class Question(models.Model):
    id_block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='questions')
    text_of_question = models.TextField()

    def __str__(self):
        return self.text_of_question

class Answer(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text_of_answer = models.TextField()
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.text_of_answer