---
id: 3886dd8f-5ee1-4f83-afcf-0ca4bf8cd229
title: Learn Coding in 12 Years
slug: learn-coding-in-12-years
author: Admin
cover: /static/images/blogs/screenshot2026-08-1020-29-30.png
date_posted: 2026-08-16
last_modified: 2026-08-16
draft: false
tags: impact
---
Out for a walk one day, a woman came across a construction site and saw three men working. She asked the first man, “What are you doing?” Annoyed by the question, the first man barked, “Can’t you see that I’m laying bricks?” Not satisfied with the answer, she asked the second man what he was doing. The second man answered, “I’m building a brick wall.” Then, turning his attention to the first man, he said, “Hey, you just passed the end of the wall. You need to take off that last brick.” Again not satisfied with the answer, she asked the third man what he was doing. And the man said to her while looking up in the sky, “I am building the biggest cathedral this world has ever known.” While he was standing there and looking up in the sky the other two men started arguing about the errant brick. The man turned to the first two men and said, “Hey guys, don’t worry about that brick. It’s an inside wall, it will get plastered over and no one will ever see that brick. Just move on to another layer.”

The moral of the story is that when you know the whole system and understand how different pieces fit together (bricks, walls, cathedral), you can identify and fix problems faster (errant brick).

What does it have to do with creating your own Web server from scratch?

**I believe to become a better developer you MUST get a better understanding of the underlying software systems you use on a daily basis and that includes programming languages, compilers and interpreters, databases and operating systems, web servers and web frameworks. And, to get a better and deeper understanding of those systems you MUST re-build them from scratch, brick by brick, wall by wall.**

Confucius put it this way:

> *“I hear and I forget.”*



![Hear](https://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_hear.png)

> *“I see and I remember.”*



![See](https://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_see.png)

> *“I do and I understand.”*



![Do](https://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_do.png)

I hope at this point you’re convinced that it’s a good idea to start re-building different software systems to learn how they work.

In this three-part series I will show you how to build your own basic Web server. Let’s get started.

First things first, what is a Web server?



![HTTP Request/Response](https://ruslanspivak.com/lsbaws-part1/LSBAWS_HTTP_request_response.png)

In a nutshell it’s a networking server that sits on a physical server (oops, a server on a server) and waits for a client to send a request. When it receives a request, it generates a response and sends it back to the client. The communication between a client and a server happens using HTTP protocol. A client can be your browser or any other software that speaks HTTP.

What would a very simple implementation of a Web server look like? Here is my take on it. The example is in Python (tested on Python3.7+) but even if you don’t know Python (it’s a very easy language to pick up, try it!) you still should be able to understand concepts from the code and explanations below: