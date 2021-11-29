import os
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from board.models import BoardTable
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage
from main import settings
import urllib

# Create your views here.
def index(request, page):
    boardTable = BoardTable.objects.all()

    paging = Paginator(boardTable, 2)
    try:
        context ={
            'boardTable' : paging.page(page)
        }
    except EmptyPage:
        context={
            'boardEmpty' : paging.page(paging.num_pages)
        }
    return render(request,'board/index.html',context);

def detail(request, boardId):

    boardInfo = BoardTable.objects.get(id = boardId)
    boardInfo.board_like_cnt += 1;
    boardInfo.save()
    context={
        'boardInfo' : boardInfo
    }
    return render(request,'board/detail.html', context)

def update(request, boardId):
    board = BoardTable.objects.get(id = boardId)
    if (request.method == 'POST'):
        board.board_title = request.POST.get('title')
        board.board_context = request.POST.get('context')
        boardUp.board_up_dt = datetime.now()
        boardUp.save()

        return redirect("BD:BIndex")
        
    else:
        if(board.board_user == request.user.username):
            context={
                'board' : board
            }
            return render(request,'board/update.html',context)
        else:
            return redirect('/')

def delete(request, boardId):
    message = "<script>"
    message = message + "alert('"+boardId+"번 게시물을 삭제했습니다.')"
    message = message + "document.location.href='/board/' </script>";
    BoardTable.objects.get(id=boardId).delete()
    return HttpResponse(message)

def add(request):
    if(request.method=='POST'):
        if(request.user.username == ""):
            return redirect('login')
        board = BoardTable()
        board.board_title = request.POST.get('title')
        board.board_context = request.POST.get('context')
        board.board_user = request.POST.get(request.user.username)
        board.board_dt = datetime.now()
        board.board_up_dt = datetime.now()
        board.board_like_cnt = 0
        board.save()

        path = settings.MEDIA_ROOT + "/" + str(BoardTable.id)
        os.mkdir(path)
        for i in request.FILES.getlist('files'):
            upLoadFile = open(settings.MEDIA_ROOT + "/" + str(i), 'wb' )
            for chunk in i.chunks():
                upLoadFile.write(chunk)
        # chunk = 업로드되는 파일의 로딩의 단위 

        return redirect('BD:BDetail', board.id )
    else: 
        return render(request,'board/add.html')


def upload(request):
    if request.method == 'POST':
        for i in request.FILES.getlist('files'):
            upLoadFile = open(settings.MEDIA_ROOT + "/" + str(i), 'wb' )
            for chunk in i.chunks():
                upLoadFile.write(chunk)
                # chunk = 업로드되는 파일의 로딩의 단위 
    return render(request,'board/upload.html')

def updown(request):
    dirList = os.listdir(settings.MEDIA_ROOT)
    context = {
        'dirList' : dirList
    }
    return render(request,'board/updown.html', context)

def download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, str(filename))
    file_name = urllib.parse.quote(filename.encode('utf-8'))
    readFile = open(file_path, 'rb')
    response = HttpResponse(readFile.read())
    response['Content-Disposition'] = 'attachment; filename*=UTF8\'\'%s'%file_name
    return (response)