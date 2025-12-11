from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from .models import UserProfile, Notification
from django.urls import reverse

# local import to check artist relation
try:
    from artist.models import Artist
except Exception:
    Artist = None

@login_required
def home_view(request):
    user = request.user
    
    # KITA KIRIM CONFIG USER KE TEMPLATE
    # Ini menjawab pertanyaanmu: "Bagaimana sistem tahu ada jeda?"
    # Jawabannya: Kita kirim variabel 'ad_wait_time' ini.
    
    context = {
        'user': user,
        'ad_wait_time': user.get_wait_time(),         # Angka: 15 atau 0
        'audio_quality': user.subscription.audio_quality_label(), # Text: Standard/High
        'allow_download': user.is_download_allowed(), # Boolean: True/False
    }
    
    # Context ini nanti dipakai di HTML (user_app/home.html)
    # Contoh HTML: 
    # <script> var delay = {{ ad_wait_time }}; </script>
    
    return render(request, 'user_app/home.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat. Silakan login.')
            return redirect('user:login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Respect explicit next param (could be a path or a named view)
            next_param = request.GET.get('next') or request.POST.get('next')
            if next_param:
                # try reversing if it's a view name, otherwise treat as path
                try:
                    return redirect(reverse(next_param))
                except Exception:
                    return redirect(next_param)

            # No explicit next: if user is an Artist, send to artist dashboard
            try:
                if Artist and Artist.objects.filter(user=user).exists():
                    return redirect('artists:dashboard')
            except Exception:
                # fall back silently if artist app unavailable
                pass

            return redirect('user:home')
    else:
        form = UserLoginForm()
    return render(request, 'user_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')


@login_required
def profile_view(request):
    try:
        profile = request.user.profile_obj
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil diperbarui.')
            return redirect('user:profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user_app/profile.html', {'form': form, 'profile': profile})


@login_required
def notifications_view(request):
    notes = Notification.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'user_app/notifications.html', {'notifications': notes})


@login_required
def upgrade_subscription_view(request):
    # placeholder: real upgrade should interact with finance/payment flow
    messages.info(request, 'Fitur upgrade belum diimplementasikan di demo ini.')
    return redirect('user:profile')