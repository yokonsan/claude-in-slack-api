import asyncio
from os import getenv

from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
CLAUDE_BOT_ID = getenv("CLAUDE_BOT_ID")


class SlackClient(AsyncWebClient):

    CHANNEL_ID = None
    LAST_TS = None

    async def chat(self, text):
        if not self.CHANNEL_ID:
            raise Exception("Channel not found.")

        resp = await self.chat_postMessage(channel=self.CHANNEL_ID, text=text)
        print("c: ", resp)
        self.LAST_TS = resp["ts"]

    async def open_channel(self):
        if not self.CHANNEL_ID:
            response = await self.conversations_open(users=CLAUDE_BOT_ID)
            self.CHANNEL_ID = response["channel"]["id"]

    async def get_reply(self):
        for _ in range(150):
            try:
                resp = await self.conversations_history(channel=self.CHANNEL_ID, oldest=self.LAST_TS, limit=2)
                print("r: ", resp)
                msg = [msg["text"] for msg in resp["messages"] if msg["user"] == CLAUDE_BOT_ID]
                if msg and not msg[-1].endswith("Typing…_"):
                    return msg[-1]
            except (SlackApiError, KeyError) as e:
                print(f"Get reply error: {e}")

            await asyncio.sleep(1)

        raise Exception("Get replay timeout")

    async def get_stream_reply(self):
        l = 0
        for _ in range(150):
            try:
                resp = await self.conversations_history(channel=self.CHANNEL_ID, oldest=self.LAST_TS, limit=2)
                msg = [msg["text"] for msg in resp["messages"] if msg["user"] == CLAUDE_BOT_ID]
                if msg:
                    last_msg = msg[-1]
                    more = False
                    if msg[-1].endswith("Typing…_"):
                        last_msg = str(msg[-1])[:-11] # remove typing…
                        more = True
                    diff = last_msg[l:]
                    l = len(last_msg)
                    yield diff
                    if not more:
                        break
            except (SlackApiError, KeyError) as e:
                print(f"Get reply error: {e}")

            await asyncio.sleep(2)

client = SlackClient(token=getenv("SLACK_USER_TOKEN"))

if __name__ == '__main__':
    async def server():
        await client.open_channel()
        while True:
            prompt = input("You: ")
            await client.chat(prompt)

            reply = await client.get_reply()
            print(f"Claude: {reply}\n--------------------")

    asyncio.run(server())
