#Nirvaris Pages

A simple Django app to add pages to your website.

You add them via django admin interface and they will be avaliable in your website.

- [Nirvaris Default Theme](https://github.com/nirvaris/nirvaris-theme-default)
- [Nirvaris Profile](https://github.com/nirvaris/nirvaris-profile)

A requirements file is provided with some other dependencies from PyPi.

#Quick start

To install the Pages, use pip from git:

```
pip install git+https://github.com/nirvaris/nirvaris-pages
```

- Your INSTALLED_APPS setting should look like this::

```
    INSTALLED_APPS = (
        ...,
        'n_profile',
        'themedefault',
        'pages',
    )
```

- You have to run migrate, as it uses the db to store the pages content and meta-tags. 

- you have to add the url to your urls file:  ```url(r'^page/', include('pages.urls'))```

- You can access the page on your website by ```<your-url>/pages/<relative_url>```, relative_url is a page field you set when you add a page via Django admin

- The layout of the page will follow the theme.
