---
layout: home
title: Home
nav_order: 1
nav_exclude: false
permalink: index.html
seo:
  type: Course
  name: Just the Class
---

# Introduction to Computational Thinking with Data

{: .mb-2 }
UC Berkeley, Summer 2022
{: .mb-2 .fs-6 .text-grey-dk-000 }

{: .mb-2 }
**Instructors:** James Weichert (<a>jweichert@berkeley.edu</a>), Will Furtado (<a>willfurtado@berkeley.edu</a>)
{: .mb-0 .fs-5 .text-grey-dk-000 }

<!--{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>-->

## Announcements

- [announcements](announcements.md),
- a [course calendar](calendar.md),
- a [staff](staff.md) page,
- and a weekly [schedule](schedule.md).

{% for module in site.modules %}
{{ module }}
{% endfor %}


Just the Class is a template that extends the popular [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme, which provides a robust and thoroughly-tested foundation for your website. Just the Docs include features such as:

- automatic [navigation structure](https://just-the-docs.github.io/just-the-docs/docs/navigation-structure/),
- instant, full-text [search](https://just-the-docs.github.io/just-the-docs/docs/search/) and page indexing,
- and a set of [UI components](https://just-the-docs.github.io/just-the-docs/docs/ui-components) and authoring [utilities](https://just-the-docs.github.io/just-the-docs/docs/utilities).
