from django import template
import re

register = template.Library()

@register.filter
def go_to(value):
    content = value.content
    tags = value.hashtags.all()

    for tag in tags:
        content = re.sub(r'\#' + tag.content + r'\b', '<a href="/movies/' + str(tag.pk) + '/hashtag/">#' + tag.content + '</a>', content)
    return content