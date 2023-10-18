


section .data

	firstMsg db "Ingrese un numero: "
	len1 equ $ - firstMsg
	secondMsg db "La solucion es: "
	len2 equ $ - secondMsg
	i dq 0
	solution dq 0
	char dq 0

section .text
	global _start


_start: 
	mov rax, 1
	mov rdi, 1
	mov rsi, firstMsg
	mov rdx, len1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, i
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

inicio_programa:
	xor rax, rax
	xor rcx, rcx
	mov rbx, [i]
	sub rbx, 30H
	xor r8, r8

loop_suma:
	inc rcx
	mov rax, rcx
	mul rax
	xor rdx, rdx
	add r8, rax
	cmp rcx, rbx
	jne loop_suma



imprime_num:
	mov [solution], r8
	xor r9, r9
	xor rdx, rdx
	mov rbx, 10
	mov rax, r8

guarda_pila:
	div rbx
	push rdx
	xor rdx, rdx
	inc r9
	cmp rax, 0
	jne guarda_pila

imprime:

	mov rax, 1
	mov rdi, 1
	mov rsi, secondMsg
	mov rdx, len2
	syscall


saca_imprime:
	pop rbx
	add rbx, 30H
	mov [solution], rbx


    mov rax, 1
    mov rdi, 1
    mov rsi, solution
    mov rdx, 1
    syscall

	dec r9
	cmp r9, 0
	jne saca_imprime

final:
	mov rax, 1
	mov rdi, 1
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, 60
	mov rdi, 0
	syscall












