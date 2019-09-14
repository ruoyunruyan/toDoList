from django.db import models


class ThingsModel(models.Model):

    THING_STATUS = (
        (1, '已完成'),
        (2, '未完成')
    )
    content = models.CharField(max_length=32, verbose_name='待办事项')
    status = models.SmallIntegerField(choices=THING_STATUS, default=2, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'things'
        verbose_name = '待办清单'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']

    def __str__(self):
        return self.content
