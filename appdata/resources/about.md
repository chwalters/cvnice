# About

## A NiceGUI Portfolio App for Jobseekers

CVNice (ResumeNice) is a web application for jobseekers that has three main functions:

1. Create and edit a resume/CV based on [jsonresume.org](https://jsonresume.org) schema
   (import and export JSON, create PDF)

2. Create and track job offers by simply pasting content, using
[Gemini](https://ai.google.dev/gemini-api/docs/models/gemini) AI analysis to parse the 
job offer and stores it. The user can 'apply'  which will create a custom CV/resume and a cover 
letter (cover letter drafted by the AI).  These can be submitted to the hiring manager.

3. Allows use of custom document templates which will be rendered as either PDF or 
docx (templates must be in a format supported by [carbone.io](https://carbone.io)

## Why?

This is a portfolio application for Chris Walters (@chwalters) and Harry Long (@harrylong96).

Chris and Harry are developers and interested to apply new technology to showcase their 
skills using the latest tools, including AI, for potential employers and customer contracts.

## Technologies Used
We decided to use [NiceGUI](https://nicegui.io) which is a [Python](https://www.python.org) library that
allows developers to create rich, functional websites without directly writing
[Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

Under the hood, [NiceGUI](https://nicegui.io) is using [Quasar](https://quasar.dev), a
[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) based framework. 

[NiceGUI](https://nicegui.io) was used to create the frontend elements. For backend, 
we used [Pydantic](https://docs.pydantic.dev/latest/) for data validation,
[FastAPI](https://fastapi.tiangolo.com) to work in conjunction with
[BasicLingua](https://github.com/FareedKhan-dev/basiclingua-LLM-Based-NLP) which is 
a [Gemini](https://ai.google.dev/gemini-api/docs/models/gemini) AI based API 
for particular instructional tasks. 

For our database we chose to use [Supabase](https://supabase.com) as it was suitable for the size and use-case of the project.

We're using [carbone.io](https://carbone.io) for PDF and DOCX document generation.

For analytics, we have used [Posthog](https://posthog.com) and [sentry.io](https://sentry.io) for crash reporting.

## Terms and Conditions

This site is not guaranteed to work as a production service and is for education,
demonstration and hopefully is useful to you.

## Open Source - Contributor Covenant Code of Conduct

### Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

### Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

### Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at walters@cvnice.com

All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

### Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

#### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

#### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

#### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

#### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.