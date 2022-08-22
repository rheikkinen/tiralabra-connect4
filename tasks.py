from invoke import task

@task
def play(c):
    c.run("poetry run python3 src/play.py")

@task
def test(c):
    c.run("poetry run pytest")

@task
def coverage(c):
    c.run("poetry run coverage run --branch -m pytest")
    c.run("poetry run coverage html")