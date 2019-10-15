import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    def get_list_queryset(self):
        request = self.request # NOQA
        qs = super().get_list_queryset() # NOQA
        if request.user.is_superuser: # NOQA
            return qs
        return qs.filter(owner=request.user) # NOQA

    def save_models(self,):
        if not self.org_obj: # NOQA
            self.new_obj.owner = self.request.user # NOQA
        return super().save_models() # NOQA


class GlobalSetting(CommAdminView):
    site_title = 'TypeIdea管理后台'
    site_footer = 'Powerby -- WCJ'

xadmin.site.register(CommAdminView, GlobalSetting)