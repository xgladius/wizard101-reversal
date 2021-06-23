import idaapi
import idautils
import idc

call_sendevent_adr = idc.find_binary(0, SEARCH_DOWN, "E8 ? ? ? ? 90 EB 63")
call_offset = ida_bytes.get_wide_dword(call_sendevent_adr + 1) + 5
sendevent_adr = call_sendevent_adr + call_offset

for func_adr in XrefsTo(sendevent_adr, 0):
    f = func_adr.frm
    
    if ida_bytes.get_wide_byte(f - 9) == 0xD3: # this means the argument is passed non statically
        continue
    
    str_adr = idc.find_binary(f, SEARCH_UP, "48 8D 15")
    if str_adr == 0xffffffffffffffff:
        continue
        
    real_str_adr = str_adr + ida_bytes.get_wide_dword(str_adr + 3) + 7
    print(ida_bytes.get_strlit_contents(real_str_adr, -1, ida_nalt.STRTYPE_C))
