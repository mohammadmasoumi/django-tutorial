from django.db import models
from store.utils import id_generator


__all__ = ('Product', 'Collection', 'Promotion')


class Promotion(models.Model):
    descrition = models.TextField()
    discount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.descrition}-{self.discount}"

    __repr__ = __str__


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # circular dependency
    # '+' do no create reverse relation in product
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    __repr__ = __str__


"""
Product   Collection
1           1
many        1
many        1

ManyToOne

product_1 collection_1
product_2 collection_1
product_3 collection_2


CASCADE -> removed collection_2 remove all products connected to collection
SET_NULL -> removed collection_2 set null value to all products connected to collection
PROTECTED -> you are not allowed to remove a collection with product


ManyToMany

Student Courses
1       many
many    1
many    many


Student

    asghar
    ali
    taghi

Course

    math
    art
    science

Master 

    name
    department

Department
    name
    university

StudentCourseMaster
    std_id  c_id    m_id    year    score   
    asghar  math    masoumi 93-94   10

"""
# class Student(models.Model):
#     pass

# class Course(models.Model):
#     pass

# class Master(models.Model):
#     pass

# class StudentCourseMaster(models.Model):
#     student = models.ForeignKey(Student)
#     course = models.ForeignKey(Course)
#     master = models.ForeignKey(Master)
#     year = models.IntegerChoices()

class Product(models.Model):
    # id = models.CharField(
    #     max_length=16, primary_key=True, default=id_generator
    # ) 
    slug = models.SlugField(max_length=100) # the-green-cafe
    title = models.CharField(max_length=100) # varchar(100)
    description = models.TextField()
    # 9999.99 max_digit: 6, decimal_places: 2
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    inventory = models.PositiveIntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    last_update = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta: 
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return f"{self.title}"

    __repr__ = __str__
