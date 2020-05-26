import random
from django.shortcuts import *
from django.http import *
from pymysql import *
from django.views.decorators.csrf import *
from django.core.files.storage import *
import smtplib
import http.client

conn = Connect("127.0.0.1", "root", "", "goodreads")


def loginpage(request):
    return render(request, "login.html")


@csrf_exempt
def login(request):
    global conn
    s = "select * from admin1"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    flag = False
    email = request.POST["Email"]
    password = request.POST["password"]

    print(email,password)
    for row in result:
        print("==>",row)
        if (str(row[0]) == str(email) and str(row[1]) == str(password)):
            flag = True
            break
    if flag == False:
        return render(request, "login.html")
    else:
        request.session["adminEmail"] = email
        return render(request, 'admindashboard.html')


def addadmin(request):
    return render(request, "addadmin.html")


@csrf_exempt
def insertadmin(request):
    print(request.POST)
    email=request.POST['email']
    Password=request.POST['Password']
    Mobileno=request.POST['Mobileno']
    s="insert into  admin1 values('{}','{}','{}','0')".format(email,Password,Mobileno)
    result=Insert(s)
    d={"message":"admin added successfully"}

    return redirect(showadmin)

def adminlogout(request):
    try:
        request.session['adminEmail']
        del request.session['adminEmail']
        return redirect(loginpage)
    except:
        return redirect(loginpage)

def changepassword(request):
    return render(request, "Changepassword.html")


