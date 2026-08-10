# Public Portfolio Website

This is a generic version of my portfolio website.
It features GitHub API requests for public repositories and a contact form using Resend to send input data to a specific Email address.

## Preparing GitHub and Resend access tokens

Create a personal access token on GitHub. During installation, paste your key in the .env file.
Create an API Key on Resend. During installation, paste your key in the .env file.

## Setting up the GitHub API

Open github_api.py in the services directory, find the github_api_url variable and replace <yourusername> with your GitHub username.

## Completing Config

Open config.py in the base directory, find the MAIL_RECIPIENT variable and add the Email address you want to use for receiving the contact form Emails.

## Installation

**Install Base Dependencies**

```bash
sudo apt install -y python3 python3-venv python3-dev
sudo apt install -y supervisor nginx git
```

**Download the Repository to your Server**

```bash
git clone https://github.com/fionaeff/public_portfolio_website
```

**Create a Virtual Environment and Download the Dependencies**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Create an .env File in the Base Directory and add the required Variables**

```bash
SECRET_KEY=2344jkbb2kj34523563456lb
GITHUB_API_KEY=<yourkey>
RESEND_API_KEY=<yourkey>
```

To generate a random SECRET_KEY, use the following command:

```bash
python3 -c "import uuid; print(uuid.uuid4().hex)"
```

**Install Gunicorn**

```bash
pip install gunicorn
```

Start Gunicorn using the following command:
```bash
gunicorn -b localhost:8000 -w 4 public_portfolio_website:app
```

**Setting up Supervisor**

Open /etc/supervisor/conf.d/public_portfolio_website.conf and add the following:
```bash
[program:public_portfolio_website]
command=/home/user/public_portfolio_website/venv/bin/gunicorn -b localhost:8000 -w 4 public_portfolio_website:app
directory=/home/user/public_portfolio_website
user=user
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

Afterwards:
```bash
sudo supervisorctl reload
```

Set up Nginx, Certbot for SSL certificates and redirect your domain to the IP address of your server.

**Deploying Application Updates**

```bash
git pull
sudo supervisorctl stop public_portfolio_website
sudo supervisorctl start public_portfolio_website
```

# License

[MIT](https://choosealicense.com/licenses/mit/)