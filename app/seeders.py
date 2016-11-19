from .models import Topic, Side, Opinion
import barnum
import random


def make_opinion(side):
    data = {
        'side': side,
        'content': barnum.create_sentence(max=10),
        'likes': random.randint(1, 1000)
    }
    return Opinion.objects.create(**data)


def make_side(topic):
    data = {
        'topic': topic,
        'title': barnum.create_sentence(max=5)
    }
    return Side.objects.create(**data)


def make_topic():
    data = {
        'title': barnum.create_sentence(max=5),
        'description': barnum.create_sentence(min=14)
    }
    return Topic.objects.create(**data)


def seed(n=1):
    for i in range(n):
        topic = make_topic()
        for j in range(random.randint(2, 3)):
            side = make_side(topic)
            for k in range(random.randint(5, 100)):
                make_opinion(side)
    print('complete')
