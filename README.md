angular-dashboard-django
========================

A storage backend and demo for malhar-angular-dashboard. This allows you to save dashboards in Django. 
It uses the User model to remember dashboards per user. User must be logged in to work.

## Quick Demo with fig/Docker

1. `fig up`
2. Syncdb with `fig run --rm web ./manage.py syncdb --all`
3. Go to http://localhost:8000/angular_dashboard/demo/

## Integrate with existing django/angular application

1. Add `'angular_dashboard',` to INSTALLED_APPS
2. Add `url(r'^angular_dashboard/', include('angular_dashboard.urls')),` in urls.py
3. See /angular_dashboard/templates/angular_dashboard/dashboard.html and
/angular_dashboard/static/angular_dashboard/app.js for example of using it.
