from django.shortcuts import render
from.models import Heath_Record,Csv
from pandas import read_csv
from graph import utils,indi
def index(request):
    queryset=Heath_Record.objects.all()
    x=[i.average_pulse  for i in queryset]
    y=[i.calorie_burnage for i in queryset]
    chart=utils.plot(x,y)
    data=Csv.objects.all()
    mydata=[i.csv for i in data]
    print(mydata[0])      
    print(mydata[1])
    df1 = read_csv(mydata[0])
    df2 = read_csv(mydata[1])
    z=df2['x']
    k=df2['y']
    chart2=indi.plot(z,k)
    return render(request,'index.html',{'key':chart,'key2':df1.to_html(),'key3':df2.to_html(),'key4':chart2})
    
   
