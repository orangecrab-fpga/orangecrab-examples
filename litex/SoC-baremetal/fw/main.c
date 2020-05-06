#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <crc.h>
#include <stdint.h>
#include <stdbool.h>

#include <generated/csr.h>
#include <generated/mem.h>
#include <generated/git.h>



int main(int i, char **c)
{	

	printf("\n");

	printf("Hello from OrangeCrab! o/ \n");
 	printf("firmware built: "__DATE__ " " __TIME__ " \n\n");

 	printf("      Migen git sha1: "MIGEN_GIT_SHA1"\n");
 	printf("      LiteX git sha1: "LITEX_GIT_SHA1"\n");
 	printf("\n");
	
	return 0;
}
