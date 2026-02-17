#!/usr/bin/env bash
set -e

FILE="docs/yang-mills/vasquez-reduction-yang-mills.tex"

grep -q "Conditional" "$FILE" || {
  echo "ERROR: Conditional language missing"
  exit 1
}

grep -q "No proof" "$FILE" || {
  echo "ERROR: Explicit no-proof disclaimer missing"
  exit 1
}

grep -q "No claim" "$FILE" || {
  echo "ERROR: Explicit no-claim language missing"
  exit 1
}

echo "Conditional disclaimer check passed."

