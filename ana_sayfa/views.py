from django.shortcuts import render
from .models import TeknoProje

def anasayfa(request):
    # Veritabanındaki tüm "Büşra'nın Web Projeleri" kayıtlarını alıyoruz
    projelerim = TeknoProje.objects.all()
    # 'projeler' değişkeni ile bu veriyi HTML'e gönderiyoruz
    return render(request, "anasayfa.html", {'projeler': projelerim})