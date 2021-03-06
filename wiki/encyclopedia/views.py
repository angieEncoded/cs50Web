from django.shortcuts import render, redirect
from django import forms
from django.utils import encoding
from . import util
from . import angie
# from django.utils.html import strip_tags # took this back out since I am using Django's built in now
from random import seed, randrange, choice
# from markdown2 import Markdown
# import my own markdown converter
from . import convertmarkdown

# markdowner = Markdown()

# My little class so I don't have to lose my JS muscle memory
console = angie.Console()




# Some basic django forms
class NewEntryForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

class searchForm(forms.Form):
    q = forms.CharField()






def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):

    # Get the entry and if there is no entry send back a 404 page
    entry = util.get_entry(title)
    if entry == None:
        return render(request, "encyclopedia/404.html", {
            "error": f"The entry '{title}' does not yet exist"
        })
    
    # convert it to html
    #htmlEntry = markdowner.convert(entry)
    htmlEntry = convertmarkdown.convertIt(entry) # my markdown converter



    # Send back the entry found
    return render(request, "encyclopedia/entry.html", {
        "entry": htmlEntry,
        "title": title
    })

def search(request):

    if request.method == "POST":

        form = searchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["q"]
        
            # check if it matches an entry and if it does, redirect to the page with the search string
            if util.get_entry(query):
                return redirect("title", query)

            # get the list of current entries
            currentEntries = util.list_entries()
            filteredList = []
            for item in currentEntries:
                if query in item:
                    filteredList.append(item)
            
            # check and see if there is anything in the filtered list and send back to the home page if there isn't
            if len(filteredList) == 0:
                    return render(request, "encyclopedia/index.html", {
                        "entries": util.list_entries(),
                        "empty": f"No entries match the search: {query} "
                    })

            # Send that list through to a new page
            return render(request, "encyclopedia/partials.html", {
                "partials": filteredList 
            })
       
    # In case the user happens to try a GET or something else, send them to the main home page
    return redirect("index")




def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")

    if request.method == "POST":

        # Access to the raw fields in the form
        # This was my first version since I didn't want to use Django forms initially
        # title = request.POST.get("title")
        # content = request.POST.get("content")

        # Get the form and use Django's cleanup functions
        # However, it seems that we don't have to use Django to display the form, we can still build it 
        # in the html and use the class inside of python and get access to all the validation stuff Django does
        form = NewEntryForm(request.POST)
        if form.is_valid():


            title = form.cleaned_data["title"]
            # console.log(request.POST['title'])
            # Holy macaroni, this was a mess. I noticed a bug in which every time I saved an entry, it added some 
            # extra lines that I didn't expect. That led me to do this search:
            # django forms adding two extra whitespace lines on save
            # which led here:
            # https://forum.djangoproject.com/t/django-form-is-adding-extra-spaces-everytime-content-is-edited/3986/9
            # which led here
            # https://stackoverflow.com/questions/63732994/is-there-a-way-to-remove-lines-being-added-to-markdown-file-from-django-textarea
            # which led here
            # https://stackoverflow.com/questions/63004501/newlines-in-textarea-are-doubled-in-number-when-saved
            # which finally led here 
            # https://stackoverflow.com/questions/63017214/why-did-bytes-solve-my-newlines-problem
            # which didn't actually answer the question... so I looked it up in the docs and ended up using this module to force
            # it to a bytestring
            # https://docs.djangoproject.com/en/3.2/ref/unicode/
            content = form.cleaned_data["content"] 
            content = encoding.smart_bytes(content, encoding='utf-8', strings_only=False, errors='strict') 
            # console.log(content)
          
            # Check if the title exists
            entry = util.get_entry(title)
            if entry != None:
                return render(request, "encyclopedia/new.html", {
                    "error": "An entry with the name exists.",
                    "title": title, 
                    "content": content
                })

            # if it doesn't exist then we get to save the new entry and send the user there
            util.save_entry(title, content)
            return redirect("title", title)




def edit(request, title):

    # If we are getting the page, send the editing template
    if request.method == "GET":

        # get the entry data and render the template with the data
        content = util.get_entry(title)
        console.log(content)
        return render(request, "encyclopedia/edit.html", {
            "title": title, 
            "content": content
        })


    # going to handle th post request in here
    if request.method == "POST":

        # create a new django form
        form = NewEntryForm(request.POST)
        if form.is_valid():
            # console.log(request.POST['title'])
            # Holy macaroni, this was a mess. I noticed a bug in which every time I saved an entry, it added some 
            # extra lines that I didn't expect. That led me to do this search:
            # django forms adding two extra whitespace lines on save
            # which led here:
            # https://forum.djangoproject.com/t/django-form-is-adding-extra-spaces-everytime-content-is-edited/3986/9
            # which led here
            # https://stackoverflow.com/questions/63732994/is-there-a-way-to-remove-lines-being-added-to-markdown-file-from-django-textarea
            # which led here
            # https://stackoverflow.com/questions/63004501/newlines-in-textarea-are-doubled-in-number-when-saved
            # which finally led here 
            # https://stackoverflow.com/questions/63017214/why-did-bytes-solve-my-newlines-problem
            # which didn't actually answer the question... so I looked it up in the docs and ended up using this module to force
            # it to a bytestring
            # https://docs.djangoproject.com/en/3.2/ref/unicode/


            content = form.cleaned_data["content"]
            content = encoding.smart_bytes(content, encoding='utf-8', strings_only=False, errors='strict') 

            incomingTitle = form.cleaned_data["title"]
            # console.log(form.cleaned_data['title'])
            # console.log(title)
            # console.log(incomingTitle)
            # console.log(title == incomingTitle)
            # check and make sure the incoming title is the same as the title from the page

            # console.log(content)

            if title == incomingTitle:

                # Save the data
                util.save_entry(title, content)
                return redirect("title", title)
            else: 
                return render(request, "encyclopedia/edit.html", {
                "error": "What you submitted doesn't match this page",
                "content": content,
                "title": title
            })
        else:
            content = form.cleaned_data["content"]
            return render(request, "encyclopedia/edit.html", {
                "error": "Form did not pass validation",
                "content": content,
                "title": title
            })


def random(request):
    # console.log("hit the route")


    seed() # seed the generator from the current time (default)
    # Get the entries
    entries = util.list_entries()

    # figure out how many there are
    # figure out the equivelent of Math.floor(Math.random() * whatever.length))
    randomNumber = randrange(len(entries))

    # render that random page
    return redirect("title", entries[randomNumber])
    # console.log(entries[randomNumber])
