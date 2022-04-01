from django.db import models
from django.db.models import Q 
from teachers.models import TeacherAccount

# Create your models here.
class Faulty(models.Model):
    faulty = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.faulty




# choice=(
#     ('first','first'),
#     ('second','second'),
#     ('third','third'),
#     ('fourth','fourth'),
#     ('fifth','fifth'),
#     ('sixth','sixth'),
#     ('seventh','seventh'),
#     ('eighth','eighth'),
#     ('all','all')
# )


choice =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
)





class Subject(models.Model):
    semister    = models.IntegerField(choices=choice)
    subject     = models.CharField(max_length=50)
    faulty      = models.ForeignKey(Faulty, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject




day_choices = (
    ('sunday','sunday'),
    ('monday','monday'),
    ('tuesday','tuesday'),
    ('wednesday','wednesday'),
    ('thursday','thursday'),
    ('wednesday','wednesday'),
    ('friday','friday')
)




class Routine(models.Model):
    semister    = models.CharField(choices=choice,max_length=50)
    faulty      = models.ForeignKey(Faulty, on_delete=models.CASCADE)
    subject     = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day         = models.CharField(max_length=50,choices=day_choices)
    time        = models.CharField(max_length=20)
    teacher     = models.ForeignKey(TeacherAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.faulty.faulty



