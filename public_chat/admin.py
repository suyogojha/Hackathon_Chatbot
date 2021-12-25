from django.contrib import admin
from django.core import paginator
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import models



from public_chat.models import publicchatRoom, publicroomchatmessage
# Register your models here.



class publicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', ['title']]
    search_fields = ['id', 'title']
    list_display = ['id',]


    class Meta:
        model = publicchatRoom


admin.site.register(publicchatRoom, publicChatRoomAdmin)

class CachingPaginator(Paginator):
    def _get_count(self):
        
        
        if not hasattr(self, "_count"):
            self._count = None
            
        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self.__count = cache.get(key, -1)
                if self._count == -1:
                    self.__count = super().count
                    cache.set(key, self.__count, 3600)
            except:
                self.__count = len(self.object_list)
        return self.__count
    
    count = property(_get_count)
    
    
    
class publicroomchatMessageAdmin(admin.ModelAdmin):
    list_filter = ['room', 'user', 'timestamp']
    list_display = ['room', 'user', 'timestamp', 'content']
    search_fields = ['room_title', 'user_username', 'content']
    readonly_fields = ['id', 'user', 'room', 'timestamp']
    
    show_full_result_count = False
    paginator = CachingPaginator
    
    class Meta:
        model = publicroomchatmessage
        
        
admin.site.register(publicroomchatmessage, publicroomchatMessageAdmin)