[app]

# عنوان التطبيق الذي سيظهر للمستخدم على الجهاز.
title = ToDoApp

# اسم حزمة الأندرويد (يجب أن يكون فريداً).
package.name = todoapp
# نطاق الحزمة (ضروري أن يكون فريداً وخاصاً بك).
package.domain = com.mycustomapp # <-- غيّر هذا إلى اسم فريد خاص بك (مثال: com.yourname.todoapp)!

# إصدار التطبيق (يمكن زيادته مع كل تحديث).
version = 0.1

# مسار ملف الأيقونة الخاص بتطبيقك.
# لقد قمت بتحديثه لاستخدام book.jpg وتأكدت من إزالة التعليق.
icon.filename = %(source.dir)s/book.jpg

# المجلد الأساسي لمشروعك (نقطة).
source.dir = .
# امتدادات الملفات التي يجب تضمينها في حزمة التطبيق.
# تأكد من أن 'jpg' موجود لأن لديك 'book.jpg'.
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# ملف الدخول الرئيسي لتطبيق Kivy الخاص بك.
main.py = main.py

# متطلبات بايثون لتطبيقك. Buildozer سيقوم بتثبيتها.
# KivyMD و Plyer ضروريان لتطبيقك هذا.
requirements = python3,kivy,kivymd,plyer

# أذونات الأندرويد التي يحتاجها تطبيقك.
# INTERNET (للوصول للإنترنت) و VIBRATE (للاهتزاز مع الإشعارات).
android.permissions = INTERNET, VIBRATE

# minapi (أدنى إصدار أندرويد مدعوم)
android.minapi = 21.
android.targetsdk = 33

android.archs = arm64-v8a

# تفعيل AndroidX (ضروري للإصدارات الحديثة من SDK).
android.enable_androidx = True

android.release = False

android.debug = True
