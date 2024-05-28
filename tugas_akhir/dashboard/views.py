from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
def show_kelahiran(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tugas_akhir']
    collection = db['kelahiran']
    
    data = collection.find()
    
    return render(request, 'kelahiran.html', {'data': data})

def show_kematian(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tugas_akhir']
    collection = db['kematian']
    
    data = collection.find()
    
    return render(request, 'kematian.html', {'data': data})

def show_kedatangan(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tugas_akhir']
    collection = db['kedatangan']
    
    data = collection.find()
    
    return render(request, 'kedatangan.html', {'data': data})

def show_kepindahan(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tugas_akhir']
    collection = db['kepindahan']
    
    data = collection.find()
    
    return render(request, 'kepindahan.html', {'data': data})

def index(request):
    return render(request, 'index.html')