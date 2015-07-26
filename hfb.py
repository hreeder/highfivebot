#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from pircel import bot

logger = logging.getLogger(__name__)


def high_five(server_handler, who_from, to, message):
    logger.debug('Got message: %s', message)
    send = server_handler.channels[to].send_message
    if '\o/' in message:
        send('\o/')
    elif 'o/' in message:
        send('\1ACTION \1')
    elif '\o' in message:
        send('o/')


def join_on_invite(server_handler, who_from, who, channel):
    if who == server_handler.identity.nick:
        server_handler.channels[channel].join()


def main():
    irc_bot = bot.IRCBot.from_default_args(nick='\o')

    irc_bot.server.add_callback('privmsg', high_five)
    irc_bot.server.add_callback('invite', join_on_invite)

    # setup logging
    log_level = logging.DEBUG if irc_bot.args.debug else logging.INFO
    log_date_format = "%Y-%m-%d %H:%M:%S"
    log_format = "%(asctime)s\t%(levelname)s\t%(module)s:%(funcName)s:%(lineno)d\t%(message)s"
    logging.basicConfig(level=log_level, format=log_format, datefmt=log_date_format)
    logging.captureWarnings(True)

    irc_bot.main()

if __name__ == '__main__':
    main()
