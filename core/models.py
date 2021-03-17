from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
	# Title
	title = models.CharField('Título', max_length=500, blank=False, null=False)
	# Resumo
	resume = models.TextField(default='')
	# Conteúdo
	content = RichTextField()
	# Data_publicação
	date_published = models.DateField('Data de Publicação', auto_now_add=True)
	# Slug
	slug = models.SlugField('Slug', editable=False)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		if Post.objects.filter(slug=self.slug):
			self.slug += '-1'
		super().save(*args, **kwargs)
	