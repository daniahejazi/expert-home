from django.contrib import admin


from .models import Expert, Cerificate, Vocation


# admin.site.register(Expert)
# admin.site.register(Cerificate)

class CerificateInline(admin.TabularInline):
    model = Cerificate
    extra = 1
    


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('created_at','name', 'general_specialization', "sum_experience_years")
    search_fields = ('name', 'general_specialization')
    list_filter = ('general_specialization', 'sum_experience_years')
    list_per_page = 2
    ordering = ('-created_at',)
    
    inlines = [CerificateInline]


admin.site.register(Vocation)