from django.shortcuts import render
import joblib
import pandas as pd
import numpy as np
#from sklearn.preprocessing import StandardScalar


def index(request):
    if(request.method == 'POST'):
        bateryCapacity = request.POST['BC']
        ram = request.POST['RAM']
        camera = request.POST['NOC']
        pr = request.POST['PR']
        sr = request.POST['SR']
        rom = request.POST['RO']
        r = request.POST['Rating']
        print(ram,r,bateryCapacity,camera,rom,sr)
        decisionTreeRegressor = joblib.load('DecisionTreeMobile.sav')
        ls = np.array([[r],[bateryCapacity],[sr],[ram],[rom],[camera],[pr]]).reshape(-1,1)
        lis = [r,bateryCapacity,sr,ram,rom,camera,pr]
        # sc = StandardScalar()
        # lis = sc.fit_transform(lis)
        ans = decisionTreeRegressor.predict([lis])
        ans = int(ans//2.5)
        return render(request,'index.html',{'Ans':ans})
    return render(request,'index.html')
# Create your views here.
