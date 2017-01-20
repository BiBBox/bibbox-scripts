#! /bin/bash

if [[ "$setup" != "done" ]]; then
	python3 "$bibboxdir/$bibboxscriptfolder/setup-liferay/scripts/main.py"
fi