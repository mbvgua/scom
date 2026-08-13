"""
utility function to be used in jinja2 templates. simply formats raw markdown
into clean html, ensuringits properly styled with appropriate tags

currently only 1 function:
    - format_markdown_to_html
"""

import markdown
from markupsafe import Markup


def format_markdown_to_html(text: str):
    html_content = markdown.markdown(
        text, extensions=["fenced_code", "codehilite", "extra"]
    )
    return Markup(html_content)
