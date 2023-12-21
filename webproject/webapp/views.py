from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from webapp.models import Employee
from webapp.forms import EmployeeForm
def read(request):
	employee=Employee.objects.all()
	return render(request,'apps/result.html',{'e':employee})
def insert(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	e=Employee.objects.get(id=id)
	e.delete()	
	return redirect('/result')
def update(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'e':employee})
def index(request):
	return render(request,'apps/index.html')
def home(request):
	return render(request,'apps/home.html')
@login_required
def gallery(request):
	return render(request,'apps/gallery.html')
def service(request):
	return render(request,'apps/service.html')
def logout(request):
	return render(request,'apps/logout.html')