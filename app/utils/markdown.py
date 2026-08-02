import markdown
from markupsafe import Markup


def format_markdown_to_html(text: str):
    if text:
        html_content = markdown.markdown(text)
        return Markup(html_content)

    return ""
