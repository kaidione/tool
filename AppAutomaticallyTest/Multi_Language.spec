# -*- mode: python ; coding: utf-8 -*-
import sys
import os.path as osp
sys.setrecursionlimit(5000)

block_cipher = None

SETUP_DIR = "D:\\pythonEnvironment\\pycharm\\AppAutomaticallyTest\\"
a = Analysis(
    ['Multi_Language.py',
    'D:\\pythonEnvironment\\pycharm\\AppAutomaticallyTest\\testCase\\Test_Multi_Language_win.py',
    'D:\\pythonEnvironment\\pycharm\\AppAutomaticallyTest\\base\\basePage_win.py',
    'D:\\pythonEnvironment\\pycharm\\AppAutomaticallyTest\\common\\data_util.py',
    'D:\\pythonEnvironment\\pycharm\AppAutomaticallyTest\\common\\PowerShell.py',
    'D:\\pythonEnvironment\\pycharm\AppAutomaticallyTest\\pageObjects\\jump_to_page_win.py'
    ],
    pathex=["D:\\pythonEnvironment\\pycharm\\AppAutomaticallyTest\\"],
    binaries=[],
    datas=[
    (SETUP_DIR+'common','common'),
    (SETUP_DIR+'config','config'),
    (SETUP_DIR+'data','data'),
    (SETUP_DIR+'testCase','testCase'),
    (SETUP_DIR+'report','report'),
    (SETUP_DIR+'temps','temps')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['zmq'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Multi_Language',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Multi_Language',
)
