from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method=="POST":
        un=request.POST['name'] #username
        em=request.POST['email'] #email
        pd1=request.POST['password']
        pd2=request.POST['re_password']
        if pd1==pd2:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html") 
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=un,email=em,password=pd1)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return render (request,"register.html")
    else:
        return render(request,"register.html")       
def client(request):
    return render(request,"client.html")
def contact(request):
    return render(request,"contact.html")
def health(request):
    return render(request,"health.html")
def medicine(request):
    return render(request,"medicine.html")
def news(request):
    return render(request,"news.html")
def login(request):
    if request.method=="POST":
        un=request.POST['name']
        pd=request.POST['pass']
        user=auth.authenticate(username=un,password=pd)
        if user is not None:
            auth.login(request,user)
            return redirect("index")
        else:
            messages.info(request,"Invalid credentials")
            return render(request,"register.html")

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("index")

def diabetes(request):
    return render(request,"diabetes.html")

def diabetespredict(request):
    if request.method=="POST":
        preg=request.POST['preg']
        glucose=request.POST['glucose']
        bp=request.POST['bp']
        skin=request.POST['skin']
        insulin=request.POST['insulin']
        bmi=request.POST['bmi']
        pedigree=request.POST['pedigree']
        age=request.POST['age']
        import pandas as pd
        df=pd.read_csv(r"D:\diabeties\medic\static\datasets\diabetes.csv")
        print(df.isnull().sum())
        print(df.dropna())
        X_train=df[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]
        y_train=df[["Outcome"]]
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestClassifier
        ran=RandomForestClassifier()
        log=LogisticRegression()
        ran.fit(X_train,y_train)
        pred=ran.predict([[preg,glucose,bp,skin,insulin,bmi,pedigree,age]])
        
        return render(request,"diabetespredict.html",
                      {"preg":preg,"glucose":glucose,"bp":bp,"skin":skin,"insulin":insulin,"bmi":bmi,"pedigree":pedigree,"age":age,"pred":pred})
    
    else:
        return render(request,"diabetespredict.html")
    
