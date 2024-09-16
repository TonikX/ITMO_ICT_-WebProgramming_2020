from django.contrib import admin
from newspapersapp.models import Editor, Newspaper, PostOffice, PrintingHouse, InStock


class EditorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name')
    list_display_links = ('first_name', 'middle_name', 'last_name')


class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'edition_index',
                    'editor',
                    'price')
    list_display_links = ('name',
                          'edition_index',
                          'editor',
                          'price')


class PostOfficeAdmin(admin.ModelAdmin):
    list_display = ('number', 'address')
    list_display_links = ('number', 'address')


class PrintingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'status')
    list_display_links = ('name', 'address', 'status')


class InStockAdmin(admin.ModelAdmin):
    list_display = ('newspaper',
    	            'post_office',
    	            'printing_house',
    	            'print_run')
    list_display_links = ('newspaper',
    	                  'post_office',
    	                  'printing_house',
    	                  'print_run')


admin.site.register(Editor, EditorAdmin)
admin.site.register(Newspaper, NewspaperAdmin)
admin.site.register(PostOffice, PostOfficeAdmin)
admin.site.register(PrintingHouse, PrintingHouseAdmin)
admin.site.register(InStock, InStockAdmin)
