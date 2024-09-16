from django.contrib import admin
from board.models import Racer, Team, Car, Race, Comment


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_country')
    list_display_links = ('team_name', 'team_country')


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'car_description')
    list_display_links = ('car_number', 'car_description')


class RacerAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'experience',
                    'grade_of_license',
                    'car',
                    'team')
    list_display_links = ('first_name',
                          'middle_name',
                          'last_name',
                          'experience',
                          'grade_of_license',
                          'car',
                          'team')


class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_name',
                    'series',
                    'year',
                    'winner')
    list_display_links = ('race_name',
                          'series',
                          'year',
                          'winner')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'tag')
    list_display_links = ('text', 'created', 'tag')


admin.site.register(Team, TeamAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Comment, CommentAdmin)
