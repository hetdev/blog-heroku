from django.contrib import admin

from article.models import Article, ContactRequest


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'publication_date',
        'active',
        'creation_date',
        'last_modification_date',
    )


admin.site.register(Article, ArticleAdmin)


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'content',
        'contact_date',
        'creation_date',
        'last_modification_date',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(ContactRequest, ContactRequestAdmin)
