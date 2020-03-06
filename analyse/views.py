from django.shortcuts import render
from importlib import reload
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import ScrapeForm
import json
import re
from .utils import *

# Create your views here.

def analyse_data(request):
	if request.method == 'POST':
		data_features=['camera','battery','performance','storage','budget']
		x=request.POST.get('url')
		det=x.find('ref')
		det2=x.find('product-reviews')+16
		finalst=x[det2:det-1]
		flag=False
		objct=Features.objects.all()
		if objct:
			for i in objct:
				if i.url==x:
					flag=True
		if flag==True:
			default=[]
			#pos_comment=[]
			#neg_comment=[]
			positive=""
			negative=""
			neutral=""
			obj=Features.objects.get(url=x)
			details_lst=obj.details.split(';')
			details_lst.pop(0)
			print(details_lst)

			camera_pos,camera_neg,camera_neu,battery_pos,battery_neg,battery_neu,performance_pos,performance_neg,performance_neu,storage_pos,storage_neg,storage_neu,budget_pos,budget_neg,budget_neu,name,price,img_url,rating,details=obj.camera_pos,obj.camera_neg,obj.camera_neu,obj.battery_pos,obj.battery_neg,obj.battery_neu,obj.performance_pos,obj.performance_neg,obj.performance_neu,obj.storage_pos,obj.storage_neg,obj.storage_neu,obj.budget_pos,obj.budget_neg,obj.budget_neu,obj.name,obj.price,obj.img_url,obj.rating,details_lst
			default.append(float(camera_pos))
			default.append(float(camera_neu))
			
			default.append(float(camera_neg))
			positive=str(int(float(camera_pos)))
			negative=str(int(float(camera_neg)))
			neutral=str(int(float(camera_neu)))

			pos_comment=obj.positive_comment.split('/')
			neg_comment=obj.negative_comment.split('/')



		else:
			details_lst=""
			pos_comment_lst=""
			neg_comment_lst=""
			positive=""
			negative=""
			neutral=""
			default=[]
			#pos_comment=[]
			#neg_comment=[]
			obj=productjson(x)
			print("fdsfdfdfds")
			camera_pos,camera_neg,camera_neu,battery_pos,battery_neg,battery_neu,performance_pos,performance_neg,performance_neu,storage_pos,storage_neg,storage_neu,budget_pos,budget_neg,budget_neu,name,price,img_url,rating,details,pos_comment,neg_comment=analyse()
			for i in details:
				details_lst=details_lst+" ; "+i
			for j in pos_comment:
				pos_comment_lst=pos_comment_lst+" / "+j
			for k in neg_comment:
				neg_comment_lst=neg_comment_lst+" / "+k

			Features.objects.create(
				camera_pos=camera_pos,
				camera_neg=camera_neg,
				camera_neu=camera_neu,
				battery_pos=battery_pos,
				battery_neg=battery_neg,
				battery_neu=battery_neu,
				performance_pos=performance_pos,
				performance_neg=performance_neg,
				performance_neu=performance_neu,
				storage_pos=storage_pos,
				storage_neg=storage_neg,
				storage_neu=storage_neu,
				budget_pos=budget_pos,
				budget_neg=budget_neg,
				budget_neu=budget_neu,
				url=x,
				name=name,
				price=price,
				img_url=img_url,
				rating=rating,
				details=details_lst,
				unique_id=finalst,
				positive_comment=pos_comment_lst,
				negative_comment=neg_comment_lst,
				)
			default.append(float(camera_pos))
			default.append(float(camera_neu))
			default.append(float(camera_neg))
			positive=str(int(float(camera_pos)))
			negative=str(int(float(camera_neg)))
			neutral=str(int(float(camera_neu)))
			#pos_comment=obj.positive_comment.split('/')
			#neg_comment=obj.negative_comment.split('/')
		print(default)
		labels=[0]
		labels1='Camera'
		#default1=[55 ,44]

		return render(request,'analyse/analyse2.html',{
			
			'name':name,
			'price':price,
			'img_url':img_url,
			'rating':rating,
			'details':details,
			'data_features':data_features,
			'default':default,
			'labels':labels,
			'finalst':finalst,
			'labels1':labels1,
			'positive':positive,
			'negative':negative,
			'neutral':neutral,
			'pos_comment':pos_comment,
			'neg_comment':neg_comment,


			}
			)
		
	else:
		obhome=Features.objects.all()

		return  render(request, 'analyse/analyse1.html',{'obhome':obhome})



