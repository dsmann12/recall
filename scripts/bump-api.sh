#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Usage: ./scripts/bump-api.sh <patch|minor|major>"
  exit 1
fi

# Save the repo root directory
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO_ROOT/api"

# Get current version
CURRENT_VERSION=$(uv version --short)

# Bump version using uv
uv version --bump $1

# Get new version
NEW_VERSION=$(uv version --short)

echo "Bumping API version: $CURRENT_VERSION → $NEW_VERSION"

# Return to repo root for git operations
cd "$REPO_ROOT"

# Commit and tag
git add api/pyproject.toml api/uv.lock
git commit -m "bump(api): $CURRENT_VERSION → $NEW_VERSION"
git tag "api-v$NEW_VERSION"

echo "✅ API bumped to $NEW_VERSION and tagged as api-v$NEW_VERSION"
echo "Run 'git push --follow-tags' to push changes"