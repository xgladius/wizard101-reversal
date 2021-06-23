import idaapi
import idautils
import idc

error_sprintf_func = idc.find_binary(0, SEARCH_DOWN, "4C 8B DC 48 83 EC 58")

for func_adr in XrefsTo(error_sprintf_func, 0):
    f = func_adr.frm
    str_adr = idc.find_binary(f, SEARCH_UP, "48 8D 05")
    if str_adr == 0xffffffffffffffff:
        continue
    real_str_adr = str_adr + ida_bytes.get_wide_dword(str_adr + 3) + 7
    name_str = ida_bytes.get_strlit_contents(real_str_adr, -1, ida_nalt.STRTYPE_C)
    idc.set_name(idc.get_func_attr(str_adr, idc.FUNCATTR_START), name_str, idc.SN_NOCHECK)
    
