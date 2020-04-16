from graphene import ObjectType, String, Schema

#primer nodo del grafo Query
class Query(ObjectType):
    #consulta hello, nodo a consultar
    hello = String(name=String(default_value='stranger'))

    #respuesta a la consulta
    def resolve_hello(root, info, name, *args, **kwargs):
        return 'hello %s' %name

#schema principal del api
ROOT_SCHEMA = Schema(query=Query)