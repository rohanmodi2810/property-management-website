from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from property.models import owner, Customer, sales, property, requirement
from property.models import curr
from django.core.files.storage import FileSystemStorage
import numpy as np

# Create your views here.
from django.http import HttpResponse

pid = 0
sid = 0
_username_owner = ""



def signup_buyer(request):
    return render(request, 'signup_buyer.html')


def signup_owner(request):
    return render(request, 'signup_owner.html')


def log_in_page_owner(request):
    return render(request, 'log_in_page_owner.html')


def log_in_page_buyer(request):
    return render(request, 'log_in_page_buyer.html')


def go_to_owner_home(request):
    return render(request, 'owner_home.html')


def go_to_customer_home(request):
    return redirect('/search_property/')


def about(request):
    global sid
    global pid
    c = curr.objects.all()

    for i in c:
        pid = i.pid
        sid = i.sid

    print(pid)
    return render(request, 'home.html')


def temp(request):
    return render(request, 'temp.html')


def loginpage_owner(request):
    return render(request, 'log_in.html')


def loginpage_buyer(request):
    return render(request, 'log_in_buyer.html')


def login_owner(request):
    if request.method == "POST":
        username = request.POST['uname']
        pass1 = request.POST['psw']

    user = auth.authenticate(username=username, password=pass1)

    if user is not None:
        auth.login(request, user)
        global _password_owner
        _password_owner = pass1;
        global _username_owner
        _username_owner = username;
        return redirect('/go_to_owner_home/')
    else:
        messages.info(request, 'Please sign up to be a part of real city family')
        return render(request, "log_in.html")


def login_buyer(request):
    if request.method == "POST":
        username = request.POST['uname']
        pass1 = request.POST['psw']

    print('came to login buyer')
    user = auth.authenticate(username=username, password=pass1)

    if user is not None:
        auth.login(request, user)
        global _password_buyer
        _password_buyer = pass1;
        global _username_buyer
        _username_buyer = username;
        return redirect('/go_to_customer_home/')
    else:
        messages.info(request, 'Please sign up to be a part of real city family')
        return render(request, "log_in_buyer.html")


def register_buyer(request):
    username = request.POST['username']
    pass1 = request.POST['password']
    pass2 = request.POST['password1']
    email = request.POST['email-id']

    if pass1 == pass2:
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already taken.')
            return render(request, 'signup_buyer.html')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'email-id already taken.')
            return render(request, 'signup_buyer.html')
        else:
            user = User.objects.create_user(username=username, password=pass1, email=email)
            user.save();
            messages.info(request, 'Welcome to family of real city,please login')
            global _username1
            _username1 = username
            global _password1
            _password1 = pass1
            global _email_id1
            _email_id1 = email
            return render(request, 'index (1).html')
    else:
        messages.warning(request, 'Please note that both password field should contain identical password')
        return render(request, 'signup_buyer.html')


def register_seller(request):
    username = request.POST['username']
    pass1 = request.POST['password']
    pass2 = request.POST['password1']
    email = request.POST['email-id']

    if pass1 == pass2:
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already taken.')
            return render(request, 'signup_owner.html')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'email-id already taken.')
            return render(request, 'signup_owner.html')
        else:
            user = User.objects.create_user(username=username, password=pass1, email=email)
            user.save();
            messages.info(request, 'Welcome to family of real city,please login')
            global _username2
            _username2 = username;
            global _password2
            _password2 = pass1;
            global _email_id2
            _email_id2 = email;
            return render(request, 'index(2).html')
    else:
        messages.warning(request, 'Please note that both password field should contain identical password')
        return render(request, 'signup_owner.html')


def seller_info(request):
    username = _username2;
    pass1 = _password2;
    email = _email_id2;
    first_name = request.POST['First_name']
    second_name = request.POST['Second_name']
    DOB = request.POST['dob']
    gender = request.POST['gender']
    b_address = request.POST['address']
    number = request.POST['contact']

    if owner.objects.filter(owner_id=username).exists():
        messages.warning(request, 'Enter Correct Useranme')
        return render(request, 'index(2).html')
    elif owner.objects.filter(email=email).exists():
        messages.warning(request, 'Enter Correct email')
        return render(request, 'index(2).html')
    else:
        seller = owner(owner_id=username, email=email, first_name=first_name, second_name=second_name, DOB=DOB,
                       gender=gender, b_address=b_address, number=number)
        seller.save()
        messages.warning(request, 'please login')
        return render(request, 'log_in.html')


