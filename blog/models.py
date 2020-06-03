from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    comment = models.TextField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name

class Sets(models.Model):
    set_id = models.IntegerField(primary_key=True)
    set_topic = models.CharField(max_length=500)
    set_date = models.CharField(max_length=500)
    set_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    set_question1 = models.CharField(max_length=500)
    set_option1a = models.CharField(max_length=500)
    set_option1b = models.CharField(max_length=500)
    set_option1c = models.CharField(max_length=500)
    set_answer1 = models.CharField(max_length=500)
    set_img1 = models.CharField(max_length=500)

    set_question2 = models.CharField(max_length=500)
    set_option2a = models.CharField(max_length=500)
    set_option2b = models.CharField(max_length=500)
    set_option2c = models.CharField(max_length=500)
    set_answer2 = models.CharField(max_length=500)
    set_img2 = models.CharField(max_length=500)

    set_question3 = models.CharField(max_length=500)
    set_option3a = models.CharField(max_length=500)
    set_option3b = models.CharField(max_length=500)
    set_option3c = models.CharField(max_length=500)
    set_answer3 = models.CharField(max_length=500)
    set_img3 = models.CharField(max_length=500)

    set_question4 = models.CharField(max_length=500)
    set_option4a = models.CharField(max_length=500)
    set_option4b = models.CharField(max_length=500)
    set_option4c = models.CharField(max_length=500)
    set_answer4 = models.CharField(max_length=500)
    set_img4 = models.CharField(max_length=500)

    set_question5 = models.CharField(max_length=500)
    set_option5a = models.CharField(max_length=500)
    set_option5b = models.CharField(max_length=500)
    set_option5c = models.CharField(max_length=500)
    set_answer5 = models.CharField(max_length=500)
    set_img5 = models.CharField(max_length=500)

    def __str__(self):
        return self.set_topic

        
class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_text = models.TextField(blank=True, null=True)
    article_text2 = models.TextField(blank=True, null=True)
    article_title = models.CharField(max_length=500)
    article_logo = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    article_summary = models.CharField(max_length=50000)

    def __str__(self):
        return self.article_title
   
class Trending(models.Model):
    trending_id = models.IntegerField(primary_key=True)
    trending_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trending_title = models.CharField(max_length=500)
    trending_logo = models.CharField(max_length=500)
    trending_author = models.CharField(max_length=500)
    trending_date = models.CharField(max_length=500)
    trending_url = models.IntegerField()

    def __str__(self):
        return self.trending_title
    
class Editor(models.Model):
    editor_id = models.IntegerField(primary_key=True)
    editor_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    editor_summary = models.CharField(max_length=1000000)
    editor_title = models.CharField(max_length=500)
    editor_logo = models.CharField(max_length=500)
    editor_author = models.CharField(max_length=500)
    editor_date = models.CharField(max_length=500)
    editor_url = models.IntegerField()

    def __str__(self):
        return self.editor_title

class Hotnews(models.Model):
    hotnews_id = models.IntegerField(primary_key=True)
    hotnews_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hotnews_title = models.CharField(max_length=500)
    hotnews_logo = models.CharField(max_length=500)
    hotnews_author = models.CharField(max_length=500)
    hotnews_date = models.CharField(max_length=500)
    hotnews_url = models.IntegerField()

    def __str__(self):
        return self.hotnews_title

class Tech(models.Model):
    tech_id = models.IntegerField(primary_key=True)
    tech_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tech_title = models.CharField(max_length=500)
    tech_logo = models.CharField(max_length=500)
    tech_author = models.CharField(max_length=500)
    tech_date = models.CharField(max_length=500)
    tech_url = models.IntegerField()

    def __str__(self):
        return self.tech_title

class Suggested(models.Model):
    suggested_id = models.IntegerField(primary_key=True)
    suggested_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    suggested_title = models.CharField(max_length=500)
    suggested_logo = models.CharField(max_length=500)
    suggested_author = models.CharField(max_length=500)
    suggested_date = models.CharField(max_length=500)
    suggested_url = models.IntegerField()

    def __str__(self):
        return self.suggested_title    


class Catlist(models.Model):
    catlist_id = models.IntegerField(primary_key=True)
    catlist_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    catlist_summary = models.CharField(max_length=1000000)
    catlist_title = models.CharField(max_length=500)
    catlist_logo = models.CharField(max_length=500)
    catlist_author = models.CharField(max_length=500)
    catlist_date = models.CharField(max_length=500)
    catlist_url = models.IntegerField()

    def __str__(self):
        return self.catlist_title