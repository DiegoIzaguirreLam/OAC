;rdi = arr
;rsi = ini
;rdx = falt
;rcx = X

	global asmLlenaIniFalt
	section .text

asmLlenaIniFalt:
	xor r8, r8 ;r8 = contador
	sub rcx, 2
loop_llena:
	mov ebx, [rdi + 4*r8]
	mov r15, rdx
	jmp es_Primo
	primo:
		mov rdx, r15
		mov dword [rsi + 4*r8], 1
		mov dword [rdx + 4*r8], 0
		jmp actualiza_Falt
	no_primo:
		mov rdx, r15
		mov dword [rsi + 4*r8], 0
		mov dword [rdx + 4*r8], 0
	sigue_loop:
	inc r8
	cmp r8, rcx
	jne loop_llena

fin:
	ret

es_Primo:
	mov r12, 2
	loop_primo:
		cmp r12, rbx
		je primo
		mov rax, rbx
		xor rdx, rdx
		div r12
		cmp rdx, 0
		je no_primo
		inc r12
		jmp loop_primo

actualiza_Falt:
	xor r12, r12
	xor rax, rax
	xor r13, r13
	loop_falt:
		cmp r12, r8
		je sigue_loop
		mov eax, [rsi + 4*r12]
		cmp eax, 0
		jne sigue_loop_falt
		mov eax, [rdx + 4*r12]
		cmp eax, 0
		jne sigue_loop_falt
		mov eax, [rdi + 4*r12]
		mov r13d, ebx
		sub r13d, eax
		mov dword [rdx + 4*r12], r13d
		sigue_loop_falt:
		inc r12
		jmp loop_falt

