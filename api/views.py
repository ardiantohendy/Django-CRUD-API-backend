from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    book = {'title' : 'thus spoke of zarathusta', 'author': 'nichca', 'published_date': 'Feb. 24, 1890'}
    return Response(book)