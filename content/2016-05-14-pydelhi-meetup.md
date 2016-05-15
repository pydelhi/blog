Title: PyDelhi MayPy
Slug: pydelhi-14-05-16
Date: 2016-01-17 12:00
Category: Meetup
Author: Harshit Tyagi
Email: harshit.bvcoe@gmail.com

![Think open-source]({filename}/images/pydelhi-14-05-16.jpg)

Summary: PyDelhi members coming together and meeting up to learn, collaborate, give encouragement and seek advice from members who are such excellent source of support.

May 14th marked by scorching heat and to tackle it we had some cool Python libraries and Framework to learn, share and interact at the PyDelhi Meetup at Fueled Noida sec-16. Attended by 70 python enthusiasts.

<!-- [![PyDelhi Meetup]()](https://twitter.com/PyDelhi/status/731416447285518336) -->

###Hackathon Listing Platform using Django Framework

First we had Pulkit Pahwa, an experienced Django Developer taking up a knowledge enriching session on [Django web framework](https://docs.djangoproject.com/en/1.9/). The agenda was to build a hackathon listing platform sort of a mini-hackerearth which required basic knowledge of Python. Started with the creation of the django project,and then an app for hackathon related information with the models.py dealing with the data and model fields, urls.py for url configuration and mapping the urls to the handlers lodged in the views.py of our app using the [Django ORM](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwjX_tCO8NvMAhXLuo8KHZCiB2UQFggwMAM&url=https%3A%2F%2Fwww.fullstackpython.com%2Fobject-relational-mappers-orms.html&usg=AFQjCNFCZ-M7K54mFXSClQAffl7vacgmag&sig2=M8go3MJ7AxAyLGI3Q-FV4A). The interaction led process of request response cycle and how django's modules handle the requests and rendering the data onto the templates. A nicely pulled up session came to an end with our dummy hackathon lists brightening up our pages running on our very own django's development server with developers getting in touch with the awesomeness(speed and ease) of the Django Framework.

Refreshments are just a way to get to interact with people about their work experience, their findings, and best practices of problem solving. You never know which statement might prove helpful to you at what point in your project.



###Getting Python to interact with Java and objc using PyJnius and PyObjus
![PyDelhi Meetup]({filename}/images/pydelhi-may-2.jpg)

Next we had a talk on "Getting python to interact with java, objc using PyJnius and PyObjus."
by Akkshay Arora, - Python, linux lover, core dev of [kivy](http://kivy.org­). The discussion invlolved a few python libraries which provide modules and methods to interact with other languages without diving much into it. The usage of this can simply be explained by thinking of a situation where you can have the best of two languages with the knowledge of one -  feels weird right? But this is actually possible.

[PyJNIus](https://github.com/kivy/pyjnius) - A Python module to access Java classes as Python classes using JNI.

With a quick overview : 
```python
from jnius import autoclass
autoclass('java.lang.System').out.println('Hello world')
Hello world
Stack = autoclass('java.util.Stack')
stack = Stack()
stack.push('hello')
stack.push('world')
print stack.pop()
world
print stack.pop()
hello
```

Now with this great library the difference to other projects is that apps can take advantage of 
[python-for-android’s](https://kivy.org/planet/2016/05/android-apps-with-python-flask-and-a-webview/) relatively extensive toolchain including python3.5 support, the ability to build popular libraries like numpy, support for multiple architectures, and access to the Android API via PyJNIus or Plyer rather than SL4A.



[PyObjus](https://github.com/kivy/pyobjus) - Python module for accessing Objective-C classes as Python classes using Objective-C runtime reflection.

```python
from pyobjus import autoclass, objc_str
from pyobjus.dylib_manager import load_framework, INCLUDE
load_framework(INCLUDE.AppKit)
# get nsalert class
NSAlert = autoclass('NSAlert')
# create an NSAlert object, and show it.
alert = NSAlert.alloc().init()
alert.setMessageText_(objc_str('Hello world!'))
alert.runModal()
```
So, autoclass is the heart of pyobjus. With this function, you load Objective C classes into pyobjus which then constructs a Python wrapper around these objects. You can load external code into pyobjus using the load_framework function, or by using load_dylib. The
load_framework function uses NSBundle for loading the framework into pyobjus, and the load_dylib function uses ctypes for loading external .dylib objects into pyobjus.

Well this is just a trailer and here we believe the script of the movie should be written by you. Keep exploring and explain yourself the reason why these excellent libraries and frameworks have been built with a Project or application.
Because Necessity is long gone. Now innvovation mothers Invention.
Subscribe to our blog and follow us on social media and keep coming to the meetups on alternate saturdays.

Looking forward to meet you!! Till then this is PyDelhi signing off.
