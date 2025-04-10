from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from profiles.models import Profile

# Create your views here.

def post_list_and_create(request):
    form =PostForm(request.POST or None)
    # qs =Post.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if form.is_valid():
            author= Profile.objects.get(user=request.user)
            instance=form.save(commit=False)
            instance.author=author
            instance.save()
            return JsonResponse ({
                'title': instance.title,
                'body':instance.body,
                'author': instance.author.user.username,
                'id': instance.id,
            })
            return JsonResponse({'msg':'Post created!'})

    context ={
        'form': form,
        
    }

    return render(request, 'posts/main.html', context)

def load_post_data_view(request, num_posts):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        visible=3
        upper=num_posts
        lower =upper -visible
        size = Post.objects.all().count()
        
        qs =Post.objects.all()
        data=[]
        for obj in qs:
            item={
                'id':obj.id,
                'title':obj.title,
                'body':obj.body,
                'liked': True if request.user in obj.liked.all() else False,
                'count': obj.like_count,
                'author':obj.author.user.username
            }
            data.append(item)
        return JsonResponse({'data':data[lower:upper],'size': size})

@require_POST
@login_required
def like_unlike_post(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            pk = request.POST.get('pk')
            if not pk:
                return JsonResponse({'error': 'Missing post ID'}, status=400)

            post = Post.objects.get(pk=pk)
            user = request.user

            if user in post.liked.all():
                post.liked.remove(user)
                liked = False
            else:
                post.liked.add(user)
                liked = True

            return JsonResponse({'liked': liked, 'count': post.like_count})

        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request type'}, status=400)



def hello_world_view(request):
    return JsonResponse({'text': 'hello world x2'})