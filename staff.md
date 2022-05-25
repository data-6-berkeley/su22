---
layout: page
title: Staff
description: Data 6 Summer 2022 Course Staff.
---

# Staff

Staff information is stored in the `_staffers` directory and rendered according to the layout file, `_layouts/staffer.html`.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}


## Undergraduate Student Instructors (uGSIs)

{% assign teaching_assistants = site.staffers | where: 'role', 'uGSI' %}
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}

## Tutors

{% assign tutors = site.staffers | where: 'role', 'Tutor' %}
{% for staffer in tutors %}
{{ staffer }}
{% endfor %}
