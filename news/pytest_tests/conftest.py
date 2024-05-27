import pytest

from news.models import Comment, News

@pytest.fixture
def news():
    return News.objects.create(title='Заголовок', text='Текст')
