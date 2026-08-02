"""
utility functions used inhandling anything regarding markdown within the
application.contains 1 function:
    - format_markdown_to_html
"""

import markdown
from markupsafe import Markup


def format_markdown_to_html(text: str):
    """
    accepts any text formatted with markdown markup, and converts it into well
    defined html. this is mainly used in rendering the "blog.content" sections
    in both the vlog card and the blog post. this happens as it creates a
    simple jinja2 filter that can be placed inline in the templates to perform
    the rendering. Jinja2 is really nice!
    """
    if text:
        html_content = markdown.markdown(text)
        return Markup(html_content)

    return ""
