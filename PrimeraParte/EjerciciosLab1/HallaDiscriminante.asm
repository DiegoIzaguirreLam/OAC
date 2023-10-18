

section .data
	firstMsg db "Ingrese los numeros: "
	len1 equ $ - firstMsg
	secondMsg db "La solucion es: "
	len2 equ $ - secondMsg
	negativo db "-"
	len3 equ $ - negativo

	a dq 0
	b dq 0
	c dq 0
	char dq 0
	solution dq 0

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
	mov rsi, a
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, b
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, c
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, [b]
	sub rax, 30H

	mul rax
	xor rdx, rdx

	mov r8, rax


	mov rax, [a]
	sub rax, 30H
	mov rcx, [c]
	sub rcx, 30H

	mul rcx
	mov rcx, 4
	mul rcx
	xor rdx, rdx

	cmp r8, rax
	sub r8, rax
	mov [solution], r8

	mov rax, 1
	mov rdi, 1
	mov rsi, secondMsg
	mov rdx, len2
	syscall
evalua_negativo:
	jge imprime
	;imprime el simbolo - para negativo
	mov rax, 1
	mov rdi, 1
	mov rsi, negativo
	mov rdx, len3
	syscall

	mov rax, -1
	mul r8
	xor rdx, rdx
	mov [solution], rax

imprime:;pushea en pila el resultado digito por digito
    xor rcx, rcx
    mov r8, 10
    mov rcx, [solution]
    xor rbx, rbx
    xor rdx, rdx

division:; para imprimir el numero con cantidad de digitos desconocida, guardaremos digito a digito en la pila y los iremos sacando 
    mov rax, rcx
    cmp rax, r8 ;si el numero es de 1 digito (<10, almacenado en r8) entonces sale del bucle
    jl aux
    
    ;despues del div, rdx: residuo y rax: cociente
    div r8 ; saca el menor digito y lo guarda en la pila (esto solo se ejecuta cuando ya se sabe que el numero es de mas de 1 digito)
    inc rbx
    push rdx;rdx contiene el residuo al dividir el numero entre 10
    
    mov rcx, rax
    jmp division

aux:
    push rax
    inc rbx ; rbx almacena el numero de digitos de la solucion, para luego saber cuantos numeros hay que retirar de la pila


loopprint:
    cmp rbx, 0 
    je final
    dec rbx 
    pop rcx

    add rcx, 30H ; hallamos el valor ASCII del numero para imprimirlo (numero equivalente para el caracter)
    mov [solution], rcx ; movemos el numero que vamos a imprimir a solution

    mov rax, 1
    mov rdi, 1
    mov rsi, solution
    mov rdx, 1
    syscall
    jmp loopprint

    mov r8, 10
    mov [char], r8
final:
	mov rax, 1
	mov rdi, 1
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, 60
	mov rdi, 0
	syscall


