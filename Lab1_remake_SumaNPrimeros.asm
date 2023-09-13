

section .data 
	pregunta db "Ingrese un numero para n: "
	len1 equ $ - pregunta
	respuesta db "La solucion es: "
	len2 equ $ - respuesta
	number dq 0
	solution dq 0

section .text
	global _start



_start:
	mov rax, 1
	mov rdi, 1
	mov rsi, pregunta
	mov rdx, len1
	syscall


	mov rax, 0
	mov rdi, 0
	mov rsi, number
	mov rdx, 1
	syscall

	mov rcx, [number]
	SUB rcx, 30H

	xor r9, r9
	loop:
		mov rax, rcx
		MUL rax
		add r9, rax
		dec rcx
		cmp rcx, 0
		je fin_loop
		jmp loop

	fin_loop:
	mov rax, 1
	mov rdi, 1
	mov rsi, respuesta
	mov rdx, len2
	syscall

	mov r8, 10
	xor rbx, rbx
	mov rax, r9
	;pusheo todo a la pila
	pushea_pila:
	xor rdx, rdx
	div r8
	push rdx
	inc rbx
	cmp rax, 0
	jne pushea_pila


	saca_pila:
	pop r8
	add r8, 30H
	mov [solution], r8
	mov rax, 1
	mov rdi, 1
	mov rsi, solution
	mov rdx, 1
	syscall
	dec rbx
	cmp rbx, 0
	jne saca_pila


;SYS_EXIT
	mov rax, 60
	mov rdi, 0
	syscall





