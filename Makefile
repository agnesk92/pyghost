tests:
	docker run -ti pyghost-ubuntu:v2.0 pytest --doctest-modules .
	docker run -ti pyghost-ubuntu:v2.0 pytest

