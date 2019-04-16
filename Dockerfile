FROM heroku/miniconda

# Grab requirements.txt.
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

RUN conda install scikit-learn

RUN conda install numpy

RUN conda install pandas