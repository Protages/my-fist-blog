from django import template

from blog.models import Category


register = template.Library()


@register.inclusion_tag('blog/list_categories_tag.html')
def list_blog_categories(cat_selected=None):
    categories = Category.objects.all()
    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag('blog/search_form_tag.html')
def search_form(query):
    categories = Category.objects.all()
    return {'categories': categories, 'query': query}