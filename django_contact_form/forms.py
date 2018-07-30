from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_content = forms.CharField(widget=forms.Textarea, required=True)

    helper = FormHelper()

    helper.layout = Layout(

        PrependedText('contact_name', '<span class="fa fa-user"></span>', placeholder="Name"),
        PrependedText('contact_email', '<span class="fa fa-envelope"></span>', placeholder="Email"),
        PrependedText('contact_content', '<span class="fa fa-comment"></span>', placeholder="Message"),
        Submit('save', 'Submit', css_class='btn btn-outline-primary btn-block'),
        
    )


    helper.form_show_labels = False
    # StrictButton('Submit', name='submit', value='go', css_class='btn btn-primary'),
    #    StrictButton('Submit', name='submit', value='submit', css_class='btn btn-outline-primary btn-block'),
