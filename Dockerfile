FROM python:3
COPY ./test.py  /py/
WORKDIR /py/
CMD ["python3" ,"./test.py"] 
