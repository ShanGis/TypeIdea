from django.test import TestCase
from django.db import connection
from django.db.models import Q, F, Count, Sum
from django.contrib.auth.models import User
from django.test.utils import override_settings

from .models import Category


class TestCategory(TestCase):
    @override_settings(DEBUG=True)    
    def setUp(self):
        user = User.objects.create_user('wcj', '583306676@qq.com', '1')
        # for i in range(10):
        #     category_name = "cate_{}".format(i)
        #     # category = Category.objects.create(name=category_name, owner=user)
        Category.objects.bulk_create(
            [Category(name="cate_{}".format(i), owner=user) for i in range(10)]
        )

    @override_settings(DEBUG=True)    
    def test_filter(self):
        # “字段__选择条件”查询语句用法示例
        # categories = Category.objects.filter(status__gt=0)
        # categories = Category.objects.filter(name__icontains="cate")

        # “对象__选择条件”连续下划线查询语句用法示例
        # current_user = Category.objects.filter(owner__username__startswith='w')

        # Q对象查询示例
        # q_lookup = Category.objects.filter(
        #     Q(id=1) | Q(id=2)
        # )
        # print(q_lookup)

        # F对象查询实例
        # f_lookup = Category.objects.filter(id=1).update(status = F('status') + 1)

        # QuerySet对象懒加载对应的SQL语句查询示例
        # print("-----查看当前QuerySet将要执行的SQL语句-----")
        # print(f_lookup.query)
        # print("---------------------------- -")

        # 单条语句查询实例
        # categories = categories.get(name="cate_1")

        # Count语句及Annotate语句用法示例

        ''' 一种普通实现逻辑'''
        # users = User.objects.filter(username='wcj')
        # user = users[0]
        # print(user.category_set.count())

        '''基于Count和Annotate的实现'''
        # users_cate_count = User.objects.filter(username='wcj').annotate(cate_count=Count('category'))
        # user_cate_count = users_cate_count[0]
        # print(user_cate_count.cate_count)

        '''Sum查询语句的用法示例'''
        wcj_status_sums = User.objects.annotate(status_sum=Sum('category__status')).get(username='wcj')
        print(wcj_status_sums.status_sum)

        # 查看一次数据库连接执行的所有SQL语句示例
        print("-----查看已经执行的SQL语句-----")
        print(connection.queries)
        print("---------------------------- -")

    def test_value(self):
        '''values和values_list用法示例'''
        categories = Category.objects.values('id',"name")
        print(categories)
        for n in categories:
            print(n['name'])
            print(n['id'])


        print('----' * 20)
        categories1 = Category.objects.values_list('id', 'name')
        print(categories1)
        for n in categories1:
            print(n[0])
            print(n[1])
