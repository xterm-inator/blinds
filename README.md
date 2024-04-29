# Automated Blinds using Rollease Acmeda V1 Controller

This project is designed to automate blinds built with Rollease Acmeda hardware. Using the V1 Controller and Slack Workspace, you can easily control your blinds with simplified commands.

## Setup
### Hub
Once started it should automatically find the hub if it is on the same local subnet.
### Slack
A Slack app needs to be created in your workspace.

Go to https://api.slack.com/apps and create an app.

Then edit the new app and create an App-Level Token with `connections:write` scope.

Copy the token and set SLACK_APP_TOKEN environment variable with it.

Next in the app settings enable Socket Mode.

Then in the app Features OAuth & Permissions copy the Bot User OAuth Token and set SLACK_BOT_TOKEN to that.

### App

**Docker Compose:**

```yml
services:
  blinds:
    image: ghcr.io/xterm-inator/blinds:latest
    container_name: blinds
    restart: always
    network_mode: "host"
    environment:
      - SLACK_BOT_TOKEN=xapp-
      - SLACK_APP_TOKEN=xoxb-
```

### Blinds
The blinds on the hub will need to be named 'Blind 1' with each blind having a different number

## Usage

Once everything has been set up then slack should be able to be used to control your blinds.

**Slack Commands:**

`/blinds 1 up` move blind 1 up

`/blinds 1 down` move blind 1 down

`/blinds 1 2 up/down` move listed blinds up or down 

`/blinds all up/down` move all blinds up or down 

`/blinds all 70` move all blinds to {0-100}% closed 

## Contributing
Contribute to this project by submitting a pull request or issue on GitHub. All bug reports, feature suggestions, and code enhancements from the community are welcome.
