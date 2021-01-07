from django.db import models

# Create your models here.
# ORM 操作数据库表的
# select * from table_name
# table_name.objects.all()

# class = table user_app_project

# 变量 = 字段(类型,长度) id  creat_time
# class Project(models.Model):
#     """
#     项目表
#     """
#     name = models.CharField("名称",max_length=50,default="",blank=False,null=True)
#     describe = models.TextField("描述",default="")
#     status = models.BooleanField("状态", default=True)
#     create_time = models.DateTimeField("创建时间", auto_now=True)
#
#     def __str__(self):
#         return self.name
#
# class Module(models.Model):
#     """
#     模块表
#     """
#     Project = models.ForeignKey(Project,on_delete=models.CASCADE)  #on_delete=models.CASCADE 级联删除
#     name = models.CharField("名称",max_length=50,default="",blank=False,null=True)
#     describe = models.TextField("描述", default="")
#     create_time = models.DateTimeField("创建时间", auto_now=True)
#
#     def __str__(self):
#         return self.name