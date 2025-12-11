from django.contrib import admin
from .models import AdminUser
from artist.models import Artist, Song, SongPurchase
from django.contrib.auth.admin import UserAdmin

# AdminUser
@admin.register(AdminUser)
class CustomAdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_admin')
    list_filter = ('is_staff', 'is_superuser', 'is_admin')

# Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'user', 'created_at')

# Song
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'upload_date', 'play_count', 'purchase_count')

# SongPurchase
@admin.register(SongPurchase)
class SongPurchaseAdmin(admin.ModelAdmin):
    list_display = ('song', 'buyer', 'price_paid', 'purchase_date')

