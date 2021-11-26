from django.shortcuts import render,redirect
from board.models import BoardTable
from datetime import datetime

# Create your views here.
def index(request):
    boardTable = BoardTable.objects.values('id','board_user','board_title','board_like_cnt').order_by('-id')
    context ={
        'boardTable' : boardTable
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
    context={
        
    }
    return render(request,'board/update.html')

def delete(request, boardId):
    context={
        
    }
    return render(request,'board/delete.html')

def add(request):
    if(request.method=='POST'):
        if(request.user.username == ""):
            return redirect('login')
        board = BoardTable()
        board.board_title = request.POST.get('title')
        board.board_context = request.POST.get('context')
        board.board_user = request.POST.get(request.user.username)
        board.board_dt = str(datetime.now()).replace("'","").replace('"','')
        board.board_up_dt = str(datetime.now()).replace("'","").replace('"','')
        board.board_like_cnt = 0
        board.save()

        return redirect('BD:BDetail', board.id )
    else: 
        return render(request,'board/add.html')
