FROM python:3.12

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

COPY --chown=user . ./app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# RUN python3 -m venv /app/.venv

# RUN source .venv/bin/activate
# RUN .venv/bin/activate

# ENV PATH="/.venv/bin:$PATH"

RUN python manage.py collectstatic --noinput

RUN pip install uvicorn
CMD ["uvicorn", "setup.asgi:application", "--host", "0.0.0.0", "--port", "7860"]

# ENTRYPOINT ["python", "manage.py", "runserver"]

# CMD ls /usr/lib/python3.12/site-packages/Lib/site-packages
# CMD pip freeze