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

import pprint
import WebCalls

def tests():
    zipwhipClient = WebCalls()

    sessionKey="ccb65584-8507-43e0-b574-807923ddf46c:789432512"
    friendNumber="ptn:/4257772300"
    messageId="387978813489359552"

    #pprint.pprint(zipwhipClient.log_in(phone_number="80094794447", password="&qYDgGyT[q[62T>TrG^]"))

    pprint.pprint(zipwhipClient.user_get(session_key=sessionKey))

    pprint.pprint(zipwhipClient.contact_list(sessionKey, 1, 2))

    pprint.pprint(zipwhipClient.contact_save(sessionKey, friendNumber, "Seattle", "api@zipwhip.com",
                                             "Alan", "Capps", "", "Contact me for support", "WA"))

    #pprint.pprint(zipwhipClient.contact_delete(sessionKey, "2341863503"))

    pprint.pprint(zipwhipClient.conversation_list(sessionKey, 2, 0))

    pprint.pprint(zipwhipClient.conversation_get(sessionKey, "4233621183", 2, 0))

    #pprint.pprint(zipwhipClient.conversation_delete(sessionKey, "4233621183"))

    pprint.pprint(zipwhipClient.message_send(session_key=sessionKey,
                                             recipient=friendNumber,
                                             message_body="Hello World!\n\nSent via Zipwhip Api."))

    pprint.pprint(zipwhipClient.message_list(sessionKey, 2, 0))

    pprint.pprint(zipwhipClient.message_read(sessionKey, messageId))

    #pprint.pprint(zipwhipClient.message_delete(sessionKey, messageId))


# end tests()

def main():
    # Run all tests associated with Parser
    tests()
    #asdf
# end main()
main()