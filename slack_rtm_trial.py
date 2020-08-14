# https://medium.com/@ritikjain1272/how-to-make-a-slack-bot-in-python-using-slacks-rtm-api-335b393563cd
import os
import datetime
import subprocess
from slack import RTMClient

TOKEN = "YOUR_TOKEN"
job_name = "YOURJOB"
bot_name = "BOTNAME"
notify_list = ['user1', 'user2']
lock_file = f"/tmp/{job_name}.lock"
OCCUPIED = False
TARGET_SCRIPT = "SCRIPT_PATH"


@RTMClient.run_on(event="message")
def saku_cmd_listner(**payload):
    data = payload['data']
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    notifiers = " ".join(notify_list)

    if bot_id == "":
        user = data.get("user", "")
        channel_id = data['channel']
        print("from channel: {}".format(channel_id))

        text = data.get("text", "")
        print("text:\n{}".format(text))
        ts = int(data['ts'].split('.')[0])
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(f"timestamp: {timestamp}")
        # text = text.split(">")[-1].strip()

        response = ""
        if "help me erinnnn" in text.lower():
            response = f"hi <@{user}>!"
        elif job_name in text and bot_id in text:
            if os.path.exists(lock_file):
                # dont do anything if lock exists
                # TODO: send slack and mention it's another restore job
                with open(lock_file, mode='r') as lf:
                    content = lf.readlines()
                    launch_by = content[0].split(":")[1].strip()
                    start_time = content[1].split(":")[1].strip()
                msg = f"Sorry, user <@{launch_by}> {job_name} in progress... start from {start_time}"
                print(msg)
                web_client.chat_postMessage(
                    channel=user,
                    text=msg,
                    username=bot_name,
                )
                return
            else:
                try:
                    global OCCUPIED
                    OCCUPIED = True
                    web_client.chat_postMessage(
                        channel=channel_id,
                        link_names=1,
                        text=f"{notifiers} start to process {job_name}",
                        username=bot_name,
                    )
                    with open(lock_file, mode='w') as lf:
                        lf.write(f"launch by: <@{user}>\n")
                        lf.write(f"datetime : {timestamp}\n")
                    restore_script = TARGET_SCRIPT
                    proc = subprocess.Popen(["bash", restore_script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    while proc.returncode is None:
                        for line in iter(proc.stdout.readline, " "):
                            msg = line.decode('utf8')
                            if not msg:
                                break
                            print(msg)
                            web_client.chat_postMessage(
                                channel=user,
                                text=msg,
                                username=bot_name,
                            )
                        os.sleep(30)
                        proc.poll()
                    print("return code: {}".format(proc.returncode))
                except Exception as e:
                    print(f"Exception found: {e}")
                finally:
                    OCCUPIED = False
                    os.remove(lock_file)
                if proc.returncode == 0:
                    print("done restore")
                    response = f"<@{user}> well done. {job_name} successfully"
                else:
                    response = f"<@{user}> something wrong when {job_name}. Please check private message for detail"
        else:
            response = str("dummy")
            return

        web_client.chat_postMessage(
            channel=channel_id,
            # channel=user,
            text=response,
            username=bot_name,
        )


try:
    rtm_client = RTMClient(token=TOKEN)
    print("Bot is up and running")
    rtm_client.start()
except Exception as e:
    print("error:")
    print(e)
finally:
    if OCCUPIED:
        os.remove(lock_file)
