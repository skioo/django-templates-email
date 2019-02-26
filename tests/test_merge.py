from datetime import date
from unittest import skip

from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.test import TestCase, override_settings
from pytest import raises

from templates_email.merge import merge

expected_html = """<html>
<head>
</head>
<body style="background-color:linen" bgcolor="linen">
    <p style="color:maroon; margin-left:40px">Hi bobby tables,</p>

    <p style="color:maroon; margin-left:40px">You just signed up for my website, using:
    </p><dl>
        <dt>username</dt>
        <dd>bob</dd>

        <dt>join date</dt>
        <dd>Feb. 5, 2007</dd>
    </dl>
    

    <p style="color:maroon; margin-left:40px">Thanks, you rock!</p>

</body>
</html>"""  # noqa


class EmailTemplateMergeTest(TestCase):
    def test_it_should_inline_styles_and_generate_plaintext(self):
        context = dict(
            username='bob',
            full_name='bobby tables',
            joindate=date(2007, 2, 5)
        )
        merged_email = merge('standalone.html', context, 'en')
        assert merged_email.template == 'standalone-en.html'
        assert merged_email.language == 'en'
        assert merged_email.subject == 'My subject for bob'
        assert merged_email.html == expected_html
        assert merged_email.plain == """
    Hi bobby tables,

    You just signed up for my website, using:

        username
        bob

        join date
        Feb. 5, 2007

    Thanks, you rock!
"""

    def test_it_should_merge_all_parts_of_a_modularized_template(self):
        context = dict(
            username='bob',
            full_name='bobby tables',
            joindate=date(2007, 2, 5)
        )
        merged_email = merge('derived.html', context, 'en')
        assert merged_email.subject == 'My subject for bob'
        assert merged_email.html == expected_html

    def test_it_should_use_the_language_to_select_the_template_and_format_dates(self):
        context = dict(
            username='bob',
            full_name='bobby tables',
            joindate=date(2007, 2, 5)
        )
        merged_email = merge('derived.html', context, 'fr')
        assert merged_email.template == 'derived-fr.html'
        assert merged_email.language == 'fr'
        assert merged_email.subject == 'Mon sujet pour bob'
        assert merged_email.html == """<html>
<head>
</head>
<body style="background-color:linen" bgcolor="linen">
    <p style="color:maroon; margin-left:40px">Bonjour bobby tables,</p>

    <p style="color:maroon; margin-left:40px">Vous venez de vous inscrire a mon site:
    </p><dl>
        <dt>nom d'utilisateur</dt>
        <dd>bob</dd>

        <dt>date d'inscription</dt>
        <dd>5 février 2007</dd>
    </dl>
    

    <p style="color:maroon; margin-left:40px">Merci!</p>
</body>
</html>"""  # noqa

    def test_it_should_raise_an_exception_if_there_is_no_template_for_the_language(self):
        with raises(TemplateDoesNotExist):
            merge('derived.html', {}, 'jp')

    def test_it_should_use_the_fallback_language_if_there_is_no_template_for_the_requested_language(self):
        merged_email = merge(
            template_name='derived.html',
            context=dict(
                username='bob',
                full_name='bobby tables',
                joindate=date(2007, 2, 5)
            ),
            language='jp',
            fallback_language='en'
        )
        assert merged_email.template == 'derived-en.html'
        assert merged_email.language == 'en'
        assert merged_email.html == expected_html

    def test_it_should_raise_an_exception_if_there_is_no_template_for_either_language(self):
        with raises(TemplateDoesNotExist):
            merge('does-not-exist.html', {}, 'en', fallback_language='en')

    # I can't get this to work because the fallback language has already been determined
    # when the settings module was loaded (and when the merge function was called the first time).
    # I don't know how to solve this without making everything much more dynamic (and cumbersome, and slow).
    @skip("configuration is too static")
    @override_settings(TEMPLATES_EMAIL={'FALLBACK_LANGUAGE': 'en'})
    def test_it_should_honor_the_default_fallback_language_settings(self):
        merged_email = merge('derived.html', {}, 'jp')
        assert merged_email.template == 'derived-en.html'
        assert merged_email.language == 'en'
        assert merged_email.html == expected_html

    @skip("I believe it is because render-blocks doesn't recurse up the 'extends' chain")
    def test_it_should_merge_all_parts_of_a_deeply_derived_template(self):
        context = dict(
            username='bob',
            full_name='bobby tables',
            joindate=date(2007, 2, 5)
        )
        merge('derived-twice.html', context, 'en')

    def test_it_should_report_syntax_error_in_template(self):
        with raises(TemplateSyntaxError, match='Invalid block tag'):
            merge('template_with_syntax_error.html', {}, 'en')

    def test_it_should_report_runtime_error(self):
        with raises(TypeError, match='is not iterable'):
            merge('template_with_runtime_error.html', {'l': 1}, 'en')
