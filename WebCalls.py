# Copyright (C) 2013 Zipwhip, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE

import urllib.parse
import urllib.request
import urllib.error
import json

class WebCalls(object):
    def __init__(self, base_url="http://network.zipwhip.com/"):
        """WebCalls provides a wrapper for all web calls currently available for
            Ziphip. Zipwhip Web Calls returns the json unparsed to the caller.

        Args:
            base_url, A String, the URL that will be used for making webcalls.
              This is most beneficial if you have a test environment setup
              with Zipwhip.
        """

        self.base_url = base_url
        # end init()

    def __post(self, url, uri, values):
        params = urllib.parse.urlencode(values)
        full_url = url + uri + "?%s" % params
        try: response = urllib.request.urlopen(full_url)
        except urllib.error.URLError as e:
            print(e)
            raise
        readResponse = response.read()
        data = readResponse.decode('utf-8')
        jsonResponse = json.loads(data)

        return jsonResponse
        # end post()

    def log_in(self, phone_number, password):
        """log_in takes a username and password and returns json with the
            account's session key. A sessionkey lasts forever, so it is
            best to store the sessionkey and use it for future purposes.

        Args:
            phone_number: A string, for US domestic use 10-digit number.
                For International numbers use full E.164 format.
            password: A string, password associated with phone number.

        Returns:
            json response:
            { "response": "8ef1211f-d9f2-4c81-906f-7d27da5a32f8:309626613",
              "success": true }
        """
        uri = "user/login"

        values = {'username' : phone_number,
                  'password' : password }

        return(self.__post(self.base_url, uri, values))
        # end log_in()

    def user_get(self, session_key):
        """user_get provides information about the logged in user or account
            associated with sessionKey passed in.

        Args:
            session_key: A String, the GUID representation of a logged in user.
                A sessionKey can be retrieved by calling log_in().

        Returns:
            json response:
            { "response":
                { "user":
                    { "firstName": "Zipwhip,"
                      "lastName": "Inc.",
                      "businessName": null,
                      "mobileNumber": "8559479447"
                      ...
        """

        uri = "user/get"

        values = {'session' : session_key}
        return(self.__post(self.base_url, uri, values))
        # end user_get()

    def contact_list(self, session_key, page=1, page_size=999):
        """contact_list provides a list of contacts associated with the account.

        Args:
            session_key, A String, the GUID representation of a logged in user.
            page, An int, reguested page of contacts, starts at page 1.
            page_size, An int, the number of contacts per page.

        Returns:
            json response:
            { "total": 2,
              "response": [{
              "address": "ptn:/2062164915",
              "birthday": null,
              "business": null,
              "carrier": "Zipwhip",
              ...

        """

        uri = "contact/list"

        values = {'session' : session_key,
                  'page' : page,
                  'pageSize' : page_size}
        return(self.__post(self.base_url, uri, values))
        # end contact_list()

    def contact_save(self, session_key, address, city=None, email=None, first_name=None, last_name=None,
                     loc=None, notes=None, state=None):
        """contact_save, saves the details of a contact

     Args:
         session_key, A String, the GUID representation of a logged in user.
         address, A String, the string representation of a phone number.
           Phone numbers will need to start with "ptn:/"
           US Domestic numbers will be a full 10 digit number.
           International numbers need to be in E.164 format.
         Optional:
         city, A String, takes the city in which the live.
         email, A String, their email address.
         first_name, A String, their first name.
         last_name, A String, their last name.
         loc, A String, their location.
         notes, A String, notes about them as a user.
         state, A String, the state that they live.

     Returns:
         json response:
         { "response": {
           "address": "ptn:/2069797487",
           "birthday": null,
           "business": null,
           "carrier": "ATT",
           ...
     """
        uri = "contact/save"

        values = {'session' : session_key,
                  'address' : address,
                  'city' : city,
                  'email' : email,
                  'firstName' : first_name,
                  'lastName' : last_name,
                  'loc' : loc,
                  'notes' : notes,
                  'state' : state}

        return(self.__post(self.base_url, uri, values))
        # end contact_save()

    def contact_delete(self, session_key, id):
        """contact_delete deletes a contact record by the given contactID
	
        Args:
            session_key, A String, the GUID representation of a logged in user.
            id, A String, the ID of a contact, can be looked up using contact/list

        Returns:
            json response:
            { "response": false,
              "success": true }
        """
        uri = "contact/delete"

        values = {'session' : session_key,
                  'contact' : id}

        return(self.__post(self.base_url, uri, values))
        # end contact_delete()

    def conversation_list(self, session_key, limit=999, start=0):
        """conversation_list provides a list of conversations associated with
            with the account.

        Args:
            session_key, A String, the GUID representation of a logged in user.
            limit, An Int, the number of results per page.
            start, An Int, the starting conversation.

        Response:
            json response:
            { "total": 2,
              "response": [{
              "address": "ptn:/2068308909",
              "bcc": null,
              "cc": null,
              "dateCreated": "2013-04-18T11:44:57-07:00",
              ...
        """
        uri = "conversation/list"

        values = {'session' : session_key,
                  'limit' : limit,
                  'start' : start}

        return(self.__post(self.base_url, uri, values))
        # end conversation_list()

    def conversation_get(self, session_key, id, limit=30, start=0):
        """conversation_get retreives conversation details and messages
		that specific to the conversation ID provided.
	
        Args:
            session_key, A String, the GUID representation of a logged in user.
            id, A String, the unique identifier for a conversation, can be
                obtained by doing a conversation_list.
            limit, An Int, the max number of messages to be returned per call.
            start, An Int, starting message for current request.

        Response:
            json response:
            { "response": {
              "conversation": {
              "address": "ptn:/3608964896",
              ...
              "messages": [{
              "address": "ptn:/3608964896",
              "advertisement": null,
              "bcc": null,
              "body": "Nada much.",
              ...
        """
        uri = "conversation/get"

        values = {'session' : session_key,
                  'fingerprint' : id,
                  'limit' : limit,
                  'start' : start}

        return(self.__post(self.base_url, uri, values))
        # end conversation_get()

    def conversation_delete(self, session_key, id):
        """conversation_delete deletes the conversation based on the provided
            id. It also deletes the associated messages.

        Args:
            session_key: A String, the GUID representation of a logged in user.
            id, A String, the unique identifier for a conversation, can be
                obtained by doing a conversation_list.

        Response:
            json response:
            { "response": true
              "success": true }
        """
        uri = "conversation/delete"

        values = {'session' : session_key,
                  'fingerprint' : id}

        return(self.__post(self.base_url, uri, values))
        # end conversation_delete()

    def message_list(self, session_key, limit=30, start=0):
        """message_list retreives messages for account. A start of 0 provides
            newest to oldest messages.

        Args:
            session_key, A String, the GUID representation of a logged in user.
            limit, An Int, the max number of messages to be returned per call.
            start, An Int, starting message for current request.

        Response:
            { "total": 2,
              "response": [{
              "address": "ptn:/2064122950",
              "advertisement": "\n\nSent via Zipwhip",
              "bcc": null,
              "body": " ffff",
              ...
        """
        uri = "message/list"

        values = {'session' : session_key,
                  'limit' : limit,
                  'start' : start}

        return(self.__post(self.base_url, uri, values))
        # end message_list()

    def message_send(self, session_key, recipient, message_body):
        """message_send sends a message from the logged in user's phone number.
		
        Args:
            session_key, A String, the GUID representation of a logged in user.
            receipient, A String, the string representation of a phone number.
              Phone numbers will need to start with "ptn:/"
              US Domestic numbers will be a full 10 digit number.
              International numbers need to be in E.164 format.
            message_body, A String, the message to be sent. Message bodies are
              limited to 160 bytes.

        Response:
            json response:
            { "response": {
              "fingerprint": "4236521183",
              "root": "327559093363723008",
              "tokens": [ {
              "contact": 1989548603,
              "device": 309626613,
              "fingerprint": "42336654183",
              "message": "327545678963723008" }]},
              "success": true
            }
        """
        uri = "message/send"

        values = {'session' : session_key,
                  'contacts' : recipient,
                  'body' : message_body}

        return(self.__post(self.base_url, uri, values))
        # end message_send()

    def message_read(self, session_key, id):
        """message_read marks the given message as read in Zipwhip's database.

        Args:
            session_key, A String, the GUID representation of a logged in user.
            id, A String, the unique identifier returned by message_send.

        Response:
            json response:
            { "response": false,
              "success": true }
        """
        uri = "message/read"

        values = {'session' : session_key,
                  'message' : id}

        return(self.__post(self.base_url, uri, values))
        # end message_read()

    def message_delete(self, session_key, id):
        """message_delete marks the given message as deletedd in Zipwhip's
            database.

        Args:
            session_key, A String, the GUID representation of a logged in user.
            id, A String, the unique identifier returned by message_send.

        Response:
            json response:
            { "response": false,
              "success": true }
        """
        uri = "message/delete"

        values = {'session' : session_key,
                  'message' : id}

        return(self.__post(self.base_url, uri, values))
        # end message_delete()
# end WebCalls