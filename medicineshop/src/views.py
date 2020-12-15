from .models import Insurance
from .models import Customer
from .models import Medicine
from .models import Payment
from .models import availability
from .models import orderlist
from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form=UserCreationForm()
    return render(request,'src/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
    return render(request,'src/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')


def home(request):
    return render(request, 'src/index.html')

def custform(request):
    dict = {'add': True}
    return render(request, 'src/cust.html', dict)


def custforminsert(request):
    try:
        cust = Customer()
        cust.c_id = request.POST['c_id']
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(c_id=foo)
        cust.c_id = request.POST['c_id']
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def custformview(request, foo):
    cust = Customer.objects.get(c_id=foo)
    dict = {'cust': cust}
    return render(request, 'src/cust.html', dict)


def custformdelete(request, foo):
    cust = Customer.objects.get(c_id=foo)
    cust.delete()
    return render(request, 'src/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'src/custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'src/med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['m_id']
        med.mname = request.POST['mname']
        med.quantity = request.POST['quantity']
        med.m_type = request.POST['type']
        med.price = request.POST['price']
        med.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(m_id=foo)
        med.m_id = request.POST['m_id']
        med.mname = request.POST['mname']
        med.quantity = request.POST['quantity']
        med.m_type = request.POST['type']
        med.price = request.POST['price']
        med.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(m_id=foo)
    print(foo)
    dict = {'med': med}
    return render(request, 'src/med.html', dict)


def medformdelete(request, foo):
    med = Medicine.objects.get(m_id=foo)
    med.delete()
    return render(request, 'src/index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'src/medtable.html', dict)

def ordform(request):
    med=Medicine.objects.all()
    dict = {'add': True,'med':med}
    return render(request, 'src/ord.html', dict)


def ordforminsert(request):
    try:
        o = orderlist()
        o.o_id = request.POST['o_id']
        o.m_id = request.POST['m_id']
        o.c_id = request.POST['c_id']
        o.quantity = request.POST['quantity']
        m=Medicine.objects.get(m_id=o.m_id)
        o.cost=int(m.price)*int(o.quantity)
        o.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def ordformupdate(request, foo):
    try:
        o = orderlist.objects.get(o_id=foo)
        o.o_id = request.POST['o_id']
        o.c_id = request.POST['c_id']
        o.m_id = request.POST['m_id']
        o.quantity = request.POST['quantity']
        m=Medicine.objects.get(m_id=o.m_id)
        o.cost=int(m.price)*int(o.quantity)
        o.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def ordformview(request, foo):
    o = orderlist.objects.get(o_id=foo)
    med=Medicine.objects.all()
    dict = {'ord': o,'med':med}
    return render(request, 'src/ord.html', dict)


def ordformdelete(request, foo):
    o = orderlist.objects.get(o_id=foo)
    o.delete()
    return render(request, 'src/index.html')


def ordtable(request):
    o = orderlist.objects.all()
    med=Medicine.objects.all()
    dict = {"ord": o,"med":med}
    return render(request, 'src/ordtable.html', dict)


def insform(request):
    dict = {'add': True}
    return render(request, 'src/ins.html', dict)


def insforminsert(request):
    try:
        i=Insurance()
        i.ins_no = request.POST['ins_no']
        i.c_id = request.POST['c_id']
        i.company = request.POST['company']
        i.percent = request.POST['percent']
        i.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def insformupdate(request, foo):
    try:
        i=Insurance.objects.get(ins_no=foo)
        i.ins_no = request.POST['ins_no']
        i.c_id = request.POST['c_id']
        i.company = request.POST['company']
        i.percent = request.POST['percent']
        i.save()
    except IntegrityError:
        return render(request, "src/new.html")
    return render(request, 'src/index.html')


def insformview(request, foo):
    i=Insurance.objects.get(ins_no=foo)
    print(foo)
    dict = {'ins': i}
    return render(request, 'src/ins.html', dict)


def insformdelete(request, foo):
    i=Insurance.objects.get(ins_no=foo)
    i.delete()
    return render(request, 'src/index.html')


def instable(request):
    i=Insurance.objects.all()
    dict = {"ins": i}
    return render(request, 'src/instable.html', dict)


def cart(request):
    c=Customer.objects.all()
    dict = {"cust": c}
    return render(request, 'src/cart.html', dict)

def viewpurchase(request):
    c = request.POST['c_id']
    o = orderlist.objects.filter(c_id=c)
    s=0
    for obj in o:
        s+=obj.cost
    dict = {"ord": o,"s":s}
    return render(request, 'src/viewcart.html', dict)
