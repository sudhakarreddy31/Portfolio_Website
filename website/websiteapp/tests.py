from django.test import TestCase
from django.urls import reverse
from websiteapp.models import GalleryImage  

class ViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/home.html')

    def test_about_view(self):
        response = self.client.get(reverse('About'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/about.html')

    def test_skills_view(self):
        response = self.client.get(reverse('Skills'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/skills.html')

    def test_work_view(self):
        response = self.client.get(reverse('Work'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/work.html')

    def test_contact_view(self):
        response = self.client.get(reverse('Contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/contact.html')

    def test_gallery_list_view(self):
        # Create some test data for the GalleryImage model
        GalleryImage.objects.create(title='Image 1', image='image1.jpg')
        GalleryImage.objects.create(title='Image 2', image='image2.jpg')

        response = self.client.get(reverse('Gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websiteapp/gallery.html')
        self.assertIn('images', response.context)
        self.assertEqual(len(response.context['images']), 2) 