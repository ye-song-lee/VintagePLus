from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    
    ROLE_CHOICES = (
        ('S','seller'),
        ('M','manager'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='seller', verbose_name='역할')

    
    #score = models.IntegerField(default=0)
    level = models.IntegerField(default=1) #레벨
    point = models.IntegerField(default=0) #포인트
    #sell = models.IntegerField(default=0) #판매완료+판매중
    end = models.IntegerField(default=0) #판매완료
    ing = models.IntegerField(default=0) #판매중
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

class Items(models.Model):
    name = models.CharField(max_length=64) #상품명
    minprice = models.IntegerField() #최소가격
    description = models.TextField() #상품설명
    img = models.ImageField(upload_to='items',null=True)

    class Meta:
        db_table = 'items'
        verbose_name = '상품'
        verbose_name_plural = '상품'
