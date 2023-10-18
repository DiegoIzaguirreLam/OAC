;rdi = arr
;rsi = ini
;rdx = falt
;rcx = N
;r8 = X

	global funcion_asm
	section .text

funcion_asm:
	xor r9, r9
	xor r12, r12
	sub r8, 2

loop_funcion:
	mov eax, [rdi + 4*r9]
	mov r10, rdx
	jmp es_Primo

	primo:
		mov rdx, r10
		mov dword [rsi + 4*r9], 1
		mov dword [rdx + 4*r9], 0
		jmp marcaAnteriores
		sigue_primo:
		mov r12, r9
		jmp sigue_loop
	no_primo:
		mov rdx, r10
		mov dword [rsi + 4*r9], 0
		mov dword [rdx + 4*r9], 0
	sigue_loop:
	inc r9
	cmp r9, r8
	jne loop_funcion

final_loop:
	dec r8 ; ahora es X-2
	dec rcx

loop_llena:
	mov dword [rsi + 4 * r8], 0 
	mov dword [rdx + 4 * r8], 0
	inc r8
	cmp r8, rcx
	jne loop_llena

fin:
	ret


es_Primo:
	mov r11d, 2
	mov r13d, eax
	loop_primo:
		mov eax, r13d
		cmp r11d, r13d
		je primo 
		xor rdx, rdx
		div r11d
		cmp edx, 0
		je no_primo
		inc r11d
		jmp loop_primo

marcaAnteriores:
	mov r11, r12

loop_marca:
	cmp r11, r9
	je sigue_primo
	mov eax, [rsi + 4*r11]
	cmp eax, 0
	jne sigue_marca
	maraca:
	mov ebx, [rdi + 4*r9]
	mov eax, [rdi + 4*r11]
	sub ebx, eax
	mov [rdx + 4*r11], ebx
	sigue_marca:
	inc r11
	jmp loop_marca
