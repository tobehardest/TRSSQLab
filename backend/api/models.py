from django.db import models

# 定义抽象基类
class TrajectoryBase(models.Model):
    trajectory = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'api'

# 数据集表
class ChengduData(TrajectoryBase):
    pass

class PortoData(TrajectoryBase):
    pass

class XianData(TrajectoryBase):
    pass

# 查询集表
class ChengduQuery(TrajectoryBase):
    pass

class PortoQuery(TrajectoryBase):
    pass

class XianQuery(TrajectoryBase):
    pass

# 定义结果集的抽象基类
class ResultBase(models.Model):
    start = models.IntegerField(max_length=100)
    end = models.IntegerField(max_length=100)
    score = models.FloatField(db_index=True,max_length=100)

    class Meta:
        abstract = True

# 结果集表 - 需要设置外键
class ChengduResultsDTW(ResultBase):
    queryid = models.ForeignKey(ChengduQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qdwt")
    dataid = models.ForeignKey(ChengduData, on_delete=models.CASCADE, null=True, blank=True,related_name="ddwt")

class PortoResultsDTW(ResultBase):
    queryid = models.ForeignKey(PortoQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qdwt")
    dataid = models.ForeignKey(PortoData, on_delete=models.CASCADE, null=True, blank=True,related_name="ddwt")

class XianResultsDTW(ResultBase):
    queryid = models.ForeignKey(XianQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qdwt")
    dataid = models.ForeignKey(XianData, on_delete=models.CASCADE, null=True, blank=True,related_name="ddwt")


class ChengduResultsEDR(ResultBase):
    queryid = models.ForeignKey(ChengduQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qedr")
    dataid = models.ForeignKey(ChengduData, on_delete=models.CASCADE, null=True, blank=True,related_name="dedr")

class PortoResultsEDR(ResultBase):
    queryid = models.ForeignKey(PortoQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qedr")
    dataid = models.ForeignKey(PortoData, on_delete=models.CASCADE, null=True, blank=True,related_name="dedr")

class XianResultsEDR(ResultBase):
    queryid = models.ForeignKey(XianQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qedr")
    dataid = models.ForeignKey(XianData, on_delete=models.CASCADE, null=True, blank=True,related_name="dedr")
class ChengduResultsERP(ResultBase):
    queryid = models.ForeignKey(ChengduQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qerp")
    dataid = models.ForeignKey(ChengduData, on_delete=models.CASCADE, null=True, blank=True,related_name="derp")

class PortoResultsERP(ResultBase):
    queryid = models.ForeignKey(PortoQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qerp")
    dataid = models.ForeignKey(PortoData, on_delete=models.CASCADE, null=True, blank=True,related_name="derp")

class XianResultsERP(ResultBase):
    queryid = models.ForeignKey(XianQuery, on_delete=models.CASCADE, null=True, blank=True,related_name="qerp")
    dataid = models.ForeignKey(XianData, on_delete=models.CASCADE, null=True, blank=True,related_name="derp")