@csrf_exempt
def updatepassword(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    email = str(request.session['adminEmail'])
    s = "select * from admin1 where Email='" + email + "' and Password='" + request.POST["oldpassword"] + "'"
    print("hello")
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    if result:
        s = "update admin1 set Password='" + request.POST["newpassword"] + "' where Email='" + email + "'"
        print("Bye")
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        d = {"message": "password changed successfully"}
        return render(request, "admindashboard.html", {"ar": d})
    else:
        d = {"message": "invalid credentials"}
        return render(request, "changepassword.html", {"ar": d})


def showadmin(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from admin1"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []

    for row in result:
        d = {}
        d["Email"] = row[0]
        d["Password"] = row[1]
        d["Mobileno"] = row[2]
        d["otp"] = row[3]
        x.append(d)
    return render(request, "showadmin.html", {"ar": x})


# def insertadmin(request):
#     conn = Connect("127.0.0.1", "root", "", "goodreads")
#     s = "insert into admin1 values('" + request.GET["Email"] + "','" + request.GET["Password"] + "','" + request.GET[
#         "Mobileno"] + "',0)"
#     cr = conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     d = {"message": "Admin added successfully"}
#     return render(request, "insertadmin.html", {"ar": d})




def removeadmin(request):
    s = "delete from admin1 where Email='" + request.GET["q"] + "'"
    result=Delete(s)
    return HttpResponseRedirect("showadmin")


def save(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "update admin1 set Mobileno='" + request.GET["Mobileno"] + "' where Email='" + request.GET["Email"] + "'"
    # s="update admin1 set otp='"+request.GET["otp"]+"' where Email='"+request.GET["Email"]+"'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect("showadmin")


def editadmin(request):
    Email = request.GET["q"]
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from admin1 where Email='" + Email + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    result = cr.fetchone()
    d = {"Email": result[0], "Password": result[1], "Mobileno": result[2], "otp": result[3]}
    return render(request, "editadmin.html", {"ar": d})


def addcategory(request):
    return render(request, "addcategory.html")


@csrf_exempt
def insertcategory(request):
    file = request.FILES["photo"]
    print(file)
    uploadname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    fs = FileSystemStorage()
    fs.save(uploadname, file)
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "insert into category values('" + request.POST["catname"] + "','" + request.POST[
        "description"] + "','" + uploadname + "')"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "category added successfully"}
    return render(request, "insertcategory.html", {"ar": d})


def showcategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"catname": row[0], "description": row[1], "catphoto": row[2]}
        x.append(d)
    return render(request, "showcategory.html", {"ar": x})


def removecategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "delete from category where catname='" + request.GET["q"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect("showcategory")

    # def editcategory(request):
    return render(request, "editcategory.html")


@csrf_exempt
def save(request):
    try:
        file = request.FILES["photo"]
    except:
        file = ""

    if file != "":
        print(f"if condition{file}")
        file = request.FILES["photo"]
        uploadname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
        s = "update category set description='" + request.POST[
            "description"] + "',catphoto='" + uploadname + "' where catname='" + request.POST["catname"] + "'"
        fs = FileSystemStorage()
        fs.save(uploadname, file)
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
    else:
        print(f"else condition:-{file}")
        s1 = "update category set description='" + request.POST["description"] + "' where catname='" + request.POST[
            "catname"] + "'"
        cr = conn.cursor()
        cr.execute(s1)
        conn.commit()

    return HttpResponseRedirect("showcategory")


def editcategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from category where catname='" + request.GET["q"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    result = cr.fetchone()
    d = {"catname": result[0], "description": result[1], "catphoto": result[2]}
    return render(request, "editcategory.html", {"ar": d})


def addbook(request):
    global conn
    s = " select catname from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)
    x = []
    for i in result:
        x.append(i[0])
    return render(request, "addbook.html", {"ar": x})


@csrf_exempt
def insertbook(request):
    file = request.FILES["photo"]
    print(file)
    name = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "insert into books values(NULL,'" + request.POST["title"] + "','" + request.POST["description"] + "'," + \
        request.POST["price"] + ",'" + request.POST["edition"] + "','" + request.POST["author"] + "','" + request.POST[
            "genre"] + "','" + request.POST["catname"] + "','" + name + "')"
    fs = FileSystemStorage()
    fs.save(name, file)
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "book added successfully"}
    # return render(request, "insertbook.html", {"ar": d})
    return redirect(booksview)


# def openajax(request):
#         return render(request,"ajaxdemo.html")
#
# def showbook(request):
#     global conn
#     cr = conn.cursor()
#     s="select catname from category"
#     cr.execute(s)
#     result = cr.fetchall()
#     x=[]
#     for row in result:
#         d={"catname":row[0]}
#         x.append(d)
#     return render(request,"ajaxdemo.html",{"ar":x})
#
# def getbooks(request):
#     global conn
#     catname=request.GET["catname"]
#     print(catname)
#     s="select * from books where catname='"+catname+"'"
#     print('')
#     cr=conn.cursor()
#     cr.execute(s)
#     result=cr.fetchall()
#     x=[]
#     for row in result:
#         d={"bookid":row[0],
#            "title":row[1],
#            "description":row[2],
#            "price":row[3],
#            "edition":row[4],
#            "author":row[5],
#            "genre":row[6],
#            "catname":row[7],
#            "photo":row[8]}
#         x.append(d)
#     print(x)
#     return JsonResponse(x,safe=False)
# def deleteaction(request):
#     id=request.GET["id"]
#     print(id)
#     s="delete from books where bookid=('{id}')"
#     print(s)
#     global conn
#     cr=conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     return HttpResponse("SUCCESS")
# @csrf_exempt
# def editdataaction(request):
#     bookid=request.POST['bookid']
#     title=request.POST['title']
#     description=request.POST['description']
#     price=request.POST['price']
#     edition=request.POST['edition']
#     author=request.POST['author']
#     genre=request.POST['genre']
#     catname=request.POST['catname']
#     photo=request.POST['photo']
#     s=f"update books set title='{title}',description=('{description}'),price='{price}',edition='{edition}',author='{author}',genre='{genre}',catname='{catname}',photo='{photo}' where bookid=('{bookid}')"
#     print(s)
#     global conn
#     cr=conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     return HttpResponse("SUCCESS")
#
# #def changepassword(request):
#    # return render(request,"changepassword")
#
#
# def showbook2(request):
#     global conn
#     s = " select catname from category"
#     cr = conn.cursor()
#     cr.execute(s)
#     result = cr.fetchall()
#     print(result)
#     x=[]
#     for row in result:
#         d={"catname":row[0]}
#         x.append(d)
#     return render(request,"addbook.html",{"ar".x})
from database import *


def booksview(request):
    query = "select catname from category"
    result = Fetchall(query)
    x = []
    for i in result:
        x.append(i[0])
    return render(request, 'books.html', {"data": x})


def viewbooks(request):
    catname = request.GET['catname']
    query = f"select * from books where catname='{catname}'"
    result = Fetchall(query)
    x = []
    for row in result:
        disct = {}
        disct['id'] = row[0]
        disct['title'] = row[1]
        disct['description'] = row[2]
        disct['price'] = row[3]
        disct['edition'] = row[4]
        disct['author'] = row[5]
        disct['genre'] = row[6]
        disct['category'] = row[7]
        disct['photo'] = row[8]
        x.append(disct)
        data = {"x": x}
    return JsonResponse(data, safe=False)
    # q = f"select* from packages where name='{name}'"
    # result2=Fetchall(q)
    # y=[]
    # for row in result2:
    #     dict={}
    #     dict['pid']=row[0]
    #     dict['name']=row[1]
    #     dict['noofbooks']=row[2]
    #     dict['validity']=row[3]
    #     dict['price']=row[4]
    #     y.append(dict)
    #     data = {"y":y}
    # return JsonResponse(data,safe=False)


def deltebooks(request):
    id = request.GET['id']
    query = f"delete from books where bookid={id}"
    result = Delete(query)
    return HttpResponse(result)


def editbook(request):
    id = request.GET['id']
    print(id)
    sql = f"select * from books where bookid={id}"
    print(sql)
    result = Fetchall(sql)
    x = []
    for row in result:
        disct = {}
        disct['id'] = row[0]
        disct['title'] = row[1]
        disct['description'] = row[2]
        disct['price'] = row[3]
        disct['edition'] = row[4]
        disct['author'] = row[5]
        disct['genre'] = row[6]
        disct['category'] = row[7]
        disct['photo'] = row[8]
        x.append(disct)
        data = {"x": x}
    return JsonResponse(data, safe=False)


@csrf_exempt
def updateData(request):
    bookid = request.POST['id']
    title = request.POST['title']
    description = request.POST['description']
    price = request.POST['price']
    edition = request.POST['edition']
    author = request.POST['author']
    genre = request.POST['genre']
    file = ""
    try:
        file = request.FILES["file"]
    except:
        file = ""
    if file != "":
        name = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
        # print (id,title,description,price,edition,author,genre,file)
        s = f"update books set title='{title}',description=('{description}'),price='{price}',edition='{edition}',author='{author}',genre='{genre}',photo='{name}' where bookid=('{bookid}')"
        result = Update(s)
        fs = FileSystemStorage()
        fs.save(name, file)
    else:
        s = f"update books set title='{title}',description=('{description}'),price='{price}',edition='{edition}',author='{author}',genre='{genre}' where bookid=('{bookid}')"
        result = Update(s)
    return HttpResponse("success")


def samplebook(request):
    id = request.GET['id']
    # print(id)
    query = f"select * from sample where bookid='{id}'"
    result = Fetchall(query)
    # print(result)
    x = []
    for row in result:
        disct = {}
        disct['sid'] = row[0]
        disct['bookid'] = row[1]
        disct['description'] = row[2]
        disct['photo'] = row[3]
        x.append(disct)
    print(x)
    # return HttpResponse(data)
    return render(request, 'samplebook.html', {"ans": x, "id": id})


@csrf_exempt
def insertsample(request):
    file = request.FILES["photo"]
    print(file.name)
    name = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "insert into sample values(NULL,'" + request.POST["bookid"] + "','" + request.POST[
        "description"] + "','" + name + "')"
    fs = FileSystemStorage()
    fs.save(name, file)
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "sample added successfully"}
    return redirect(booksview)


