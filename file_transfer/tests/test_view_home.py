from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import resolve, reverse

from file_transfer.models import File
from file_transfer.views import FileListView


class HomeTests(TestCase):
    def setUp(self):
        temp = SimpleUploadedFile('1.txt', b'11111111')
        self.file = File.objects.create(document=temp)
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, FileListView)

    def test_home_view_contains_link_to_file_download_link(self):
        file_url = self.file.document.url
        self.assertContains(self.response, 'href="{0}"'.format(file_url))

    # def test_home_view_contains_link_to_topics_page(self):
    #     board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
    #     self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))