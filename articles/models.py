from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):

    topic = models.CharField(max_length=30)
    articles = models.ManyToManyField(Article, through='TagArticle',
                                      through_fields=('tag', 'article'),
                                      related_name='scopes')

    def __str__(self):
        return self.topic

    def is_main(self):
        main_value = False
        tag_relations = self.tagarticle_set.all()
        for tag in tag_relations:
            if tag.main:
                main_value = True
                return main_value
            else:
                return main_value

    class Meta:
        verbose_name = 'Разедел'
        verbose_name_plural = 'Разделы'


class TagArticle(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return f'{self.article} - {self.tag} - Основной: {self.main}'

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
