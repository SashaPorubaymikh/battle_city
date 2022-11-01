# -*- mode: python -*-

block_cipher = None


a = Analysis(['Tanks.py', 'Blocks.py', 'Boom.py', 'Bullet.py', 'Controls.py', 'dead.py', 'Dynamite.py', 'Enemy.py', 'flag.py', 'Friend.py', 'Levels.py', 'menu.py', 'Player.py', 'pyganim.py', 'status_bar.py', 'timer.py'],
             pathex=['E:\\Tanks\\Battle_city'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='Tanks',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Tanks')
