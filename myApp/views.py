from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def hello_world(request):
    return Response({'message': 'Hello,World'})


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({'message': 'Hello, Sara'})
    elif request.method == "POST":
        return Response({'message': 'Hello, {}'.format(request.data["name"])})


@api_view(['POST'])
def calc(request):
    try:
        num1 = request.data["num1"]
        num2 = request.data["num2"]
        opr = request.data["opr"]

    except:
        return Response({"error": "send two numbers and an operation..."},
                        status=status.HTTP_400_BAD_REQUEST)

    else:
        if isinstance(num1, int) and isinstance(num2, int):
            if opr == "add":
                return Response({"result": num1+num2}, status=status.HTTP_200_OK)
            elif opr == "min":
                return Response({"result": num1-num2}, status=status.HTTP_200_OK)
            elif opr == "div":
                return Response({"result": num1/num2}, status=status.HTTP_200_OK)
            elif opr == "mul":
                return Response({"result": num1*num2}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "send a valid operation..."}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "send an integer number..."}, status=status.HTTP_400_BAD_REQUEST)

