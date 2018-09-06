from django.shortcuts import render

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

import string

def index(request):
    for key in r.scan_iter("user:*"):
        output = r.get(key)

    return render(request, 'movies/index.html')
