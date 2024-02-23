import ctypes

atributo_ocultar = 0x02

returns = ctypes.windll.kernel32.SetFileAttributesW('hidden.txt', atributo_ocultar)

if returns:
    print('File hidden!')
else:
    print('File not hidden!')