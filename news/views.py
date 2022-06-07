from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http import JsonResponse

from .email import send_welcome_email
from .models import Article,NewsLetterRecipients
from .forms import NewsLetterForm, NewArticleForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date, "news": news, "letterForm": form})
    # date = dt.date.today()
    # news = Article.todays_news()   
    # if request.method == 'POST':
    #     form=NewsLetterForm(request.POST)
    #     if form.is_valid():
    #         # After validating a form instance the values of the form 
    #         # are saved inside cleaned_data property which is a dictionary
    #         name = form.cleaned_data['your_name']
    #         lastname=form.cleaned_data['your_lastname']
    #         email = form.cleaned_data['email']
    #         recipient = NewsLetterRecipients(name = name,lastname=lastname,email =email)
    #         recipient.save()
    #         # import the from send_welcome_email and call it after we validate the form 
    #         # passing in the name and the email of the user subscribing
    #         send_welcome_email(name,lastname,email)
    #         HttpResponseRedirect('news_today')          
    # else:
    #     form = NewsLetterForm()        
    # return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})


# This fn will get the name and email from our AJAX request, 
# save the user in the database and sends the welcome email.
#  It then returns a JSON response to tell us the action has been completed successfully
def newsletter(request):
    name = request.POST.get('your_name')
    lastname = request.POST.get('your_lastname')
    email = request.POST.get('email')
    recipient=NewsLetterRecipients(name=name, lastname=lastname,email=email)
    recipient.save()
    send_welcome_email(name,lastname, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

#decorator limits the access to article view function to only authenticated users
@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user=request.user
    if request.method=='POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.editor=current_user
            article.save()
        return redirect('newsToday') 
    else:
        form=NewArticleForm()
    return render(request, 'new_article.html',{"form":form})           
# def article(request,article_id):
    # try:
    #     article = Article.objects.get(id = article_id)
    # except Article.DoesNotExist:
    #     raise Http404()
    # return render(request,"all-news/article.html", {"article":article})

