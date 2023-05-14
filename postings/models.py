from django.db import models
from users.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Postings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목",max_length=100)
    content = models.TextField("내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        "게시글 썸네일",
        upload_to='postings/statics/',
        blank=True,
        default='postings/statics/default.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        )
    likes = models.ManyToManyField(User, related_name="like_articles")
    url = models.URLField("URL", blank=True, null=True)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    # 댓글 작성자 = 유저모델 FK로 받아오기
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # # 게시글에 댓글을 작성함으로 게시글도 FK로 받아오기
    posting = models.ForeignKey(Postings, on_delete=models.CASCADE)
    # 댓글 TextField
    comment = models.TextField("댓글")   # verbosename="댓글"=> admin에서 댓글로 표시됨
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
