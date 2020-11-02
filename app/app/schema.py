import graphene
import tracks.schema
import users.schema
import graphql_jwt

class Mutation(users.schema.Mutation,tracks.schema.Mutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(mutation=Mutation)