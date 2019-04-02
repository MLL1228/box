from django.db import models
# Create your models here.


# 用户权限表，存储 用户名、首次登录、上次登录、 用户权限 以及 是否激活状态
class User(models.Model):
    Username = models.CharField(max_length=50)  # 用户名
    firstLoginTime = models.BigIntegerField()  # 首次登录时间戳
    lastLoginTime = models.BigIntegerField()  # 上次登录时间戳
    privilege = models.SmallIntegerField(default=0)  # 0: 普通 1：编辑 2：管理
    isActive = models.BooleanField(default=True)  # 默认为激活

    # 返回用户的 username
    def __str__(self):
        return self.username


# 改进计划表
class Plan(models.Model):
    content = models.TextField()  # 计划内容
    owner = models.CharField(max_length=50)  # owner
    reviewer = models.CharField(max_length=50)  # reviewer
    expectFinishTime = models.BigIntegerField()  # 预期完成时间
    actualFinishTime = models.BigIntegerField()  # 实际完成时间
    createTime = models.BigIntegerField()  # 创建时间
    lastModifyTime = models.BigIntegerField()  # 最后修改时间
    createUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='plan_createUser')  # 创建者
    lastModifyUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='plan_modifyUser')  # 最后修改人
    finishStatus = models.BooleanField(default=False)  # 完成状态, 默认未完成
    isActive = models.BooleanField(default=True)  # 计划有效状态，默认有效

    def __str__(self):
        return self.content[:50]


# 问题表
class Problem(models.Model):
    title = models.CharField(max_length=200)  # 问题点
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)  # 关联计划
    creatUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='prob_createUser')  # 创建人
    creatTime = models.BigIntegerField()  # 创建时间
    lastModifyUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='prob_modifyUser')  # 最后修改人
    lastModifyTime = models.BigIntegerField()  # 最后修改时间
    isActive = models.BooleanField(default=True)  # 默认存在

    def __str__(self):
        return self.title


# bug定级表
class BugLevel(models.Model):
    priority = models.CharField(max_length=20, unique=True)  # bug 级别 ，唯一
    description = models.CharField(max_length=50, unique=True)  # bug 描述， 唯一
    isActive = models.BooleanField(default=True)  # 决定是否展示

    def __str__(self):
        return self.description


# 故障原因/故障类型
class BugReason(models.Model):
    reason = models.CharField(max_length=50, unique=True)  # bug 产生原因
    isActive = models.BooleanField(default=True)  # 决定是否展示

    def __str__(self):
        return self.reason


# 故障来源
class BugSource(models.Model):
    source = models.CharField(max_length=50, unique=True)  # bug来源
    isActive = models.BooleanField(default=True)  # 决定是否展示

    def __str__(self):
        return self.source


# 业务线
class Line(models.Model):
    lineName = models.CharField(max_length=50, unique=True)  # 业务线，唯一
    owner = models.CharField(max_length=50)  # 业务线负责人
    isActive = models.BooleanField(default=True)  # 默认为 true

    def __str__(self):
        return self.lineName


# 平台
class Platform(models.Model):
    platformName = models.CharField(max_length=50, unique=True)  # 平台名称
    owner = models.CharField(max_length=50)  # platform负责人
    isActive = models.BooleanField(default=True)  # 默认为 True

    def __str__(self):
        return self.platformName


# 通知人p
class NotiPeople(models.Model):
    username = models.CharField(max_length=50, unique=True)  # 通知人，唯一
    isActive = models.BooleanField(default=True)  # 有效的通知人

    def __str__(self):
        return self.username


# BugInfo
class BugInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    startTime = models.BigIntegerField()
    endTime = models.BigIntegerField()
    influenceRange = models.BigIntegerField()
    influenceType = models.SmallIntegerField()  # 0: 用户数 ， 1： 请求数
    moreReason = models.TextField()
    process = models.TextField()
    owner = models.CharField(max_length=50)
    notifyType = models.SmallIntegerField()  # 0: 微信 1：邮件
    isNotify = models.BooleanField(default=False)  # 0:未通知  1： 已通知
    createTime = models.BigIntegerField()
    lastModifyTime = models.BigIntegerField()
    createPeople = models.CharField(max_length=50)
    lastModifyPeople = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)

    priority = models.ForeignKey(BugLevel, on_delete=models.PROTECT)
    lineName = models.ManyToManyField(Line, through="Bug2LineName")
    platformName = models.ManyToManyField(Platform, through="Bug2Platform")
    reason = models.ForeignKey(BugReason, on_delete=models.PROTECT)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    bugSource = models.ForeignKey(BugSource, on_delete=models.PROTECT)
    notifyPeople = models.ManyToManyField(NotiPeople, through="Bug2NotiPeople")

    def __str__(self):
        return self.title


# Bug2LineName
class Bug2LineName(models.Model):
    bugID = models.ForeignKey(BugInfo, on_delete=models.PROTECT)
    lineNameID = models.ForeignKey(Line, on_delete=models.PROTECT)
    isActive = models.BooleanField(default=True)


# Bug2Platform
class Bug2Platform(models.Model):
    bugID = models.ForeignKey(BugInfo, on_delete=models.PROTECT)
    lineNameID = models.ForeignKey(Platform, on_delete=models.PROTECT)
    isActive = models.BooleanField(default=True)


# Bug2NotiPeople
class Bug2NotiPeople(models.Model):
    bugID = models.ForeignKey(BugInfo, on_delete=models.PROTECT)
    notipeople = models.ForeignKey(NotiPeople, on_delete=models.PROTECT)
    isActive = models.BooleanField(default=True)