# def viewsample(request):
#     id = request.GET['id']
#     print(id)
#     query = f"select * from sample where sid='{id}'"
#     result = Fetchall(query)
#     print(result)
#     x = []
#     for row in result:
#         disct = {}
#         disct['sid'] = row[0]
#         disct['bookid'] = row[1]
#         disct['description'] = row[2]
#         disct['photo'] = row[3]
#         x.append(disct)
#         data = {"x": x}
#     print(data['x'][0])
#     return HttpResponse(data)


@csrf_exempt
def deletesample(request):
    id = request.GET['id']
    print(id)
    query = f"delete from sample where sid={id}"
    result = Delete(query)
    return HttpResponse(result)


    cr.execute(s)
    conn.commit()
    conn.close()
    return HttpResponse("SUCCESS")



def adduser(request):
    return render(request, "signup.html")


@csrf_exempt
def insertuser(request):
    email = request.POST["id"]
    password = request.POST["password"]
    name = request.POST["name"]
    address = request.POST["address"]
    state = request.POST["state"]
    mobile = request.POST["mobileno"]
    file = request.FILES["photo"]
    print(email, file, password)
    pname = ("categoryphotos/newpics/" + str(random.randint(1, 10000)) + file.name)
    print(pname)
    global conn
    s = f"insert into usersignup values('{email}','{password}','{name}','{address}','{state}','{mobile}','{pname}')"
    print(s)
    fs = FileSystemStorage()
    fs.save(pname, file)
    result=Insert(s)
    return HttpResponse("SUCCESS")