def analyse_data1(self):
	if request.method=='POST':
		data_features=['camera','battery','performance','storage','budget']
		
		x=request.POST.get('url')
		in1=url.find('product-reviews')
		in2=url[:in1-1]
		flag=False
		objct=Features.objects.all()
		if objct:
			for i in objct:
				if i.url==x:
					flag=True



def charts_data(request):
	labels= ['positive','negative']
	default=[59,40]
	data={
	   'labels':labels,
	   'default':default,
	   'sales':100,
	   'customers':10,
	}
	return render(request,'analyse/res.html',{'customers':100,'sales':1000,'labels':labels,'default':default})

def aspects_view(request,finalst,spec):
	ob=Features.objects.all()
	ob1={}
	default=[]
	labels=[]
	details_lst=[]
	details=[]
	pos_comment=[]
	neg_comment=[]
	labels1=""
	positive=""
	negative=""
	neutral=""
	data_features=['camera','battery','performance','storage','budget']
	name,price,img_url,rating,st1_pos,st2_neg=" "," "," "," "," "," "


	for i in ob:
		if finalst in i.url:
			ob1=i

	if ob1:
		x=0
		for j in data_features:
			if j==spec:
				x=data_features.index(j)
		
		name=ob1.name
		price=ob1.price
		img_url=ob1.img_url
		rating=ob1.rating
		details_lst=ob1.details.split(';')
		details_lst.pop(0)

		pos_comment=ob1.positive_comment.split('/')
		neg_comment=ob1.negative_comment.split('/')
		
		if spec=='camera':
			st1_posnum=float(ob1.camera_pos)
			st2_neunum=float(ob1.camera_neu)
			st3_negnum=float(ob1.camera_neg)
			labels1='Camera'
		if spec=='battery':
			st1_posnum=float(ob1.battery_pos)
			st2_neunum=float(ob1.battery_neu)
			st3_negnum=float(ob1.battery_neg)
			labels1='Battery'
		if spec=='performance':
			st1_posnum=float(ob1.performance_pos)
			st2_neunum=float(ob1.performance_neu)
			st3_negnum=float(ob1.performance_neg)
			labels1='Performance'
		if spec=='storage':
			st1_posnum=float(ob1.storage_pos)
			st2_neunum=float(ob1.storage_neu)
			st3_negnum=float(ob1.storage_neg)
			labels1='Storage'
		if spec=='budget':
			st1_posnum=float(ob1.budget_pos)
			st2_neunum=float(ob1.budget_neu)
			st3_negnum=float(ob1.budget_neg)
			labels1='Budget'

		#st1_pos=spec+'_pos'
		#print(st1_pos)
		#st1_posnum=ob1.battery_pos
		#st2_neg=spec+'_neg'
		#st2_negnum=ob1.st2_neg
		default.append(st1_posnum)
		default.append(st2_neunum)
		default.append(st3_negnum)
		labels.append(x)
		positive=str(int(float(st1_posnum)))
		neutral=str(int(float(st2_neunum)))
		negative=str(int(float(st3_negnum)))

		#print(details_lst)




	return render(request,'analyse/res1.html',{
			'name':name,
			'price':price,
			'img_url':img_url,
			'rating':rating,
			'details':details_lst,
			'data_features':data_features,
			'default':default,
			'labels':labels,
			'finalst':finalst,
			'labels1':labels1,
			'positive':positive,
			'negative':negative,
			'neutral':neutral,
			'pos_comment':pos_comment,
			'neg_comment':neg_comment,
		})