from .simple_dwm_request import SimpleDwmRequest


class DwmRequests:
    # Request messages with an empty value
    dwm_pos_get = SimpleDwmRequest(0x02)
    dwm_upd_rate_get = SimpleDwmRequest(0x04)
    dwm_cfg_get = SimpleDwmRequest(0x08)
    dwm_sleep = SimpleDwmRequest(0x0A)
    dwm_loc_get = SimpleDwmRequest(0x0C)
    dwm_baddr_get = SimpleDwmRequest(0x10)
    dwm_reset = SimpleDwmRequest(0x14)
    dwm_ver_get = SimpleDwmRequest(0x15)
    dwm_status_get = SimpleDwmRequest(0x32)