def viewuser(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from usersignup"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(list(result))
    x = []
    for row in result:
        print(row)
        d = {}
        d["email"] = row[0]
        d["password"] = row[1]
        # d["confirmpassword"] = row[2]
        d["name"] = row[2]
        d["address"] = row[3]
        d["state"] = row[4]
        d["mobile"] = row[5]
        d["photo"] = row[6]
        x.append(d)
    print(x)
    return render(request, 'user.html', {"ans": x})



@csrf_exempt
def deleteuser(request):
    id = request.GET['email']
    print(id)
    query = f"delete from usersignup where email='{id}'"
    result = Delete(query)
    return HttpResponse(result)


def edituser(request):
    email = request.GET['email']
    # password = request.GET['password']

    print(email)
    # s="select * from usersignup where email="+email
    s = f"select * from usersignup where email={email}"
    print(s)
    result = Fetchall(s)
    print(result)
    x = []
    for row in result:
        d = {}
        d["email"] = row[0]
        d["password"] = row[1]
        # d["confirmpassword"] = row[2]
        d["name"] = row[2]
        d["address"] = row[3]
        d["state"] = row[4]
        d["mobile"] = row[5]
        d["photo"] = row[6]
        x.append(d)
    print(x)
    return render(request, 'userEdit.html', {"ar": x})

    # print(password)
    # confirmpassword = request.GET['confirmpassword']
    # print(confirmpassword)
    # name = request.GET['name']
    # print(name)
    # address = request.GET['address']
    # print(address)
    # state = request.GET['state']
    # print(state)
    # mobile = request.GET['mobile']
    # print(mobile)
    # photo = request.GET['photo']
    # print(photo)
    # return render(request, 'userEdit.html', {'email':email,"password":password,"confirmpassword":confirmpassword,"name":name,"address":address,"state":state,"mobile":mobile,"photo":photo})


def cardShow(request):
    query = "select * from category"
    result = Fetchall(query)
    print(result)
    x = []
    for row in result:
        disct = {}
        disct['catname'] = row[0]
        disct['description'] = row[1]
        disct['catphoto'] = row[2]
        x.append(disct)
    return render(request, 'cardShow.html', {"ans": x})


def saveuser(request):
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    name = request.POST['name']
    address = request.POST['address']
    state = request.POST['state']
    mobile = request.POST['mobileno']
    file = request.FILES["photo"]
    picname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    # print (id,title,description,price,edition,author,genre,file)
    s = f"update usersignup set password='{password}',confirmpassword='{confirmpassword}',name='{name}',address='{address}',state='{state}',mobile='{mobile}',photo='{picname}' where email=('{email}')"
    result = Update(s)
    fs = FileSystemStorage()
    fs.save(name, file)
    return HttpResponse("success")


def addpackage(request):
    return render(request, "packageinsert.html")


@csrf_exempt
def insertpackage(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")

    s = "insert into packages values(NULL ,'" + request.POST["name"] + "','" + request.POST["noofbooks"] + "','" + \
        request.POST["validity"] + "','" + request.POST["price"] + "')"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponse("Package added successfully")


def showpackage(request):
    query = "select * from packages"
    result = Fetchall(query)
    print(result)
    x = []
    for row in result:
        disct = {}
        disct['pid'] = row[0]
        disct['name'] = row[1]
        disct['numberofbooks'] = row[2]
        disct['validity'] = row[3]
        disct['price'] = row[4]
        x.append(disct)
    return render(request, 'viewpackage.html', {"ans": x})


def deletepackage(request):
    id = request.GET['q']
    print(id)
    query = f"delete from packages where pid='{id}'"
    result = Delete(query)
    return HttpResponse(result)


def editpackage(request):
    pid = request.GET['q']
    # password = request.GET['password']

    print(pid)
    # s="select * from usersignup where email="+email
    s = f"select * from packages where pid={pid}"
    print(s)
    result = Fetchall(s)
    print(result)
    x = []
    for row in result:
        disct = {}
        disct['pid'] = row[0]
        disct['name'] = row[1]
        disct['numberofbooks'] = row[2]
        disct['validity'] = row[3]
        disct['price'] = row[4]
        x.append(disct)
    print(disct)
    return render(request, 'editpackage.html', {"ar": x})


@csrf_exempt
def savepackage(request):
    pid = request.POST['id']
    name = request.POST['name']
    noofbooks = request.POST['noofbooks']
    validity = request.POST["validity"]
    price = request.POST["price"]
    # name = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    # print (id,title,description,price,edition,author,genre,file)
    s = f"update packages set name='{name}',noofbooks='{noofbooks}',validity='{validity}',price='{price}' where pid=('{pid}')"
    result = Update(s)
    # fs = FileSystemStorage()
    # fs.save(name, file)
    return redirect(showpackage)


def loginpage2(request):
    return render(request, "userlogin.html")


@csrf_exempt
def userlogin(request):
    global conn
    email = request.GET["Email"]
    password = request.GET["password"]
    s = f"select * from usersignup where email='{email}' and password='{password}'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    if result:
        request.session["Email"] = email
        return HttpResponseRedirect('/')
    else:
        return render(request, "userlogin.html")


def logoutuser(request):
    try:
        del request.session["Email"]
    except:
        pass
    return HttpResponseRedirect('/')


@csrf_exempt
def changeuserpassword(request):
    return render(request, "changeuserpassword.html")


@csrf_exempt
def updateuserpassword(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    email = str(request.session['Email'])
    s = "select * from usersignup where Email='" + email + "' and Password='" + request.POST["oldpassword"] + "'"
    print("hello")
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    if result:
        s = "update usersignup set password='" + request.POST["newpassword"] + "',confirmpassword='" + request.POST[
            'newpassword'] + "' where Email='" + email + "'"
        print("Bye")
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        d = {"message": "password changed successfully"}
        return render(request, "userlogin.html", {"ar": d})
    else:
        d = {"message": "invalid credentials"}
        return render(request, "changeuserpassword.html", {"ar": d})


# def index(request):
#     query = "select * from category"
#     result = Fetchall(query)
#     print(result)
#     return render(request, 'index.html', {'category': result})


def contact(request):
    return render(request, 'contact.html')


def showgenre(request):
    catname = request.GET['catname']
    query = f"select * from books where catname='{catname}'"
    result = Fetchall(query)
    print(result)
    return HttpResponse(result)


def showgenre(request):
    catname = request.GET['catname']
    query = f"select bookid,genre,photo from books where catname='{catname}'"
    result = Fetchall(query)
    print(result)
    bookstitle = []
    bookdata = []
    for row in result:
        if not bookstitle:
            bookstitle.append(row[1])
            dist = {}
            dist['bookid'] = row[0]
            dist['photo'] = row[2]
            dist['genre'] = row[1]
            dist['catname'] = catname
            bookdata.append(dist)
        elif row[1] in bookstitle:
            pass
        else:
            bookstitle.append(row[1])
            dist = {}
            dist['bookid'] = row[0]
            dist['photo'] = row[2]
            dist['genre'] = row[1]
            dist['catname'] = catname
            bookdata.append(dist)
    return render(request, 'bookgenre.html', {'bookdata': bookdata,'catname':catname})


@csrf_exempt
def showgenrebooks(request):
    catname = request.GET['catname']
    genre = request.GET['genre']
    query = f"select * from books where catname='{catname}' and genre='{genre}'"
    result = Fetchall(query)
    print(result)
    booksdata = []
    for row in result:
        dist = {'tid': row[0], 'title': row[1], 'discription': row[2], 'price': row[3], 'author': row[5],
                'genre': row[6], 'photo': row[8]}
        booksdata.append(dist)
    print(booksdata)
    return render(request, 'showgenrebooks.html', {'booksdata': booksdata})


def categorybooks(request):
    query = "select * from category"
    result = Fetchall(query)
    return render(request, 'categorybooks.html', {'category': result})

def showgenrebooksapmle(request):
    tid = request.GET['tid']
    query = f"select * from books where bookid={tid}"
    query2 = f"select * from sample where bookid={tid}"
    result = Fetchone(query)
    result2 = Fetchall(query2)
    firstlist = {'bookid': result[0], 'title': result[1], 'description': result[2], 'price': result[3],
                 'author': result[5], 'genre': result[6], 'catname': result[7], 'photo': result[8]}
    photolist = []
    if result2:
        for row in result2:
            dist = {}
            dist['sid'] = row[0]
            dist['bookid'] = row[1]
            dist['description'] = row[2]
            dist['photo'] = row[3]
            photolist.append(dist)
    print(firstlist)
    return render(request, 'showgenrebooksapmle.html', {'firstlist': firstlist, 'photolist': photolist})
# def demo(request):
#     query2 = f"select * from sample"
#     result2 = Fetchall(query2)
#     photolist = []
#     for row in result2:
#         dist = {}
#         dist['sid'] = row[0]
#         dist['bookid'] = row[1]
#         dist['description'] = row[2]
#         dist['photo'] = row[3]
#         photolist.append(dist)
#     print(photolist)
#     return render(request, 'demo1.html', {'photo1': photolist})

def index(request):
    query = f"select * from books"
    result = Fetchall(query)
    # print(result)
    bookstitle = []
    bookdata = []
    for row in result:
        if not bookstitle:
            bookstitle.append(row[1])
            bookdata.append(row[5])
            bookdata.append(row[6])
            bookdata.append(row[7])
        elif row[1] in bookstitle:
            pass
        else:
            bookstitle.append(row[1])
            bookdata.append(row[5])
            bookdata.append(row[6])
            bookdata.append(row[7])
    # print(bookdata)
    return render(request, 'index2.html', {'bookdata': bookdata})


def offer(request):
    offerquery = "select * from packages"
    offerresult = Fetchall(offerquery)
    # email = request.session["Email"]
    ##  request.session['email'] = "email"
    offer = []
    for row in offerresult:
        dist = {}
        dist['pid'] = row[0]
        dist['name'] = row[1]
        dist['noofbooks'] = row[2]
        dist['validity'] = row[3]
        dist['price'] = row[4]
        offer.append(dist)
    return render(request, 'offers.html', {'offers': offer})


@csrf_exempt
def viewallbooks(request):
    search = request.POST['search']
    if search == "":
        query = "select * from books"
    else:
        query = f"select * from books where title='{search}' or author='{search}' or catname='{search}' or genre='{search}'"
    print(query)
    result = Fetchall(query)
    print(result)
    bookdatalist = []
    if result:
        for row in result:
            firstlist = {'bookid': row[0], 'title': row[1], 'description': row[2], 'price': row[3],
                         'author': row[5], 'genre': row[6], 'catname': row[7], 'photo': row[8]}
            bookdatalist.append(firstlist)
    else:
        bookdatalist.append({'result': 'no'})
    return JsonResponse(bookdatalist, safe=False)


CARTLIST = []


def addtocart(request):
    global CARTLIST
    CARTLIST = []
    try:
        CARTLIST = request.session['addtocart']
    except:
        pass
    print('first', CARTLIST)
    bookid = request.GET['bookid']
    qty = request.GET['qty']
    query = f"SELECT `bookid`, `title`, `description`, `price`, `edition`, `author`, `genre`, `catname`, `photo` FROM `books` WHERE bookid={bookid}"
    result = Fetchall(query)
    flag = False
    for row1 in CARTLIST:
        if int(bookid) == int(row1['bookid']):
            if int(row1['qty']) < int(qty):
                row1['qty'] = qty
                row1['price'] = float(row1['price']) * float(row1['qty'])
                # print("hello")
                flag = True
                break
            else:
                flag = True
                break
    if flag == False:
        for row in result:
            dict = {}
            dict['bookid'] = bookid
            dict['qty'] = qty
            dict['title'] = row[1]
            dict['photo'] = row[8]
            dict['price'] = float(row[3]) * float(qty)
            CARTLIST.append(dict)
    print(CARTLIST)
    request.session['addtocart'] = CARTLIST
    datalength = len(request.session['addtocart'])
    return HttpResponse(datalength)


def showcartproducat(request):
    total = 0
    li = []
    try:
        li = request.session['addtocart']
        for row in request.session['addtocart']:
            total += float(row['price'])
    except:
        pass
    print(total)
    print(li)
    return render(request, 'showcartproducat.html', {'total': total, 'datalist': li})


def delete_from_cart(request):
    bookid = request.GET["bookid"]
    # print(bookid)
    li = request.session['addtocart']
    # print(li)
    print(li)
    for i in range(0, len(li)):
        if int(li[i]["bookid"]) == int(bookid):
            del li[i]
            break
    print(li)
    request.session['addtocart'] = li
    return HttpResponseRedirect('showcartproducat')


def processtopay(request):
    # request.session["Email"]
    if 'Email' not in request.session:
        return HttpResponseRedirect('loginpage2')
    else:
        total = 0
        for row in request.session['addtocart']:
            total += float(row['price'])
        email = request.session["Email"]
        query = f"SELECT `email`, `password`, `name`, `address`, `state`, `mobile`, `photo` FROM `usersignup` WHERE email='{email}'"
        result = Fetchone(query)
        print(result)
        userdata = {'email': email, 'mobile': result[5], 'name': result[2], 'address': result[3], 'total': total}
        return render(request, 'processtopay.html', {'userdata': userdata})


from datetime import *


@csrf_exempt
def payment_action(request):
    email = request.session["Email"]
    name = request.POST['name']
    mobile = request.POST['mobile']
    address = request.POST['address']
    total = request.POST['total']
    paymentmode = request.POST['paymentmode']
    dateoforder = date.today()
    if paymentmode == "Cash":
        query = f"INSERT INTO `bills`(`totalamount`, `email`, `address`, `mobile`, `status`, `typeofbill`,`dateoforder`,`rating`) VALUES ({total},'{email}','{address}','{mobile}','pending','{paymentmode}','{dateoforder}','pending')"
    else:
        query = f"INSERT INTO `bills`(`totalamount`, `email`, `address`, `mobile`, `status`, `typeofbill`,`dateoforder`,`rating`) VALUES ({total},'{email}','{address}','{mobile}','complete','{paymentmode}','{dateoforder}','pending')"
    Insert(query)

    # return HttpResponse(1)
    qr = "select billid from bills order by billid DESC"
    t1 = Fetchall(qr)
    billid = t1[0][0]
    print(request.session['addtocart'])
    for row in request.session['addtocart']:
        qr1 = f"INSERT INTO `billdetails`( `billid`, `bookid`, `price`, `qty`,`ratingstatus`) VALUES ({billid},{row['bookid']},{float(row['price']) * float(row['qty'])},{row['qty']},'pending')"
        result = Insert(qr1)
        print(result)
        print(qr1)
    del request.session['addtocart']
    return JsonResponse({'billid': billid}, safe=False)


def thankspage(request):
    bill_id = request.GET['billid']
    return render(request, 'thankyou.html', {"bill_id": bill_id})


def insertebook(request):
    global conn
    s = "select * from packages"
    cr = conn.cursor()
    cr.execute(s)
    res = cr.fetchall()
    x = []
    for row in res:
        d = {}
        d["pid"] = row[0]
        d["pname"] = row[1]
        x.append(d)
    return render(request, "ebooks.html", {"ar": x})


@csrf_exempt
def ebooks(request):
    # ebookid = request.POST["ebookid"]
    pid = request.POST["pid"]
    title = request.POST["title"]
    description = request.POST["description"]
    file = request.FILES["file"]
    pname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    print(pname)
    global conn
    s = "insert into ebooks values(NULL,'" + pid + "','" + title + "','" + description + "','" + pname + "')"
    fs = FileSystemStorage()
    fs.save(pname, file)
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    # conn.close()
    return HttpResponse("SUCCESS")


def viewebookscover(request):
    pid = request.GET['pid']
    query = f"select Title from ebooks where pid={pid}"
    result = Fetchall(query)
    ebooktitle = []
    for row in result:
        ebooktitle.append(row[0])
    return JsonResponse(ebooktitle, safe=False)


@csrf_exempt
def Subscription(request):
    if 'Email' in request.session:
        pid = request.POST['pid']
        email = request.POST['email']
        price = request.POST['price']
        dateofbuy = date.today()
        query = f"INSERT INTO `subscription`(`pid`, `email`, `status`, `dateofbuy`, `amount`) VALUES ({pid},'{email}','Active','{dateofbuy}','{price}')"
        result = Insert(query)
        return HttpResponse("sucess")
    else:
        return HttpResponseRedirect('fail')


def viewebooks(request):
    if 'Email' in request.session:
        email = request.session['Email']
        query = f"SELECT pid FROM `subscription` WHERE email='{email}'"
        result = Fetchall(query)
        pidlist = []
        ebookslist = []
        if result:
            for row in result:
                pidlist.append(row[0])
            for row1 in pidlist:
                query1 = f"select * from ebooks where pid={row1}"
                result1 = Fetchall(query1)
                # ebookslist.append(result1)
                for row2 in result1:
                    dist = {}
                    dist['eboooksid'] = row2[0]
                    dist['pid'] = row2[1]
                    dist['title'] = row2[2]
                    dist['desc'] = row2[3]
                    dist['file'] = row2[4]
                    ebookslist.append(dist)
        return render(request, 'viewebooks.html', {'data': ebookslist})
    else:
        return HttpResponseRedirect('loginpage2')


def readebooksfull(request):
    ebookid = request.GET['ebookid']
    query = "select * from ebooks where ebookid={}".format(str(ebookid))
    print(query)
    result = Fetchone(query)
    return render(request, 'readebooksfull.html', {'data': result})


def pendingpayment(request):
    query = "select * from bills"
    result = Fetchall(query)
    paymentstatus = []
    for row in result:
        dist = {}
        dist['id'] = row[0]
        dist['totalamount'] = row[1]
        dist['email'] = row[2]
        dist['address'] = row[3]
        dist['mobile'] = row[4]
        dist['status'] = row[5]
        dist['typeofbill'] = row[6]
        dist['dateoforder'] = row[7]
        dist['rating'] = row[8]
        paymentstatus.append(dist)
    return render(request, 'paymentstatus.html', {'data': paymentstatus})


def changepayment(request):
    id = request.GET['id']
    query = f"UPDATE `bills` SET `typeofbill`='done' WHERE billid={id}"
    result = Update(query)
    return HttpResponseRedirect('pendingpayment')


from http.client import HTTPResponse
import http.client


def dispatch(request):
    id = request.GET['id']
    mobile = request.GET['mobile']
    query = f"UPDATE `bills` SET `status`='sucess' WHERE billid={id}"
    result = Update(query)
    print(result)
    msg = f"Your Product Bill id {id} is dispatched."
    msg = msg.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                 '/VMMCloudMessaging/AWS_SMS_Sender?username=radhikabhatia&password=ZHLHK6IJ&message=' + msg + '&phone_numbers=' + str(
                     mobile))
    response = conn.getresponse()
    return HttpResponseRedirect('pendingpayment')


def requestforrating(request):
    id = request.GET['id']
    email = request.GET['email']
    mobile = request.GET['mobile']
    query = f"UPDATE `bills` SET `rating`='done' WHERE billid={id}"
    v = Update(query)
    print(v)
    query1 = f"select * from billdetails where billid={id}"
    result = Fetchall(query1)
    listpending = []
    for row in result:
        listpending.append(row[2])
    print(listpending)
    for row in listpending:
        msg = f"Will you please take a minute to share your experience click on http://127.0.0.1:8000/ratemyproduct?billid={id}&bookid={row}"
        print(msg)
        msg = msg.replace(" ", "%20")
        conn = http.client.HTTPConnection("server1.vmm.education")
        conn.request('GET',
                     '/VMMCloudMessaging/AWS_SMS_Sender?username=radhikabhatia&password=ZHLHK6IJ&message=' + msg + '&phone_numbers=' + str(
                         mobile))
        response = conn.getresponse()
        print(response)
        sender = 'python.vmm@gmail.com'
        receiver = email
        password = 'vmmpython'
        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(sender, password)
            body = msg
            subject = "Subject:Rating "
            msg = subject + body
            # msg='Subject:Demo <h1>This is a test e-mail message.</h1>'
            smtpserver.sendmail(sender, receiver, msg)
            print('Sent')
            smtpserver.close()
        except smtplib.SMTPException:
            print("Not Sent")
    return HttpResponse('success')


def ratemyproduct(request):
    billid = request.GET['billid']
    bookid = request.GET['bookid']
    query = f"select * from bills where `billid`={billid} order by dateoforder DESC"
    result = Fetchone(query)
    # print(result)

    queryfind=f"SELECT `ratingid`, `rating`, `bookid`, `review`, `email` FROM `ratings` WHERE bookid={bookid}"
    print(queryfind)
    result1=Fetchall(queryfind)
    ratingss=[]
    if result1:
        for row in result1:
            dist={}
            dist['rating']=row[1]
            dist['comment']=row[3]
            dist['email']=row[4]
            ratingss.append(dist)
    return render(request, 'ratemyproduct.html', {'bookid': bookid, 'result': result,'rating':ratingss})


@csrf_exempt
def addrating(request):
    bookid = request.POST['bookid']
    email = request.POST['email']
    rating = request.POST['rating']
    comment = request.POST['comment']
    querycheck = f"SELECT `ratingid`, `rating`, `bookid`, `review`, `email` FROM `ratings` WHERE email='{email}' and bookid={bookid}"
    print(querycheck)
    resultcheck = Fetchall(querycheck)
    print("fr", resultcheck)
    if resultcheck:
        updatequesry = f"UPDATE `ratings` SET `rating`='{rating}',`bookid`='{bookid}',`review`='{comment}',`email`='{email}' WHERE email='{email}' and bookid={bookid}"
        result1 = Update(updatequesry)
        print('update:-',result1)
    else:
        query = f"INSERT INTO `ratings`(`rating`, `bookid`, `review`, `email`) VALUES ('{rating}','{bookid}','{comment}','{email}')"
        result2 = Insert(query)
        print('insert:-',result2)
    return HttpResponseRedirect('/')


def demo(request):
    return render(request, 'demo.html')
