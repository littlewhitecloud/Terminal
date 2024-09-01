from ctypes import byref, windll

from constant import MARGINS

dwmapi = windll.dwmapi


def ExtendFrameIntoClientArea(hwnd, cxl, cxr, cxt, cxb) -> None:
    margins = MARGINS(cxl, cxr, cxt, cxb)
    dwmapi.DwmExtendFrameIntoClientArea(hwnd, byref(margins))
