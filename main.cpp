#include <iostream>
#include "hashfunction.h"
#include <string.h>
#include <sstream>

using namespace std;


extern "C"
unsigned int * gethashcode(char * cstr)
{
    // Output the hello world text
    unsigned int len = (unsigned int) strlen(cstr);
    const unsigned char * un_cstr = (const unsigned char * ) (cstr);
    unsigned int * hashcodes = new unsigned int[16];
    hashcodes[0] = Hsieh(un_cstr, len);
    hashcodes[1] = RSHash(un_cstr, len);
    hashcodes[2] = JSHash(un_cstr, len);
    hashcodes[3] = BKDR(un_cstr, len);
    hashcodes[4] = DJBHash(un_cstr, len);
    hashcodes[5] = DEKHash(un_cstr, len);
    hashcodes[6] = APHash(un_cstr, len);
    hashcodes[7] = CRC32(un_cstr, len);
    hashcodes[8] = SDBM(un_cstr, len);
    hashcodes[9] = OCaml(un_cstr, len);
    hashcodes[10] = SML(un_cstr, len);
    hashcodes[11] = BOB3(un_cstr, len);
    hashcodes[12] = FNV32(un_cstr, len);
    hashcodes[13] = BOB4(un_cstr, len);
    hashcodes[14] = BOB1(un_cstr, len);
    hashcodes[15] = BOB2(un_cstr, len);
    return hashcodes;
}

int main()
//int main(char * str)
{
    char * input;
    cin >> input;
    // Output the hello world text
    //const char * hashcodes_str = gethashcode(input);
    //cout << hashcodes_str << endl;
    return 0;
}
