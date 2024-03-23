import os
import asyncio

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import aiopulse


hub: aiopulse.hub
event_loop: asyncio.AbstractEventLoop
rollers = {}

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.command('/blinds')
def control_blinds(ack, respond, command):
    global rollers, event_loop, hub
    ack()

    cmd = command['text'].split()
    print(cmd)
    action = 'up'
    roller_names = []

    for idx, c in enumerate(cmd):
        if idx == len(cmd) - 1:
            action = c
            break

        if c == 'all':
            for roller in hub.rollers.values():
                roller_names.append(roller.name)
            continue

        roller_names.append(f"Blind {c}")
    print(rollers)
    for name in roller_names:
        print(f"Move {name} {action}")
        r = rollers[name]
        if action == 'up':
            event_loop.create_task(r.move_up())
        elif action == 'down':
            event_loop.create_task(r.move_down())
        else:
            event_loop.create_task(r.move_to(int(action)))


async def find_hub():
    global hub
    async for found_hub in aiopulse.Hub.discover():
        hub = found_hub

    hub.callback_subscribe(hub_callback)
    print(hub)


async def hub_callback(update_type):
    global rollers
    print(f"Hub {update_type.name} updated")
    if update_type.name == 'rollers':
        for roller in hub.rollers.values():
            rollers[roller.name] = roller


async def main():
    global hub, event_loop, rollers
    event_loop = asyncio.get_running_loop()

    await find_hub()

    if hub is None:
        return

    event_loop.create_task(hub.run())

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).connect()

    while True:
        await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
