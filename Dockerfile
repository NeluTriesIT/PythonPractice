FROM python

COPY BasicExercises BasicExercises

COPY execute_all.py execute_all.py

RUN ls /home/

ENTRYPOINT ["python3", "execute_all.py"]

