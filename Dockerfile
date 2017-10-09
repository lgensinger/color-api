# use an official python runtime as parent image
FROM python

# copy needed directories into container
ADD . /

# install pythong requirements
RUN cd scripts && pip install -e .

# make port available to the world outside this container
EXPOSE 5000

# run api
CMD ["python", "app/app.py"]