.. contents::

==============================
Inplace Edit Form Extra Fields
==============================

Information
===========

Inplace Edit Form Extra Field is a Django application that adds other useful fields.

It is distributed under the terms of the GNU Lesser General Public
License <http://www.gnu.org/licenses/lgpl.html>

Requeriments
============

 * `Django Inplace Edit <http://pypi.python.org/pypi/django-inplaceedit/>`_

And other eggs, but it is important: If you want to use one of the fields, you do not have to install its requirements

Installation
============

After installing `Django Inplace Edit <http://pypi.python.org/pypi/django-inplaceedit/#installation>`_

In your settings.py
-------------------

::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',

        #.....................#

        'inplaceeditform',
        'inplaceeditform_extra_fields',
    )

If you want overwrite the adaptors for any case in your project:

::

    ADAPTOR_INPLACEEDIT = {'textarea': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',
                           'image': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                           'fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
                           'm2mcomma': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField'}

If you want, you can register these fields in your settings, with other keys:

::

    ADAPTOR_INPLACEEDIT = {'auto_fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
                           'auto_m2m': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField',
                           'image_thumb': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                           'tiny': 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField',}

And after when you want use this specific adaptor you indicate it, e.g.:

::

   {% inplace_edit "content.field_name" adaptor="tiny" %}


Because these fields are not in django-inplaceedit
==================================================

 * They have dependece of the other eggs
 * They are a particular solution
 * Theese do not work immediately, you have to code them

AdaptorAutoCompleteForeingKeyField and AdaptorAutoCompleteManyToManyField
=========================================================================

These fields are dependent of `Django Ajax Select <http://pypi.python.org/pypi/django-ajax-selects/>`_. You have to create a channel (lookup)

::

    {% inplace_edit "content.field_name" adaptor="auto_fk", lookup="my_lookup" %}

For more info, visit the `doc of ajax select <https://github.com/twidi/django-ajax-select/blob/master/ajax_select/docs.txt#L101>`_

AdaptorImageThumbnailField
==========================

This field is dependent of `Sorl thumbnail <http://pypi.python.org/pypi/sorl-thumbnail/>`_. You only should indicate the size.

::

    {% inplace_edit "content.field_name" adaptor="image_thumb", size="16x16" %}

It can help you, configure in your settings:

::

    THUMBNAIL_DEBUG = True

AdaptorTinyMCEField
===================

This field is dependent of `cmsutils <http://pypi.python.org/pypi/cmsutils>`_.

::

    {% inplace_edit "content.field_name" adaptor="tiny" %}


Development
===========

You can get the leading edge version of inplaceedit-extra-fields by doing a checkout
of its repository:

  https://github.com/goinnn/django-inplaceedit-extra-fields
