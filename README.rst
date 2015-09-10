=====
Nirvaris Pages
=====

A simple Django app to add pages to your website.

you add them via django admin interface and they will be avaliable in your website.

Quick start
-----------

To install the Pages, use pip from git:

pip install git+https://github.com/nirvaris/nirvaris-pages

1. Add "pages" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'pages',
    )

2. You have to run makemigrations and migrate, as it uses the db to store the pages content and meta-tags. 

3. Copy the templates on the app's template folder to your application template folders
	These templates are used to render the pages. You should use them for your own style
	
4. You can access the page on your website by
	<your-url>/pages/<relative_url>
	
	relative_url is a page field you set when you add a page via django admin
	
5. you have to add the url to your urls file:  url(r'^page/', include('pages.urls')),