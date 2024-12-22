import platform

block_cipher = None

a = Analysis(
    ["aa_watcher_window/__main__.py"],
    pathex=[],
    binaries=[("aa_watcher_window/aa-watcher-window-macos", "aa_watcher_window")] if platform.system() == "Darwin" else [],
    datas=[
        ("aa_watcher_window/printAppStatus.jxa", "aa_watcher_window"),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="aa-watcher-window",
    contents_directory=".",
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="aa-watcher-window",
)
