from re import template
from django.shortcuts import render
from django.http import HttpResponse
# from recommend_app.forms import PostSearchForm



def index(request):
    return render(request, 'recommend_app/index.html')

def ver1(request):
    return render(request, 'recommend_app/ver1.html')

def ver2(request):
    return render(request, 'recommend_app/ver2.html')

# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name = 'recommend_app/search.html'

#     def form_valid(self.form):
#         SearchWord = form.cleaned_data['search_word']
#         post_list = Post.objects.filter()