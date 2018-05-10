from django.shortcuts import render
from django.http import JsonResponse
from .models import Word
import requests
import json
import os

def home(request):
    with open('dictionary.json') as f:
        letter_json = json.load(f)
    letters = [{'letter': chr(i), 'count': len(letter_json[chr(i)])} for i in range(97, 123)]
    saved_word = Word.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'letters': letters, 'saved_word': saved_word})


def letter(request, key):
    with open('dictionary.json') as f:
        letter_json = json.load(f)
    if 97 <= ord(key) <= 123:
        words = letter_json[key][:20]
    else:
        words = []

    return render(request, 'letter.html', {'key': key, 'words': words})


def add_word(request):
    try:
        ajax_word = request.POST.get('word')[5:]
        word = Word(word=ajax_word)
        word.save()
        saved = True
    except:
        saved = False
    return JsonResponse({'message': saved})


def delete_word(request):
    try:
        ajax_word = request.POST.get('word')
        word = Word.objects.filter(word=ajax_word).get()
        word.delete()
        removed = True
    except:
        removed = False

    return JsonResponse({'message': removed})


def search_word(request):
    word = request.GET.get('word')[5:]
    data = {'data': [], 'message': False}
    try:
        app_id = os.environ['APP_ID']
        app_key = os.environ['APP_KEY']
        language = 'en'
        url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + language + '/' + word
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        if r.status_code == 200:
            json_data = json.loads(r.text)
            print(json_data)
            for senses in json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
                temp_data = {}
                if 'definitions' in senses:
                    temp_data['definition'] = senses['definitions'][0]
                else:
                    continue
                if 'examples' in senses:
                    temp_data['example'] = senses['examples'][0]['text']
                else:
                    temp_data['example'] = 'None'
                data['data'].append(temp_data)
            data['message'] = True
            data['word'] = json_data['results'][0]['word']
        else:
            data['word'] = 'No meaning Found'
    except:
        data['message'] = False

    return JsonResponse(data)


def get_word(request):
    try:
        key, count = request.GET.get('count').split('-')
        print(count)
        count = int(count)
        with open('dictionary.json') as f:
            letter_json = json.load(f)
            if 97 <= ord(key) <= 123:
                words = letter_json[key][count:count+20]
                data = {'words': words, 'message': True, 'key': key, 'count': str(count+20)}
            else:
                data = {'words': '', 'message': False}
    except:
        data = {'words': False, 'message': False}

    return JsonResponse(data)