# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['./main.py'],
             binaries=[],
             datas=[('./icon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          [],
          name='WTF_Folder_AutoSaver',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_environ={'TCL_LIBRARY': 'tcl', 'TK_LIBRARY': 'tk'},
          icon='icon.ico',
          console=False,)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               runtime_tmpdir=None,
               console=False,
               icon='icon.ico'
               )
