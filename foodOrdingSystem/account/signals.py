from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import Profile
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except:
            Profile.objects.create(user=instance)


