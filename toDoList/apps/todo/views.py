from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http

from . models import ThingsModel


class IndexView(View):
    """首页显示"""
    def get(self, request):
        things = ThingsModel.objects.order_by('-create_time').filter(is_delete=False)
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
                return http.JsonResponse({'error': 'thing save fail'})
            return redirect(reverse('home'))
        return {'error': 'no content'}


class AboutView(View):
    """关于本站"""
    def get(self, request):
        return render(request, 'about.html')


class EditView(View):
    """待办事项编辑"""
    def get(self, request, id):
        """获取编辑页面"""
        try:
            thing = ThingsModel.objects.get(id=id)
        except:
            return http.JsonResponse({'error': 'no thing select'})
        content = thing.content
        return render(request, 'edit.html', {'content': content})

    def post(self, request, id):
        """编辑待办事项 应该用put请求 不搞前端了"""
        content = request.POST.get('content')
        if content:
            try:
                ThingsModel.objects.filter(id=id).update(content=content)
            except:
                return http.JsonResponse({'error': 'thing not exists'})
            return redirect(reverse('home'))
        return http.JsonResponse({'error': 'no content'})

    def delete(self, request, id):
        """删除待办事项"""
        try:
            ThingsModel.objects.filter(id=id).update(is_delete=True)
        except:
            return http.JsonResponse({'code': 0})
        return http.JsonResponse({'code': 1})


class LineThrough(View):
    """划掉  撤销"""
    def get(self, request, id):
        try:
            thing = ThingsModel.objects.get(id=id)
        except:
            return http.JsonResponse({'error': 'thing not exists'})
        # 获取当前的状态
        status = thing.status
        # 取相反的状态
        thing.status = 2 if status == 1 else 1
        # 保存
        thing.save()
        return redirect(reverse('home'))
