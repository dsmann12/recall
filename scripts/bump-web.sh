#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Usage: ./scripts/bump-web.sh <patch|minor|major>"
  exit 1
fi

# Save the repo root directory
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO_ROOT/web"

# Get current version
CURRENT_VERSION=$(npm pkg get version | tr -d \")

# Bump version using npm
npm version $1 --no-git-tag-version

# Get new version
NEW_VERSION=$(npm pkg get version | tr -d \")

echo "Bumping WEB version: $CURRENT_VERSION → $NEW_VERSION"

# Return to repo root for git operations
cd "$REPO_ROOT"

# Commit and tag
git add web/package.json web/package-lock.json
git commit -m "bump(web): $CURRENT_VERSION → $NEW_VERSION"
git tag "web-v$NEW_VERSION"

echo "✅ WEB bumped to $NEW_VERSION and tagged as web-v$NEW_VERSION"
echo "Run 'git push --follow-tags' to push changes"