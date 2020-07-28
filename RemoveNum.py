def remove_num_from_str(instr) :
    outstr = ""

    for i in instr :
        if not i.isdigit() :
            outstr += i

    return outstr

if __name__ == __main__ :
    testStr = input('문자열 입력 : ')
    remove_num_from_str(testStr)
