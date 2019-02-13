### GATEKEEPER
[Challenge Link](https://capturetheflag.withgoogle.com/?#beginners/re-gatekeeper)

#### Dynamic Analysis
		$ ./gatekeeper
		/===========================================================================\
		|               Gatekeeper - Access your PC from everywhere!                |
		+===========================================================================+
		[ERROR] Login information missing
		Usage: ./gatekeeper <username> <password>

		$ ./gatekeeper username password
		/===========================================================================\
		|               Gatekeeper - Access your PC from everywhere!                |
		+===========================================================================+
		 ~> Verifying....
		ACCESS DENIED
		 ~> Incorrect username

#### Debugging
- Username can be easily found: `0n3_W4rM`

		lea        rdi, qword [aVerifying] ; argument #1 for method text_animation, " ~> Verifying.", CODE XREF=main+43
		call       text_animation ; text_animation
		mov        edi, 0x3     ; argument #1 for method verify_animation
		call       verify_animation ; verify_animation
		mov        rax, qword [rbp+var_B0]
		add        rax, 0x8
		mov        rax, qword [rax]
		lea        rsi, qword [a0n3w4rm] ; argument "__s2" for method j_strcmp, "0n3_W4rM"
		mov        rdi, rax     ; argument "__s1" for method j_strcmp
		call       j_strcmp     ; strcmp
		test       eax, eax
		je         loc_a7b

- We need to find password

		$ ./gatekeeper 0n3_W4rM password
		/===========================================================================\
		|               Gatekeeper - Access your PC from everywhere!                |
		+===========================================================================+
		 ~> Verifying.......ACCESS DENIED
		 ~> Incorrect password

- in (`loc_a7b` --> `loc_b2a` --> `loc_ac8`)

		loc_ac8:
		mov        rdx, qword [rbp+var_10] ; CODE XREF=main+390
		mov        rax, qword [rbp+var_8]
		add        rax, rdx
		movzx      eax, byte [rax]
		mov        byte [rbp+var_11], al
		mov        rax, qword [rbp+var_10]
		mov        rdi, rax     ; argument "__s" for method j_strlen
		call       j_strlen     ; strlen
		sub        rax, qword [rbp+var_8]
		lea        rdx, qword [rax-1]
		mov        rax, qword [rbp+var_10]
		add        rax, rdx
		mov        rcx, qword [rbp+var_10]
		mov        rdx, qword [rbp+var_8]
		add        rdx, rcx
		movzx      eax, byte [rax]
		mov        byte [rdx], al
		mov        rax, qword [rbp+var_10]
		mov        rdi, rax     ; argument "__s" for method j_strlen
		call       j_strlen     ; strlen
		sub        rax, qword [rbp+var_8]
		lea        rdx, qword [rax-1]
		mov        rax, qword [rbp+var_10]
		add        rdx, rax
		movzx      eax, byte [rbp+var_11]
		mov        byte [rdx], al
		add        qword [rbp+var_8], 0x1

- in `loc_ac8`, it reverses the password argument through loop and 
- in the next step below, it compares it with `zLl1ks_d4m_T0g_I`

		mov        edi, 0x3     ; argument #1 for method verify_animation
		call       verify_animation ; verify_animation
		mov        rax, qword [rbp+var_10]
		lea        rsi, qword [aZll1ksd4mt0gi] ; argument "__s2" for method j_strcmp, "zLl1ks_d4m_T0g_I"
		mov        rdi, rax     ; argument "__s1" for method j_strcmp
		call       j_strcmp     ; strcmp
		test       eax, eax
		jne        loc_bba

- And we can easily find the password should be `I_g0T_m4d_sk1lLz`

		$ ./gatekeeper 0n3_W4rM I_g0T_m4d_sk1lLz
		/===========================================================================\
		|               Gatekeeper - Access your PC from everywhere!                |
		+===========================================================================+
		 ~> Verifying.......Correct!
		Welcome back!
		CTF{I_g0T_m4d_sk1lLz}
