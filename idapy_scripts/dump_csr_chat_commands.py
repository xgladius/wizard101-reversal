import idaapi
import idautils
import idc

table_glob_adr = idaapi.get_name_ea(0, "chat_command_global")
# goto any function that has a chat command, there will be a dword_whatever underneath the function that contains the string, name it chat_commmand_global
gen_xrefs = XrefsTo(table_glob_adr, 0)
for func_adr in gen_xrefs:
    f = func_adr.frm
    str_adr = idc.find_binary(f, SEARCH_UP, "48 8D 15")
    real_str_adr = str_adr + ida_bytes.get_wide_dword(str_adr + 3) + 7
    print(ida_bytes.get_strlit_contents(real_str_adr, -1, ida_nalt.STRTYPE_C))
