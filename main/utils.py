from django.contrib.auth.models import User

def is_student(user):
    return user.groups.filter(name='Students').exists()

def is_mentors(user):
    return user.groups.filter(name='Mentors').exists()