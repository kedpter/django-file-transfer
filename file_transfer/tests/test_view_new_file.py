from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from file_transfer.models import File


class NewTopicTests(TestCase):
    def setUp(self):
        pass


    def test_new_file_view_upload_file_success(self):
        self.file = SimpleUploadedFile('1.txt', b'123')
        self.client.post(reverse('new_file'), {'document': self.file})
        self.assertTrue(File.objects.exists())


    # def test_new_topic_view_not_found_status_code(self):
    #     url = reverse('new_topic', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)
    #
    # def test_new_topic_url_resolves_new_topic_view(self):
    #     view = resolve('/boards/1/new/')
    #     self.assertEquals(view.func, new_topic)
    #
    # def test_new_topic_view_contains_link_back_to_board_topics_view(self):
    #     new_topic_url = reverse('new_topic', kwargs={'pk': 1})
    #     board_topics_url = reverse('board_topics', kwargs={'pk': 1})
    #     response = self.client.get(new_topic_url)
    #     self.assertContains(response, 'href="{0}"'.format(board_topics_url))
    #
    # def test_csrf(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     self.assertContains(response, 'csrfmiddlewaretoken')
    #
    # def test_contains_form(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     form = response.context.get('form')
    #     self.assertIsInstance(form, NewTopicForm)
    #
    #
    # def test_new_topic_invalid_post_data(self):
    #     '''
    #     Invalid post data should not redirect
    #     The expected behavior is to show the form again with validation errors
    #     '''
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.post(url, {})
    #     form = response.context.get('form')
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTrue(form.errors)
