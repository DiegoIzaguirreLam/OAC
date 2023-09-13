

section .data
	firstMsg db "La nota del alumno es: "
	len1 equ $ - firstMsg
	;arrNotas dq 13, 16, 20, 16, 13
	;numNotas dq 5
	arrNotas dq 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 12, 12, 15, 15, 17, 17, 18, 18, 19, 19, 20, 20
	numNotas dq 31
	solution dq 0

section .text
	global _start

_start:
	xor rcx, rcx
	xor r8, r8 ;lleva la cuenta
	mov rbx, [arrNotas] ;almacena el resultado parcial del xor
	inc r8 

loop_xor:
	cmp r8, [numNotas]
	jge fin_loop
	xor rbx, [arrNotas + 8*r8]
	inc r8
	jmp loop_xor

fin_loop:
	mov [solution], rbx
	mov rax, 1
	mov rdi, 1
	mov rsi, firstMsg
	mov rdx, len1
	syscall

;pushea en pila el resultado digito por digito
    xor rcx, rcx
    mov r8, 10
    mov rcx, [solution]
    mov rbx, 0
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

final:
;sys_exit
	mov rax, 60
	mov rdi, 0

