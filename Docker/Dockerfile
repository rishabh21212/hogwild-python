FROM python:3.6.3

RUN python3.6 -m pip install pip --upgrade

COPY src /hogwild-python/src/
COPY setup.py /hogwild-python/

RUN cd /hogwild-python/ && python3.6 -m pip install -e . --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
