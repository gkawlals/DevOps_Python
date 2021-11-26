from django.shortcuts import HttpResponse, render

def test(request):
    return HttpResponse("test");

def index(request):
    return HttpResponse("index Page");

# notice 경로를 입력하면 notice Page 출력
def notice(request):
    return HttpResponse("notice Page");

def board(request, boardId):
    #print(boardId);
    print(type(boardId));
    message = f'{boardId} page';
    return HttpResponse(message);

def language(request, lang):
    # if(lang == 'ko'):
    #     return HttpResponse("한국어");
    # elif(lang == 'en'):
    #     return HttpResponse("영어");
    # elif(lang == 'jp'):
    #     return HttpResponse("일본어");
    # else:
    #     return HttpResponse("알수없는 언어");
    lang_code = {'ko':'한국어', 'en':'영어', 'jp':'일본어'};

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
    print(type(raw));
    return HttpResponse(raw);

def reg8(request, raw):
    print(type(raw));
    return HttpResponse(raw);

def reg9(request, raw):
    print(type(raw));
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

def reg13(request, raw1, raw2):
    message = raw1 + "-" + raw2;
    return HttpResponse(message);

def reg14(request, raw1):
    print(type(raw1));
    return HttpResponse(raw1);

def reg15(request, raw1):
    print(type(raw1));
    return HttpResponse(raw1);

def email(request, raw1):
    print(type(raw1));
    return HttpResponse(raw1);

def lang(request, raw1):
    print(type(raw1));
    return HttpResponse(raw1);

def temp1(request):
    return render(request, 'temp1.html');

def temp2(request):
    context = {
        "key":"value",
        "num" :100,
        "float" : 1.234,
        "str" : "문자열",
        "list" : [10,20,'리스트'],
        "dic" : {"a" : "a값", "b" :"b값"},
    }
    return render(request, 'temp2.html', context);

def temp3(request):
    context = {
        "list" : [10,20,'리스트'],
        "dic" : {"a" : "a값", "b" :"b값"},
    }
    return render(request, 'temp3.html', context);

def quiz1(request):
    context = {
        "번호" : [ [1,2,3,4,5], ['육','7','팔','구','10'], [11,12,13,14,15] ],
    }
    return render(request, 'quiz/quiz1.html', context);

def quiz2(request):
    # context = {
    #     "네이버":"http://www.naver.com",
    #     "다음":"http://www.daum.net",
    #     "구글":"http://www.google.com",
    # }
    context = {
        "site": [ 
            {
                "네이버":"http://www.naver.com",
                "다음":"http://www.daum.net",
                "구글":"http://www.google.com",
            }
        ]
    }
    return render(request, "quiz/quiz2.html", context);

def quiz3(request):
    context = {
        "menu":['순위','국가','승점','승','무','패','득점','실점','골득실'],
        "score":[
            [1, {'이란':'http://www.naver.com'}, 17,5,2,0,6,0,6],
            [2, {'대한민국':'http://www.daum.net'}, 13,4,1,2,9,7,2],
            [3, {'시리아':'http://www.google.com'}, 8,2,2,23,2,3,-1],
        ],
    }
    return render(request, "quiz/quiz3.html", context);

def image(request):
    return render(request, 'image.html');