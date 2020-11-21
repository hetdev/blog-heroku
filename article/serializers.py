import socket

from rest_framework import serializers

from article.models import Article, ContactRequest


class ArticleListSerializer(serializers.ModelSerializer):
    detail_link = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'slug',
            'author',
            'content',
            'publication_date',
            'detail_link',
        )

    def get_detail_link(self, obj: Article):

        return f'{self.root.context["request"].build_absolute_uri("/")}api' \
               f'/article/detail/{obj.slug}/{obj.id}'


class ArticleDetailSerializer(serializers.ModelSerializer):
    list_link = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'slug',
            'author',
            'content',
            'publication_date',
            'list_link',
        )

    def get_list_link(self, obj: Article):

        return f'{self.root.context["request"].build_absolute_uri("/")}api' \
               f'/article/list'


class ContactRequestCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRequest
        fields = (
            'name',
            'email',
            'content',
            'contact_date',
        )
