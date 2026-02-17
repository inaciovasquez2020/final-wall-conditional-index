#!/usr/bin/env bash
set -e
FILE="docs/yang-mills/vasquez-reduction-yang-mills.tex"
grep -q "Conditional" "$FILE"
grep -q "No proof" "$FILE"
grep -q "No claim" "$FILE"