def buyer_info(request):
    cust_id = _username1;
    pass1 = _password1;
    email = _email_id1;
    first_name = request.POST['First_name']
    second_name = request.POST['Second_name']
    c_address = request.POST['address']
    number = request.POST['contact']

    if Customer.objects.filter(cust_id=cust_id).exists():
        messages.warning(request, 'Enter Correct Useranme')
        return render(request, 'index (1).html')
    elif Customer.objects.filter(email=email).exists():
        messages.warning(request, 'Enter Correct email')
        return render(request, 'index (1).html')
    else:
        buyer = Customer(cust_id=cust_id, email=email, first_name=first_name, second_name=second_name,
                         c_address=c_address, number=number)
        buyer.save()
        messages.warning(request, 'Please Login')
        return render(request, 'log_in_buyer.html')


def owner_history(request):
    username = _username_owner

    p = sales.objects.filter(cust_id=username)
    d = {'p': p}
    return render(request, 'history.html', d);


def customer_history(request):
    username = _username_buyer

    p = sales.objects.filter(cust_id=username)
    d = {'p': p}
    return render(request, 'history_customer.html', d);


def add(request):
    return render(request, 'index.html')


def update_this(request, id):
    p = property.objects.get(prop_id=id)
    d = {'p': p}
    return render(request, 'update_this.html', d)


def update_id(request, id):
    name = request.GET['flate_name']
    ptyp = request.GET['ptype']
    floor_no = request.GET['floor_no']
    price = request.GET['price']
    size = request.GET['size']
    age = request.GET['age']
    address = request.GET['address']

    city = request.GET['area']
    print(123)
    p = property.objects.get(prop_id=id)
    if (name != ""):
        p.pname = name
    if (floor_no != ""):
        p.floor = int(floor_no)
    if (ptyp != ""):
        p.ptype = int(ptyp)
    if (price != ""):
        p.price = int(price)
    if (size != ""):
        p.size = int(size)
    if (age != ""):
        p.p_age = int(age)
    if (address != ""):
        p.p_address = address
    if (city != ""):
        p.area = city
    p.save()
    d = {'p': p}
    return render(request, 'owner_home.html', d)


def update(request):
    p = property.objects.filter(owner_id=_username_owner, pstatus=False)
    list = [i for i in range(len(p))]
    print(len(p))
    d = {'p': p, 'len': list, 'c': 0}

    return render(request, 'updateProp.html', d);


def delete(request):
    p = property.objects.filter(owner_id=_username_owner, pstatus=False)
    d = {'p': p}

    return render(request, 'delete.html', d);


def delete_this(request, id):
    p = property.objects.get(prop_id=id)
    p.delete()
    p = property.objects.all()
    d = {'p': p}
    return render(request, 'owner_home.html', d);


def myProperty(request):
    p = property.objects.filter(owner_id=_username_owner, pstatus=False)

    s = list(sales.objects.filter(owner_id=_username_owner))
    sold = []
    print(len(list(p)))
    print(_username_owner)
    for i in s:
        sold.extend(property.objects.filter(prop_id=i.prop_id))
    print(len(sold))
    d = {'p': p, 's': sold}
    # print(sold[0].pname)
    return render(request, 'myProperty.html', d);


def view_this(request, id):
    p = property.objects.get(prop_id=id)
    d = {'p': p}
    return render(request, 'view_this.html', d)


