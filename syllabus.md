---
layout: page
title: Syllabus
nav_order: 2
description: >-
    Course policies and information.
---

# Syllabus &#x1F4D6;
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Welcome	&#x1F44B;

Welcome to Data 6 Summer 2022! On behalf of Data 6 course staff, we’re excited to be teaching you this summer and hope you enjoy this class as much as we enjoy teaching it. Whether you’re a first-time college student or a seasoned veteran student, Data 6 is the perfect course to get started with coding and data science. This course is specifically designed without any prerequisites or assumed prior knowledge of computer science or statistics — we will teach you **everything** you need to succeed in this class and prepare you for further data science and/or computer science classes. Along the way, you’ll gain practical experience working with data and using Python code to extract useful insights from real-world data sets. Even if this is the last data science class you ever take, we hope you’ll gain useful skills that you can apply to your own major or field of study, especially in the social sciences.

One of—in our opinion—the best parts of data science at Berkeley is the opportunity to learn from other students. All members of course staff are current undergraduates at UC Berkeley who have taken other data science classes and have experience teaching in classes like Data 8. Believe it or not, we were all once students taking introductory data science and computer science classes and just as confused and overwhelmed as you. We know what it’s like to step into a class feeling out of place, but also know what it’s like to finish a class feeling fulfilled and confident in your ability to succeed in data science and computer science at Berkeley. You are here for a reason — you are all talented students and are all more than capable of being great data scientists, computer scientists, engineers, social scientists, and more. We want to do our best to support you this summer, so please don’t hesitate to reach out to any of us via email or Ed if you have any questions or concerns.

We are continually revising course materials, assignments, and policies to improve the course and make this the best learning experience for you all. We welcome constructive feedback about what we can improve, and will try our best to incorporate your feedback into future lectures and assignments.

Again, welcome to Data 6 — we can’t wait to meet you and are super excited to be teaching you this summer!

