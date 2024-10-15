from django import template

register = template.Library()


@register.simple_tag
def center_def(value):
    if value:
        return "translate-middle-x text-center"
    else:
        return ''


@register.simple_tag
def ie_special(value, center):
    if center:
        return str(float(value) - 1.8)
    else:
        return value


@register.simple_tag
def display_sensor_info(value, unit, code):
    return f'{value} {unit}'



@register.simple_tag
def image_url_converter(image_url):
    img2 = image_url.replace('.png', '_ie.png')
    print('123', image_url)
    return img2
