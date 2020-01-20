from django.urls import path
from .views import EntryList, EntryDetail, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
	path('', EntryList.as_view(), name = 'home'),
	path('detail/<int:pk>/', EntryDetail.as_view(), name = 'detail'),
	path('book/new/', BookCreateView.as_view(), name='add'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete')
]
