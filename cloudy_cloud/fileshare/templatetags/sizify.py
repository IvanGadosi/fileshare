from django import template

register = template.Library()
def sizify(value):
    if value < 512000:
        value = value / 1024.0
        ext = 'kb'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'mb'
    else:
        value = value / 1073741824.0
        ext = 'gb'
    return '{} {}'.format(round(value, 2), ext)

register.filter('sizify', sizify)