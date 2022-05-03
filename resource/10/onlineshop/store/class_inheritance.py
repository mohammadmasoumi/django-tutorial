
class A:
    class Meta:
        my_property = "class A"

class B(A):
    class Meta(A.Meta):
        my_property = A.Meta.my_property + " " + "Class B"


print(B.Meta.my_property)