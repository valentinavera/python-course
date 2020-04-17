from graphene_django import DjangoObjectType
from blog.models import Category as CategoryModel, Post as PostModel
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from blog.forms import CategoryModelForm
from graphql_jwt.decorators import login_required

class Category(DjangoObjectType):
    #nodo del grafo
    class Meta:
        model = CategoryModel
        filter_fields = {
            'name':['exact', 'icontains', 'istartswith'],
            'is_active':['exact']
        }
        interfaces = (relay.Node, )

class Post (DjangoObjectType):
    class Meta: 
        model = PostModel
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'text':['icontains'],
            'excerpt': ['icontains'],
            'is_active':['exact'],
            'category__name':['exact','icontains'],
            'created_at':['gt', 'gte', 'lt', 'lte']
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    categories = DjangoFilterConnectionField(Category)
    category = relay.Node.Field(Category)
    posts = DjangoFilterConnectionField(Post)
    post = relay.Node.Field(Post)

    @login_required
    def resolve_categories(self,info, *args, **kwargs):
        return CategoryModel.objects.filter(**kwargs)


class CategoryMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CategoryModelForm


class Mutation(ObjectType):
    category = CategoryMutation.Field()