"""
utility function to be used in jinja2 templates.

currently contains:
    - format_markdown_to_html
    - calculate_reading_time
"""

import math

import markdown
from markupsafe import Markup


def format_markdown_to_html(text: str):
    """
    simply formats raw markdown into clean html, ensuringits properly styled
    with appropriate tags
    """
    html_content = markdown.markdown(
        text, extensions=["fenced_code", "codehilite", "toc", "extra"]
    )

    # NOTE: since im parsing things, everything is rendered as plain html tags
    # with no additional bootstrap styling. this fixes that for the tables. the
    # other minor details are resolved in the .css styling
    html_content = html_content.replace(
        "<table>",
        '<div class="table-responsive"><table class="table table-striped table-hover table-custom-header table-bordered">',
    ).replace(
        "</table>",
        "</table></div>",
    )
    return Markup(html_content)


def calculate_reading_time(text: str) -> int:
    """
    calculates the average time, in minutes, it takes to read through a blog.
    NOTE:
        - It assumes the average reader reads 200wpm
        - minimum time it might take to read any blog is 1 minute
    """

    word_count = len(text.split())
    minutes = math.ceil(word_count / 200)
    return max(1, minutes)
