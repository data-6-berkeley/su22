---
layout: page
title: Making Your Own Website
tagline: Lab 8: Website Development
nav_exclude: true
---

# Lab 8: Making Your Own Website

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

In this lab we will take a brief detour away from Python and data science libraries to talk about websites and web development. **By the end of this lab, you will have created your own public-facing website** that you can show off to your friends and family and customize with more information about you, showcase school or personal projects, and more (if you want, of course).

This lab will probably take 2 hours to complete, so buckle in! Course staff are here to help with troubleshooting and any questions you might have.

## Overview
Websites can take a variety of forms, and are created in a variety of ways. On the most basic level, a website consists of pages created in a markup language, like HTML (HyperText Markup Language). If you have ever used “Inspect” or “Inspect Element” on a website (Figure 1), you have probably seen HTML before. It consists of tags that start and end with angle brackets (e.g. `<html>`). Even though HTML doesn’t support more complicated code like if-statements or for loops (HTML technically isn’t even a programming language), when combined with other code it is capable of creating amazingly complex websites.

<figure style="margin:auto">
<img src="https://data6.org/su22/assets/lab08/fig1.png" style="width:50%"/>
<figcaption>Figure 1</figcaption>
</figure>

**Website development** also usually involves writing code in a variety of other languages, including CSS (for styling your website), JavaScript (for making your website more responsive), and PHP (for integrating your website with a database). However, to create a simple website you don’t need to know anything about these more complicated languages.

In fact, the website you will create today will simplify things a lot by taking care of many of the behind-the-scenes details, including formatting, styling, and hosting. You will also be able to create your website in [markdown](https://en.wikipedia.org/wiki/Markdown), the same language that is used to create markdown cells in Jupyter Notebooks. This way, you don’t even have to worry about understanding HTML (which is a big time-saver).

To make things as simple as possible, we will use [GitHub Pages](https://pages.github.com/) to build and host our website (on the world wide web!). GitHub Pages is great because it is free and integrates well with the GitHub version control system. Once you create your website, you will host it on GitHub Pages with your own GitHub account and will be able to edit it whenever you want. As an example of what’s possible with GitHub Pages, look no further than the Data 6 website — it was created using the same tools you’ll learn today.

**Let's get started!**

## Step 1 — Creating a GitHub Account
First you will have to set a GitHub account to allow you to develop and publish your website. GitHub is free and is also used in a lot of data science and computer science classes at Berkeley. If you already have a GitHub account (that you want to use for this lab), you can skip this step.

1. **Create a [GitHub](https://github.com/) Account** (go to the site and click “Sign Up” in the top right).
  * Your username is up to you, but it may be a good idea to choose something professional since you might use this account in the future for something else. Your website URL will contain your username.
  * After entering your credentials, it may ask you questions like “What kind of work do you do, mainly?”. You can skip these; scroll all the way to the bottom and continue.
  * You’ll then need to verify your email address.

## Step 2 — Creating a Blank Website

1. **Create a New Repository.** It may prompt you to do this after verifying your email; if it doesn’t, you can go to [GitHub](https://github.com/) and click the green “New” button.
  * A **repository**, or repo for short, is like a folder for a project.
  * You will need to select a name for the repository. You can name the repository whatever you want, but we’d recommend something like `“data-6-website”`, `“[NAME]-website”` or `“portfolio”`
  * Make sure to select Public and add a `README` file. Overall, your settings should look like this (but with a different username and repo name):

<figure>
<img src="https://data6.org/su22/assets/lab08/fig2.png" style="width:50%"/>
<figcaption>Figure 2 - Repository Settings</figcaption>
</figure>
2. Enable GitHub Pages for your Repo. GitHub Pages is the feature we will use to create our website. Follow these steps:
  * From your repo’s main page, click the “Settings” tab in the top right corner.
  * Click “Pages” in the menu on the left (it should be towards the bottom).
  * Under “Branch”, change “None” to “main”. Click “Save”.
  * Under “Theme Chooser”, click “Choose a theme”. It will allow you to choose one of several themes; pick the one you like the most and click “Select theme”. If you end up not liking your choice, you can always come back to this menu and change the theme, so don’t worry. Note: If you are brought to a page that has you try and edit your file (it may say something like “Edit new file”), just click “Cancel”.
  * After you follow these steps, your site will be public. You will be shown its URL; it will be in the form `<your github username>.github.io/<your repo name>`. Keep a tab open with your website while working on the rest of the assignment.

<figure>
<img src="https://data6.org/su22/assets/lab08/fig3.png" style="width:50%"/>
<figcaption>Figure 3 - Publishing via GitHub Pages</figcaption>
</figure>

## Step 3 — Adding Content

## Step 4 — Customizing Your Website

## Markdown Guide

| **Syntax** | **Usage** | **Example** |
| `#` | Header (Adding multiple `#` in succession decreases the size of the header) | `## This is a Level 2 Header` |
| `**TEXT**` | Bold Text | `**This text will be bolded` |
| `*TEXT*` | Italic Text | `*This text will be italicized` |
| `[TEXT](LINK)` | Hyperlink (the `TEXT` will be displayed, and clicking on it will redirect to the website at `LINK`) | `[Data 6 Website](https://data6.org/su22/)`

<hr>

The Summer 2022 version of the website development lab was adapted by James Weichert from the [Data 94 Spring 2021 Homework 9](http://data94.org/resources/assets/homework/hw09/), created by Suraj Rampure.
