
;asmHallaDistancias(longi,lat,dist,cant,convert);
;rdi = longi
;rsi = lat
;rdx = dist
;rcx = cant
;xmm0 = convert


global asmHallaDistancias
	section .text


asmHallaDistancias:
	
	xorpd xmm3, xmm3
	xorpd xmm4, xmm4
	xor r8,r8 ; contador
	movss xmm1, [rdi]
	movss xmm2, [rsi]
	inc r8
loop:
	movss xmm3, [rdi + 4*r8]
	movss xmm4, [rsi + 4*r8]
	subss xmm3, xmm1
	subss xmm4, xmm2
	mulss xmm3, xmm3
	mulss xmm4, xmm4
	addss xmm3, xmm4
	sqrtss xmm3, xmm3
	mulss xmm3, xmm0
	movss [rdx + 4*r8 - 4], xmm3
	inc r8
	cmp r8, rcx
	jne loop
	ret

