# Provenance and reorganization

Original repository: [TannerGilbert/Tutorials](https://github.com/TannerGilbert/Tutorials)  
Original author: Gilbert Tanner  
Snapshot reorganized: `d5e25a0f182a7a396dd2c9a8c3248134070fab0e`  
License: MIT; the original `LICENSE` file is unchanged.

## Changes in this fork

- Moved 162 existing tutorial files into topic folders under `tutorials/`.
- Kept the original filenames and relative layouts inside each topic.
- Removed 24 generated files under `.vs/`, `bin/` and `obj/`.
- Preserved notebooks, source, datasets, trained model assets and illustrative media byte for byte.
- Replaced the root README with an attributed catalog.
- Retained the original root README as `UPSTREAM_README.md`.
- Expanded ignore rules for Python environments, editor state and .NET build output.

The move and removal record is [reorganization.json](reorganization.json). It retains each file's original path and Git blob SHA, allowing exact integrity checks. Removed generated files remain in Git history.

## Scope of review

The full 189-file inventory was classified. The 133 readable teaching files (including notebook source cells) were inspected. Datasets, images and model binaries were retained by their original blob hashes; no new model validation or data-content audit was performed.

This is a curated reference collection. It is not presented as a new implementation or industrial deployment.
