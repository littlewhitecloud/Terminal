from ctypes import Structure, c_int

WS_THICKFRAME = 0x00040000
WS_VISIBLE = 0x10000000


GWL_STYLE, GWL_EXSTYLE = -16, -20


class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth", c_int),
        ("cxRightWidth", c_int),
        ("cyTopHeight", c_int),
        ("cyBottomHeight", c_int),
    ]
