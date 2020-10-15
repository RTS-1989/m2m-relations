from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, TagArticle


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print(form.cleaned_data)
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter == 0:
            raise ValidationError('Укажите основной раздел')
        elif counter > 1:
            raise ValidationError('Основной раздел может быть только один!')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = TagArticle
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline
    ]


admin.site.register(Tag)
