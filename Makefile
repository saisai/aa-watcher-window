.PHONY: build test package clean

build:
	poetry install
	# if macOS, build swift
	if [ "$(shell uname)" = "Darwin" ]; then \
		make build-swift; \
	fi

build-swift: aa_watcher_window/aa-watcher-window-macos

aa_watcher_window/aa-watcher-window-macos: aa_watcher_window/macos.swift
	swiftc $^ -o $@

test:
	aa-watcher-window --help

typecheck:
	poetry run mypy aa_watcher_window/ --ignore-missing-imports

package:
	pyinstaller aa-watcher-window.spec --clean --noconfirm

clean:
	rm -rf build dist
	rm -rf aa_watcher_window/__pycache__
	rm aa_watcher_window/aa-watcher-window-macos
