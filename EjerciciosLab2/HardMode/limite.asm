;rdi = n

	global asmFuncion
	section .text

asmFuncion:
	mov r8, 1
	cvtsi2sd xmm3, r8
	movsd xmm1, xmm3
	cvtsi2sd xmm2, rdi
	divsd xmm1, xmm2
	addsd xmm1, xmm3 ; xmm1 = x
	movsd xmm0, xmm3 ;xmm0 = res
	mov r8, rdi

potencia_n:
	sar r8, 1 ;hago el shift a la derecha
	jb multiplica
	sigue:
	mulsd xmm1, xmm1
	cmp r8, 0
	jne potencia_n

final:
	ret

multiplica:
	mulsd xmm0, xmm1
	jmp sigue

