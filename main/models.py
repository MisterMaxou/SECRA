import random, string
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


def generate_link():
    link = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(30))
    while Work.objects.filter(link=link):
        link = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(30))
    return link


class Work(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de création')
    last_version_date = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Date de la dernière modification')
    title = models.CharField(max_length=150, verbose_name='Titre')
    description = models.TextField(max_length=500, verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ATTENTION AU ON_DELETE
    public = models.BooleanField(default=True, verbose_name="Visible par d'autres personnes que les contributeurs")
    link = models.CharField(max_length=30, default=generate_link, blank=True)
    def __str__(self):
        return self.title + ", par " + str(self.user)
    def get_title(self):
        return self.title
    def reset_link(self):
        self.link = generate_link
        self.save()
    def get_nbr_contributors(self):
        contributors_id = Version.objects.filter(work=self).values('user').distinct()
        return len(contributors_id)



class Version(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de création')
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ATTENTION AU ON_DELETE
    text = tinymce_models.HTMLField(verbose_name='')
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    def __str__(self):
        s = "Contrib de " + str(self.user) + " à " + str(self.work.title)
        return s

    # def __str__(self):
    #     return self.text
        # return "Version de '" + self.work.get_title() + "' par " + str(self.user)