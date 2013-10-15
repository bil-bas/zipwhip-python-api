
==================
Zipwhip Python API
==================

Thank you for expressing interest in the Zipwhip API for Python.

Zipwhip offers are a range of tools and support to transform your idea or
business into a texting reality.Texting is powerful high-priority medium,
one that offers prime real estate on cell phones all across the globe.

Using the Zipwhip API:
Zipwhip uses Java internally, but we are accessible by all languages.
Recently, we began creating a Python API to access Zipwhip. We use it quite
a bit in our Arduino projects around the office.

Want a few extra tools programmed for you, we offer our Java api publicly,
used by all of our Java projects. As time goes on we will be releasing
additions to our Python Library. We will be providing Parsers, Data Store
implementation, and Zipwhip specific data objects.

Once you know how to send a message, save some contacts and conversations
your going to want to start receiving messages from your
loyal coworkers/consumers.

We offer a few different ways for you to receive messages.
1. You can bind into our socket server and receive messages, contact, and
     conversation changes.
2. Short Polling, you choose the interval only query when it is important
     to you.
3. Webhooks, have a service hosted already and want to augment it with text.
     We can get you set with Webhooks, our server will automatically POST to
     your server with the changes to your account.

If at any point you have a question about the API provided please reach out to
api@zipwhip.com.

Basic Usage
===========
    #!/usr/bin/env python

    from ZipwhipApi.calls.WebCalls import WebCalls

    zipwhipClient = WebCalls()

    jsonResponse = zipwhipClient.log_in(username="8559479447",
                                        password="&qYDgGyT[q[62T>TrG^]")

    {
        "response": "8ef1211f-d9f2-4c81-906f-7d27da5a32f8:309626613",
        "success": "true"
    }

    jsonResponse = zipwhipClient.messsage_send(
                        session_key="8ef1211f-d9f2-4c81-906f-7d27da5a32f8:309626613",
                        recipient="ptn:/8559479447",
                        message_body="Hello World, from Zipwhip's Python Api!")

    {
      "response": {
        "fingerprint": "4236521183",
        "root": "327559093363723008",
        "tokens": [
        {
          "contact": 1989548603,
          "device": 309626613,
          "fingerprint": "42336654183",
          "message": "327545678963723008"
        }
        ]
      },
      "success": "true"
    }