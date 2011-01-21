# Automates several buildout tasks
# http://ircubic.net/2009/11/portable-django-project-with-buildout.html

.DEFAULT_GOAL = development
.PHONY = development clean

bootstrap.py :
	curl -O http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

bin/buildout : bootstrap.py
	python bootstrap.py

development : bin/buildout
	./bin/buildout

clean :
	rm -rf bin develop-eggs eggs parts .installed.cfg downloads bootstrap.py *.egg-info