from django.shortcuts import render
from django import template
from models import Menu
# Create your views here.

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu = Menu.objects.filter(title=menu_name).first()
    if not menu:
        return ''
    def build_menu(menu_item):
        children = menu_item.children.all()
        is_active = menu_item.url == current_url
        return {
            'title': menu_item.title,
            'url': menu_item.url,
            'is_active': is_active,
            'children': [build_menu(child) for child in children],
            'is_expanded': is_active or any(build_menu(child)['is_active'] for child in children),
        }
    menu_data = build_menu(menu)
    return render(context, 'menu.html', {'menu': menu_data})
