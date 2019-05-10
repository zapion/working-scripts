# support only slackclient ~=1.0

from slackclient import SlackClient
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-c", "--channel", help="choose channel", dest="channel")
parser.add_argument("-m", "--message", help="message to send", dest="message")
parser.add_argument("-f", "--file", help="file to send", dest="file_upload")

args = parser.parse_args()

TOKEN = ""  # need a valid api token
CHANNEL = ""
MESSAGE = ""
FILE = ""

if args.message:
    MESSAGE = args.message

if args.channel:
    CHANNEL = args.channel

if args.file_upload:
    FILE = args.file_upload

client = SlackClient(TOKEN)

if MESSAGE:
    ret = client.api_call('chat.postMessage',
                          channel=CHANNEL,
                          text=MESSAGE,
                          )

if os.path.isfile(FILE):
    CONTENT = open(FILE, mode='r', encoding="utf-8").read()
    ret = client.api_call('file.upload',
                          channel=CHANNEL,
                          title="db-diff-hourly",
                          mode="snippet",
                          content=CONTENT,
                          filename=args.file_upload,
                          )
