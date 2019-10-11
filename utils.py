from sty import fg, bg, ef, rs

def pretty_menu(lst,horizontal=True):
    st = ""
    for item in lst:
        st += fg.da_white + "["
        st += fg.li_green + item['key']
        st += fg.li_yellow + item['data']
        st += fg.da_white + "] "
        st += fg.li_white + item['desc'] + " "
    print (st)
