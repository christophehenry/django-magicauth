# Django Magicauth

Django Magicauth brings password-less authentication to your project.

*How it works*

 - The user inputs their email address.
 - An email is sent to the user with a link that contains a one-time token.
 - Once they click on this link, they are logged in to the service.

For a detailed step-by-step with screenshots of the default templates, see #Step-by-step-in-pictures.

## Fonctionnement (FR)

Authentifiez vos utilisateurs sans mot de passe avec Django Magicauth.

*Comment ça marche*

 - Les utilisateurs renseignent leur adresse email.
 - Ils reçoivent alors un email avec un lien de connexion.
 - Lorsqu'ils cliquent sur le lien, ils sont authentifiés et redirigés sur le service.

Pour un détail du fonctionnement en image, voir #Step-by-step-in-pictures.


# Installations and testing instructions

## Quick start

1. Install Magicauth
```sh
pip install git+https://github.com/betagouv/django-magicauth.git
```

2. Add "magicauth" to your INSTALLED_APPS in `settings.py`
```python
INSTALLED_APPS = [
    # all your apps
    "magicauth",
]
```

2. Include the magicauth URLconf in your app's `url.py`
```python
# After your previous imports
from magicauth import views as magicauth_views
from magicauth.urls import urlpatterns as magicauth_urls

urlpatterns = [
    # here are your URL patterns
]

urlpatterns.extend(magicauth_urls)
```

3. Add the following items in your project's settings.py`

```
MAGICAUTH_FROM_EMAIL = 'contact@mysite.com'
MAGICAUTH_LOGGED_IN_REDIRECT_URL_NAME = 'home'
```

4. Run `python manage.py migrate` to create the polls models.

5. Setup your [mailer](https://docs.djangoproject.com/en/2.2/topics/email/#console-backend) in `settings.py`
In dev mode, you can use a [console mailer](https://docs.djangoproject.com/en/2.2/topics/email/#console-backend)

6. Make sure you have the following middlewares
```
MIDDLEWARE = [
    # [...] other middleware you may have
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]
```

## Contribute to Magicauth

To contribute to Magicauth, you can install the package in the "editable" mode

```
pip uninstall django-magicauth  # just in case...
pip install -e git+https://github.com/betagouv/django-magicauth.git#egg=django-magicauth
```

You can also install a specific branch, for instance for testing a PR. To install branch `my-branch`:

```
pip install -e git+https://github.com/betagouv/django-magicauth.git@my-branch#egg=django-magicauth
```

Django-magicauth is now a dependency of your project, and you can edit the code located here:

```
cd src/django-magicauth
```

### run tests

Create a virtual env for the project or reuse one and source it.

Install dependencies and run `tox`

```
cd src/django-magicauth
pip install -r requirements.txt
tox
```

# Step-by-step in pictures

Note : the screenshots below use the default templates, which don't look very nice. It is expected that you replace them with your own better-looking ones.

Step 1 : the user goes to the login page. (see `LoginView` in `magicauth/views.py`)

<kbd><img src="https://user-images.githubusercontent.com/911434/86135682-74ed2180-baeb-11ea-9d0c-cd18d05857c7.png" /></kbd>


Step 2 : The user inputs their email address in the login page.

<kbd><img src="https://user-images.githubusercontent.com/911434/86130756-efff0980-bae4-11ea-8df7-9fe183a6d5dd.png" /></kbd>


Step 3 : The user sees a confirmation page (`EmailSentView`), explaining that an email has been sent.

<kbd><img src="https://user-images.githubusercontent.com/911434/86130765-f2f9fa00-bae4-11ea-88b9-c74e2b791fff.png" /></kbd>

An email is sent to the user with a link that contains a one-time token.

<kbd><img src="https://user-images.githubusercontent.com/911434/86136856-d6fa5680-baec-11ea-833f-696968cb762f.png" /></kbd>


The link looks something like this :

<kbd><img src="https://user-images.githubusercontent.com/911434/86130775-f8574480-bae4-11ea-9158-a06cdcb29e8b.png" /></kbd>


Step 4 : once they click on the button and follow the link, the user is directed to a wait page (this is optional) (`WaitView`)

<kbd><img src="https://user-images.githubusercontent.com/911434/86130782-fbeacb80-bae4-11ea-8d7e-4ff9a42ae5ed.png" /></kbd>

Step 5 : the user is logged in to the service (`ValidateTokenView`) and redirected to the landing page.

<kbd><img src="https://user-images.githubusercontent.com/911434/86133987-5be37100-bae9-11ea-844a-97ba5de5722d.png" /></kbd>

