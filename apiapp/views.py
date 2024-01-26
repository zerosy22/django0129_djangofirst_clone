from rest_framework.response import Response
from rest_framework.decorators import api_view 

#python에서 @으로 시작하는 단어는 decorator 라고 하는데 실제 함수를 호출하면
#특정 내용을 삽입해서 함수를 실행합니다.
#반복적으로 사용하는 내용이나 직접 작성하기 번거로운 내용을 decorator로 만듭니다.

#GET 요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request):
    return Response("Hello REST API")
