# patch_locale.py

import locale

# Save original reference
_original_setlocale = locale.setlocale

# Monkey patch with English fallback
def safe_setlocale(category, loc=None):
    try:
        return _original_setlocale(category, loc)
    except locale.Error:
        print(f"[locale patch] Failed locale: {loc}, falling back to English")
        # Try common English locale for Windows and Unix
        for fallback in ["en_US.UTF-8", "English_United States.1252", "C"]:
            try:
                return _original_setlocale(locale.LC_ALL, fallback)
            except locale.Error:
                continue
        raise  # If none of the fallbacks work

# Apply patch
locale.setlocale = safe_setlocale
