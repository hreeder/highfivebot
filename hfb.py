#!/usr/bin/env python
# -*- coding: utf8 -*-
import logbook
from tornado import ioloop

from possel import irc

loopinstance = ioloop.IOLoop.instance()
logger = logbook.Logger(__name__)


def high_five(server_handler, who_from, to, message):
    logger.debug('Got message: {}', message)
    send = server_handler.channels[to].send_message
    if '\o/' in message:
        send('\o/')
    elif 'o/' in message:
        send('\1ACTION \1')
    elif '\o' in message:
        send('o/')


def join_channel(server_handler, who_from, who, channel):
    if who == server_handler.identity.nick:
        server_handler.channels[channel].join()


def main():
    args = irc.get_parsed_args()

    line_stream, server_handler = irc.get_attached_instances(args)

    irc.connect(args, line_stream, server_handler)

    server_handler.add_callback('privmsg', high_five)
    server_handler.add_callback('invite', join_channel)

    loghandler = logbook.StderrHandler(level=logbook.DEBUG if args.debug else logbook.INFO)

    with loghandler.applicationbound():
        loopinstance.start()

if __name__ == '__main__':
    main()
