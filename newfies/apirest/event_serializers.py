# -*- coding: utf-8 -*-

#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from rest_framework import serializers
from appointment.models.events import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    **Create**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type:application/json" -X POST --data '{"name": "myrule", "frequency": "YEARLY", "params": "1"}' http://localhost:8000/rest-api/event/

        Response::

            HTTP/1.0 201 CREATED
            Date: Fri, 14 Jun 2013 09:52:27 GMT
            Server: WSGIServer/0.1 Python/2.7.3
            Vary: Accept, Accept-Language, Cookie
            Content-Type: application/json; charset=utf-8
            Content-Language: en-us
            Allow: GET, POST, HEAD, OPTIONS

    **Read**:

        CURL Usage::

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/rest-api/event/

            curl -u username:password -H 'Accept: application/json' http://localhost:8000/rest-api/event/%event-id%/

        Response::

            {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [
                    {

                    }
                ]
            }

    **Update**:

        CURL Usage::

            curl -u username:password --dump-header - -H "Content-Type: application/json" -X PATCH --data '{"name": "mylittle phonebook"}' http://localhost:8000/rest-api/event/%event-id%/

        Response::

            HTTP/1.0 200 NO CONTENT
            Date: Fri, 23 Sep 2011 06:46:12 GMT
            Server: WSGIServer/0.1 Python/2.7.1+
            Vary: Accept-Language, Cookie
            Content-Length: 0
            Content-Type: text/html; charset=utf-8
            Content-Language: en-us
    """
    creator = serializers.Field(source='creator')

    class Meta:
        model = Event

