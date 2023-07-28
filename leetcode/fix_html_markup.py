s = "<div>hello world<div>"

def find_second(s, tag='<div>'):
    count = 0
    for i, c in enumerate(s):
        if c == tag[0]:
            if s[i:i+len(tag)] == tag:
                count += 1
                if count % 2 == 0:
                    return i

def fix_html_markup(s):
    tag='<div>'
    if tag not in s or s.count(tag) == 1:
        return s
    
    id = find_second(s, tag)
    s = s [:id] + '</' + tag[1:] + s[id+len(tag):]
    print(s)


fix_html_markup(s)