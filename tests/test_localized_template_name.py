from unittest import TestCase

from templates_email.merge import localized_template_name


class TransactionalEmailLocalizedTemplateNameTest(TestCase):
    def test_it_should_localize_template_name_with_extension(self):
        assert 'email/test-en.html' == localized_template_name('email/test.html', 'en')

    def test_it_should_localize_template_name_without_extension(self):
        assert 'email/test-en' == localized_template_name('email/test', 'en')
