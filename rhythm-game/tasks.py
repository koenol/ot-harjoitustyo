from invoke import task
from subprocess import call
from sys import platform
import sys

def pty_status():
    if sys.platform != 'win32':
        return True
    else:
        return False

@task
def start(ctx):
    ctx.run("python src/index.py", pty=pty_status())

@task
def test(ctx):
    ctx.run("pytest src", pty=pty_status())

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=pty_status())

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty_status())
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))