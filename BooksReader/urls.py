"""BooksReader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("loginpage", loginpage),
    path("login", login),
    path("addadmin", addadmin),
    path("insertadmin", insertadmin),
    path("showadmin", showadmin),
    path("editadmin", editadmin),
    path("saveadmin", save),
    path("changepassword", changepassword),
    path("updatepassword", updatepassword),
    path("removeadmin", removeadmin),
    path("addcategory", addcategory),
    path('adminlogout',adminlogout),
    path("insertcategory", insertcategory),
    path("showcategory", showcategory),
    path("removecategory", removecategory),
    path("editcategory", editcategory),
    path("savecategory", save),
    path("addbook", addbook),
    path("insertbook", insertbook),
    path("logoutuser", logoutuser),
    path("booksview", booksview),
    path("viewbooks", viewbooks),
    path("deltebooks", deltebooks),
    path("editbook", editbook),
    path("updateData", updateData),
    path("samplebook", samplebook),
    path("insertsample", insertsample),
    # path("viewsample", viewsample),
    path("deletesample", deletesample),
    path("adduser", adduser),
    path("insertuser", insertuser),
    path("viewuser", viewuser),
    path("deleteuser", deleteuser),
    path("edituser", edituser),
    path("saveuser", saveuser),
    path("cardShow", cardShow),
    path("addpackage", addpackage),
    path("insertpackage", insertpackage),
    path("showpackage", showpackage),
    path("deletepackage", deletepackage),
    path("editpackage", editpackage),
    path("savepackage", savepackage),
    path("loginpage2", loginpage2),
    path("userlogin", userlogin),
    path("changeuserpassword", changeuserpassword),
    path("updateuserpassword", updateuserpassword),
    path("", index),
    path("contact", contact),
    path("showgenre", showgenre),
    path("showgenrebooks", showgenrebooks),
    path("categorybooks", categorybooks),
    path("showgenrebooksapmle", showgenrebooksapmle),
    # path("demo",demo),
    path("viewallbooks", viewallbooks),
    path("addtocart", addtocart),
    path("showcartproducat", showcartproducat),
    path("delete_from_cart", delete_from_cart),
    path("processtopay", processtopay),
    path("payment_action", payment_action),
    path("thankspage", thankspage),
    path("insertebook", insertebook),
    path("ebooks", ebooks),
    path("offer", offer),
    path("viewebookscover", viewebookscover),
    path("Subscription", Subscription),
    path("viewebooks", viewebooks),
    path("readebooksfull", readebooksfull),
    path("pendingpayment", pendingpayment),
    path("changepayment", changepayment),
    path("dispatch", dispatch),
    path("requestforrating", requestforrating),
    path("ratemyproduct", ratemyproduct),
    path("demo", demo),
    path("addrating", addrating),
]
