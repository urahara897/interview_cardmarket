#!/bin/bash

# Manual semantic release trigger script
# This can be used to manually create a release if the automated workflow fails

echo "Triggering manual semantic release..."

# Install semantic release tools
npm install -g semantic-release
npm install -g @semantic-release/changelog
npm install -g @semantic-release/git
npm install -g conventional-changelog-conventionalcommits

# Configure Git
git config --global user.name "Automated Release System"
git config --global user.email "release-automation@github.com"

# Create semantic release config
cat > .releaserc.json << 'EOF'
{
  "branches": ["main"],
  "plugins": [
    ["@semantic-release/commit-analyzer", {
      "preset": "conventionalcommits",
      "releaseRules": [
        {"type": "feat", "release": "minor"},
        {"type": "fix", "release": "patch"},
        {"type": "perf", "release": "patch"},
        {"type": "revert", "release": "patch"},
        {"type": "docs", "release": false},
        {"type": "style", "release": false},
        {"type": "chore", "release": false},
        {"type": "refactor", "release": "patch"},
        {"type": "test", "release": false},
        {"type": "build", "release": "patch"},
        {"type": "ci", "release": false}
      ]
    }],
    ["@semantic-release/release-notes-generator", {
      "preset": "conventionalcommits",
      "writerOpts": {
        "commitsSort": ["subject", "scope"],
        "commitPartial": "**{{type}}:** {{subject}} {{#if scope}}*{{scope}}*{{/if}}"
      }
    }],
    ["@semantic-release/changelog", {
      "changelogFile": "CHANGELOG.md"
    }],
    "@semantic-release/github",
    ["@semantic-release/git", {
      "assets": ["CHANGELOG.md"],
      "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
    }]
  ]
}
EOF

# Run semantic release
echo "Running semantic release..."
npx semantic-release --debug

echo "Release process completed!"
