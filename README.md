# django-modeltranslation-sync

This package contains two scripts to convert translated database fields to Portable Object file (.po) and back. The idea is to get all translated string from database to translation systems like Transifex or Lingui. Required packages are ``django`` and ``django-modeltranslation``. 

## Installation

1. Install the package::
    
    pip install django-modeltranslation-sync
    
2. Add ``modeltranslation_sync`` to ``INSTALLED_APPS``
3. Add the following to your ``settings.py``:
    	
	MODELTRANSLATION_LOCALE_PATH = "path.to.modeltrans.locale"
    MODELTRANSLATION_PO_FILE = "filename.po"


## Usage

To convert translated model fields to .po file use the following command:

	$ python manage.py save_trans

To load translated strings to database use the following command:

	$ python manage.py load_trans

## Licence

The MIT License (MIT)

Copyright (c) 2015 djentlemen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
