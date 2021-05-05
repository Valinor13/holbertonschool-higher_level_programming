#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", None)
say_my_name(None, "White")
say_my_name("Bob")
try:
    say_my_name(None, "White")
except Exception as e:
    print(e)
