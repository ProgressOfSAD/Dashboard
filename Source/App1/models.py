from django.db import models

# user's basic information
class UserInfo(models.Model):
    # user's id, setting by system
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 16)
    # stored by md5
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 64)
    # true for male, false for female
    gender = models.NullBooleanField(null = True)
    # user's phone number, default = ''
    phone = models.CharField(max_length = 20)
    # the user is authentication or not
    auth = models.BinaryField(default = False)
    auth_info = models.CharField(max_length = 255)
    real_name = models.CharField(max_length = 20)
    # other information, such as introduction
    other = models.TextField()

# user's other information for interaction
class UserExtended(models.Model):
    # the same as UserInfo.user_id
    # user_id = models.IntegerField()
    user_id = models.OneToOneField("UserInfo", on_delete=models.CASCADE)
    # the book of user's collection, store the book_id
    collection = models.TextField()
    # reservation = models.TextField()
    # borrowed = models.TextField()
    # returned = models.TextField()
    # user's credit for borrowing book, range [0, 5]
    borrow_credit = models.IntegerField(default = 5)
    # user's credit for comment, range [0, 5]
    comment_credit = models.IntegerField(default = 5)
    # user's credit to report others's comment
    report_credit = models.IntegerField(default = 5)

# manager's information
class ManagerInfo(models.Model):
    # manager's id, setting by system
    manager_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    # stored by md5
    password = models.CharField(max_length = 32)
    gender = models.NullBooleanField()
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    other = models.TextField()

# book's information
class BookInfo(models.Model):
    book_id = models.AutoField(primary_key = True)
    ISBN = models.CharField(max_length = 16)
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    # the brief introduction to the book
    brief = models.TextField()
    publish_time = models.CharField(max_length = 20)
    press = models.CharField(max_length = 32)
    type = models.CharField(max_length = 32)

# book's state information
class BookExtended(models.Model):
    # the same as BookInfo/book_id
    book_id = models.OneToOneField("BookInfo", on_delete=models.CASCADE)
    # book_id = models.IntegerField()
    # the score of the book. Store the user's number given the score
    # socre's range[1, 5]
    score1 = models.IntegerField(default = 0)
    score2 = models.IntegerField(default = 0)
    score3 = models.IntegerField(default = 0)
    score4 = models.IntegerField(default = 0)
    score5 = models.IntegerField(default = 0)
    browsing_times = models.IntegerField(default = 0)
    # the state of the book
    # such as: borrowed(2), reserved(1), normal(0)
    state = models.IntegerField(default = 0)
    # stock = models.IntegerField(default = 1)

class User_Book(models.Model):
    # the same as User_Info.user_id
    user_id = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    book_id = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    time = models.CharField(max_length = 12)
    # the state can be do nothing(0), order(1), bollow(2), return(3)
    state = models.IntegerField(default = 0)

# the book's type list
class TypeList(models.Model):
    type_id = models.IntegerField(default = 0)
    type_name = models.CharField(max_length = 20)

class Comment(models.Model):
    comment_id = models.CharField(max_length = 64, primary_key = True)
    # the same as UserInfo.user_id
    user_id = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    # the same as BookInfo.book_id
    book_id = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    reported_times = models.IntegerField(default = 0)
    comment_time = models.CharField(max_length = 20)
    content = models.TextField()
    agree = models.IntegerField(default = 0)
    disagree = models.IntegerField(default = 0)

class ScoreToBook(models.Model):
    # user id
    user_id = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    book_id = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    class Meta:
        unique_together=("user_id","book_id")
    # the score given to the book by uesr
    score = models.IntegerField(default = 5)

class AgreeDisagree(models.Model):
    # comment_id = models.CharField(max_length = 64)
    comment_id = models.ForeignKey("Comment", on_delete=models.CASCADE)
    # user
    user_id = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    # True is agree, False is disagree
    agree_disagree = models.NullBooleanField(null = True)
    # the reason for reporting the comment
    reported = models.CharField(max_length = 255, default = "")
