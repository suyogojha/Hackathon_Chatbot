from django.db import models
from django.conf import settings
from django.db.models.base import Model

# Create your models here.
class publicchatRoom(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="user who are connected to chat")

    def __str__(self):
        return self.title
    
    
    def connect_user(self, user):
        is_user_added = False
        if not  user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_added = True
        elif user in self.users.all():
            is_user_added = True
        return is_user_added
    
    def disconnect_user(self, user):
        is_user_removed = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_user_removed = True
        return is_user_removed
    
    
@property
def group_name(self):
    return f"PublicChatRoom-{self.id}"


class publicroomchatmessageManager(models.Manager):
    def by_room(self, room):
        qs = publicroomchatmessage.objects.filter(room=room).order_by("-timestamp")
        return qs
    

class publicroomchatmessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(publicchatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)
    
    
    objects = publicroomchatmessageManager()
    
    
    def __str__(self):
     return self.content