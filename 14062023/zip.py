def local_time(func):
    def wrapper(*args, **kwargs):
        print("Начало")
        res = func(*args, **kwargs)
        print("Конец")
        return res
    return wrapper 
def action(title, tag):
    print(f"title={title},tag = {tag}")
    return f"<{tag}>{title}/<{tag}>"

action = local_time(action)
res = action("Привет","р1")
print(res)