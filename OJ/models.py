from distutils.command.build_scripts import first_line_re
import imp
from django.db import models
from froala_editor.fields import FroalaField

#########################################################################################################################

class Problem(models.Model):
    DIFFICULTY = (("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"))
    STATUS = (("Unsolved", "Unsolved"), ("Solved", "Solved"))
    name = models.CharField(max_length=100, default="")
    description = FroalaField(default="")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    time_limit = models.IntegerField(default=2, help_text="in seconds")
    memory_limit = models.IntegerField(default=128, help_text="in kb")

    def __str__(self):
        return self.name

#########################################################################################################################

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return ("TC: " + str(self.id) + " for Problem: " + str(self.problem))