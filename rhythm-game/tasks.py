from invoke import task
from subprocess import call
from sys import platform

@task
def start(ctx):
    ctx.run("python src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))