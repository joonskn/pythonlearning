def gbv_result(com_choi,hu_choi,result_t,result_s):
    result_o = com_choi - hu_choi
    result_t.append(result_o)
    if result_o == -1 or result_o == 2:
        result_s.append(result_o)

def cal(result_t,result_s):
    rtlen = len(result_t)
    rslen = len(result_s)
    return (rslen/rtlen)*100

def fwp(cal):
    print(f'승률: {cal:.1f}%')

