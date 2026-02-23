meta:
  environment: python
  toolchain:
    name: pip
    version: 3.11
build:
  requirementsPath: requirements.txt
run:
  script: python app.py
  containerPort: 80