Best,
[James](https://data6.org/su22/staff/#instructors) and [Will](https://data6.org/su22/staff/#instructors)

<hr>

## About	&#x1F9D0;

From the course catalog: Data 6 is an introduction to computational thinking and quantitative reasoning, designed to prepare students for further coursework in data science, computer science, and statistics (in particular, Foundations of Data Science, Data 8). This course emphasizes the use of computation to gain insight about quantitative problems with real data from the social sciences.

Data 6 uses the Python programming language to teach computation. It also uses the [Jupyter Notebook](https://jupyter.org/) environment, which makes it easy to get started with programming without needing to use a text editor or terminal and is very popular in data science applications. Jupyter Notebooks are also used in courses like [Data 8](http://data8.org/) and [Data 100](https://ds100.org/), so it’s helpful to get a head start using them.

This class serves a different purpose than several other classes that may sound similar. Specifically:
* [**Data 8**](http://data8.org/): Data 8 (Foundations of Data Science) is the first course in the data science sequence and a core requirement for the data science major and minor. While some of the topics are similar, Data 6 does not cover nearly as much statistics and inference as Data 8. Instead, we dive deeper into the mechanics of Python and how to use Python to generate insights from data using real-world data sets (mostly from the social sciences). After taking Data 6, you will be more than well-equipped to take (and succeed in) Data 8.
* [**CS 10**](https://cs10.org/sp22/): CS 10 (The Beauty and Joy of Computing) is a similar class to Data 6 in that it is intended as an introduction to computing that assumes no prior experience with programming. However, CS 10 focuses less on Python and data science, and more on abstract ideas in computer science. It is a fantastic alternative (or complement) to Data 6.
* [**CS 61A**](https://cs61a.org/) and [**CS 88**](https://cs88-website.github.io/sp22/): Both CS 61A (Structure and Interpretation of Computer Programs) and CS 88 (Computational Structures in Data Science) also teach Python, but serve a slightly different purpose than Data 6 — namely, these courses are designed to introduce students to computer science, not to computing *in* data science. They cover the Python language in far greater detail than we will, but they do not cover how to work with real-world data. These courses are also substantially more fast-paced than Data 6, so they are excellent courses to take after Data 6 and/or Data 8.

For the Summer 2022 iteration of Data 6, we have rearranged the order of some topics to more gradually ramp up to more advanced topics and give you the tools to work with real-world data earlier on in the semester. This new ordering means that some of the lectures will be out of sync with the ordering of materials from previous iterations of the course. If you want to review material from past semesters, just keep in mind that you may not have learned certain concepts yet, and that’s perfectly ok.

The rough topic breakdown for this summer is as follows:
* Week 1: Introduction to Python and Jupyter Notebooks
* Week 2: Data Visualization
* Week 3: Working with real-world tabular data using the `datascience` Python library
* Week 4: Python Functions and Control
* Week 5: More Python (and more real-world applications)
* Week 6: Probability and Simulation

Lecture slides will be posted to the website right before each lecture to allow you to follow along if you want. You are also welcome to experiment with the concepts you’ve learned by writing or editing code in the Jupyter Notebook we provide for each lecture (feel free to change it however you want — we promise you won’t break anything). **There is no one textbook that covers the content of this course the way we intend on covering, so all of the material you’ll need to succeed in Data 6 will be presented in lecture, labs, homeworks, and discussions.** If you want to review additional material, we will post optional readings from online textbooks for other courses (e.g. Data 8) along with most lectures.

## Logistics &#x1F5D3;

**Lecture**: Mondays & Wednesdays, 10-12PM; Tuesdays & Thursdays, 10AM-11AM in [Wheeler](https://www.berkeley.edu/map?wheeler) 212

**Lab**: (Usually) Tuesdays & Thursdays, 11AM-12PM in [Wheeler](https://www.berkeley.edu/map?wheeler) 212

**Discussion**: Fridays, 10AM-12PM in [Dwinelle](https://www.berkeley.edu/map?dwinelle) 105 & 130

**Office Hours (Optional)**: Tuesdays & Thursdays, 1PM-3PM in [Evans](https://www.berkeley.edu/map?evans) 6

The full schedule is available on the [Schedule](http://www.data6.org/su22/schedule) page.

## Course Components	&#x1F4D2;
While this course is designed to fit into a six-week summer session, the pace of Data 6 over the summer is roughly twice as fast as the pace of a 4-unit class in the fall or spring semester. To compensate for the fast pace of the summer, we have more lectures and lab time than during the academic year. We do our best to make sure that we spend enough time on each concept, and that the material is approachable for all students.

Part of making sure that we're providing the best learning experience for you is checking in on your progress and getting feedback about the pace of the class. Each week, we will send out a survey asking for your feedback on how comfortable you are with the previous week's concepts and how we can better support you going forward. Responding to the weekly surveys constitutes 5% of your [final grade](https://data6.org/su22/syllabus/#grading), but the surveys are graded on completion. The surveys will be anonymous and we encourage you to be honest about how you're feeling and how you're doing in the class so we can better support you.

All of the course components (lectures, labs, discussions, homeworks, office hours, and quizzes/exams) are designed to provide valuable learning experiences and help you master core concepts in data science and computing.      

### Lecture
There will be four lectures per week. n lecture, we’ll introduce you to new ideas and concepts in programming and data science. Lectures will be recorded and posted after class for you to review in the future. All lecture resources (slides, code, supplemental readings) will be linked on the course website. We will begin on Berkeley Time (10 minutes after the hour), and **attendance is mandatory**.

During each lecture, there will be a few points at which we stop and ask you to answer a short question. We call these questions Quick Checks. They serve two purposes:
* For us to get a gauge of how well the class understands the material we’re currently covering
* For you to get a gauge of how well you understand the material we’re currently covering

**Quick Checks are graded on completion, not correctness**. It’s not important to get these questions right on your first try – but it’s important to try them. You will be given time in lecture to answer them. If you have to miss a lecture for whatever reason, just answer that lecture’s Quick Check whenever you catch up on the lecture.

Additionally, in some lecture notebooks, we will post optional practice problems. These are not required, but we recommend that you complete them.

### Lab
There are two lab sections per week that follow immediately after the Tuesday and Thursday lectures. In lab, we’ll spend the first ~10 minutes going over some demos that are relevant to that week’s material. You'll spend the remaining ~40 minutes working on the lab notebook that is available on the course website. Lab notebooks will give you an opportunity to apply the concepts you learn in lecture to real-world data and to practice coding in Python. While working on lab notebooks is required, **the notebooks themselves are not graded** — so don't worry if you don't finish the full notebook by the end of the lab.

Lab notebooks are also great opportunities to work on problems with your peers. The hope is that by participating and collaborating during labs, you will be able to better understand the concepts and finish your homework more quickly. **Discussing questions and approaches to problems with classmates is highly encouraged**, but please note that you must always write your own answers and code in your jupyter notebooks, both on labs and homeworks.

### Discussion

### Homework


### Office Hours and Ed

### Quizzes and Exams

This course does not have a midterm. Instead

## Communication	&#x1F4AC;

This class **does not** use bCourses — all of the materials and assignments for the class can be found on the Data 6 website.

For class communication, we will be using Ed Discussion (or simply “Ed,” as we will call it), the campus’ discussion platform. Ed is where you will see announcements from course staff, ask questions about course material, and get help from staff and other students on assignments and concepts. Ed allows students to respond to questions from other students, so we hope you will help out your classmates by responding to questions you have the answer to, or asking questions about things you’re confused about. It’s likely that other students have many of the same questions as you! Please review the Ed etiquette guidelines before posting on Ed.

You will be added to Ed automatically, but email James ([jweichert@berkeley.edu](jweichert@berkeley.edu)) if you’re not sure how to access it.


## Technology &#x1F4BB;

We will be using several websites this semester. Here’s what they’re all used for:
* [Course Website](http://www.data6.org/su22): where all content and assignments will be posted.
* [Ed](https://edstem.org/us/courses/22794/discussion/): discussion forum where all announcements will be sent, and where all student-staff and student-student communication will occur.
* [DataHub](http://datahub.berkeley.edu/): we use DataHub to host jupyter notebook assignments. Don’t worry too much about how this works, just access all assignments by clicking the link on the Data 6 website.
* [Gradescope](https://www.gradescope.com/courses/402405): where all homeworks will be submitted and all grades will live. (We don’t use bCourses)

Since all Data 6 material is accessible online, there are no requirements in terms of specific computer hardware. All you need is a laptop with internet and a web browser (Google Chrome or Firefox tend to work best). If you looking to purchase a laptop for college, Prof. Yan put together this [helpful guide](https://docs.google.com/document/d/1avUDkT5yvW_XycvVYP9LevJP791a9CdxuCAzQB1tYfc/edit?usp=sharing).

Here are a few helpful resources when it comes to technology:
* Read this [Berkeley IT website](https://technology.berkeley.edu/wi-fi) to learn how to connect to the campus WiFi network, Eduroam.
* The [Student Technology Equity Program](https://technology.berkeley.edu/STEP) provides free laptop loans for students.

## Policies &#x1F4D1;

### Grading

Here's how we will calculate your final grade:

| **Component** | **Weight** | **Notes** |
| Participation | 15% | Participation in lecture, labs, and discussions |
| In-Class Quick Checks | 5% | Graded on completion, no drops |
| Weekly Surveys | 5% | Graded on completion, no drops |
| Homeworks | 40% | 5 homeworks with 1 homework drop (10% each) |
| Quizzes | 20% | 2 quizzes (10% each) |
| Final Exam | 15% | In-Class on 8/12 |

### Late Policy and Extensions

### Academic Honesty

### A Note on Letter Grades

## Accommodations	&#x1F91D;

## Acknowledgements 🙏

The Summer 2022 version of Data 6 is based on [Data 94](http://data94.org/), created and taught by [Suraj Rampure](https://rampure.org/) in Spring 2021 at UC Berkeley, and the Summer 2021 version of [Data 6](http://data6.org/su21/), taught by Ian Castro and Isaac Merritt. Data 6 and Data 94 are loosely based on Data C6, taught by Ian Castro in Summer 2020 at UC Berkeley, which in turn was based on Data 8R, taught by Henry Milner in Summer 2017, also at UC Berkeley. These classes were based on [Data 8](http://data8.org/) at UC Berkeley.

For Summer 2022, Professors [Lisa Yan](https://www2.eecs.berkeley.edu/Faculty/Homepages/yanlisa.html) and [Deborah Nolan](https://statistics.berkeley.edu/people/deborah-nolan) have updated some of the curriculum and assignments, with help from Will Furtado, Kevin Miao and James Weichert.

When creating Data 6, we've referred to the materials of several other courses:

- [Data 8](http://data8.org), [CS 10](http://cs10.org), and [CS 61A](http://cs61a.org) at UC Berkeley
- [CS 106A](http://cs106a.stanford.edu) at Stanford
- [CSE 160](https://courses.cs.washington.edu/courses/cse160/) at the University of Washington

---

The website uses [Just the Class](https://kevinl.info/just-the-class/).
