from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonSerializer

@api_view(['POST'])
def post_person(request):
    data = {
        'name': request.data['name'],
        'last_name': request.data['last_name'],
        'age': request.data['age']

    }

    ser = PersonSerializer(data=data)

    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_persons(request):
    persons = Person.objects.all()
    ser = PersonSerializer(persons, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET', 'DELETE'])
def get_put_delete_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found !"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = PersonSerializer(person)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        ser = PersonSerializer(person, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_person(request):
    persons = Person.objects.filter(name=request.query_params['name'])
    if persons:
        ser = PersonSerializer(persons, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)









