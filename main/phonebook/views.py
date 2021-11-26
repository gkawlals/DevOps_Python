from django.shortcuts import render, redirect
from phonebook.models import PhoneBook

# Create your views here.
def index(request):
    alluser = PhoneBook.objects.values('id','이름','전화번호');
    context = {
        "pb_user" : alluser,
    }
    return render(request, 'phonebook/index.html', context);

def add(request):
    
    if (request.method == 'GET'):
        
        if(str(request.user) != 'AnonymousUser'):
            return render(request, 'phonebook/add.html')
        else:
            return redirect('login')
        
    elif(request.method == 'POST'):
            name = request.POST.get("name")
            tel = request.POST.get("tel")
            email = request.POST.get("email")
            add = request.POST.get("add")
            birth = request.POST.get("birth") # html에서 받아오는 parameter값 들고오기
            birth = birth.replace('"','').replace("'","").replace(".","-")
            auther = request.user.username
            
            phonebook = PhoneBook() # 만들어 놨던 테이블의 컬럼들을 지정 후 바로 때려 넣기 
            phonebook.이름 = name
            phonebook.전화번호 = tel
            phonebook.주소 = add
            phonebook.이메일 = email
            phonebook.생년월일 = birth
            phonebook.작성자 = auther
            phonebook.save()  # save 명령을 통해서만 저장이된다. 

            return redirect("PB:IndexUrl")
            
    return render(request, 'phonebook/add.html');


def delete(request, user_id):

    user = PhoneBook.objects.values('id','이름','주소','이메일','생년월일').get(id = user_id);
    PhoneBook.objects.get(id = user_id).delete();
    context = {
        'user' : user
    }
    message = "<script>"
    message = message + "alert('"+request.user.username+"님이 탈퇴되었습니다.')"
    message = message + "document.location.href='/' </script>";


    return render(request, 'phonebook/delete.html',context);


def detail(request):
    return render(request, 'phonebook/detail.html');

def update(request, user_id):

    if(request.method == 'POST'):
        name = request.POST.get("name")
        tel = request.POST.get("tel")
        email = request.POST.get("email")
        add = request.POST.get("add")
        birth = request.POST.get("birth") # html에서 받아오는 parameter값 들고오기
        birth = birth.replace("'","").replace('"','').replace(".","-")
        auther = request.POST.get("auther")

        phonebook = PhoneBook.objects.get(id=user_id) # 만들어 놨던 테이블의 컬럼들을 지정 후 바로 때려 넣기 
        phonebook.이름 = name
        phonebook.전화번호 = tel
        phonebook.주소 = add
        phonebook.이메일 = email
        phonebook.생년월일 = birth
        phonebook.작성자 = auther
        phonebook.save()  # save 명령을 통해서만 저장이된다. 

        return redirect("PB:IndexUrl")
    else:
        
        pb_user = PhoneBook.objects.values('id','이름','주소','이메일','생년월일', '작성자').get(id = user_id);
        print(user_id);
        context = {
            'pb_user' : pb_user
        }
        if( request.user.username != ''):
            if(str(request.user) == pb_user['작성자']):
                return render(request,'phonebook/update.html', context)
        else:
            return redirect('/')

        return render(request, 'phonebook/update.html',context);

def detail(request, user_id):
    user = PhoneBook.objects.values('id','이름','주소','이메일','생년월일').get(id = user_id);
    print(user_id);
    context = {
        'user' : user
    }
    return render(request, 'phonebook/detail.html',context);

def PBdetail(request, user_id):
    user = PhoneBook.objects.values('id','이름','주소','이메일','생년월일','작성자').get(id = user_id);
    print(user_id);
    context = {
        'pb_user' : user
    }
    return render(request, 'phonebook/PBdetail.html',context);