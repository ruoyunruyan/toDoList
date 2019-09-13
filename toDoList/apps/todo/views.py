from django.shortcuts import render
from django.views import View
from django import http

from . models import ThingsModel


class IndexView(View):
    """首页显示"""
    def get(self, request):
        things = ThingsModel.objects.order_by('-update_time').filter(is_delete=False)
        return render(request, 'index.html', {'things': things})

    def post(self, request):
        """创建待办事项"""
        thing = request.POST.get('thing')
        # 判断是否为空
        if thing:
            # 保存数据
            try:
                ThingsModel.objects.create(content=thing)
            except:
                return {'msg': '保存失败'}
            return http.HttpResponse(b'hello world')
        return {'mag': '未输入'}


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class EditView(View):

    def get(self, request):
        return render(request, 'edit.html')

    def post(self, request, id):
        return {'mas': 'ok'}

    def delete(self, request, id):
        ThingsModel.objects.filter(id=id).update(is_delete=True)
        return http.JsonResponse({'msg': 'delete success'})
