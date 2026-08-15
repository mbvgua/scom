---
id: d52122a6-41b0-4f04-b47e-e7731bed9706
title: A simple markdown overview!
slug: simple-markdown-overview
author: Admin
cover: /static/images/blogs/suzuki.png
draft: false
date_posted: 2026-08-13
last_modified: 2026-08-13
tags: events
---

# Table of Contents

1. [Headings](#headings)
1. [Paragraphs](#paragraphs)
1. [Horizontal Breaks](#horizontal-breaks)
2. [Lists](#lists)
1. [Emphasis & Italics](#emphasis-&-italics)
1. [Links](#links)
1. [Images](#images)
1. [CodeBlocks & Inline Code](#codeblocks-&-inline-code)
1. [Tables](#tables)
1. [Blockquotes](#blockquotes)
1. [Html elements](#html-elements)
1. [Footer](#footer)

## Headings

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit. Pellentesque vel lacinia neque. Praesent nulla quam, ullamcorper in sollicitudin ac, molestie sed justo. Cras aliquam, sapien id consectetur accumsan, augue magna faucibus ex, ut ultricies turpis tortor vel ante. In at rutrum tellus.

# Sample heading 1

## Sample heading 2

### Sample heading 3

#### Sample heading 4

##### Sample heading 5

###### Sample heading 6

## Paragraphs

This is the first paragraph. It flows naturally as you type.

This is a brand new paragraph because there is a blank line above it.  
This line is immediately below the previous one because it uses a soft break (two spaces at the end of the line above).

Mauris viverra dictum ultricies. Vestibulum quis ipsum euismod, facilisis metus sed, varius ipsum. Donec scelerisque lacus libero, eu dignissim sem venenatis at. Etiam id nisl ut lorem gravida euismod.

## Horizontal Breaks

---
***
___

## Lists

Unordered:

- Fusce non velit cursus ligula mattis convallis vel at metus[^2].
- Sed pharetra tellus massa, non elementum eros vulputate non.
    - this is a nested one
    - pretty cool
- Suspendisse potenti.

Ordered:

1. Quisque arcu felis, laoreet vel accumsan sit amet, fermentum at nunc.
2. Sed massa quam, auctor in eros quis, porttitor tincidunt orci.
3. Nulla convallis id sapien ornare viverra.
4. Nam a est eget ligula pellentesque posuere.

## Emphasis & Italics

*This text is italicized* and _so is this_.
**This text is bolded** and __so is this__.
***This text is bolded and italicized***.
~~This text is struck through~~.

## Links

[Visit GitHub](https://github.com)
[FastAPI Documentation](https://fastapi.tiangolo.com "Official FastAPI Docs")

## Images

![](/static/images/blogs/llama.png)

## CodeBlocks & Inline Code

Now some code:

```

const ultimateTruth = 'this theme is the best!';

console.log(ultimateTruth);

```

And here is some `inline code`!

## Tables

Now a table:


| Left Align | Center Align | Right Align |
| :---       | :---:        | ---:        |
| Row 1      | Data 1       | $10.00      |
| Row 2      | Data 2       | $5.50       |
| col 3 is   | Data 3       | $1600       |
| col 2 is   | Data 4       | $12         |
| zebra      | are neat     | $1          |

## Blockquote

The following is a blockquote:

> "The only limit to our realization of tomorrow will be our doubts of today."
> — Franklin D. Roosevelt

## Html Elements

<p style="color: red;">This text is red.</p>
<div align="center">
  <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy
</div>



[^1]: this is a footnote. It should highlight if you click on the corresponding superscript number.

[^2]: hey there, i'm using no style please!

[^3]: this is another footnote.

[^4]: this is a very very long footnote to test if a very very long footnote brings some problems or not. I strongly hope that there are no problems but you know sometimes problems arise from nowhere.
