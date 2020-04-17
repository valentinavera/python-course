from graphene import ObjectType, String, Schema
from .blog_schema import Query as BlogQuery

class Query(BlogQuery):
    pass
    # hello = String(name=String(default_value="stranger"))

    # def resolve_hello(root, info, name, *args, **kwargs):
    #     return 'Hello %s' % name

ROOT_SCHEMA = Schema(query=Query)
