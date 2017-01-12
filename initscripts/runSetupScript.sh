#! /bin/bash

if [[ "$bibboxdir" != "done" ]]; then
	python3 "$bibboxdir/$bibboxscriptfolder/setup-liferay/scripts/main.py"
fi