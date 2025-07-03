from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Parca, Fotograf, Firma
from .forms import ParcaForm

def is_admin(user):
    return user.is_staff

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('parca_listesi')
    else:
        form = UserCreationForm()
    return render(request, 'envanter/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST': # Hata düzeltildi: tırnak işareti eklendi
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('parca_listesi')
    else:
        form = AuthenticationForm()
    return render(request, 'envanter/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('parca_listesi')

@login_required
def parca_listesi(request):
    parcalar = Parca.objects.all()
    firmalar = Firma.objects.all()

    firma_id = request.GET.get('firma')
    if firma_id:
        parcalar = parcalar.filter(firma__id=firma_id)

    parcalar = parcalar.order_by('-eklenme_tarihi')
    
    context = {
        'parcalar': parcalar,
        'firmalar': firmalar
    }
    return render(request, 'envanter/parca_listesi.html', context)

@login_required
def parca_ekle(request):
    firmalar = Firma.objects.all()
    if request.method == 'POST':
        form = ParcaForm(request.POST)
        # Fotoğraf yüklenip yüklenmediğini kontrol et
        if not request.FILES.getlist('images'):
            return render(request, 'envanter/parca_ekle.html', {
                'form': form,
                'error': 'En az bir fotoğraf yüklemelisiniz.',
                'firmalar': firmalar
            })

        if form.is_valid():
            firma_adi = form.cleaned_data.get('firma_adi')
            firma, created = Firma.objects.get_or_create(ad=firma_adi)

            parca = form.save(commit=False) # Parçayı henüz kaydetme
            parca.ekleyen_kullanici = request.user # Mevcut kullanıcıyı ata
            parca.firma = firma # Firma objesini ata
            parca.save() # Şimdi kaydet
            for f in request.FILES.getlist('images'):
                Fotograf.objects.create(parca=parca, resim=f)
            return redirect('parca_listesi')
    else:
        form = ParcaForm()
    return render(request, 'envanter/parca_ekle.html', {'form': form, 'firmalar': firmalar})

@login_required
@user_passes_test(is_admin)
def parca_duzenle(request, pk):
    parca = get_object_or_404(Parca, pk=pk)
    firmalar = Firma.objects.all()
    if request.method == 'POST':
        form = ParcaForm(request.POST, instance=parca)
        if form.is_valid():
            firma_adi = form.cleaned_data.get('firma_adi')
            firma, created = Firma.objects.get_or_create(ad=firma_adi)

            parca = form.save(commit=False)
            parca.firma = firma
            parca.save()
            for f in request.FILES.getlist('images'):
                Fotograf.objects.create(parca=parca, resim=f)
            return redirect('parca_listesi')
    else:
        form = ParcaForm(instance=parca, initial={'firma_adi': parca.firma.ad})
    return render(request, 'envanter/parca_duzenle.html', {'form': form, 'parca': parca, 'firmalar': firmalar})

@login_required
@user_passes_test(is_admin)
def parca_sil(request, pk):
    parca = get_object_or_404(Parca, pk=pk)
    if request.method == 'POST':
        parca.delete()
        return redirect('parca_listesi')
    return redirect('parca_listesi') # GET isteğiyle gelirse listeye yönlendir

@login_required
@user_passes_test(is_admin)
def fotograf_sil(request, pk):
    fotograf = get_object_or_404(Fotograf, pk=pk)
    if request.method == 'POST':
        fotograf.delete()
    return redirect('parca_duzenle', pk=fotograf.parca.pk)