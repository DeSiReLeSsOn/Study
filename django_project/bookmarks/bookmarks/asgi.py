from django.http import HttpResponse, HttpRequest, Http404

# Create your tests here.
def posts_list(posts, year):
    if year > 2023 or year < 1990 :
        raise Http404()
    return HttpResponse(f"posts:{year}")

print(posts_list('posts', 1990))