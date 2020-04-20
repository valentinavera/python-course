from graphene import ObjectType
import graphql_jwt
from django import forms
from django.core.mail import EmailMultiAlternatives
from graphene_django.forms.mutation import DjangoFormMutation

class EmailForm(forms.Form):
    subject = forms.CharField(min_length=5, max_length=64)
    message = forms.CharField(min_length=20)

    def save(self, *args, **kwargs):
        subject = self.cleaned_data['subject'] #si es null arroja exepción
        message = self.cleaned_data.get('message')
        body_text = "Hola \n%s" % message
        sender = 'test@local.com'
        to = ['to@local.com']
        body_htlm = """
        <div style="background:black; color:white">
        %s
        </div>
        """ % message

        email_message = EmailMultiAlternatives(subject=subject,body=body_text,from_email=sender, to=to)
        email_message.attach_alternative(body_htlm,'text/html')
        #email_message.attach()
        email_message.send()

class EmailMutation(DjangoFormMutation):
    class Meta:
        form_class= EmailForm

class Mutation(ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    send_mail = EmailMutation.Field()