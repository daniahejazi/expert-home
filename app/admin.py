from django.contrib import admin


from .models import Expert, Cerificate, Vocation


# admin.site.register(Expert)
# admin.site.register(Cerificate)

class CerificateInline(admin.TabularInline):
    model = Cerificate
    extra = 1
    


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)
    list_per_page = 2
    ordering = ('-yearsExperiance',)
    
    inlines = [CerificateInline]


admin.site.register(Vocation)