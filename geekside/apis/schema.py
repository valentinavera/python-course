from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value='stranger'))

    def resolve_hello(root, info, name, *args, **kwargs):
        return 'hello %s' %name

ROOT_SCHEMA = Schema(Query=Query)