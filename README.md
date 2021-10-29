# Home Assistant Desktop Reicever

The goal is to provide a

home-assistant-desktop-reciever is a small autostarting daemon that runs in the user session of a linux desktop.

Currently it only uses the rest APIs of HA, so no changes are needed there.

Whilst most of this would be possible with a lot of manual setup via the command line switches and ssh, this is easier to set up, more extensible and more secure.

It should work on all standard Linux desktops; GNOME, KDE/Plasma, XFCE, whatever that follows the standards

Forked from: davidedmundson/home-assistant-desktop-receiver

## What it provides

* Notification receiver. HA notifications appear as normal desktop notifications

* A binary "sensor" of whether the computer is not just on, but actually active (not locked and activity within the past n minutes). Useful for automation

* A switch for dpms (screen management)

## Non-goals

I don't intend for this to be a GUI desktop client. There's not a lot of code overlap

## Setup

Create notify device in Home Asssitant:
```
notify:
    - name: Linux-Desktop
      platform: rest
      resource: http://IPADDRESS/FQDN:8124/notifications
```

Put the ip/fqdn of the computer where you want to recvieve the notifications/run the python script.
**Be careful to no end the "resource:" with a /, it will not work as it is right now.**

Run the python

## Testing
For testing go to Developer tools, services, go to YAML mode.
```
service: notify.linux_desktop
data:
  message: Test messages
```

## Plans

* Replace with MQTT

* Updating HA state directly via web API (means we need to know HA location and auth)

* Make it discoverable on the HA side.
