from django.shortcuts import HttpResponse

def test(request):
    return HttpResponse("test");

def index(request):
    return HttpResponse("index Page");

def notice(request):
    return HttpResponse("notice Page");
    #notice 경로를 입력하면 notice page 출력

def board(request, boardId):
    print(boardId);
    print(type(boardId));
    message = f'{boardId} page';
    return HttpResponse(message);

def language(request, lang):
    
    lang_code = {'ko':'한국어', 'en': '영어', 'jp' : '일본어'}

    if lang_code.get(lang):
        message = f'{lang_code.get(lang)}';
    else :
        message = '알수없는 언어';
    return HttpResponse(message);


def reg1(request, raw):
    return HttpResponse(raw);


def reg2(request, raw):
    return HttpResponse(raw);

def reg3(request, raw):
    return HttpResponse(raw);

def reg4(request, raw):
    return HttpResponse(raw);

def reg5(request, raw):
    return HttpResponse(raw);

def reg6(request, raw):
    return HttpResponse(raw);

def reg7(request, raw):
    print(type(raw))
    return HttpResponse(raw);

def reg8(request, raw):
    print(type(raw))
    return HttpResponse(raw);

def reg9(request, raw):
    print(type(raw))
    return HttpResponse(raw);

def reg10(request, raw):
    print(type(raw));
    
    return HttpResponse(raw);

def reg11(request, raw):
    print(type(raw));
    
    return HttpResponse(raw);
    
def reg12(request, raw):
    print(type(raw));
    
    return HttpResponse(raw);
   