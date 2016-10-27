#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An example of merging dictionaries using built-in update function."""

import data

data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                                  'Stevie Nicks': ['vocals', 'tambourine']}
data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
