#using getsizeof()
import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print(f"{sys.getsizeof(Tuple1)} bytes")

#using inbuilt__sizeof__()
print(f"Size of Tuple2: {Tuple2.__sizeof__()} bytes")