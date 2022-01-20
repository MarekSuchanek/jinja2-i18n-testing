import babel.support
import jinja2
import pathlib


DIR_TRANSLATIONS = pathlib.Path('./translations')
DIR_TEMPLATES = pathlib.Path('./templates')
OUTPUT = pathlib.Path('./out.html')
LANGUAGES = ['cs']

if __name__ == '__main__':
    loader = jinja2.FileSystemLoader(DIR_TEMPLATES)
    translations = babel.support.Translations.load(
        DIR_TRANSLATIONS,
        LANGUAGES,
    )
    env = jinja2.Environment(
        extensions=['jinja2.ext.i18n'],
        loader=loader,
    )  # add any other env options if needed
    env.install_gettext_translations(translations)

    template = env.get_template('test.html.j2')
    rendered_template = template.render()
    OUTPUT.write_text(
        data=rendered_template,
        encoding='utf-8',
    )

