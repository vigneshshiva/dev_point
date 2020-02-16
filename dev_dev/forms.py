from django import forms
from .models import ask_question,answer_question
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ask_Question_Form(forms.ModelForm):
    class Meta:
        model = ask_question
        fields = ('__all__')
class Answer_Question_Form(forms.ModelForm):
    class Meta:
        model = answer_question
        fields = ('answer',)
        # widgets = {
        #     'answer': CKEditorUploadingWidget(config_name='default',attrs={'class':'answer_question_wid'})
        # }
# class Like_add(forms.ModelForm):
#     class Meta:
#         model = Like_add
#         fields = ('__all__')
