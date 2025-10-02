[app]
title = My TodoApp
package.name = mytodoapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy,kivymd,plyer
icon.filename = book.jpg
orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.build_tools = 34.0.0
android.arch = arm64-v8a
android.permissions = INTERNET,WAKE_LOCK
log_level = 2
source.include_patterns = assets/*,images/*
presplash.filename = book.jpg
