from social.models import SocialNetwork


def is_author(obj, user_id: int):
    return True if obj.user.id == user_id else False


def get_social_network_by_filter(**kwargs):
    return SocialNetwork.objects.filter(**kwargs)

# Создал utils 