from django.test import TestCase

from django.contrib.auth.models import User
from .models import Message

# Create your tests here.
class SnsTests(TestCase):

    def test_check(self):
        usr = User.objects.filter(username='test').first()

        msg = Message.objects.filter(content="test").first()
        self.assertIs(msg.owner_id, usr.id)
        self.assertEqual(msg.owner.username, usr.username)
        self.assertEqual(msg.group.title, 'public')

        msgs = Message.objects.filter(content__contains="test").all()
        self.assertIs(msgs.count(), 2)
        
        c = Message.objects.all().count()
        self.assertIs(c,5)
        
        msg1 = Message.objects.all().first()
        msg2 = Message.objects.all().last()
        self.assertIsNot(msg1, msg2)

