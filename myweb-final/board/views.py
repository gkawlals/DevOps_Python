from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("board/test");

def boarder(request, boardId):
    message = boardId + ' 페이지 입니다.';
    return HttpResponse(message);

# chart 라는 subapp 생성
# mainapp에서 chart 라는 경로로 들어오면
# 모든 경로는 chart subapp 이동
# chart/ 숫자 2000 ~ 2021  0000 년도 페이지
# chart/ 숫자 01 ~ 12  00월 페이지
