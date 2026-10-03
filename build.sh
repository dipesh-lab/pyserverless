#!/bin/bash

echo "Install poetry export plugin"
poetry self add poetry-plugin-export
echo "Poetry export plugin installed"


rm -rf build/lambda
mkdir -p build/lambda

echo "Export to requirement.txt file"
poetry export --without dev --format requirements.txt --output build/requirements.txt

python3.14 -m pip install \
  --requirement build/requirements.txt \
  --target build/lambda \
  --platform manylinux2014_x86_64 \
  --implementation cp \
  --python-version 3.14 \
  --only-binary=:all:

cp -a src/* build/lambda/

cd build/lambda

read -r NAME VERSION <<< "$(poetry version --no-ansi)"
echo "Build name ${NAME} and version ${VERSION}"
zip -r "../${NAME}.zip" . -x '**/__pycache__/*' '**/*.pyc'