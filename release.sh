#!/bin/bash

poetry version patch
# read -r NAME VERSION <<< "$(poetry version --no-ansi)"
# git tag -a ${VERSION} -m "Release version ${VERSION}"
# echo "Release name ${NAME} and version ${VERSION}"
echo "Release version applied"
./build.sh
echo "Release complete"
next=$(poetry version minor --dry-run --short)
echo "Update next development version to ${next}"
poetry version "${next}.dev"