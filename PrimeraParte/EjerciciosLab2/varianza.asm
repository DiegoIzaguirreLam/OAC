;rdi = arr
;rsi = n

	global asmCalculaVar
	section .text

asmCalculaVar:
	
	xor r8, r8
	xorpd xmm3, xmm3
	xorpd xmm4, xmm4
	cvtsi2ss xmm5, rsi

loop_media:
	movss xmm1, [rdi+4*r8]
	addss xmm3, xmm1
	inc r8
	cmp r8, rsi
	jne loop_media

divide_media:
	divss xmm3, xmm5
	xor r8, r8

loop_var:
	movss xmm1, [rdi+4*r8]
	subss xmm1, xmm3
	mulss xmm1, xmm1
	addss xmm4, xmm1
	inc r8
	cmp r8, rsi
	jne loop_var

divide_var:
	divss xmm4, xmm5
	movss xmm0, xmm4
	ret


