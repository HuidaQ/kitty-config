import getpass
import re
import socket

from kitty.fast_data_types import Color
from kitty.tab_bar import as_rgb
from kitty.utils import color_as_int


LOCAL_USER = getpass.getuser()
LOCAL_HOST = socket.gethostname().split(".", 1)[0]
LOCAL_PREFIX_RE = re.compile(
    rf"^(?:{re.escape(LOCAL_USER)}@)?{re.escape(LOCAL_HOST)}(?::\s*)?"
)

LEFT = ""
RIGHT = ""
ELLIPSIS = "…"
ALERT_FG = Color(255, 95, 95)
PREFERRED_TAB_LEN = 20

def _rgb(color):
    return as_rgb(color_as_int(color))


def clean_title(title):
    title = LOCAL_PREFIX_RE.sub("", title or "").strip()
    return title or "~"


def _truncate(text, max_len):
    if max_len <= 0 or len(text) <= max_len:
        return text
    if max_len <= len(ELLIPSIS):
        return ELLIPSIS[:max_len]
    return text[: max_len - len(ELLIPSIS)] + ELLIPSIS


def draw_title(data):
    title = clean_title(data.get("title") or "")
    prefix = "".join(
        str(data.get(key) or "")
        for key in ("bell_symbol", "activity_symbol", "tab.last_focused_progress_percent")
    )
    return f"{prefix}{title}"


def draw_tab(draw_data, screen, tab, before, max_tab_length, index, is_last, extra_data):
    bar_bg = _rgb(draw_data.default_bg)
    pill_bg = _rgb(draw_data.active_bg if tab.is_active else draw_data.inactive_bg)
    fg = _rgb(draw_data.active_fg if tab.is_active else draw_data.inactive_fg)
    # if tab.needs_attention:
    #     fg = _rgb(ALERT_FG)

    tab_len = max(5, min(PREFERRED_TAB_LEN, max_tab_length))
    title_width = max(1, tab_len - len(LEFT) - len(RIGHT))
    title = _truncate(clean_title(tab.title), title_width)

    screen.cursor.fg = pill_bg
    screen.cursor.bg = bar_bg
    screen.draw(LEFT)

    screen.cursor.fg = fg
    screen.cursor.bg = pill_bg
    screen.draw(title)

    screen.cursor.fg = pill_bg
    screen.cursor.bg = bar_bg
    screen.draw(RIGHT)

    if not is_last:
        screen.cursor.fg = bar_bg
        screen.cursor.bg = bar_bg
        screen.draw(" ")

    return screen.cursor.x
