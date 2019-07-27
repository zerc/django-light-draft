import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

from tests import factories as f

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class DraftTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(DraftTestCase, cls).setUpClass()
        cls.post = f.BlogPostFactory(tags_count=2, blocks_count=2)
        cls.admin_change_url = reverse('admin:blog_blogpost_change', args=(cls.post.pk,))
        cls.admin_preview_url = reverse('admin:blog_blogpost_preview', args=(cls.post.pk,))
        cls.admin_user = f.UserFactory(username='admin')
        cls.admin_user.set_password('admin')
        cls.admin_user.save()

    def setUp(self):
        super(DraftTestCase, self).setUp()
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(firefox_options=options)
        self.selenium.get('{}/admin/'.format(self.live_server_url))
        self.assertEqual('{}/admin/login/?next=/admin/'.format(self.live_server_url), self.selenium.current_url)
        self.selenium.find_element_by_name('username').send_keys('admin')
        self.selenium.find_element_by_name('password').send_keys('admin')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        WebDriverWait(self.selenium, 2).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        self.assertEqual('{}/admin/'.format(self.live_server_url), self.selenium.current_url)

    def tearDown(self):
        self.selenium.quit()
        super(DraftTestCase, self).tearDown()

    def test_ok(self):
        url = '{}{}'.format(self.live_server_url, self.admin_change_url)
        self._get_url(url)

        self.selenium.find_element_by_id('id_title').send_keys('Exiting new title')

        draft_element = self.selenium.find_elements_by_css_selector('#content-main .object-tools a.previewlink')
        self.assertEqual(len(draft_element), 1)

        draft_element = draft_element[0]
        draft_element.is_displayed()
        self.assertEqual(draft_element.text, 'DRAFT PREVIEW')

        draft_element.click()
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        time.sleep(1)  # need some delay after switching tabs...

        expected_part_url = '{}{}?hash=blog:blogpost:{}'.format(
            self.live_server_url,
            self.post.get_absolute_url(),
            self.post.pk
        )

        self.assertTrue(self.selenium.current_url.startswith(expected_part_url))

    def _get_url(self, url):
        """Helper to open an URL and check that we weren't redirected somewhere."""
        self.selenium.get(url)
        self.assertEqual(url, self.selenium.current_url)
