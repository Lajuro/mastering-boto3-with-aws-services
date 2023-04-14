# FIRST STEPS

In order to create these projects, you will need the following required tools:

- [FIRST STEPS](#first-steps)
  - [Python 3.6 or higher](#python-36-or-higher)
  - [AWS CLI](#aws-cli)
  - [Boto3 (Python library)](#boto3-python-library)
  - [AWS account](#aws-account)
  - [IAM user with the right permissions](#iam-user-with-the-right-permissions)

## Python 3.6 or higher

You can download Python from the [official website](https://www.python.org/downloads/).

## AWS CLI

You can download AWS CLI from the [official website](https://aws.amazon.com/cli/).

## Boto3 (Python library)

You can install Boto3 with pip:

```bash
pip install boto3
```

In my case, as I prefer to use virtual environments, I installed it with env:

```bash
python -m venv .venv
source .venv/bin/activate

pip install boto3
```

> **Warning**
> If you use Bash, it will work properly, but for PowerShell and CMD you will need to use the following command:

```bash
python -m venv .venv

# PowerShell
.venv\Scripts\Activate.ps1

# CMD
.venv\Scripts\activate.bat
```

## AWS account

You can create an AWS account from the [official website](https://aws.amazon.com/).

## IAM user with the right permissions

You can create an IAM user from the [official website](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

In order to get the `ACCESS_KEY` and `SECRET_KEY`, you can follow this article on Medium: [Installing and Configuring the AWS CLI](https://medium.com/@simonazhangzy/installing-and-configuring-the-aws-cli-7d33796e4a7c).
