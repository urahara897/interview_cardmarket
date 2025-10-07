# Semantic Release Configuration

This file explains how the `.releaserc.json` file works for automated releases.

## Configuration Overview

The `.releaserc.json` file controls how semantic release works. Here's what each part does:

### Branch Configuration

```json
"branches": ["main"]
```

- Only creates releases from the `main` branch
- Other branches won't trigger releases

### Plugin 1: Commit Analyzer

```json
"@semantic-release/commit-analyzer"
```

- Analyzes commit messages to decide what type of release to make
- Uses conventional commits format (feat:, fix:, etc.)

#### Release Rules:

- `feat:` → Minor release (1.0.0 → 1.1.0) - New features
- `fix:` → Patch release (1.0.0 → 1.0.1) - Bug fixes
- `perf:` → Patch release - Performance improvements
- `revert:` → Patch release - Reverting changes
- `refactor:` → Patch release - Code refactoring
- `build:` → Patch release - Build system changes
- `docs:` → No release - Documentation changes
- `style:` → No release - Code style changes
- `chore:` → No release - Maintenance tasks
- `test:` → No release - Test changes
- `ci:` → No release - CI/CD changes

### Plugin 2: Changelog Generator

```json
"@semantic-release/changelog"
```

- Automatically updates the `CHANGELOG.md` file
- Groups changes by type and version
- Writes to: `CHANGELOG.md`

### Plugin 3: GitHub Release

```json
"@semantic-release/github"
```

- Creates releases on GitHub
- Adds version tags
- Publishes release notes

### Plugin 4: Git Committer

```json
"@semantic-release/git"
```

- Commits changes back to repository
- Includes changelog in the commit
- Uses message: `chore(release): ${nextRelease.version} [skip ci]`
- `[skip ci]` prevents infinite loops

## How It Works

1. **Commit Analysis**: Looks at commits since last release
2. **Version Decision**: Decides patch/minor/major based on commit types
3. **Changelog Update**: Updates `CHANGELOG.md` with new changes
4. **GitHub Release**: Creates release with version tag
5. **Git Commit**: Commits changelog changes back to repo

## Example Commits

### Will Create Releases:

```bash
git commit -m "feat: add user login"        # → Minor release
git commit -m "fix: bug fix"                # → Patch release
git commit -m "perf: improve speed"         # → Patch release
```

### Will NOT Create Releases:

```bash
git commit -m "chore: cleanup code"         # → No release
git commit -m "docs: update readme"         # → No release
git commit -m "test: add tests"             # → No release
```

### Won't Be Recognized:

```bash
git commit -m "random message"              # → No release
git commit -m "add stuff"                   # → No release
```
