#!/bin/bash
# Unpack ../bundle.tgz (if present), narrate new/changed stories, rebuild the index.
set -e
cd "$(dirname "$0")/../.."
[ -f ../bundle.tgz ] && tar xzf ../bundle.tgz && mv ../bundle.tgz ../bundle.last.tgz
export KOKORO_DIR="$HOME/.cache/kokoro"
PY="$KOKORO_DIR/venv/bin/python"
for f in stories/src/*.py; do
  id=$(basename "$f" .py)
  case "$id" in build_story|make_index) continue;; esac
  if [ ! -f "stories/$id.json" ] || [ "$f" -nt "stories/$id.json" ]; then
    echo "narrating $id"; "$PY" stories/src/build_story.py "$f" stories > /tmp/story_$id.log 2>&1 || { echo "FAILED $id"; tail -5 /tmp/story_$id.log; }
  fi
done
"$PY" stories/src/make_index.py
