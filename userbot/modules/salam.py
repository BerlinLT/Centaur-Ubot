from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Dulu Biar Sopan**")


@register(outgoing=True, pattern=r"^\.pe(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@register(outgoing=True, pattern="^\.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum...**")


@register(outgoing=True, pattern="^\.w(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Wa'alaikumsalam {DEFAULTUSER}**")
    sleep(3)
    await typew.edit("**Jangan lupa makan ya cantiku❤️...**")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumsalam**")


CMD_HELP.update(
    {
        "salam": "**Plugin : **`salam`\
        \n\n  •  **Syntax :** `.p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `.pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `.l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `.ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `.semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `.ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `.sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `.k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `.j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
        \n\n  •  **Syntax :** `.w`\
        \n  •  **Function : **jawab salam!!!🔥\
    "
    }
)
