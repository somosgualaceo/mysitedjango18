from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	video = forms.CharField(help_text='Ej: http://www.youtube.com/watch?v=vGs1kl' , required=False, widget=forms.TextInput(attrs={'pattern':'^(http|https)://(www\.)?youtube\.com/watch\?v=.+$'}))


	class Meta:
		model = Post
		fields = ('title', 'text', 'imagen', 'imagen2', 'video',)
		labels ={
		'title': 'Titulo',
		'text': 'Texto'
		}		

	def clean_video(self):
		url = self.cleaned_data['video']
		if len(url) > 0:
			params = url.split('?v=', 1)
			codigo = params[1].split('&', 1)[0]
			return codigo
		else:
			return ''		
                