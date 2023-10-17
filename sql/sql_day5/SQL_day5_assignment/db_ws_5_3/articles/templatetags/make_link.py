from django import template
import re

register = template.Library()

@register.filter
def go_to(value):
    content = value.content
    tags = value.hashtag_set.all()

    for tag in tags:
        content = re.sub(r'\#' + tag.content + r'\b', '<a href="/articles/' + str(tag.pk) + '/hashtag/">#' + tag.content + '</a>', content)
    return content