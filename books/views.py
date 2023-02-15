from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"  # これを見るためにはpermissionがいるという意味だろう


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(title__icontains="beginners")
    def get_queryset(
        self,
    ):
        # 呼び出してないけどこの関数、自動で実行されているのだな。。。。なぜ.そもそもなぜ関数にする必要があるのだろう。上のやつに加えるじゃダメなんかね。。試したらできた！！どっちでもOK
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
