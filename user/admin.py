from django.contrib import admin
from .models import (
    UserProfile, 
    UserPreferences, 
    FreeSubscription, 
    PremiumSubscription, 
    Notification
)

# 1. Admin untuk Profil User
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'bio')
    search_fields = ('user__username', 'display_name')

# 2. Admin untuk Preferensi
@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'audio_quality')

# 3. Admin untuk Subscription (Free)
@admin.register(FreeSubscription)
class FreeSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'start_date')
    list_filter = ('status',)

# 4. Admin untuk Subscription (Premium)
@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'next_billing_date')
    list_filter = ('status',)

# 5. Admin untuk Notifikasi
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'timestamp')
    list_filter = ('is_read',)
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Tandai sebagai sudah dibaca"