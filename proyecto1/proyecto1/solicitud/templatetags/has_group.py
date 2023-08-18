from django import template

register = template.Library()

@register.filter(name='has_groups')
def has_groups(user, group_list):
    list = [word.strip() for word in group_list.split(',')]
    return user.groups.filter(name__in= list).exists()