def add_property(request):
    global property
    global pid
    c = curr.objects.all()
    name = request.POST['flate_name']
    ptyp = int(request.POST['ptype'])
    floor_no = int(request.POST['floor_no'])
    price = int(request.POST['price'])
    size = int(request.POST['size'])
    age = int(request.POST['age'])
    address = request.POST['address']
    city = request.POST['area']

    img = request.FILES['im']
    f = FileSystemStorage()
    f.save(img.name, img)
    pid += 1
    for i in c:
        i.pid = pid
        i.save()

    Property = property(prop_id=pid, pname=name, ptype=ptyp, pstatus=False, price=price, p_address=address,
                        owner_id=_username_owner, floor=floor_no, p_age=age, size=size, area=city, image=img.name)
    Property.save()
    return render(request, 'owner_home.html')


def index(request):
    return render(request, 'index.html')


def search_property(request):
    bhk = request.GET.get('bhk', '')
    minprice = request.GET.get('minprice', '')
    maxprice = request.GET.get('maxprice', '')
    location = request.GET.get('location', '')
    minsize = request.GET.get('minsize', '')
    maxsize = request.GET.get('maxsize', '')

    all_props = property.objects.none()
    temp = property.objects.all()
    flag = False
    if bhk != '':
        temp = temp.filter(ptype=int(bhk), pstatus=False)
        print(temp)
        all_props = all_props.union(temp)
        flag = True
    if minprice != '' and maxprice != '':
        temp = temp.filter(price__gte=int(minprice), price__lte=int(maxprice), pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    elif minprice != '':
        temp = temp.filter(price__gte=int(minprice), pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    elif maxprice != '':
        temp = temp.filter(price__lte=int(maxprice), pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    if (location != ''):
        temp = temp.filter(area=location, pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    if minsize != '' and maxsize != '':
        temp = temp.filter(size__gte=int(minsize), size__lte=int(maxsize), pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    elif minsize != '':
        temp = temp.filter(size__gte=int(minsize), pstatus=False)
        all_props = all_props.union(temp)
        flag = True
    elif maxsize != '':
        temp = temp.filter(size__lte=int(maxsize), pstatus=False)
        all_props = all_props.union(temp)
        flag = True

    val = ""
    if flag == False:
        all_props = property.objects.filter(pstatus=False)
    if len(all_props) == 0:
        val = "No matches found!"
    print(all_props)
    params = {'all_props': all_props, 'val': val}
    return render(request, 'customer_home.html', params)


def done_buy(request, p_id):
    p = property.objects.get(prop_id=p_id)

    # print('done buy')
    p.pstatus = True;

    customer = _username_buyer
    owner = p.owner_id
    prop_id = p_id
    price = p.price
    global sid
    c = curr.objects.all()
    sid = sid + 1;
    for i in c:
        i.sid = sid
        i.save()

    history = sales(cust_id=customer, owner_id=owner, prop_id=prop_id, price=price, sid=sid);

    history.save();
    p.owner_id = _username_buyer;
    p.save();
    params = {'p': p}

    return render(request, 'done_buy.html', params)

def buyer_history(request):
    s =list(sales.objects.filter(cust_id=_username_buyer))
    t=[]
    for i in s:
        t.extend(property.objects.filter(prop_id=i.prop_id))
    d = {'s':t}
    return render(request, 'buyer_history.html', d);


def ContactUs(request):
    return render(request, 'ContactUs.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')


def predictPrice(request):
    return render(request, 'predictPrice.html')


def getPrice(request):
    ptyp = int(request.POST['ptype'])
    floor_no = int(request.POST['floor_no'])
    size = int(request.POST['size'])
    age = int(request.POST['age'])
    p = property.objects.all()
    x=[]
    y=[]
    for i in p:
        x.append([1, i.size, i.ptype, i.floor, i.p_age ])
        y.append([i.price])

    x = np.array(x)
    y = np.array(y)

    t = np.dot(np.linalg.pinv(np.dot(np.transpose(x),x)),np.dot(np.transpose(x),y))
    t=t.transpose()
    price = t[0][0] + t[0][1]*int(size) + t[0][2]*int(ptyp) + t[0][3]*int(floor_no) + t[0][4]*age
    d = {'p': price, 'ptyp':ptyp, 'floor':floor_no, 'size' : size, 'age' : age}
    print(t)
    return render(request, 'getPrice.html',d)
