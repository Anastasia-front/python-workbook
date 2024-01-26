def not_bad_replace_function(s: str) -> str:
    if s.find("not") == -1 or s.find("bad") == -1:
        return s
    else:
        return s.replace("not bad", "good")
