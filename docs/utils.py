from django.utils.text import slugify


def unique_slug_generator(instance, field_name="name", new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(getattr(instance, field_name), allow_unicode=True)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{id}".format(
            slug=slug,
            id=instance.id
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
