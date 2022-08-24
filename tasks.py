from invoke import task

@task
def play(c):
    c.run("python3 src/play.py", pty=True)

@task
def test(c):
    c.run("pytest", pty=True)

@task
def coverage(c):
    c.run("coverage run --branch -m pytest", pty=True)
    c.run("coverage html", pty=True)