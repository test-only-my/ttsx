# coding=utf-8
# 在匹配url之前记录上一次跳转来的页面url，为了在其他页面登录后再跳回原来页面
# get_full_path()获取到的带着原来的参数，path只会切割到/,?后面的参数会丢掉
# 然后去settings中注册'user.middle.Media'
class Media:
    def process_request(self,request):
        if request.path not in [
            '/user/register/',
            '/user/register_check/',
            '/user/login/',
            '/user/login_check/',
            '/user/logout/',
            '/cart/islogin/',
        ]:
            # print('--------url匹配之前--------')
            request.session['url_path'] = request.get_full_path()
