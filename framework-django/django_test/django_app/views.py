from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request, param=None):
    return Response({
        'param' : param
    })


@api_view(['POST'])
def post(request):
    return Response({
        'key' : 'value'
    })
