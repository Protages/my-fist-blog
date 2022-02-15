from django import template

from blog.models import Category, Comment


register = template.Library()
categories = Category.objects.all()


@register.inclusion_tag('blog/list_categories_tag.html')
def list_blog_categories(cat_selected=None):
    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag('blog/search_form_tag.html')
def search_form(query):
    return {'categories': categories, 'query': query}


# @register.simple_tag
# def get_subcomments(comment):
#     return comment.comments.all().select_related('author')